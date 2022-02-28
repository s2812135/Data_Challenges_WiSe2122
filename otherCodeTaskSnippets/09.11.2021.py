# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:01:49 2021

@author: dariu
"""


import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import pacmap
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import umap


path = "C:\\Users\dariu\\Documents\\Master Wirtschaftsinformatik\\Data Challenges\Data\\"

directorys = [
    ['training_setA/training/', 'p0'],
    ['training_setB/training_setB/', 'p1']
]

dfs_1 = []
dfs_2 = []
dfs_3 = []
dfs_4 = []
dfs_5 = []
dfs_6 = []
dfs_7 = []
dfs_8 = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
        if df_temp["Age"][1] <= 20:
            dfs_1.append(df_temp)
        elif df_temp["Age"][1] >= 20 and df_temp["Age"][1] < 30:
            dfs_2.append(df_temp)
        elif df_temp["Age"][1] >= 30 and df_temp["Age"][1] < 40:
            dfs_3.append(df_temp)
        elif df_temp["Age"][1] >= 40 and df_temp["Age"][1] < 50:
            dfs_4.append(df_temp)
        elif df_temp["Age"][1] >= 50 and df_temp["Age"][1] < 60:
            dfs_5.append(df_temp)
        elif df_temp["Age"][1] >= 60 and df_temp["Age"][1] < 70:
            dfs_6.append(df_temp)
        elif df_temp["Age"][1] >= 70 and df_temp["Age"][1] < 80:
            dfs_7.append(df_temp)
        elif df_temp["Age"][1] >= 80:
            dfs_8.append(df_temp)
       

#df = pd.concat(dfs)

dfs_1 = pd.concat(dfs_1)
dfs_2 = pd.concat(dfs_2)
dfs_3 = pd.concat(dfs_3)
dfs_4 = pd.concat(dfs_4)
dfs_5 = pd.concat(dfs_5)
dfs_6 = pd.concat(dfs_6)
dfs_7 = pd.concat(dfs_7)
dfs_8 = pd.concat(dfs_8)


imputation_dims = [
    'DBP',
    'HR',
    'O2Sat',
    'Temp',
    'SBP',
    'MAP',
    'Resp',
]
'''
for d in imputation_dims:
    mean = round(df[d].sum()/df.shape[0], 2)
    df.loc[df[d].isna(), d] = mean
    
'''
#
'''

for d in imputation_dims:
    mean = round(df[d].sum()/df.shape[0], 2)
    df.loc[df[d].isna(), d] = mean


'''

df_current = dfs_8

#%%
for d in imputation_dims:
    mean = round(df_current[d].sum()/df_current.shape[0], 2)
    df_current.loc[df_current[d].isna(), d] = mean

#%%

df_current = df_current.fillna(df_current.mean())


########################################################
#df_no_nan = df.dropna()

#df_nan_zwero = df.replace(np.NaN, 0)
#df_nan_zwero.head(n=50)

#df_nan_none = df.replace(np.NaN, None)
#df_nan_none.head(n=50)

#df_nan_mean = df.fillna(df.mean())
#df_nan_mean.head(n=50)

#df_nan_none_2= df.where(pd.notnull(df), None)
#df_nan_mean.head(n=50)

#df.shape
#df.head(n=80)

############################################################
# initializing the pacmap instance
# Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section

embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

# fit the data (The index of transformed data corresponds to the index of the original data)

X_transformed = embedding.fit_transform(df_current.values, init="pca")

###########################
#df_cut = df_nan_mean.head(n=50000)


#X_embedded = TSNE(n_components=2, learning_rate='auto',init='random').fit_transform(df_cut.values)
# visualize the embedding
#fig, ax = plt.subplots(1, 1, figsize=(6, 6))
#ax.scatter(X_transformed[:, 0], X_transformed[:, 1], cmap="Spectral", s=0.6)

############################
#reducer = umap.UMAP()
#embedding_umap = reducer.fit_transform(df_cut.values)

#plt.scatter(embedding_umap[:, 0], embedding_umap[:, 1], cmap="Spectral")
#plt.show()




'''
ax.scatter(*zip(*reduced_sepsis), color="b")
ax.scatter(*zip(*reduced_no_sepsis), color="r")
plt.show()
#%%
for j in range(50000):
    if lables[j] == 1:
        reduced_sepsis.append(embedding_umap[j])
    else:
        reduced_no_sepsis.append(embedding_umap[j])

#%%        
plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
plt.scatter(*zip(*reduced_sepsis), c="r")
plt.show()

#%% 
##############################

'''

'''

#plt.scatter(X_transformed[:, 0], X_transformed[:, 1], cmap="Spectral")
#plt.show()

reduced_sepsis = []
reduced_no_sepsis = []
lables = df["SepsisLabel"].tolist()


#%%
for j in range(len(lables)):
    if lables[j] == 1:
        reduced_sepsis.append(X_transformed[j])
    else:
        reduced_no_sepsis.append(X_transformed[j])
#%%        



'''


############################################

reduced_sepsis = []
reduced_no_sepsis = []
lables = df_current["SepsisLabel"].tolist()


#%%
for j in range(len(lables)):
    if lables[j] == 1:
        reduced_sepsis.append(X_transformed[j])
    else:
        reduced_no_sepsis.append(X_transformed[j])
#%%        




##############################################


#%%

#plt.scatter(reduced_sepsis[:, 0], X_transformed[:, 1], cmap="Spectral")

plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
plt.scatter(*zip(*reduced_sepsis), c="r")
plt.show()
#%%



'''
#%%
ax = plt.gca()
ax = plt.subplots(1, 1)
ax.scatter(*zip(*reduced_sepsis), color="b")
ax.scatter(*zip(*reduced_no_sepsis), color="r")
plt.show()
#%%
'''
#


'''
#############################################################
X_embedded = TSNE(n_components=2, learning_rate='auto',init='random').fit_transform(df.values)

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.scatter(X_transformed[:, 0], X_embedded[:, 1], cmap="Spectral", c=list(df.columns), s=0.6)

#############################################################
'''