# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

dset = pd.read_csv(r'D:\chronic_kidney_disease_updated.csv')

print(dset)
# Qs - 1
print(dset.columns)

# Qs - 2
print(dset[0:5])

# Qs - 3
print(dset.dm.unique())

# Qs - 4
def change_val(tup,dset):
    for i in tup:
        dset.replace(to_replace=i, value=np.nan, inplace=True)

change_val(( "\t"," ","?"),dset)

print(dset.dm.unique())

print(dset.rbc.unique())


# Qs - 5
def change_datatype():
    con_col = ['age', 'bp', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']
    for i in con_col:
        dset[i]= pd.to_numeric(dset[i], errors='coerce')
change_datatype()

print('age','bp')
print(dset[['age','bp']])


print(dset['rbc'])

print(dset['classs'])

# Qs - 6
ckd_val = dset[dset.classs=='ckd']
ckd_val['rbc'].value_counts().plot(kind='bar')
plt.show()

# Qs - 7
print(ckd_val['bp'].max())

# Qs - 8
dset.to_csv(path_or_buf="D:/clean_chronic_kidney_disease_updated.csv")       
          
