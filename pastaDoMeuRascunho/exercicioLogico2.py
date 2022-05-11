"""
1 Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

2 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

3 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
#############################################################################################
# 1
numero = input("Digite um numero ")

if not numero.isdigit():
    print("Nao e numero inteiro")
else:
    numero = int(numero)

if not numero % 2 == 0:
    print(f'{numero} Este numero e impar ')
else:
    print(f'{numero} Este numero e par ')

#############################################################################################