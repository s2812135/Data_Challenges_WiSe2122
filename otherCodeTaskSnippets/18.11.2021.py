# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:23:56 2021

@author: dariu
"""

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
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

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



'''
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

'''




#df_no_nan = df.dropna()

#df_nan_zwero = df.replace(np.NaN, 0)
#df_nan_zwero.head(n=50)

#df_nan_none = df.replace(np.NaN, None)
#df_nan_none.head(n=50)

###################################

df_nan_mean = df.fillna(df.mean())
#df_nan_mean.head(n=50)

###################################

#df_nan_none_2= df.where(pd.notnull(df), None)
#df_nan_mean.head(n=50)

#df.shape
#df.head(n=80)

############################################################
# initializing the pacmap instance
# Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section

#embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

# fit the data (The index of transformed data corresponds to the index of the original data)

#X_transformed = embedding.fit_transform(df_nan_mean.values, init="pca")

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

'''
#


'''
#plt.scatter(reduced_sepsis[:, 0], X_transformed[:, 1], cmap="Spectral")

plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral")
plt.scatter(*zip(*reduced_sepsis), c="r")
plt.show()

'''

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



######################################################################################
#18.11.2021

reduced_data = PCA(n_components=2).fit_transform(df_nan_mean)

kmeans = KMeans(n_clusters=5, random_state=0).fit(reduced_data)


#kmeans.labels_[:150]
#kmeans.cluster_centers_


#%%

#Plot (https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-auto-examples-cluster-plot-kmeans-digits-py)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = 0.4  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)

plt.plot(reduced_data[:, 0], reduced_data[:, 1], "k.", markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=169,
    linewidths=3,
    color="w",
    zorder=10,
)
plt.title(
    "K-means clustering on the whole dataset (PCA-reduced data)\n"
    "Centroids are marked with white cross"
)
#plt.xlim(x_min, x_max)
#plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()

#%%




