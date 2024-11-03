import click

from clients.services import ClientService
from clients.models import ClientModel

# usamos los decoradores para convertir estas funciones en comandos de click
@click.group() # este decorador convierte a la funcion clients en otro decorador
def clients():
    """Manages the clients lifecycle"""
    pass

# definimos nuestras funciones o comandos basicos
@clients.command()
@click.option('-n', '--name', 
            type=str, 
            prompt=True, 
            help='The client name')   # le decimos a click q nos ayude a pedirle al usuario los parametros requeridos
                                    # '-n', '--name', ==> usamos un shortname y el long name
                                    # type=str, ==> tipo string
                                    # prompt=True, ==> si no nos dan los parametros via patron abreviado dentro del comando, le pedimos los parametros al usuario
                                    # help='The client name'  ==> ayuda para el usuario
@click.option('-c', '--company', 
            type=str, 
            prompt=True, 
            help='The client company')
@click.option('-e', '--email', 
            type=str, 
            prompt=True, 
            help='The client email')
@click.option('-p', '--position', 
            type=str, 
            prompt=True, 
            help='The client position')
@click.pass_context   # pasamos el contexto xq la funcion lo necesita
def create(ctx, name, company, email, position):
    """Creates a new client"""
    # Inicializamos un cliente
    client = ClientModel(name, company, email, position)
    # traemos del contexto el nombre de la tabla o archivo
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    # generamos la referencia a ClientService inicializando la clase
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    # imprimimos los headers
    # usamos click.echo para imprimir y asi garantizar q se vea igual en todos los sistemas operativos
    click.echo('  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*' * 100)    # generamos una linea de asteriscos 

    for client in clients_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client['uid'], 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']
        ))


@clients.command()
@click.argument("client_uid",
                type=str)
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    # usamos un list comprehension para encontrar al cliente 
    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leve empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.argument("client_uid",
                type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    # usamos un list comprehension para encontrar al cliente 
    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client_service.delete_client(client)

        click.echo('Client deleted')
    else:
        click.echo('Client not found')


# generamosun alias para que sea facil declarar todas estas funciones en un solo GO
all = clients
