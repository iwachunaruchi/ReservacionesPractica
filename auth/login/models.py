from db.mongo import MongoConnection
from auth.collection import users_collection
from werkzeug.security import check_password_hash
from auth.authenticated.utils import generate_token  # Para generar el token JWT
#importancion de roles
from roles.colletion import roles_collection

class LoginUser:
    @staticmethod
    def authenticate_user(username, password):
        """Autentica un usuario y genera un token si las credenciales son correctas."""
        user = users_collection.find_one({"username": username})
        if not user:
            return {"error": "El usuario no existe"}

        if not check_password_hash(user["password"], password):
            return {"error": "Contraseña incorrecta"}
        
        role = roles_collection.find_one({"_id": user["_id_rol"]})
        if not role:
            return {"error": "Rol no encontrado para este usuario"}

        # Genera un token JWT
        token = generate_token(username)
        return {
            "message": "Autenticación exitosa",
            "username": username,
            "token": token,
            "rol": role["nombre"]
        }