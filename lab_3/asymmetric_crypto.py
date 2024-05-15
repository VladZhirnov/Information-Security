import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Asymmetric:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generation_key(self):
        keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
        )
        self.private_key = keys
        self.public_key = keys.public_key()

    def serialization_public_key(self, public_path):
        with open(public_path, 'wb') as public_out:
            public_out.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
            
    def serialization_private_key(self, private_path):
        with open(private_path, 'wb') as private_out:
            private_out.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))
    
    def encrypt_key(self, symmetric_key):
        encrypted_key = self.public_key.encrypt(symmetric_key,
                                        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                    algorithm=hashes.SHA256(),label=None))
        return encrypted_key

            
    
     
    