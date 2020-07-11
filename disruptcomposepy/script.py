from .interface import DisruptComposePy as DisruptCompose


def main():
    disco = DisruptCompose()

    modfiles = disco.get_modfiles()

    print(f"modfiles: {modfiles}")
