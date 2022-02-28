# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 10:27:53 2022

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
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
#import sklearn.cluster
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.cluster import OPTICS, cluster_optics_dbscan
import matplotlib.gridspec as gridspec
from sklearn.cluster import SpectralCoclustering
from sklearn.metrics import consensus_score
from sklearn.cluster import SpectralBiclustering
from sklearn import svm
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import NearMiss
from imblearn.pipeline import make_pipeline
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import RocCurveDisplay




path = "C:\\Users\dariu\\Documents\\Master Wirtschaftsinformatik\\Data Challenges\Data\\"

directorys = [
    ['training_setA/training/', 'p0'],
    ['training_setB/training_setB/', 'p1']
]
#%%
dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)
labels_true = df["SepsisLabel"].tolist()

#%%





imputation_dims = [
    'DBP',
    'HR',
    'O2Sat',
    'Temp',
    'SBP',
    'MAP',
    'Resp',
]

for d in imputation_dims:
    mean = round(df[d].sum()/df.shape[0], 2)
    df.loc[df[d].isna(), d] = mean
    
  

####################################################    
    
df = df.drop(columns=["SepsisLabel"])

df_current = df.fillna(df.mean())






X_train, X_test, y_train, y_test = train_test_split(df_current, labels_true, test_size=0.2)

#%%



X_train_ss = X_train[0:int(0.2*len(X_train))]
y_train_ss = y_train[0:int(0.2*len(y_train))]


# Create a pipeline
pipeline = make_pipeline(
    NearMiss(version=2), svm.SVC())

pipeline.fit(X_train_ss, y_train_ss)

# Classify and report the results
print(classification_report_imbalanced(y_test, pipeline.predict(X_test)))


#%%

metrics.plot_roc_curve(pipeline, X_test, y_test) 

plt.show()