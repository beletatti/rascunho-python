'''
usuario = input('Digite seu usuario: ')
qtd_caracter = len(usuario)
print(usuario,qtd_caracter, type(qtd_caracter))

if qtd_caracter < 6:
    print('you need six caracter')
else:
    print('Voce foi cadastrado no sistema')
'''
#------------------------------------------------------------------------

string1 = input('digite alguma coisa ')
string2 = input('digite alguma coisa ')

print(f'a quantidade total de caracteres digitados foi {len(string1) + len(string2)}')