# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:56:34 2021

@author: dariu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:44:26 2021

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

dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
        if df_temp["Age"][1] >= 40:
            dfs.append(df_temp)

df = pd.concat(dfs)

#df_no_nan = df.dropna()

#df_nan_zwero = df.replace(np.NaN, 0)
#df_nan_zwero.head(n=50)

#df_nan_none = df.replace(np.NaN, None)
#df_nan_none.head(n=50)

df_nan_mean = df.fillna(df.mean())
df_nan_mean.head(n=50)

#df_nan_none_2= df.where(pd.notnull(df), None)
#df_nan_mean.head(n=50)

#df.shape
#df.head(n=80)

############################################################
# initializing the pacmap instance
# Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section
embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

# fit the data (The index of transformed data corresponds to the index of the original data)
X_transformed = embedding.fit_transform(df_nan_mean.values, init="pca")

# visualize the embedding
#fig, ax = plt.subplots(1, 1, figsize=(6, 6))
#ax.scatter(X_transformed[:, 0], X_transformed[:, 1], cmap="Spectral", s=0.6)


plt.scatter(X_transformed[:, 0], X_transformed[:, 1], cmap="Spectral")
plt.show()

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
#plt.scatter(reduced_sepsis[:, 0], X_transformed[:, 1], cmap="Spectral")

plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
plt.scatter(*zip(*reduced_sepsis), c="r")
plt.show()


'''

#ax = plt.gca()
ax = plt.subplots(1, 1)
ax.scatter(*zip(*reduced_sepsis), color="b")
ax.scatter(*zip(*reduced_no_sepsis), color="r")
plt.show()



#############################################################
X_embedded = TSNE(n_components=2, learning_rate='auto',init='random').fit_transform(df.values)

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.scatter(X_transformed[:, 0], X_embedded[:, 1], cmap="Spectral", c=list(df.columns), s=0.6)

#############################################################
'''