from flask import Blueprint
from auth.register.routes import register_bp
from auth.login.routes import login_bp


auth_bp = Blueprint("auth", __name__)

# Registrar Blueprints individuales
auth_bp.register_blueprint(register_bp, url_prefix="/register")
auth_bp.register_blueprint(login_bp, url_prefix="/login")
