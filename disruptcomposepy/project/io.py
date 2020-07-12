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

        data_settings = data["settings"]

        modfiles = [ModFile(file, data_settings) for file in data["files"]]

        return modfiles
