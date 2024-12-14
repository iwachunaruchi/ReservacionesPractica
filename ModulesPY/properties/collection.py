from db.mongo import mongo_connection
properties_collection = mongo_connection.get_db()["properties"]

