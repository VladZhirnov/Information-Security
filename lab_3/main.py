import argparse

from asymmetric_crypto import Asymmetric
from symmetric_crypto import Symmetric
from work_with_file import read_json, write_key_to_file, read_file, write_text_to_file


def generate_keys(symmetric: Symmetric, asymmetric: Asymmetric, sym_key_path: str, public_key_path: str, private_key_path: str) -> None:
    """
    Generate symmetric and asymmetric keys and serialize them to files.
    """
    symmetric.generate_key()
    asymmetric.generate_key()
    asymmetric.serialize_public_key(public_key_path)
    asymmetric.serialize_private_key(private_key_path)
    symmetric.serialize_key(sym_key_path)


def encrypt_sym_key(symmetric: Symmetric, asymmetric: Asymmetric, sym_key_path: str, pub_key_path: str, path_to_save: str) -> None:
    """
    Encrypt the symmetric key using asymmetric encryption and save it to a file.
    """
    symmetric.deserialize_key(sym_key_path)
    asymmetric.deserialize_public_key(pub_key_path)
    c_sym_key = asymmetric.encrypt_key(symmetric.key)
    write_key_to_file(path_to_save, c_sym_key)


def decrypt_sym_key(symmetric: Symmetric, asymmetric: Asymmetric, enc_sym_key_path: str, priv_key_path: str, path_to_save: str) -> None:
    """
    Decrypt the symmetric key using asymmetric decryption and save it to a file.
    """
    asymmetric.deserialize_private_key(priv_key_path)
    symmetric.deserialize_key(enc_sym_key_path)
    dc_key = asymmetric.decrypt_key(symmetric.key)
    write_key_to_file(path_to_save, dc_key)


def encrypt_text(symmetric: Symmetric, orig_text_path: str, dec_sym_key_path: str, path_to_save: str) -> None:
    """
    Encrypt the text using symmetric encryption and save it to a file.
    """
    text = read_file(orig_text_path)
    symmetric.deserialize_key(dec_sym_key_path)
    c_text = symmetric.encrypt_text(text)
    write_text_to_file(path_to_save, c_text)


def decrypt_text(symmetric: Symmetric, enc_text_path: str, dec_sym_key_path: str, path_to_save: str) -> None:
    """
    Decrypt the text using symmetric decryption and save it to a file.
    """
    c_text = read_file(enc_text_path)
    symmetric.deserialize_key(dec_sym_key_path)
    dc_text = symmetric.decrypt_text(c_text)
    write_text_to_file(path_to_save, dc_text)


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

