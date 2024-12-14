from bson.objectid import ObjectId

from ModulesPY.properties.collection import properties_collection
from ModulesPY.locations.collection import locations_collection
from ModulesPY.amenities.collection import amenities_collection
from ModulesPY.availability.collection import availability_collection
from ModulesPY.availability.model import AvailabilityModel

class PropertyModel:
    @staticmethod
    @staticmethod
    def create_property(data):
        """Crear una nueva propiedad con ubicación y amenidades."""
        # Validar datos requeridos
        required_fields = ["_id_propietario", "nombre", "descripcion", "precio_por_noche", "direccion", "latitud", "longitud", "amenidades"]
        for field in required_fields:
            if field not in data:
                return {"error": f"Falta el campo obligatorio: {field}"}

        # Insertar propiedad
        propiedad = {
            "_id_propietario": ObjectId(data["_id_propietario"]),
            "nombre": data["nombre"],
            "descripcion": data["descripcion"],
            "precio_por_noche": data["precio_por_noche"]
        }
        propiedad_id = properties_collection.insert_one(propiedad).inserted_id

        # Insertar ubicación (usando `locations_collection`)
        location = {
            "_id_propiedad": propiedad_id,
            "direccion": data["direccion"],
            "latitud": data["latitud"],
            "longitud": data["longitud"]
        }
        locations_collection.insert_one(location)
        
        availability_collection.insert_one({
            "_id_propiedad": propiedad_id,
            "minimo_dias": 1,
            "maximo_dias": 30,
            "disponible": False  # Estado inicial: no disponible
        })
        # Insertar amenidades (usando `amenities_collection`)
        amenidades = [{"_id_propiedad": propiedad_id, "amenidad": amenidad} for amenidad in data["amenidades"]]
        amenities_collection.insert_many(amenidades)

        return {"message": "Propiedad creada exitosamente", "_id_propiedad": str(propiedad_id)}
    
    @staticmethod
    def get_all_properties():
        """Obtiene todas las propiedades con ubicación y amenidades."""
        properties = []
        for propiedad in properties_collection.find():
            # Convertir ObjectId a str para serializarlo en JSON
            propiedad["_id_propiedad"] = str(propiedad["_id"])
            propiedad["_id_propietario"] = str(propiedad["_id_propietario"])
            del propiedad["_id"]  # Opcional: eliminar el campo original si no es necesario

            # Obtener ubicación asociada
            location = locations_collection.find_one({"_id_propiedad": ObjectId(propiedad["_id_propiedad"])})
            propiedad["ubicacion"] = {
                "direccion": location["direccion"],
                "latitud": location["latitud"],
                "longitud": location["longitud"]
            }

            # Obtener amenidades asociadas
            amenidades = amenities_collection.find({"_id_propiedad": ObjectId(propiedad["_id_propiedad"])})
            propiedad["amenidades"] = [a["amenidad"] for a in amenidades]
            disponibilidad = AvailabilityModel.get_availability_by_property(propiedad["_id_propiedad"])
            propiedad["disponibilidad"] = disponibilidad if disponibilidad else {
                "minimo_dias": None,
                "maximo_dias": None,
                "disponible": False
            }
            properties.append(propiedad)

        return properties

    @staticmethod
    def get_property_by_id(property_id):
        """Obtiene una propiedad por su ID."""

        try:
            # Convertir el ID recibido a un ObjectId
            property_id = ObjectId(property_id)
        except Exception as e:
            return {"error": "ID de propiedad inválido"}

        # Buscar la propiedad
        propiedad = properties_collection.find_one({"_id": property_id})
        if not propiedad:
            return {"error": "Propiedad no encontrada"}

        # Convertir ObjectId a str
        propiedad["_id_propiedad"] = str(propiedad["_id"])
        propiedad["_id_propietario"] = str(propiedad["_id_propietario"])
        del propiedad["_id"]  # Eliminar el campo original

        # Obtener ubicación asociada
        location = locations_collection.find_one({"_id_propiedad": property_id})
        propiedad["ubicacion"] = {
            "direccion": location["direccion"],
            "latitud": location["latitud"],
            "longitud": location["longitud"]
        }

        # Obtener amenidades asociadas
        amenidades = amenities_collection.find({"_id_propiedad": property_id})
        propiedad["amenidades"] = [a["amenidad"] for a in amenidades]

        #disponibilidad
        disponibilidad = AvailabilityModel.get_availability_by_property(str(property_id))
        propiedad["disponibilidad"] = disponibilidad if disponibilidad else {
            "minimo_dias": None,
            "maximo_dias": None,
            "disponible": False
        }

        return propiedad