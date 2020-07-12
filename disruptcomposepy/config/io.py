import json
import os

from .converter import Converter


def _ensure_c_directory_path(c_directory, src_ft, tar_ft):
    if src_ft not in c_directory:
        c_directory[src_ft] = {}
        if tar_ft not in c_directory[src_ft]:
            c_directory[src_ft][tar_ft] = []
    return c_directory


def _ensure_config_file_exists(config_filepath):
    if not os.path.exists(config_filepath):
        raise FileNotFoundError(
            f"[!] Error: Please create a file called '{config_filepath}'"
            + " in the same directory as this binary"
        )


def get_converters(config_filepath):

    _ensure_config_file_exists(config_filepath)

    converters = []
    c_directory = {}

    with open(config_filepath) as f:
        data = json.load(f)

        for src_ft in data["format_converters"]:

            for tar_ft in data["format_converters"][src_ft]:

                specific_converters_data = data["format_converters"][src_ft][
                    tar_ft
                ]
                for index in range(len(specific_converters_data)):
                    c_data = specific_converters_data[index]
                    c = Converter(
                        _in=src_ft,
                        _out=tar_ft,
                        filepath=c_data["filepath"],
                        args=c_data["args"],
                    )
                    converters.append(c)

                    # populate missing entries so we can add a converter below
                    c_directory = _ensure_c_directory_path(
                        c_directory, src_ft, tar_ft
                    )

                    c_directory[src_ft][tar_ft].append(c)

    return (converters, c_directory)
