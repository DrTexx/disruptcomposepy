from .interface import DisruptComposePy as DisruptCompose


def main():
    disco = DisruptCompose()

    modfiles = disco.get_modfiles()
    c_directory = disco.get_converters()[1]


    c_directory = disco.get_converters()[1]
    [modfile.convert(c_directory) for modfile in modfiles]

    print(f"modfiles: {modfiles}")
