import pandas as pd
import dask as dd
import io
import numpy as np
import utils.limpieza as limpieza
df = pd.read_csv('Data_Clientes.csv')

##limpieza de varaibles
print((df['seg_un'].isna().sum())/(len(df['seg_un'])))

### esto es lo mejor para probar

df1 = limpieza.f_fillna(df)

print((df1['seg_un'].isna().sum())/(len(df1['seg_un'])))
