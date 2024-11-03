import uuid


class ClientModel:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company 
        self.email = email 
        self.position = position 
        # si nos envian el parametro uid usamos ese parametro, sino, usamos el modulo uuid, de python
        # que permite generar IDs unicos
        self.uid = uid or uuid.uuid4() # uuid4 es el estandar de la industria

    def to_dict(self):
        return vars(self)   # la funcion vars solo checa q es lo q hace le etodo _dict, y nos 
                            # permite acceder a un dicionario o a una representación como dicionario de nuestro objeto

    # un metodo estatico es un metodo q se puede ejecutar sin necesidad de una instancia de clase
    @staticmethod
    def schema():
        # representa el esquema tabular o columnas del archivo csv
        return ['name', 'company', 'email', 'position', 'uid']