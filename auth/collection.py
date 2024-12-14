from db.mongo import mongo_connection
users_collection = mongo_connection.get_db()["users"]
