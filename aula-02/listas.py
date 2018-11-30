# Estrutura de Dados - Listas
# Sintaxe: nome = [elementos]

idades = [25, 38, 18, 47]
print(idades)
print(type(idades))

endereco = ['Rua dos Fulanos, Belo Horizonte.', 2500]
print(endereco)
print(type(endereco))

#Acessando elementos da lista
rua = endereco[0]
print(rua)
numero = endereco[1]
print(rua, numero)

#Atualizando elementos da lista
endereco[1] = 2750
print(endereco)
numero = endereco[1]
print(rua, numero)