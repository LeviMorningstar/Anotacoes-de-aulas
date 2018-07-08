import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())

bol = df > 0

print(df[bol])
print()

df = df[df['W'] >0]

print(df)

# o 'and' nao consegue tratar Series entao o '&' entra no lugar dele.
# o 'or' nao consegue tratar Series enttao o '|' entra no lugar dele.

df.reset_index(inplace=True)

print(df)
print()

col ='RS RJ SP AM'.split()

df['Estado'] = col
df.set_index('Estado', inplace=True)


print(df)

input('Sair')