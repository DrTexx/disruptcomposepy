from .interface import DisruptComposePy as DisruptCompose


def main():
    disco = DisruptCompose()

    modfiles = disco.get_modfiles()
    config = disco.get_config()

    modfiles = [modfile.convert(config) for modfile in modfiles]

    print(f"modfiles: {modfiles}")
