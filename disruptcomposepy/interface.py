from . import project, config
from .paths import project_files_filepath, config_filepath


class DisruptComposePy:
    def __init__(self):
        pass

    def get_modfiles(self):
        return project.io.get_modfiles(project_files_filepath)

    def get_config(self):
        return config.io.get_config(config_filepath)
