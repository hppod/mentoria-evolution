lista = []

print(lista)

word = input("Digite uma palavra ")
integer = input("Digite um número ")
point = input("Digite um ponto flutuante ")

lista.append(word)
lista.append(int(integer))
lista.append(float(point))

print(lista)

print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))