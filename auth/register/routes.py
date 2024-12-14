from flask import Blueprint, request, jsonify
from auth.register.models import RegisterUser

register_bp = Blueprint("register", __name__)
@register_bp.route("/register", methods=["POST"])
def register():
    """Registra un nuevo usuario."""
    data = request.get_json()
    if "username" not in data or "password" not in data:
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    result = RegisterUser.create_user(data)
    if "error" in result:
        return jsonify(result), 400  # Usuario ya existe
    return jsonify(result), 201  # Us