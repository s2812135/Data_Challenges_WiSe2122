# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:28:31 2022

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


path = ""

directorys = [
    ['../training_setA/training/', 'p0'],
    ['../training_setB/training/', 'p1']
]


dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)
print("das ist df")
print(df)


df_nan_mean = df.fillna(df.mean())
#df_nan_mean = df.fillna(df.median())
print("das ist df_nan_mean")
print(df_nan_mean)

#lables = df["SepsisLabel"].tolist()


#%%



def packmap_all(df_nan_mean):
    

    
    ############################################################
    # initializing the pacmap instance
    # Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section
    embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 
    print("das ist embedding")
    print(embedding)
    # fit the data (The index of transformed data corresponds to the index of the original data)
    X_transformed = embedding.fit_transform(df_nan_mean.values, init="pca")
    print("das ist X_transformed")
    print(X_transformed)


    #plt.scatter(X_transformed[:, 0], X_transformed[:, 1], cmap="Spectral")
    #plt.show()

    ###########################################################

    reduced_sepsis = []
    reduced_no_sepsis = []
    lables = df_nan_mean["SepsisLabel"].tolist()
    print("das ist lables")
    print(lables)


    for j in range(len(lables)):
        if lables[j] == 1:
            reduced_sepsis.append(X_transformed[j])
        else:
            reduced_no_sepsis.append(X_transformed[j])

    print("Das ist reduced_sepsis")  
    print(reduced_sepsis)
    print("Das ist reduced_no_sepsis")
    print(reduced_no_sepsis)
    ###########################################################

#    plt.scatter(reduced_sepsis[:, 0], X_transformed[:, 1], cmap="Spectral")

    plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
    plt.scatter(*zip(*reduced_sepsis), c="r")
    plt.show()
    return



#######################Zum Testen
#Einmal
df_nan_mean2 = df_nan_mean

packmap_all(df_nan_mean2)
