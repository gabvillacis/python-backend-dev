from flask_wtf import CSRFProtect
from passlib.context import CryptContext

csrf = CSRFProtect()

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return crypt_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return crypt_context.hash(password)