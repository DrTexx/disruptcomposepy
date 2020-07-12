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

