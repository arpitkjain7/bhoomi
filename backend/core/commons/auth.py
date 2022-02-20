import time
import jwt
import os
from passlib.context import CryptContext
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


JWT_SECRET = os.environ.get("secret")
JWT_ALGORITHM = os.environ.get("algorithm")


def signJWT(username: str, user_role: str, user_role_id: int):
    payload = {
        "user_name": username,
        "user_role": user_role,
        "user_role_id": user_role_id,
        "expires": time.time() + 86400,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception:
        return None


def verify_hash_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def encrypt_password(password):
    return pwd_context.hash(password)


def check_user_authorization(user_details: dict, allowed_user_role_id: int):
    if user_details.get("user_role_id") <= allowed_user_role_id:
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient privileges",
            headers={"WWW-Authenticate": "Bearer"},
        )
