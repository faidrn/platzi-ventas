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
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


# generamosun alias para que sea facil declarar todas estas funciones en un solo GO
all = clients
