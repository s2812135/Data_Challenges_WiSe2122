# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:45:17 2022

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

def start_pacmac_gender():
    path = ""

    directory = 1

    if(directory == 1):
        directorys = [
        ['training_setA/training/', 'p0'],
        ]
    if(directory == 2):
        directorys = [
        ['training_setB/training/', 'p0'],
        ]
    if(directory == 3):
        directorys = [
        ['training_setA/training/', 'p0'],
        ['training_setB/training/', 'p1']
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

    #######################Zum Testen


    #df_nan_mean2 = df.fillna(df.mean()).head(n=1000)
    #df_nan_mean2 = df.fillna(df.median()).head(n=1000)
    df_nan_mean2 = df.fillna(df.mean()).head(n=500)
    # df_nan_mean2 = df.fillna(df.interpolate()).head(n=1000) ? 


    packmap_gender(df_nan_mean2, 0)



def packmap_gender(df_nan_mean, gender):
    
    df_subset = []

    for i, row in df_nan_mean.iterrows():
        if row["Gender"] == gender:
            df_subset.append(row)
        else:
            pass
            #print("Problem")

    df_subset = pd.DataFrame(df_subset)
    print("df_subset")
    print(df_subset)
    ############################################################
    # initializing the pacmap instance
    # Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section
    embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 
    print("embedding")
    print(embedding)

    # fit the data (The index of transformed data corresponds to the index of the original data)
    X_transformed = embedding.fit_transform(df_subset.values, init="pca")
    print("X_transformed")
    print(X_transformed)


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
    print("reduced_sepsis")
    print(reduced_sepsis)
    print("reduced_no_sepsis")
    print(reduced_no_sepsis)
#    plt.scatter(reduced_sepsis[:, 0], X_transformed[:, 1], cmap="Spectral")

    plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
    plt.scatter(*zip(*reduced_sepsis), c="r")
    plt.show()
    return



