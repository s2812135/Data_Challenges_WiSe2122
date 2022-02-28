# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:21:56 2022

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
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)



df_nan_mean = df.fillna(df.mean())

#lables = df["SepsisLabel"].tolist()


#%%



def packmap_age(df_nan_mean, over_under):
    
    df_subset = []

    for i, row in df_nan_mean.iterrows():
        if row["Age"] >= 40 and over_under == "over":
            df_subset.append(row)
        elif row["Age"] < 40 and over_under == "under":
            df_subset.append(row)
            

    df_subset = pd.DataFrame(df_subset)
    
    ############################################################
    # initializing the pacmap instance
    # Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section
    embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

    # fit the data (The index of transformed data corresponds to the index of the original data)
    X_transformed = embedding.fit_transform(df_subset.values, init="pca")


    #plt.scatter(X_transformed[:, 0], X_transformed[:, 1], cmap="Spectral")
    #plt.show()

    ###########################################################

    reduced_sepsis = []
    reduced_no_sepsis = []
    lables = df_subset["SepsisLabel"].tolist()


    for j in range(len(lables)):
        if lables[j] == 1:
            reduced_sepsis.append(X_transformed[j])
        else:
            reduced_no_sepsis.append(X_transformed[j])

        
    ###########################################################

#    plt.scatter(reduced_sepsis[:, 0], X_transformed[:, 1], cmap="Spectral")

    plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
    plt.scatter(*zip(*reduced_sepsis), c="r")
    plt.show()
    return



#######################Zum Testen

df_nan_mean2 = df_nan_mean.head(n=1000)

over_under = "over"
packmap_age(df_nan_mean2, over_under)
