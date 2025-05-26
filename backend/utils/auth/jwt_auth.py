import os
import uuid
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
from sqlalchemy.orm import Session
from utils.crypto.rsa_crypto import load_private_key, load_public_key, rsa_decrypt, rsa_encrypt
from internal.models.mst_users import MstUsers

load_dotenv()

ALGORITHM = os.getenv("ALGORITHM", "RS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))
SECRET_KEY = os.getenv("SECRET_KEY")

private_key = load_private_key()
public_key = load_public_key()

def serialize_data(data: dict) -> dict:
    for key, value in data.items():
        if isinstance(value, uuid.UUID):
            data[key] = str(value)
    return data

def create_access_token(db: Session, identifier: str, expires_delta: timedelta = None) -> str:
    user = db.query(MstUsers).filter((MstUsers.email == identifier) | (MstUsers.username == identifier)).first()
    if not user:
        raise ValueError("User Not Found")
    
    to_encode = serialize_data({"user_id": str(user.id), "username": str(user.username), "email": str(user.email), "roles_id": str(user.roles_id)})
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ),
        algorithm=ALGORITHM
    )
    return token

def create_refresh_token(db: Session, identifier: str, expires_delta: timedelta = None) -> str:
    user = db.query(MstUsers).filter((MstUsers.username == identifier) | (MstUsers.email == identifier)).first()
    if not user:
        raise ValueError("User Not Found")
    
    to_encode = serialize_data({"user_id": str(user.id), "username": str(user.username), "email": str(user.email), "roles_id": str(user.roles_id)})
    expire = datetime.now() + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})

    encrypted_secret = rsa_encrypt(public_key, SECRET_KEY)
    to_encode.update({"rsa_secret": encrypted_secret})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

    return token

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            public_key,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError as e:
        raise ValueError(f"Invalid access token: {str(e)}")
    
def decode_refresh_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        rsa_secret = payload.get("rsa_secret")
        if not rsa_secret:
           raise ValueError("Token tidak valid: rsa_secret tidak ditemukan")
        
        decrypted_secret = rsa_decrypt(private_key, rsa_secret)
        if decrypted_secret != SECRET_KEY:
            raise ValueError("Token tidak valid: secret tidak cocok")
        
        return payload
    except JWTError as e:
        raise ValueError(f"invalid refresh token: {str(e)}")