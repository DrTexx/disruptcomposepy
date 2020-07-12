import json
import os
from pathlib import Path

from .modfile import ModFile
from ..utils import rmdir_recursive, in_directory

FILES_WRITTEN_FILENAME = "FILES_WRITTEN.json"


def _fwj(build_path):
    return Path(build_path).joinpath(FILES_WRITTEN_FILENAME)


def get_modfiles(project_files_filepath):
    if not os.path.exists(project_files_filepath):
        print(
            f"""[!] Error: Please create a file called '{project_files_filepath}'\
            in the same directory as this binary"""
        )
        raise FileNotFoundError()

    with open(project_files_filepath) as f:
        data = json.load(f)

        data_settings = data["settings"]

        modfiles = [ModFile(file, data_settings) for file in data["files"]]

        return modfiles


def write_modfiles(modfiles, build_path, namespace):
    files_written = []
    for mf in modfiles:
        if mf.is_mutated:
            print(f"was mutated: {mf.filepath}")
            mf.update_filepath(
                Path(build_path).joinpath(namespace, mf.package_filepath)
            )

        print(f"writing {mf.filepath}...")

        modfile_dir = Path(mf.filepath).parents[0]
        modfile_dir.mkdir(parents=True, exist_ok=True)

        with open(mf.filepath, "w") as f:
            f.write(mf.data)

        files_written.append(str(mf.filepath.absolute()))

        print(mf)
    files_written_json = _fwj(build_path)
    with open(files_written_json, "w") as f:
        json.dump(
            {"files_written": [w_filepath for w_filepath in files_written]}, f
        )

    print(files_written)


def clean_build_dir(build_path):
    build_path = Path(build_path)

    print("--[ CLEANING ]--")

    if not build_path.exists():
        print("SKIPPED: no build path to clean")
        return

    if len(os.listdir(build_path)) == 0:
        print("SKIPPED: build path is empty")
        return

    fwj_filepath = _fwj(build_path)  # must be after build path exist check

    if not fwj_filepath.exists():
        print(
            f"'{fwj_filepath}' is missing, assuming clean issue"
            + " or user modifications."
        )
        raise Exception(
            f"'{fwj_filepath}' is missing."
            + f" Please manually clean {build_path} to"
            + " remove the potential for unintended deletions."
        )

    with open(fwj_filepath, "r") as f:
        data = json.load(f)
        for w_file in data["files_written"]:
            w_file = Path(w_file)
            print(
                f"Unlinking {w_file.relative_to(build_path.absolute())}... ",
                end="",
                flush=True,
            )
            if in_directory(w_file, build_path):
                w_file.unlink()
                print("DONE")
            else:
                print(
                    "SKIPPED: Please don't try deleting things outside"
                    + " of the build directory :^)"
                )

        rmdir_recursive(build_path, verbose=False)

    fwj_filepath.unlink()

    try:
        build_path.rmdir()
    except Exception:
        raise Exception(
            "Failed to clean build path. This is likely due to an unexpected file/s being encountered in build directory while cleaning."
        )
