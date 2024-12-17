from fastapi import Depends
from src.core.config import settings
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from src.db.database import get_db


def get_token_payload(token):
    try:
        return jwt.decode(token. settings.secret_key, [settings.algorithm])
    except JWTError:
        return None


def get_current_user(token):
    user = get_token_payload(token)
    return user.get("id")


def check_admin_role(token: HTTPAuthorizationCredentials = Depends(auth_scheme), db: Session = Depends(get_db)):
    user = get_token_payload(token)
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="You don't have permission to access this resource")
    return user.get("id")
