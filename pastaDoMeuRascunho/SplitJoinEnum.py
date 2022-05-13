"""
SPLIT - SEPARA UMA STRING
JOIN - JUNTAR UMA LISTA
ENUM - ENUMERAR ELEMENTOS DA LISTA
"""
string = "O Brasil o pais do futebol, o Brasil e penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

###########################################################
string = ('O Brasil e penta.')
lista = string.split(',')
string2 = ','.join(lista)

###########################################################

for indice,valor in enumerate(lista):
    print(indice,valor)

###########################################################

lista = [
    [0,"Luiz"],
    [2,"Maria"],
    [4,"Pedro"],
]
for indice, nome in lista:
    print(indice, nome)

###########################################################

lista33 = ['Luiz', 'Maria','Joao']

for indice, nome in enumerate(lista33):
    print(indice, nome)
    
###########################################################