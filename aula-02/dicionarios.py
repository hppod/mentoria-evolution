# Estrutura de Dados - Dicionários
#     Objeto do tipo Chave e Valor
#     Sintaxe: nome={'chave':'valor'}

dic = {'nome': 'Rodrigo'}
print(dic)

pessoas = {
    'Felipe': 30, 'Fulana': 18, 'Maria': 55, 'José': 80,
    'valores': [1, 3.5, 400, 5, 6],
    'pesos': {'Felipe': 68, 'Fulana': 55}
}
print(pessoas)

# Acessando valores a partir de uma chave
js = pessoas['José']
print(js)

pesos = pessoas['pesos']
print(pesos)

# Dicionários aninhados
pessoas = {
    'Felipe': {'Idade': 30, 'Cidade': 'Belo Horizonte', 'Peso': 65},
    'valores': [1, 3.5, 400, 5, 6],
}
print(pessoas)

# Acessando chaves especificas
cidfel = pessoas['Felipe']['Cidade']
print(cidfel)
pesfel = pessoas['Felipe']['Peso']
print(pesfel)

Cadastro_pessoas = {
    'Clientes': {'Cliente_01': {'Nome': 'Rodrigo',
                                'Idade': 30,
                                'Cidade': 'Belo Horizonte',
                                'Peso': 65
                                },
                 'Cliente_02': {'Nome': 'Felipe',
                                'e-mail': 'felipe10@gmail.com'
                                },
                 },
    'valores': [1, 3.5, 400, 5, 6]
}

cliente_01 = Cadastro_pessoas['Clientes']['Cliente_01']
print(cliente_01)
cliente_01_cidade = Cadastro_pessoas['Clientes']['Cliente_01']['Cidade']
print(cliente_01_cidade)
cliente_02 = Cadastro_pessoas['Clientes']['Cliente_02']
print(cliente_02)

keys = pessoas.keys()
print(keys)

values = pessoas.values()
print(values)

get = pessoas.get('Juca', 'Não existe')
print(get)

setdflt = pessoas.setdefault('Marcos',40)
print(setdflt)

items = pessoas.items()
print(items)