# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:03:45 2021

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
#############################################

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
    
df_current = df.fillna(df.mean())



###########################################################

#df_current = df  
##############################

############################################################
# initializing the pacmap instance
# Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section

embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

# fit the data (The index of transformed data corresponds to the index of the original data)

X_transformed = embedding.fit_transform(df_current.values, init="pca")



#############################################################

clust = OPTICS(min_samples=10, xi=0.75, min_cluster_size=10)
sample_size = 100000
# Run the fit
clust.fit(X_transformed[0:sample_size])

##############################################################

space = np.arange(len(X_transformed[0:sample_size]))
reachability = clust.reachability_[clust.ordering_]
labels = clust.labels_[clust.ordering_]

#print(min(clust.labels_))
#print(max(clust.labels_))
unique_labels = set(clust.labels_)


#print(len(unique_labels)-1)
#print(len(unique_labels)-1)

###############################################################
#%%


labels_050 = cluster_optics_dbscan(
    reachability=clust.reachability_,
    core_distances=clust.core_distances_,
    ordering=clust.ordering_,
    eps=0.5,
)
labels_200 = cluster_optics_dbscan(
    reachability=clust.reachability_,
    core_distances=clust.core_distances_,
    ordering=clust.ordering_,
    eps=0.4,
)

plt.figure(figsize=(10, 7))
G = gridspec.GridSpec(2, 3)
ax1 = plt.subplot(G[0, :])
ax2 = plt.subplot(G[1, 0])
ax3 = plt.subplot(G[1, 1])
ax4 = plt.subplot(G[1, 2])

# Reachability plot
#colors = ["g.", "r.", "b.", "y.", "c."]
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
#for klass, color in zip(range(0, 5), colors):
#for klass, color in zip(range(len(unique_labels)), colors):
for klass, color in zip(range(-1,len(unique_labels)-1), colors):
    Xk = space[labels == klass]
    Rk = reachability[labels == klass]
    ax1.plot(Xk, Rk, color, alpha=0.3)
ax1.plot(space[labels == -1], reachability[labels == -1], "k.", alpha=0.3)
ax1.plot(space, np.full_like(space, 2.0, dtype=float), "k-", alpha=0.5)
ax1.plot(space, np.full_like(space, 0.5, dtype=float), "k-.", alpha=0.5)
ax1.set_ylabel("Reachability (epsilon distance)")
ax1.set_title("Reachability Plot")

# OPTICS
#colors = ["g.", "r.", "b.", "y.", "c."]
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
#for klass, color in zip(range(0, 5), colors):
for klass, color in zip(range(-1,len(unique_labels)-1), colors):
    Xk = X_transformed[0:sample_size][clust.labels_ == klass]
    ax2.plot(Xk[:, 0], Xk[:, 1], color, alpha=0.3)
ax2.plot(X_transformed[0:sample_size][clust.labels_ == -1, 0], X_transformed[0:sample_size][clust.labels_ == -1, 1], "k+", alpha=0.1)
ax2.set_title("Automatic Clustering\nOPTICS")

# DBSCAN at 0.5
#colors = ["g", "greenyellow", "olive", "r", "b", "c"]
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
#for klass, color in zip(range(0, 6), colors):
for klass, color in zip(range(-1,len(unique_labels)-1), colors):
    Xk = X_transformed[0:sample_size][labels_050 == klass]
    ax3.plot(Xk[:, 0], Xk[:, 1], color, alpha=0.3, marker=".")
ax3.plot(X_transformed[0:sample_size][labels_050 == -1, 0], X_transformed[0:sample_size][labels_050 == -1, 1], "k+", alpha=0.1)
ax3.set_title("Clustering at 0.5 epsilon cut\nDBSCAN")

# DBSCAN at 2.
#colors = ["g.", "m.", "y.", "c."]
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
#for klass, color in zip(range(0, 4), colors):
for klass, color in zip(range(-1,len(unique_labels)-1), colors):
    Xk = X_transformed[0:sample_size][labels_200 == klass]
    ax4.plot(Xk[:, 0], Xk[:, 1], color, alpha=0.3)
ax4.plot(X_transformed[0:sample_size][labels_200 == -1, 0], X_transformed[0:sample_size][labels_200 == -1, 1], "k+", alpha=0.1)
ax4.set_title("Clustering at 0.4 epsilon cut\nDBSCAN")

plt.tight_layout()
plt.show()