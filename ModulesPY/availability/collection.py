from db.mongo import mongo_connection
availability_collection = mongo_connection.get_db()["availability"]
