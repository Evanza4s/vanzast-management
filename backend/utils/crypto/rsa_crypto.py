import os
import base64
from dotenv import load_dotenv
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

load_dotenv()

PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", "private_key.pem")
PUBLIC_KEY_PATH = os.getenv("PUBLIC_KEY_PATH", "public_key.pem")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "").encode()

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    with open(PRIVATE_KEY_PATH, "wb") as priv_file:
        priv_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.BestAvailableEncryption(ENCRYPTION_KEY) if ENCRYPTION_KEY else serialization.NoEncryption()
            )
        )

    with open(PUBLIC_KEY_PATH, "wb") as pub_file:
        pub_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("RSA key pair generated and saved.")

def load_public_key():
    try:
        with open(PUBLIC_KEY_PATH, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key
    except FileNotFoundError:
        raise FileNotFoundError(f"Public key file not found at {PUBLIC_KEY_PATH}. Please generate keys first.")

def load_private_key():
    try:
        with open(PRIVATE_KEY_PATH, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=ENCRYPTION_KEY if ENCRYPTION_KEY else None,
                backend=default_backend()
            )
        return private_key
    except FileNotFoundError:
        raise FileNotFoundError(f"Private key file not found at {PRIVATE_KEY_PATH}. Please generate keys first.")
    except ValueError:
        raise ValueError("Failed to load the private key. Check if the encryption key is correct.")

def rsa_encrypt(public_key, data):
    encrypted = public_key.encrypt(
        data.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode("utf-8")

def rsa_decrypt(private_key, encrypted_data):
    decrypted = private_key.decrypt(
        base64.b64decode(encrypted_data),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode("utf-8")
