import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Symmetric:
    def __init__(self):
        self.key = None

    def generation_key(self):
        self.key = os.urandom(16)
        return self.key
    
    def serialization_key(self, key_path):
        with open(key_path, "wb") as key_file:
            key_file.write(self.key)
    
    
    