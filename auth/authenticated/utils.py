import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

def generate_token(username):
    """Genera un token JWT para el usuario."""
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=1)  # El token expira en 1 hora
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
