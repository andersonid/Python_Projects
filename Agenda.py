AGENDA = {}

AGENDA['Anderson'] = {
    'telefone': '11-970355726',
    'email': 'nobre.it@gmail.com',
    'endereco': 'Rua Taquacetuba, 201',
}

AGENDA['Graziela'] = {
    'telefone': '11-972204544',
    'email': 'graziela.claro@gmail.com',
    'endereco': 'Rua Taquacetuba, 171',
}

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    print('_____________________________________________')
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('E-Mail:', AGENDA[contato]['email'])
    print('Endereco:', AGENDA[contato]['endereco'])
    print('_____________________________________________')
    print('')


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('###################################################')
    print('Contato {} adicionado com sucesso!'.format(contato))
    print('###################################################')
    print('')


print('')
mostrar_contatos()
print('')
incluir_contato('Joao', '11-965754568', 'jao@zica.co', 'Rua dos Bobos, 0')
buscar_contato('Joao')
