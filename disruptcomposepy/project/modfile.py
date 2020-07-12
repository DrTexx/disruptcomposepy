from pathlib import Path


def _debug_modfile(modfile):
    for key in dir(modfile):
        ignore = False
        if len(key) >= 2:  # can't slice chars that don't exist
            if key[:2] == "__":
                ignore = True

        if not ignore:
            print(f"{key} == {getattr(modfile, key)}\n")


def resolve_target(target, filetype):
    if target is not None:
        return target
    # process of elimination, which method makes sense for filetype x
    print("WIP: resolve target type")
    exit()


def fetch_mutations(entry):
    output = []

    if "mutations" not in entry:
        print("no mutations registered")
        return output

    muts = entry["mutations"]
    for mut in muts:
        mut = mut.upper()
        if mut in mutations:
            output.append(mutations[mut])

    return output


class ModFile:
    def __init__(self, entry):
        self.filepath = Path(*entry["filepath"])
        self.filetype = self.filepath.suffix
        self.methods = resolve_method(entry["method"], self.filetype)

    def __repr__(self):
        out = f"<ModFile targeting '{self.filepath}'>"

        return out
