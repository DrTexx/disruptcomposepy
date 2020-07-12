from . import project, config
from .paths import project_files_filepath, config_filepath, build_path


class DisruptComposePy:
    def __init__(self):
        pass

    def prepare(self):
        project.io.clean_build_dir(build_path=build_path)

    def get_modfiles(self):
        return project.io.get_modfiles(project_files_filepath)

    def write_modfiles(self, modfiles, namespace):
        project.io.write_modfiles(
            modfiles, build_path=build_path, namespace=namespace
        )

    def get_converters(self):
        return config.io.get_converters(config_filepath)
