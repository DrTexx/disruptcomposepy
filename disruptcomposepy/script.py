from .interface import DisruptComposePy as DisruptCompose


def main():
    disco = DisruptCompose()

    modfiles = disco.get_modfiles()

    [modfile.apply_mutations() for modfile in modfiles]
    disco.write_modfiles(modfiles, namespace="MUTATED")

    c_directory = disco.get_converters()[1]
    [modfile.convert(c_directory) for modfile in modfiles]

    print(f"modfiles: {modfiles}")
