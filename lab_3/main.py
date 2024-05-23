import argparse

from asymmetric_crypto import Asymmetric
from symmetric_crypto import Symmetric
from work_with_file import read_json
from encryption_functions import *


def menu():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen', '--generation', help = 'Starts key generation text mode')
    group.add_argument('-enc_key', '--encryption_key', help = 'Starts encryption key mode')
    group.add_argument('-dec_key', '--decryption_key', help = 'Starts decryption key mode')
    group.add_argument('-enc', '--encryption', help = 'Starts encryption text mode')
    group.add_argument('-dec', '--decryption', help = 'Starts decryption text mode')
    parser.add_argument("settings", type=str, help = "Path to the json file with the settings")

    args = parser.parse_args()
    settings = read_json(args.settings)
    symmetric = Symmetric()
    asymmetric = Asymmetric()
    match args:
        case args if args.generation:
            generate_keys(symmetric, asymmetric, settings["symmetric_key"], settings["public_key"], settings["private_key"])
        case args if args.encryption_key:
            encrypt_sym_key(symmetric, asymmetric, settings["symmetric_key"], settings["public_key"], settings["enc_sym_key"])
        case args if args.decryption_key:
            decrypt_sym_key(symmetric, asymmetric, settings["enc_sym_key"], settings["private_key"], settings["dec_sym_key"])
        case args if args.encryption:
            encrypt_text(symmetric, settings["initial_file"], settings["dec_sym_key"], settings["encrypted_file"])
        case args if args.decryption:
            decrypt_text(symmetric, settings["encrypted_file"], settings["dec_sym_key"], settings["decrypted_file"])


if __name__ == "__main__":
    menu()

