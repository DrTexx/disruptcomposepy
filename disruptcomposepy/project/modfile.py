from pathlib import Path
import subprocess
import os
from .mutations import mutations


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

    def convert(self, c_directory, c_select=0):
        def _get_converter(c_directory):
            if self.filetype in c_directory:
                if self.target in c_directory[self.filetype]:
                    return c_directory[self.filetype][self.target][c_select]

        def _execute(c):
            print(f"COMMAND LIST: {command_list}:")
            p = subprocess.run(command_list, stdout=subprocess.PIPE)
            if p.returncode != 0:
                print(
                    "[!] ERROR WHILE RUNNING TOOL '{str(converter_filepath)}'"
                )
                print("--[STDERR]:")
                if p.stderr:
                    print(p.stderr.decode("utf-8"))
                print("--[STDOUT]:")
                if p.stdout:
                    print(p.stdout.decode("utf-8"))

            if p.stdout:
                print(p.stdout.decode("utf-8"))

        converter = _get_converter(c_directory)

        command_list = [str(converter.filepath.resolve())]
        [command_list.append(str(arg)) for arg in converter.args]
        command_list.append(str(self.filepath.absolute()))
        # command_list.append(str(self.target_filepath.relative_to(".")))

        _execute(command_list)
