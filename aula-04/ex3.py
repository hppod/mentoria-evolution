# 3) Trabalhando com dicionários:

# a) Crie um dicionário para armazenar o nome e a idade de pessoas, Exemplo: pessoas = {'Rodrigo':30, 'Fulana':18}
# b) Imprima a idade da pessoa "Fulana"
# c) Imprima as Chaves do dicionario criado anteriormente.
# d) Imprima os valores das chaves do dicionário
# e) Busque a chave "Felipe" se ela não existe insira esta e o valor 30 (obs: use o método setdefault())

pessoas = {'Luísa': 19, 'Fulana': 18}

idadeFulana = pessoas['Fulana']
print(idadeFulana)

keys = pessoas.keys()
print(keys)

values = pessoas.values()
print(values)

dflt = pessoas.setdefault('Felipe', 30)
print(dflt)

print(pessoas)
