'''
LISTAS EM PYTHON
FATIAMENTO
APPEND, INSERT, POP, DEL, CLEAR, EXTEND, MIN, MAX e RANGE
'''

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)  # mesma coisa que fazer -> l3 = l1 + l2

l2.append('b')  # Add um novo valor na lista

l2.insert(0,'banana')  # insert o valor no Indice que deseja

l2.pop()  # deleta o ultimo indice da lista

del(l2[0])  #  deleta o indice que desejar

print(max(l2))  # Max pega maior valor da lista

print(min(l2))  # Min pega o menor valor da lista

