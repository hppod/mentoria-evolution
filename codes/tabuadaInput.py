print("Tabuada")

entrada = input("Qual tabuada você quer?: ")

print("Tabuada do %s" % entrada)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("%s * %s =" % (entrada, i), int(entrada) * i)
