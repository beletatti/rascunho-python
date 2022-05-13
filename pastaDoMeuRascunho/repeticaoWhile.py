"""
WHILE EM PHYTON
UTULZA PARA REALIZAR ACOES ENQUANTO
UMA CONDICAO FOR VERDADEIRA
"""
#########################################################
x = 0
while x < 10:
    print(x)
    x = x + 1

print('Acabou !')
#########################################################
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

    print('Acabou !')
#########################################################
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

    print('Acabou !')
#########################################################
x - 0 #COLUNA

while x < 10:
    y = 0  # LINHA
    while y < 5:
        print(f'X vale {x} e {y}')
        y += 1
    x += 1

print('Acabou !!')
#########################################################
