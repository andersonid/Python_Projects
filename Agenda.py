import os

LEADS = {}

LEADS['Anderson'] = {
    'telefone': '11-970355726',
    'email': 'nobre.it@gmail.com',
}

LEADS['Graziela'] = {
    'telefone': '11-972204544',
    'email': 'graziela.claro@gmail.com',
}


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def mostrar_todos():
    print('===================================')
    print('     MOSTRANDO TODOS OS LEADS ')
    print('===================================')

    for lead in LEADS:
        print(' Nome:', lead)
        print(' Telefone:', LEADS[lead]['telefone'])
        print(' E-mail:', LEADS[lead]['email'])
        print('===================================')


def buscar_lead(lead):
    clearConsole()
    print('===================================')
    print('    MOSTRANDO LEAD:', lead)
    print('===================================')
    print(' Telefone:', LEADS[lead]['telefone'])
    print(' E-mail:', LEADS[lead]['email'])
    print('===================================')
    buscar_lead(input('Digite o nome a pesquisar: '))

def add_lead(lead, telefone, email):
    LEADS[lead] = {
        'telefone': telefone,
        'email': email,
    }


buscar_lead(input('Digite o nome a pesquisar: '))
# mostrar_todos()
