import os
from utils.crypto.aes_crypto import aes_decrypt, aes_encrypt
from dotenv import load_dotenv

load_dotenv()

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("ENCRYPTION_KEY must be set in the .env file")

def hashing_password(password: str) -> str:
    return aes_encrypt(ENCRYPTION_KEY, password)

def verify_password(password: str, hashed_password: str) -> str:
    try:
        decrypting_password = aes_decrypt(ENCRYPTION_KEY, hashed_password)
        return decrypting_password == password
    except Exception:
        return False