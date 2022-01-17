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
    print("Nome:", contato)
    print("Telefone:", AGENDA[contato]['telefone'])
    print("E-Mail:", AGENDA[contato]['email'])
    print("Endereco:", AGENDA[contato]['endereco'])
    print("______________")

buscar_contato('Graziela')