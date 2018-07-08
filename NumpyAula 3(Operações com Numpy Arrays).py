import numpy as np

#Sempre feito indice por indice
arr = np.arange(0, 16)

print('Soma.')
t1 = arr + arr
print(t1)
print()

print('Subtração.')
t2 = arr - arr
print(t2)
print()

print('Divisão.')
t3 = (arr / arr)
print(t3)
print()

print('Multiplicação.')
t4 = arr * arr
print(t4)
print()

print('Exponenciação')
t4 = arr ** arr
print(t4)
print()

#Sempre feito indice por indice
#arr + 10
#arr - 10
#arr / 10
#arr * 10
#arr ** 10


#Metodos do Numpy

#np.sqrt(arr) calcula raiz quadrada
#np.exp(arr) calcula exponenciação
#np.mean(arr) calcula a media
#np.std(arr) calcula o padrao
#np.sin(arr) calcula o seno
#np.max(arr) maximo
#np.mim(arr) minimo


input('Sair')