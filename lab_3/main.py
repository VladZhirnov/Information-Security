import argparse
import json

from asymmetric_crypto import Asymmetric
from symmetric_crypto import Symmetric
from work_with_file import read_json


def generation_keys(symmetric, asymmetric, sym_key_path, public_key_path, private_key_path):
    symmetric.generation_key()
    asymmetric.generation_key()
    asymmetric.serialization_public_key(public_key_path)
    asymmetric.serialization_private_key(private_key_path)
    symmetric.serialization_key(sym_key_path)

def menu():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen', '--generation', help = 'Starts key generation mode')
    parser.add_argument("settings", type=str, help="Path to the json file with the settings")
    args = parser.parse_args()
    settings = read_json(args.settings)
    symmetric = Symmetric()
    asymmetric = Asymmetric()
    if args.generation is not None:
        generation_keys(symmetric, asymmetric, settings["symmetric_key"], settings["public_key"], settings["private_key"])
    
if __name__ == "__main__":
    menu()

