from werkzeug.security import generate_password_hash
from auth.collection import users_collection
#collecion de roles
from roles.colletion import roles_collection



class RegisterUser:
    @staticmethod
    def create_user(data):
        if "username" not in data or "password" not in data or "email" not in data:
            return {"error": "Faltan campos obligatorios"}
        
        if users_collection.find_one({"username": data["username"]}):
            return {"error": "El usuario ya existe"}
        
        cliente_role = roles_collection.find_one({"nombre": "cliente"})
        if not cliente_role:
            return {"error": "El rol de cliente no está configurado"}
        
        hashed_password = generate_password_hash(data["password"])
        users_collection.insert_one({
            "username": data["username"],
            "password": hashed_password,
            "email": data["email"],
            "_id_rol": cliente_role["_id"]  # Relación con el rol de cliente
        })
        return {"message": "Usuario creado exitosamente"}



