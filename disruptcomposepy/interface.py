from . import project
from .paths import project_files_filepath


class DisruptComposePy:
    def __init__(self):
        pass

    def get_modfiles(self):
        return project.io.get_modfiles(project_files_filepath)
