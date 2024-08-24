import jwt
import datetime
from app import app

def encode_jwt_token(username: str) -> str:
    return jwt.encode({
        'user': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config['SECRET_KEY'], algorithm="HS256")
