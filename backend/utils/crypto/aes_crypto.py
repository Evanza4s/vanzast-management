import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv
import secrets

load_dotenv()

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("ENCRYPTION_KEY must be set in the .env file")

def derive_key(passphrase: str, salt: bytes = None) -> tuple[bytes, bytes]:
    if salt is None:
        salt = secrets.token_bytes(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(passphrase.encode())
    return key,salt

def aes_encrypt(passphrase: str, plaintext: str) -> str:
    key, salt = derive_key(passphrase)
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

    encrypted_data = base64.b64encode(salt + iv + ciphertext).decode()
    return encrypted_data

def aes_decrypt(passphrase: str, b64_ciphertext: str) -> str:
    try:
        ciphertext = base64.b64decode(b64_ciphertext)
        salt = ciphertext[:16]
        iv = ciphertext[16:32]
        actual_ciphertext = ciphertext[32:]

        key, _ = derive_key(passphrase, salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

        return plaintext.decode()
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")