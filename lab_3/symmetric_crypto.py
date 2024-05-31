import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Symmetric:
    """
    Class for implementing symmetric algorithms
    """
    def __init__(self) -> None:
        self.key = None

    def generate_key(self) -> bytes:
        """
        Generate a random key for symmetric encryption.

        Returns:
            bytes: The generated symmetric key.
        """
        self.key = os.urandom(16)
        return self.key
    
    def serialize_key(self, key_path: str) -> None:
        """
        Serialize the symmetric key and save it to a file.

        Args:
            key_path (str): File path where the symmetric key will be saved.
        """
        with open(key_path, "wb") as key_file:
            key_file.write(self.key)

    def deserialize_key(self, key_path: str) -> None:
        """
        Deserialize the symmetric key from a file.

        Args:
            key_path (str): File path from which the symmetric key will be read.
        """
        with open(key_path, mode='rb') as key_file: 
            self.key = key_file.read()

    def encrypt_text(self, text: bytes) -> bytes:
        """
        Encrypt text using AES symmetric encryption in CBC mode.

        Args:
            text (bytes): The plaintext to be encrypted.

        Returns:
            bytes: The IV followed by the encrypted ciphertext.
        """
        iv = os.urandom(8)
        cipher = Cipher(algorithms.IDEA(self.key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        adder = padding.ANSIX923(32).padder()
        padded_text = adder.update(text) + adder.finalize()
        cipher_text = iv + encryptor.update(padded_text) + encryptor.finalize()
        return cipher_text
    
    def decrypt_text(self, text: bytes) -> str:
        """
        Decrypt text encrypted using AES symmetric encryption in CBC mode.

        Args:
            text (bytes): The ciphertext to be decrypted.

        Returns:
            str: The decrypted plaintext.
        """
        iv = text[:8]
        cipher_text = text[8:]
        cipher = Cipher(algorithms.IDEA(self.key), modes.CFB(iv))
        decrypt = cipher.decryptor()
        unpacker_text = decrypt.update(cipher_text) + decrypt.finalize()
        decrypt_text = unpacker_text.decode('UTF-8')
        return decrypt_text
    
        
    
    
    