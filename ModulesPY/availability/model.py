from bson.objectid import ObjectId
from ModulesPY.availability.collection import availability_collection

class AvailabilityModel:
    @staticmethod
    def get_availability_by_property(property_id):
        """Obtiene la disponibilidad de una propiedad específica."""
        try:
            property_id = ObjectId(property_id)
        except Exception:
            return {"error": "ID de propiedad inválido"}
        availability = availability_collection.find_one({"_id_propiedad": property_id})
        if not availability:
            return None
        return {
            "minimo_dias": availability["minimo_dias"],
            "maximo_dias": availability["maximo_dias"],
            "disponible": availability["disponible"]
        }
    
    @staticmethod
    def update_availability_to_reserved(property_id):
        """Actualiza el estado de disponibilidad a True para la propiedad especificada."""
        try:
            # Convertir el ID recibido a ObjectId
            property_id = ObjectId(property_id)
        except Exception:
            return {"error": "ID de propiedad inválido"}

        # Verificar si la disponibilidad existe para la propiedad
        availability = availability_collection.find_one({"_id_propiedad": property_id})
        if not availability:
            return {"error": "Disponibilidad no encontrada para esta propiedad"}

        # Actualizar el estado de disponibilidad a True
        result = availability_collection.update_one(
            {"_id_propiedad": property_id},
            {"$set": {"disponible": True}}
        )

        if result.matched_count == 0:
            return {"error": "Error al actualizar la disponibilidad"}

        return {"message": "Disponibilidad actualizada a True para la propiedad"}