# 9) Sobre os objetos Strings, faça:

# a) Defina uma variavel com a string: "Python é uma maldição!" e imprima
# b) Imprima o primeiro caracter da variavel.
# c) Imprima os valores do primeiro caracter até o 6.
# d) Faça a contagem de todos os caracteres utilizando uma única linha de comando.
# e) Faça uma contagem de quantas vezes a palavra dados aparece na seguinte frase:
# "dados é o novo petróleo, em Deus eu confio, para o resto me traga dados.."
# Obs: Crie uma variável chamada "frase" com a frase acima.
# f) Substitua o primeiro caracter da frase acima para maiúsculo
# g) Quebre as palavras da frase separado por virgula, criando uma lista.

py = "Python é uma maldição!"
print(py)
print(py[0])
print(py[0:6])
print(len(py))

# e

frase = 'dados são o novo petróleo, em Deus eu confio, para o resto me traga dados'
print(frase.count('dados'))
print(frase.capitalize())
print(frase.split(','))
