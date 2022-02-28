# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:48:30 2021

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

# = [Gender]

df_temp = pd.read_csv(path + 'training_setA/training/' + "p000001.psv", skiprows=0, sep='|')

print(df_temp)

dfs = df_temp["Gender"][0]
print(dfs)

#df_femp[]

'''
for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
        dfs.append(df_temp)

df = pd.concat(dfs)

'''