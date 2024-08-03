import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name',      'last_name',      'company',      'email',      'position']
clients = []


def _initilize_client_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA) 

        for row in reader:
            clients.append(row)


def _save_client_to_storage():
    temp_table_name = '{}.temp'.format(CLIENT_TABLE)
    with open(temp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(temp_table_name, CLIENT_TABLE)



def list_clients():
    global clients
    for idx,client in enumerate(clients):
        print('{uid}| {name} |{last_name} |{company} |{email} |{position}'.format(
            uid = idx, 
            name = client['name'],
            last_name = client['last_name'],
            company = client['company'],
            email = client['email'], 
            position = client['position']
            ))


def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)

    else:
        print('Client already is in the client\'s list')
   

def update_client(clients,client_name):
    i = 'name'
    for j,client in enumerate(clients):
        if client[i] == (f'{client_name}'):
            print(f'want to modify the client {client_name}')
            print('[Y]es, update client')
            print('[n]o, exit')
            command = str(input('What do you want to do? '))
            command = command.upper()
            
            if command == 'Y':
                
                updated_client_name = {
                    'name':_get_client_field('name'),
                    'last_name':_get_client_field('last_name'),
                    'company':_get_client_field('company'),
                    'email':_get_client_field('email'),
                    'position': _get_client_field('position'),
                    }
                clients[j] = updated_client_name
                update_name = updated_client_name['name']

                return print(f'The client {client_name} has been successfully updated by {update_name}')

            elif command == 'N':
                print('bey')
                sys.exit()

        elif client[i] != (f'{client_name}'):
            _is_not_in_list()
            break


def delete_client(clients,client_name,):
    for client in clients:
        if client['name'] == (f'{client_name}'):
            clients.remove(client)
        else:
            _is_not_in_list()
            break


def search_client(client_name, client_last_name):
    global clients
    
    i = 'name'
    j = 'last_name' 
    for client in clients:
        if client[i] != (f'{client_name}'):
            # if client[j] != (f'{client_last_name}'):
                continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 70)
    print('what would you like to do today?')
    print('[L]ist Client')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('Wtha is the client {} ? '.format(field_name)).capitalize()

        if field == 'Exit':
            sys.exit()
    
    return field



# def _get_client_name():
#     name_client = None
    
#     while not name_client:
#         name_client = input(f'Wtha is the client name? ')
#         name_client = name_client.capitalize()
            
#         if name_client == 'Exit':
#             sys.exit()

#     return name_client 


def _is_not_in_list():
    return print(f'Client is not in clients list')


# def for_client(client_name):
#     global clients
#     i = 'name'
#     for client in clients:
#         if client[i] == (f'{client_name}'):
#             return client
#         else:
#             return False


# def _command_input():
#     command = input()
#     command = command.upper()
#     return command


if __name__ == '__main__':
    _initilize_client_from_storage()
    _print_welcome()
    command = input(str())
    command = command.upper()

    
    if command == 'C':
        client = {
                'name':_get_client_field('name'),
                'last_name':_get_client_field('last_name'),
                'company':_get_client_field('company'),
                'email':_get_client_field('email'),
                'position': _get_client_field('position'),
            }
        create_client(client)

    
    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_name = _get_client_field('name')
        update_client(clients,client_name)
        

    elif command == 'D':
        client_name = _get_client_field('name')
        delete_client(clients,client_name)
        print(f'The client {client_name} has been deleted successfully') 

    elif command == 'S':
        client_name = _get_client_field('name')
        # client_last_name = _get_client_field('last_name')
        found = search_client(client_name )

        if found:
            print('The client {} is in the client\'s list'. format(client_name))
        else:
            print('The client: {} is not in our client\'s list'. format(client_name))

    else:
        print('Invalid command'),
        # _print_welcome()
        # _command_input()

    _save_client_to_storage()

