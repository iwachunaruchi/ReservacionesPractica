from db.mongo import mongo_connection
roles_collection = mongo_connection.get_db()["roles"]