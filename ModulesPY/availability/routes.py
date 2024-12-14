from flask import Blueprint, jsonify, request
from ModulesPY.availability.model import AvailabilityModel

availability_bp = Blueprint("availability", __name__)
@availability_bp.route("/availability/<property_id>", methods=["POST"])
def reserve_property(property_id):
    result = AvailabilityModel.update_availability_to_reserved(property_id)
    if "error" in result:
        return jsonify(result), 400  # Error en la operación
    return jsonify(result), 200  # 