import numpy as np

#Importando a biblioteca e renomeando para fácil acesso.
##Numpy é uma biblioteca para trabalhar cm algebra linear.

minha_lista = [1, 2, 3]

r = np.array(minha_lista)

print('Uma matriz em array 1 dimensão.')
print(r)
#===========================================
print ('=*=' * 15)
print()

minha_matriz = [[1,2,3],[4,5,6],[7,8,9]]

r2 = np.array(minha_matriz)

print('Uma matriz em array 2 dimensões.')
print(r2)

#===========================================
print ('=*=' * 15)
print()
#Metodo 'arange' vai criar uma sequencia de números.

r3 = np.arange(0, 10)

print('Uma lista de 0 ate 9, com 10 elementos.')
print(r3)

#===========================================
print ('=*=' * 15)
print()

zeros_linha = np.zeros(3)
zeros_matriz = np.zeros((3,3))
ums_linha = np.ones(3)
ums_matriz = np.ones((3,3))

print('Uma linha de zeros.')
print(zeros_linha)
print()
print('Uma matriz de zeros.')
print(zeros_matriz)
print()
print('Uma linha de Ums.')
print(ums_linha)
print()
print('Uma matriz de Ums.')
print(ums_matriz)

#===========================================
print ('=*=' * 15)
print()

#Matriz identidade.

MI = np.eye(3,3)
print('Matriz Indentidade.')
print(MI)

#===========================================
print ('=*=' * 15)
print()

#Metodo 'linspace' é usado para criar listas com a opção de colocar a quantidade de números dentro do parâmetro devidamente espaçados.

r4 = np.linspace(0,10,4)
print('Lista devidamente espaçada.')
print(r4)

#===========================================
print ('=*=' * 15)
print()

#Metodo 'random.rand' vai criar numeros aleatorios baseados em uma distribuição uniforme.
#Caso queira fazer uma matriz multi dimensional nao é nescessario passar uma tupla, so add um elemento extra.
r5 = np.random.rand(5)
r6 = np.random.rand(5,5)
r7 = np.random.rand(5,5,3)
print('Matriz 1 dimensão random de 0 a 1 com 5 Elementos.')
print(r5)
print()
print('Matriz 2 dimensões random de 0 a 1 com 25 Elementos.')
print(r6)
print()
print('Matriz 3 dimensões random de 0 a 1.')
print(r7)

#===========================================
print ('=*=' * 15)
print()

#Metodo 'random.randn' vai criar numeros aleatorios baseados em uma distribuição normal.

r8 = np.random.randn(4)

print('Matriz 1 dimensão random com 4 Elementos.')
print(r8)

#===========================================
print ('=*=' * 15)
print()

r9 = np.random.randint(0,100,10)

print('Matriz 1 dimensão random com numeros inteiros de 0 ate 100 com 10 Elementos.')
print(r9)

#===========================================
print ('=*=' * 15)
print()

r10 = np.round(np.random.rand(5)*100, 0)

print('Lista de numeros inteiros com o metodo "rand".')
print(r10)

#===========================================
print ('=*=' * 15)
print()

#Metodo 'reshape' usado para reformar uma matriz.

arr = np.random.rand(25)
print('matriz de 25.')
print(arr)
print()

arr2 = arr.reshape((5,5))

print('Matriz de 5 por 5.')
print(arr2)

#Pode ser usado o atributo 'arr.shape' para consultar o formato da matriz.
#Pode ser usado o atributo 'arr.max' para consultar o maior valor da matriz.
#Pode ser usado o atributo 'arr.min' para consultar o menor valor da matriz.
#Pode ser usado o atributo 'arr.argmax' para consultar o indice no qual o maior valor se encontra.
#Pode ser usado o atributo 'arr.argmin' para consultar o indice no qual o menor valor se encontra.

#===========================================
print ('=*=' * 15)
print()

input('Sair')