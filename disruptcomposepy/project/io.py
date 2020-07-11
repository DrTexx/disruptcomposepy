import json

from .modfile import ModFile


def get_modfiles():
    with open("disruptcomposepy_files.json") as f:
        data = json.load(f)

        modfiles = [ModFile(file) for file in data["files"]]

        return modfiles
