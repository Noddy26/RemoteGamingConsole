import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from libs.variables.Configuration import Configuration


class Encrpt():

    @staticmethod
    def encrypt(password):
        key = Encrpt().createKey()
        encode = password.encode()
        f = Fernet(key)
        encryption = f.encrypt((encode))
        return encryption

    @staticmethod
    def decrypt(encryption):
        key = Encrpt().createKey()
        f = Fernet(key)
        decrypted = f.decrypt(encryption)
        return decrypted.decode()

    @staticmethod
    def createKey():
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=Configuration.salt.encode(),
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(Configuration.key.encode()))
        return key
