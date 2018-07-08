import numpy as np


#Arreys de uma dimensão

arr = np.arange(0,30,3)

print(arr)
print()

#Pegando o valor do indice '2'.
t1 = arr[2]
print(t1)
print()

#Pegando do 2 ate o 5 (onde o 5 nao esta incluido).
t2 = arr[2:5]
print(t2)
print()

#Pegando do inicial ate o 5 (onde o 5 nao esta incluido).
t3 = arr[:5]
print(t3)
print()

#Pegando todos os elementos do 2 endiante.
t4 = arr[2:]
print(t4)
print()

#Alterando os valores referente aos elementos.
arr[2:] = 100
arr[:2] = 100
arr[2:2] = 100
arr[2] = 100

print('=*=' *15)
print()
#Arreys multi dimensionais.

arr2 = np.arange(50).reshape(5,10)
print(arr2)
print()

#Primeiro colchete indica as linhas, segundo os da coluna
#e1 = arr2[:3][:] or e1 = arr2[:3,:]
e1 = arr2[:3][:]
print(e1)
print()

#Metodo 'copy()' faz um novo array com as informaçoes da sua base.

arr3 = arr2[:3].copy()
print(arr3)
print()

input('Sair')