import click

from clients.services import ClientService
from clients.models import ClientModule


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n','name',
        type = str.capitalize(),
        prompt = True,
        help = 'The client name')
@click.option('-l','last_name',
        type = str.capitalize(),
        prompt = True,
        help = 'The client Last name')
@click.option('-c','company',
        type = str.capitalize(),
        prompt = True,
        help = 'The client company')
@click.option('-e','email',
        type = str.capitalize(),
        prompt = True,
        help = 'The client email')
@click.option('-p','position',
        type = str.capitalize(),
        prompt = True,
        help = 'The client position')
@click.pass_context
def create(ctx,name,last_name,company,email,position):
    """Creates a new client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = ClientModule(name,last_name,company,email,position)

    client_service.create_client(client)



@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    
    clients_list = client_service.list_clients()

    click.echo(' ID  |  NAME  | LAST NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*' * 100)

    for client in clients_list:
        click.echo('{uid}  |  {name}  |  {last_name}  |  {company}  |  {email}  |  {position}'.format(
            uid = client['uid'] ,
            name = client['name'],
            last_name = client['last_name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
            ))


@clients.command()
@click.pass_context
def update(ctx):
    """Update client)"""
    pass


@clients.command()
@click.pass_context
def delete(ctx):
    """Delete  client"""
    pass

all = clients 
    



