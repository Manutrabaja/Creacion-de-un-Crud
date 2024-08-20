import click 

from clients.services import ClientService
from clients.models import ClientModule


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n','name',
        type = str,
        prompt = True,
        help = 'The client name')
@click.option('-l','last_name',
        type = str,
        prompt = True,
        help = 'The client Last name')
@click.option('-c','company',
        type = str,
        prompt = True,
        help = 'The client company')
@click.option('-e','email',
        type = str,
        prompt = True,
        help = 'The client email')
@click.option('-p','position',
        type = str,
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
@click.argument('client_name',
                type=str)
@click.pass_context
def update(ctx, client_name):
    """Update client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    client = [client for client in client_list if client['name'] == client_name]
    
    if client:
        client = _update_client_flow(ClientModule(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type = str, default = client.name)
    client.last_name = click.prompt('New lats name', type = str, default = client.last_name)
    client.company = click.prompt('New company', type = str, default = client.company) 
    client.email = click.prompt('New email', type = str, default = client.email)
    client.position = click.prompt('New position', type = str, default = client.position)
    
    return client




all = clients 
    



