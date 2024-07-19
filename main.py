
clients = 'pablo,ricardo,'



def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already is in the client\'s list')
   

def update_client(client_name, updated_client_name):
    global clients


    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ', ')
    else:
        _is_not_in_list()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _is_not_in_list()


def search_client(client_name):
    global clients
    clients_list = clients.split(',')
    
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_coma():
    global clients
    clients += ',' 


def list_clients():
    global clients
    print(clients)


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 70)
    print('what would you like to do today?')
    print('[L]ist Client')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    


def _get_client_name():
    name_client = input(f'Wtha is the client name? ')
    name_client =name_client.capitalize()
    return name_client 


def _is_not_in_list():
    return print(f'Client is not in clients list')


# def _command_input():
#     command = input()
#     command = command.upper()
#     return command


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    
    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input(f'what is the updated client name: ')
        update_client(client_name, updated_client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name) 
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'. format(client_name))


    else:
        print('Invalid command'),
        # _print_welcome()
        # _command_input()



