"""
* CRIAR VARAVEIS PARA NOME, IDADE
* ALTURA E PESO DE UMA PESSOA
* CRIAR VARIAVEL COM O ANO ATUAL
* OBTER O ANO DE NASCIMENTO DA PESSOA (BASEADO NA IDADE E NO ANO ATUAL)
* OBTER O IMC DA PESSOA COM 2 CASAS DECIMAIS (PESO E NA ALTURA DA PESSOA)
* EXIBIR UM TEXTO COM TODOS OS VALORES NA TELA USANDO F-STRINGS(COM AS CHAVES)
"""

nome = "Richard"
idade = 22
altura = 1.80
peso = 97
ano_Atual = 2022
anoNascimento = ano_Atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem  {idade} anos, sua altura {altura} e peso {peso} seu imc e de {imc:.2f}')

