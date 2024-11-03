import csv
import os


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

    # metodo para ver q clientes tenemos almacenados en la BD
    def list_clients(self):
        with open(self.table_name, mode='r') as f: # abrimos el archivo en modo lectura (r)
            reader = csv.DictReader(f, fieldnames=Client.schema)
            # convertimos el iterable reader en una lista
            return list(reader)

    # metodo para actualizar el cliente
    def update_client(self, update_client):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        # guardamos en disco usando un metodo privado
        self._save_to_disk(updated_clients)

    def _save_to_disk(clients):
        # declaramos una tabla temporal xq el archivo ya se encuentra abierto y no podemos volver a abrirlo
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DicWriter(f, fieldnames=Client.schema())
            # escribimos todas las filas
            writer.writerows(clients)

        # ahora renombramos la tabal temporal con el nombre de la tabla original y eliminamos la tabla original
        # para hacer esto, tenemos que importar el modulo 'os'
        # primero removemos el archivo original
        os.remove(self.table_name)
        # luego renombramos la tabla temporal
        os.rename(tmp_table_name, self.table_name)


    # metodo para eliminar el cliente
    def delete_client(self, client_uid):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['uid'] == client_uid:
                clients.pop('uid')

        self._save_to_disk(clients)