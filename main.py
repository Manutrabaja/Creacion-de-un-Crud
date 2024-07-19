
clients = 'pablo, ricardo,'

def create_client(client_name):
    global clients

    clients += client_name 
    _add_coma()


def _add_coma():
    global clients
    
    clients += ', ' 


def list_clients():
    global clients

    print(clients)


def _print_wolcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')

if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    
    if command == 'C':
        client_name = (input(f'Wtha is the client name? '))
        create_client(client_name)
        list_clients()
    elif command =='D':
        pass
    else:
        prin('Invalid command')
        _print_welcome()

    print(clients)


