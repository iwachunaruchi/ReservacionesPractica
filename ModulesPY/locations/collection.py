from db.mongo import mongo_connection
locations_collection = mongo_connection.get_db()["locations"]
