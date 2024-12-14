from roles.colletion import roles_collection

def initialize_roles():
    if roles_collection.count_documents({}) == 0:
        roles_collection.insert_many([
            {"nombre": "admin", "descripcion": "Acceso completo al sistema"},
            {"nombre": "cliente", "descripcion": "Acceso limitado para reservar propiedades"}
        ])
        print("Roles inicializados correctamente")
    else:
        print("Roles ya están inicializados")