import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
minha_lista= [10, 20, 30]
#arr = np.array([10, 20, 30])
#d = {'a':10, 'b':20, 'c':30}

s = pd.Series(data=minha_lista, index=labels)

print(s)
print()
#====================================
print('=*='*15)
print()

ser1 = pd.Series([1, 2, 3, 4], index=['EUA', 'Alemanha', 'URSS', 'Japão'])
print()
print(ser1)

ser2 = pd.Series([1, 2, 3, 4], index=['EUA', 'Alemanha', 'Itália', 'Japão'])
print()
print(ser2)

t = ser1 + ser2
print()
print(t)

input('Sair')
