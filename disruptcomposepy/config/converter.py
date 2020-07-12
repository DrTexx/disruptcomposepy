from pathlib import Path


class Converter:
    def __init__(self, _in, _out, filepath, args):
        if not Path(filepath).is_file():
            raise FileNotFoundError(
                f"Filepath for converter ({_in} -> {_out})"
                + f" can't be resolved: '{filepath}'"
            )

        self.filepath = Path(filepath).resolve()
        self.args = args
