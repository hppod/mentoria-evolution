# Trabalhando com strings
frase = "A maldição do Python!"
print(frase)

# Vetor de caracteres
# Indices iniciam em 0

# Posição exata
print(frase[0])
print(frase[2])

# Intervalo de posições
print(frase[0:10])

# Intervalo de posições até o final da string
print(frase[14:])

# Métodos
# lower() - converte a string para minusculo
print(frase.lower())

# upper() - converte a string para maiusculo
print(frase.upper())

# capitalize() - converte apenas o primeiro caractere para maiusculo
print(frase.capitalize())

# islower() - retorna true caso todos os caracteres da string sejam minusuculos
print(frase.islower())

# split() - quebra a string em uma lista de caracteres
# é possível passar parametros de quebra dentro do metodo split. se não o fizer, ele quebrara a string pelos espaços em branco
print(frase.split())

# count() - retorna a quantidade de vezes que uma string foi passada por parametro
print(frase.count('Python'))

# len - conta quantos caracteres a string possui
print(len(frase))
