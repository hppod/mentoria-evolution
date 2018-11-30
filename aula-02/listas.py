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

#Operações com listas
#Criando uma nova lista
nomes = ['Felipe', 'João', 'Maria']
print(nomes)

#Contando elementos da lista
cntd = len(nomes)
print("A lista possui",cntd, "elementos")

#Verificando a existência de elementos na lista
print('Felipe' in nomes)
print('Luísa' in nomes)

#Valores máximos e minimos
maxim = max(nomes)
print(maxim)
minim = min(nomes)
print(minim)

#Concatenando listas
print(nomes)
nomes + ['José', 'Carla']
nomes = nomes + ['José', 'Carla']
print(nomes)

#Adicionando novos elementos
nomes.append('Marcelo')
print(nomes)