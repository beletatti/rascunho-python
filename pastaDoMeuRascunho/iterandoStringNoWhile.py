'''
ITERANDO STRINGS COM WHILE
'''
#######################################################################
frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_String = ''

while contador < tamanho:
     #print(frase[contador], contador)
     nova_String += frase[contador]
     contador += 1

print(nova_String)
#######################################################################
while contador < tamanho:
    letra = frase[contador]
    if letra == 'r':
        nova_String += 'R'
    else:
        nova_String += letra
    contador += 1
print(nova_String)
#######################################################################
