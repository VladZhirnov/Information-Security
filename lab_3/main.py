import argparse

from asymmetric_crypto import Asymmetric
from symmetric_crypto import Symmetric
from work_with_file import read_json, write_key_to_file


def generate_keys(symmetric, asymmetric, sym_key_path, public_key_path, private_key_path):
    symmetric.generate_key()
    asymmetric.generate_key()
    asymmetric.serialize_public_key(public_key_path)
    asymmetric.serialize_private_key(private_key_path)
    symmetric.serialize_key(sym_key_path)

def encrypt_sym_key(symmetric, asymmetric, sym_key_path, pub_key_path, path_to_save):
    symmetric.deserialize_key(sym_key_path)
    asymmetric.deserialize_public_key(pub_key_path)
    c_sym_key = asymmetric.encrypt_key(symmetric.key)
    write_key_to_file(path_to_save, c_sym_key)

def menu():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen', '--generation', help = 'Starts key generation mode')
    group.add_argument('-enc_key','--encryption_key', help='Starts encryption mode')
    parser.add_argument("settings", type=str, help="Path to the json file with the settings")
    args = parser.parse_args()
    settings = read_json(args.settings)
    symmetric = Symmetric()
    asymmetric = Asymmetric()
    if args.generation is not None:
        generate_keys(symmetric, asymmetric, settings["symmetric_key"], settings["public_key"], settings["private_key"])
    elif args.encryption_key is not None:
        encrypt_sym_key(symmetric, asymmetric, settings["symmetric_key"], settings["public_key"], settings["enc_sym_key"])

    
if __name__ == "__main__":
    menu()

