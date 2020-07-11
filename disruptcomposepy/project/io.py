import json
import os

from .modfile import ModFile


def get_modfiles(project_files_filepath):
    if not os.path.exists(project_files_filepath):
        print(
            f"""[!] Error: Please create a file called '{project_files_filepath}'\
            in the same directory as this binary"""
        )
        raise FileNotFoundError()
    with open(project_files_filepath) as f:
        data = json.load(f)

        modfiles = [ModFile(file) for file in data["files"]]

        return modfiles
