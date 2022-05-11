"""
FORMATACAO STRING
nome = "richao"
idade = 22
altura = 1.80
peso = 97
imc = peso / (altura ** 2)  # ALTURA ELEVADO A DOIS E DIVIDO POR PESO

print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')  #  :.2f -> ESTA DIZENDO QUANTAS CASA DECIMAL E' PARA TER NA VARIAVEL IMC.
print('{} tem {} anos de idade e seu imc e {}'.format(nome, idade, imc))
"""