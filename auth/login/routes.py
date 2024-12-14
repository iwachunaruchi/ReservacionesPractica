from flask import Blueprint, request, jsonify
from auth.login.models import LoginUser

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    """Inicia sesión y genera un token JWT."""
    data = request.get_json()
    if "username" not in data or "password" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    result = LoginUser.authenticate_user(data["username"], data["password"])
    if "error" in result:
        return jsonify(result), 401  # Error de autenticación
    return jsonify(result), 200  # Autenticación exitosa

@login_bp.route("/logout", methods=["POST"])
def logout():
    """Finaliza la sesión del usuario."""
    return jsonify({"message": "Logout exitoso"}), 200