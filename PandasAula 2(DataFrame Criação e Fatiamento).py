import numpy as np
import pandas as pd

# DataFrame são conjuntos de Series
np.random.seed(101)

df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print()

#Fatiamento
coluna_w = df['W']
print(coluna_w)
print()

#Adicionando
df['NEW'] = df['W'] + df['X']
print(df)
print()

#Excluindo
df.drop('NEW', axis=1)#exclui a coluna
df.drop('A', axis=0)#exclui a linha

#Para confirmar as modificações tem q usar o 'inplace=True' no final.

#df.drop('A', axis=0, inplace=True)#exclui a linha definitivamente.
#df.drop('NEW', axis=1, inplace=True)#exclui a coluna definitivamente.

#Localizando

# loc é usado para consulta pelo nome de linha e coluna
a = df.loc['A','NEW']
print(a)
print()

# iloc é usado para consulta pelos numetos dos indices.
b = df.iloc[1:4, 2:]
print(b)

input('Sair')