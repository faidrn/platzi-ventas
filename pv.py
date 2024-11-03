import click

from clients import commands as clients_commands # importamos los comandos q hemos creado

CLIENTS_TABLE = '.clients.csv' # constante global con elnormbre del archivo

#definimos el punto de entrada
#usamos el decorador para decirle a click q este es nuestro punto de entrada
@click.group()  #decorador
@click.pass_context #este decorador nos da un objeto contexto (ctx)
def cli(ctx):
    ctx.obj = {}    # inicializamos el objeto contexto como un diccionario vacio
    ctx.obj['clients_table'] = CLIENTS_TABLE   # añadimos la constante global al xontexto


# registramos los comandos
cli.add_command(clients_commands.all)

# creacion de un entorno virtual
# python3 -m venv /path/to/new/virtual/environment
# activar el entorno virtual en mac o linux
# source venv/bin/activate
# activar el entorno virtual en windows
# venv\Scripts\activate
# desactivar el entorno virtual
# deactivate