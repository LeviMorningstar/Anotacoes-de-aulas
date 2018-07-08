import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])

df.index.names = ['Grupo', 'Numero']

print(df)

# usar o 'df.xs()' quando estiver com multiniveis.


input('Sair')