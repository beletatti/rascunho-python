'''
Operador Ternario
'''
logged_user = True

if logged_user:
    msg = "Usuario logado."
else:
    msg = "Usuario precisa logar."
print(msg)
#############################################
#TERNARIO
msg = 'Usuario Logado' if logged_user else 'Usuario precisa logar.'
print(msg)
#############################################
idade = 17

if idade >= 18:
    print("Pode acessar.")
else:
    print("Nao pode acessar.")
#############################################
#TERNARIO

e_de_maior = (idade >= 18)
msg = "Pode acessar" if e_de_maior else "nao pode acessar. "

print(msg)
