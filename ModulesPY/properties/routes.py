from flask import Blueprint, request,jsonify
from ModulesPY.properties.model import PropertyModel

properties_bp = Blueprint("properties", __name__)
@properties_bp.route("/properties", methods=["POST"])
def create_property():
    """Crea una nueva propiedad."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    result = PropertyModel.create_property(data)
    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201

@properties_bp.route("/properties", methods=["GET"])
def get_all_properties():
    """Obtiene todas las propiedades."""
    properties = PropertyModel.get_all_properties()
    return jsonify(properties), 200

@properties_bp.route("/properties/<property_id>", methods=["GET"])
def get_property_by_id(property_id):
    """Obtiene una propiedad específica por su ID."""
    propiedad = PropertyModel.get_property_by_id(property_id)
    if "error" in propiedad:
        return jsonify(propiedad), 404  # Propiedad no encontrada
    return jsonify(propiedad), 200 