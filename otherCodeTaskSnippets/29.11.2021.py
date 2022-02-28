# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:51:20 2021

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



#df = df[["HR", "O2Sat", "Temp", "SBP", "MAP", "DBP", "Resp", "EtCO2"]]

#df = df[["Age", "Gender", "Unit1", "Unit2", "HospAdmTime", "ICULOS"]]


#labels_gender = df["Gender"].tolist()
#labels_unit1 = df["Unit1"].tolist()
#labels_unit2 = df["Unit2"].tolist()
#############################################

#%%

df = df[[
    "BaseExcess",
    "HCO3",
    "FiO2",
    "pH",
    "PaCO2",
    "SaO2",
    "AST",
    "BUN",
    "Alkalinephos",
    "Calcium",
    "Chloride",
    "Creatinine",
    "Bilirubin_direct",
    "Glucose",
    "Lactate",
    "Magnesium",
    "Phosphate",
    "Potassium",
    "Bilirubin_total",
    "TroponinI",
    "Hct",
    "Hgb",
    "PTT",
    "WBC",
    "Fibrinogen",
    "Platelets"
    ]]

#%%

#############################################

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

####################################################    
    
df_current = df.fillna(df.mean())

#df_current = df.fillna(2)

###########################################################

#df_current = df  
##############################

#85 labels_pred?



def calc_scores(X, labels_true, labels_pred):
    rand_score = metrics.rand_score(labels_true, labels_pred)
    adjusted_rand_score = metrics.adjusted_rand_score(labels_true, labels_pred)
    adjusted_mutual_info_score = metrics.cluster.adjusted_mutual_info_score(labels_true, labels_pred)
    silhouette_score = metrics.silhouette_score(X, labels_pred, metric='euclidean', sample_size=None, random_state=None)
    print("Rand Score: " , str(rand_score) + "\n" + 
         "Adjusted Rand Score: " , str(adjusted_rand_score) + "\n"  
          "Adjusted Mutual Information Score: " + str(adjusted_mutual_info_score) + "\n"  
          "Silhouette Score: " , str(silhouette_score) + "\n"  
         )




############################################################
# initializing the pacmap instance
# Setting n_neighbors to "None" leads to a default choice shown below in "parameter" section

embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

# fit the data (The index of transformed data corresponds to the index of the original data)

X_transformed = embedding.fit_transform(df_current.values, init="pca")

####################################################################

#reduced_data = PCA(n_components=2).fit_transform(df_current)

#reduced_data = np.double(X_transformed)


#X_transformed = np.double(X_transformed)
#kmeans = KMeans(n_clusters=6, random_state=0).fit(X_transformed)


###################################################################

sample_size = 100000
db = DBSCAN(eps=0.55, min_samples=10).fit(X_transformed[0:sample_size])

'''
                                                  
#%%

#Plot kmeans (https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-auto-examples-cluster-plot-kmeans-digits-py)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = 0.4  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = X_transformed[:, 0].min() - 1, X_transformed[:, 0].max() + 1
y_min, y_max = X_transformed[:, 1].min() - 1, X_transformed[:, 1].max() + 1
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

plt.plot(X_transformed[:, 0], X_transformed[:, 1], "k.", markersize=2)
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

sample_size = 100000
calc_scores(X_transformed[0:sample_size], labels_true[0:sample_size], kmeans.labels_[0:sample_size])

#%%

'''

################################################################################################


#Plot dbscan https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
#####################
#reduced_sepsis = []
#reduced_no_sepsis = []
#labels_true = df_current["SepsisLabel"].tolist()
#labels_true = labels_true[0:sample_size]
#X = reduced_data[0:sample_size]




#labels_true = df_current["SepsisLabel"].tolist()
#labels_true = labels_true[0:sample_size]
#X = reduced_data[0:sample_size]


#X_transformed = X_transformed[0:sample_size]


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
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true[0:sample_size], labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true[0:sample_size], labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true[0:sample_size], labels))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true[0:sample_size], labels))
print(
    "Adjusted Mutual Information: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true[0:sample_size], labels)
)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X_transformed[0:sample_size], labels))

print("-------------------------")

calc_scores(X_transformed[0:sample_size], labels_true[0:sample_size], labels)




# #############################################################################
# Plot result
#import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X_transformed[0:sample_size][class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X_transformed[0:sample_size][class_member_mask & ~core_samples_mask]
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



#


##############################################################################


'''
clust = OPTICS(min_samples=5, xi=0.6, min_cluster_size=5)
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
#%%Optics Plot https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html#sphx-glr-auto-examples-cluster-plot-optics-py


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
    eps=0.7,
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
ax4.set_title("Clustering at 0.7 epsilon cut\nDBSCAN")

plt.tight_layout()
plt.show()



calc_scores(X_transformed, labels_true, labels)


'''
##########################################


'''
##########################################
#%%
reduced_sepsis = []
reduced_no_sepsis = []

for j in range(0,sample_size):
    if labels_true[j] == 1:
        reduced_sepsis.append(X_transformed[j])
    else:
        reduced_no_sepsis.append(X_transformed[j])

       
plt.scatter(*zip(*reduced_no_sepsis), cmap="Spectral", s=0.4)
plt.scatter(*zip(*reduced_sepsis), c="r", s=0.4)
plt.show()

#%% 



#########################################

#%%
gender_female = []
gender_male = []

for j in range(0,sample_size):
    if labels_gender[j] == 0:
        gender_female.append(X_transformed[j])
    else:
        gender_male.append(X_transformed[j])

       
plt.scatter(*zip(*gender_female), cmap="Spectral", s=0.4)
plt.scatter(*zip(*gender_male), c="r", s=0.4)
plt.show()

#%% 

#########################################

#%%
unit_1 = []
unit_2 = []
no_unit = []

for j in range(0,sample_size):
    if labels_unit1[j] == 1:
        unit_1.append(X_transformed[j])
    elif labels_unit2[j] == 1:
       unit_2.append(X_transformed[j])
    else:
        no_unit.append(X_transformed[j])

       
plt.scatter(*zip(*unit_1), cmap="Spectral", s=0.4)
plt.scatter(*zip(*unit_2), c="r", s=0.4)
plt.scatter(*zip(*no_unit), c="g", s=0.4)
plt.show()

#%% 
'''