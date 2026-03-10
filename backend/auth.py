import hashlib
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"


# simple password hashing
def hash_password(password: str):

    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str):

    return hashlib.sha256(password.encode()).hexdigest() == hashed


def create_token(username: str):

    expire = datetime.utcnow() + timedelta(hours=10)

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
