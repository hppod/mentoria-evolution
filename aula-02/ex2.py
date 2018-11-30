# 2) Trabalhando com Listas, faça:

# a) Cria uma lista de valores inteiros com o nome e idades.
# b) Imprima apenas segundo elemento da lista.
# c) Imprima a quantidade de elementos da lista.
# d) Substitua o valor do segundo elemento da lista e imprima o resultado.
# e) Imprima apenas os valores do segundo elemento em diante.
# f) Remova qualquer elemento da lista e imprima o resultado.
# g) Defina uma lista chamada salarios com os valores : 900,1200,1500,800,12587,10000.
# h) Verifique se contém o valor 10000 na lista de salarios.
# i) Imprima o menor e maior valor da lista.
# j) Adicione o valor 7000 a lista.
# l) Extenda a lista com dois novos elementos utilizando apenas um método.
# m) Imprima o índice do elemento de valor 800 da lista de salarios.
# n) Faça uma ordenação dos valores da lista de salarios em ordem crescente e decrescente.

# PESSOAS
pessoas = ['Mariana, 19', 'André, 21', 'Ricardo, 25', 'Rafaela, 30']

pessoa1 = pessoas[1]
print(pessoas)

tamanho = len(pessoas)
print(tamanho)

pessoas[1] = 'Luísa, 26'
pessoa1 = pessoas[1]
print(pessoa1)

pessoas.remove('Ricardo, 25')
print(pessoas)

# SALÁRIOS
salarios = [900, 1200, 1500, 800, 12587, 10000]

print(10000 in salarios)

minim = min(salarios)
maxim = max(salarios)

print('Salário minimo:', minim, '| Salário máximo:', maxim)

salarios.append(7000)
print(salarios)

salarios = salarios + [657, 9856]
print(salarios)

idx = salarios.index(800)
print(idx)

salarios.sort()
print(salarios)

salarios.sort(reverse=True)
print(salarios)
