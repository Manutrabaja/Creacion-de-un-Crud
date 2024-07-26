import sys



clients = [
    {   'name': 'Pablo',
        'company': 'Google',
        'email': 'Pablo@google.com',
        'position': 'Software engineer',
        
        }, {
        
        'name': 'Ricardo',
        'company': 'Platzi',
        'email': 'Ricardo@platzi.com',
        'position': 'Data engineer', 

        }

        ]


def list_clients():
    global clients
    for idx,client in enumerate(clients):
        print('{uid}| {name} | {company} | {email} | {position}'.format(
            uid = idx, 
            name = client['name'],
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
   

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _is_not_in_list()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _is_not_in_list()


def search_client(client_name):
    global clients
    
    for client1 in clients:
        if client1 != client_name:
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


# def _command_input():
#     command = input()
#     command = command.upper()
#     return command


if __name__ == '__main__':
    _print_welcome()
    command = input(str())
    command = command.upper()

    
    if command == 'C':
        client = {
                'name':_get_client_field('name'),
                'company':_get_client_field('company'),
                'email':_get_client_field('email'),
                'position': _get_client_field('position'),
            }

        create_client(client)
        list_clients()
    
    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_name = _get_client_field('name'),
        updated = input(f'what is the updated client name: ')
        updated_client_name = updated.capitalize() 
        update_client(client_name, updated_client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_field('name'),
        delete_client(client_name) 
        list_clients()

    elif command == 'S':
        client_name = _get_client_field('name'),
        found = search_client(client_name)

        if found:
            print('The client {} is in the client\'s list'. format(client_name))
        else:
            print('The client: {} is not in our client\'s list'. format(client_name))


    else:
        print('Invalid command'),
        # _print_welcome()
        # _command_input()



