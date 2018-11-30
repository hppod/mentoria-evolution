# Estruturas Condicionais e Loops
#     Controles de fluxo
#     Sintaxe
#     if<condicao>:
#         instruções

if 10 > 1:
    print('O número é maior que 10')

    # Sintaxe
    # if<condicao>:
    #     instruções
    # else:
    #     instruções

x = 10
y = 1

if x > y:
    print('O número em X é maior que em Y')
else:
    print('O número em Y é maior que em X')


# Loops FOR
#     Sintaxe: for <variavel> in <condicao>: instruções

for i in [1, 2, 3, 4, 5]:
    print("Valor: %s" % i)
    print(i+2)

for c in "Python é uma linguagem de programação":
    print(c)

# Loops FOR aninhados
    # Sintaxe
    # for <variavel> in <condicao>
    #     for <variavel> in <condicao>

for i in ['1a Fase', '2a Fase', '3a Fase']:
    print(i)
    for y in ['manhã', 'tarde', 'noite']:
        print(y)
    print(' ')

# Loop while
#     Sintaxe
#     while <condicao>
#         instruções

i = 0
while i < 10:
    print(i)
    i = i + 1
