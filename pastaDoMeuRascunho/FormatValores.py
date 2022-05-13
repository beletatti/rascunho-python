"""
FORMATANDO VALORES COM MODIFICADORES

:s - Texto (string)
:d - Inteiro (int)
:f - Numeros de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais(float) :.2f
:(CARACTERE) (> ou <) (QUANTIDADE) (TTPO - s, d ou f)

> - ESQUERDA
> - DIREITA
SETA PRA CIMA - CENTRO
"""
###################################################
num1 = 10
num2 = 3
divisao = num1 / num2

print('{:.2f}'.format(divisao))
###################################################
num3 = 10

print(f'{num3:0>10}')
###################################################
nome = 'Richard Beletatti'
nome_format = '{:@>15}'.format(nome)
print(nome_format)
###################################################
nomeTest = "Richard Beletatti"

print(nomeTest.lower())   # TUDO MINUSCULA
print(nomeTest.upper())   # TUDO MAIUSCULA
print(nomeTest.title())   # PRIMEIRAS LETRAS MAIUSCULAS