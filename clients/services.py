import csv

# preguntamos al modelo el nombre de las columnas para no digitar una a una
from clients.models import Client

class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name    # nombre del archivo csv

    def create_client(self):
        # abrir el archivo csv, en modo append (a)
        with open(self.table_name, mode='a') as f:
            writer ) csv.DicWriter(f, fieldnames=Client.schema())
            # escribimos una nueva fila dentro del archivo csv
            writer.writrow(client.to_dict())