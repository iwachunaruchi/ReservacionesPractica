from flask import Flask, jsonify, request
from db.mongo import MongoConnection
from roles.initializer import initialize_roles
from flask_cors import CORS
from auth import auth_bp
from ModulesPY.properties.routes import properties_bp
from ModulesPY.availability.routes import availability_bp


app = Flask(__name__)
mongo = MongoConnection()
db = mongo.get_db()
CORS(app)

#blueprint para auth
app.register_blueprint(auth_bp, url_prefix="/auth")
#blueprint para properties
app.register_blueprint(properties_bp, url_prefix="/api")  # Propiedades
#blueprint para disponibilidad
app.register_blueprint(availability_bp, url_prefix="/api")  # Disponibilidad


@app.route('/')
def root():
    return jsonify({"message": "Bienvenido a la API con PyMongo"}), 200



if(__name__ == "__main__"):
    initialize_roles()
    app.run(debug=True)