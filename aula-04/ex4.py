# 4) Estruturas condicionais:

# a) Verifique se 5 é maior que 1, se sim, imprima "5 é maior que 1"
# b) crie as variávies x1 e y1, defina dois valores quaisquer para as duas variáveis. Verifique se x1 é maior que y1. Se sim, imprima "x1 é maior que y1", senão imprima: "y1 é maior que x1"
# c) Crie uma lista de valores como [2,3,4,5,6,7] e faça um loop para imprimir todos os valores na tela multiplicados por 2.

if 5 > 1:
    print('5 é maior que 1')

x1 = 29
y1 = 75

if x1 > y1:
    print('x1 é maior que y1')
else:
    print('y1 é maior que x1')

for i in [2, 3, 4, 5, 6, 7]:
    print("%s * 2 =" % i, i * 2)
