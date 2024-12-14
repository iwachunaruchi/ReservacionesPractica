from db.mongo import mongo_connection
amenities_collection = mongo_connection.get_db()["amenities"]
