# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:05:05 2021

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

####################################################################

#reduced_data = PCA(n_components=2).fit_transform(df_current)

#reduced_data = np.double(X_transformed)

#kmeans = KMeans(n_clusters=10, random_state=0).fit(reduced_data)


###################################################################

#sample_size = 100000

#reduced_data = X_transformed
db = DBSCAN(eps=0.5, min_samples=10).fit(X_transformed)

'''
                                                  
#%%

#Plot kmeans (https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-auto-examples-cluster-plot-kmeans-digits-py)

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
#plt.title(
#    "K-means clustering on the whole dataset (PCA-reduced data)\n"
#    "Centroids are marked with white cross"
#)
#plt.xlim(x_min, x_max)
#plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()



#%%


'''
#Plot dbscan https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
#####################
#reduced_sepsis = []
#reduced_no_sepsis = []
#labels_true = df_current["SepsisLabel"].tolist()
#labels_true = labels_true[0:sample_size]
#X = reduced_data[0:sample_size]




labels_true = df_current["SepsisLabel"].tolist()
#labels_true = labels_true[0:sample_size]
#X = reduced_data[0:sample_size]


#%%
#for j in range(len(lables)):
#    if lables_true[j] == 1:
#        reduced_sepsis.append(X_transformed[j])
#    else:
#        reduced_no_sepsis.append(X_transformed[j])
#%%    

##########################

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Adjusted Mutual Information: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X_transformed, labels))

# #############################################################################
# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X_transformed[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X_transformed[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title("Estimated number of clusters: %d" % n_clusters_)
plt.show()

'''