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
    def __init__(self, entry, settings):
        self.settings = settings
        self.package_filepath = Path(*entry["filepath"])
        self.src_filepath = Path(settings["src_root"]).joinpath(
            self.package_filepath
        )
        self.filepath = self.src_filepath
        self.data = self._read_from_filepath()
        self.filetype = self.filepath.suffix
        self.target = resolve_target(entry["target"], self.filetype)
        self.target_filepath = self.filepath.with_suffix(self.target)
        self.mutations = fetch_mutations(entry)
        self.is_mutated = False

    def _read_from_filepath(self):
        with open(self.filepath) as f:
            return f.read()

    def __repr__(self):
        out = f"<ModFile targeting '{self.filepath}'>"

        return out

    def apply_mutations(self):
        if self.mutations:
            self.is_mutated = True
            for mut in self.mutations:
                self.data = mut.apply(self)
