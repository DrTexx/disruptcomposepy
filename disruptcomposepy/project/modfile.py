from pathlib import Path


def _debug_modfile(modfile):
    for key in dir(modfile):
        ignore = False
        if len(key) >= 2:  # can't slice chars that don't exist
            if key[:2] == "__":
                ignore = True

        if not ignore:
            print(f"{key} == {getattr(modfile, key)}\n")


def resolve_method(method, filetype):
    if method is not None:
        return method
    # process of elimination, which method makes sense for filetype x
    print("WIP: resolve method")
    exit()


class ModFile:
    def __init__(self, entry):
        self.filepath = Path(*entry["filepath"])
        self.filetype = self.filepath.suffix
        self.methods = resolve_method(entry["method"], self.filetype)

    def __repr__(self):
        out = f"<ModFile targeting '{self.filepath}'>"

        return out
