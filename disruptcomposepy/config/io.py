import json
import os


def get_config(config_filepath):
    if not os.path.exists(config_filepath):
        print(
            f"""[!] Error: Please create a file called '{config_filepath}'\
            in the same directory as this binary"""
        )
        raise FileNotFoundError()
    with open(config_filepath) as f:
        return json.load(f)
