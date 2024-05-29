from asymmetric_crypto import Asymmetric
from symmetric_crypto import Symmetric
from work_with_file import write_key_to_file, read_file, write_text_to_file


def generate_keys(symmetric: Symmetric, asymmetric: Asymmetric, sym_key_path: str, public_key_path: str, private_key_path: str) -> None:
    """
    Generate symmetric and asymmetric keys and serialize them to files.

    Args:
        symmetric (Symmetric): Instance of the Symmetric class used to generate and handle the symmetric key.
        asymmetric (Asymmetric): Instance of the Asymmetric class used to generate and handle the asymmetric keys.
        sym_key_path (str): File path where the symmetric key will be saved.
        public_key_path (str): File path where the public key will be saved.
        private_key_path (str): File path where the private key will be saved.
    """
    symmetric.generate_key()
    asymmetric.generate_key()
    asymmetric.serialize_public_key(public_key_path)
    asymmetric.serialize_private_key(private_key_path)
    symmetric.serialize_key(sym_key_path)


def encrypt_sym_key(symmetric: Symmetric, asymmetric: Asymmetric, sym_key_path: str, pub_key_path: str, path_to_save: str) -> None:
    """
    Encrypt the symmetric key using asymmetric encryption and save it to a file.

    Args:
        symmetric (Symmetric): Instance of the Symmetric class used to handle the symmetric key.
        asymmetric (Asymmetric): Instance of the Asymmetric class used to handle the asymmetric keys.
        sym_key_path (str): File path where the symmetric key is stored.
        pub_key_path (str): File path where the public key is stored.
        path_to_save (str): File path where the encrypted symmetric key will be saved.
    """
    symmetric.deserialize_key(sym_key_path)
    asymmetric.deserialize_public_key(pub_key_path)
    c_sym_key = asymmetric.encrypt_key(symmetric.key)
    write_key_to_file(path_to_save, c_sym_key)


def decrypt_sym_key(symmetric: Symmetric, asymmetric: Asymmetric, enc_sym_key_path: str, priv_key_path: str, path_to_save: str) -> None:
    """
    Decrypt the symmetric key using asymmetric decryption and save it to a file.

    Args:
        symmetric (Symmetric): Instance of the Symmetric class used to handle the symmetric key.
        asymmetric (Asymmetric): Instance of the Asymmetric class used to handle the asymmetric keys.
        enc_sym_key_path (str): File path where the encrypted symmetric key is stored.
        priv_key_path (str): File path where the private key is stored.
        path_to_save (str): File path where the decrypted symmetric key will be saved.
    """
    asymmetric.deserialize_private_key(priv_key_path)
    symmetric.deserialize_key(enc_sym_key_path)
    dc_key = asymmetric.decrypt_key(symmetric.key)
    write_key_to_file(path_to_save, dc_key)


def encrypt_text(symmetric: Symmetric, orig_text_path: str, dec_sym_key_path: str, path_to_save: str) -> None:
    """
    Encrypt the text using symmetric encryption and save it to a file.

    Args:
        symmetric (Symmetric): Instance of the Symmetric class used to handle the symmetric key and encryption process.
        orig_text_path (str): File path where the original text is stored.
        dec_sym_key_path (str): File path where the decrypted symmetric key is stored.
        path_to_save (str): File path where the encrypted text will be saved.
    """
    text = read_file(orig_text_path)
    symmetric.deserialize_key(dec_sym_key_path)
    c_text = symmetric.encrypt_text(text)
    write_text_to_file(path_to_save, c_text)


def decrypt_text(symmetric: Symmetric, enc_text_path: str, dec_sym_key_path: str, path_to_save: str) -> None:
    """
    Decrypt the text using symmetric decryption and save it to a file.

    Args:
        symmetric (Symmetric): Instance of the Symmetric class used to handle the symmetric key and decryption process.
        enc_text_path (str): File path where the encrypted text is stored.
        dec_sym_key_path (str): File path where the decrypted symmetric key is stored.
        path_to_save (str): File path where the decrypted text will be saved.
    """
    c_text = read_file(enc_text_path)
    symmetric.deserialize_key(dec_sym_key_path)
    dc_text = symmetric.decrypt_text(c_text)
    write_text_to_file(path_to_save, dc_text)