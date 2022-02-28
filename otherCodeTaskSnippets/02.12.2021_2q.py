# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:01:40 2021

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



'''

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

#embedding = pacmap.PaCMAP(n_dims=2, n_neighbors=None, MN_ratio=0.5, FP_ratio=2.0) 

# fit the data (The index of transformed data corresponds to the index of the original data)

#X_transformed = embedding.fit_transform(df_current.values, init="pca")

####################################################################


#%%


model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(df_current.values)
#score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))

#print("consensus score: {:.3f}".format(score))

fit_data = df_current.values[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]

fit_data = fit_data[0:len(labels_true), 0:41]

#fit_data = fit_data[0:100000, 0:41]




#plt.matshow(fit_data, cmap=plt.cm.Blues)
plt.matshow(fit_data, cmap='Spectral')


#plt.matshow(fit_data, cmap=plt.cm.RdYlGn)
#plt.matshow(fit_data, cmap=plt.cm.YlOrRd)
#plt.matshow(fit_data)
#plt.matshow(fit_data, cmap='rainbow')
#plt.matshow(fit_data, cmap='Set1')
#plt.matshow(fit_data, cmap='tab20')
#plt.matshow(fit_data, cmap='gist_rainbow')


plt.gca().set_aspect('auto')
#plt.gca().set_aspect('equal', adjustable='box')
#plt.axis('scaled')
#plt.title("After biclustering; rearranged to show biclusters")

plt.show()


#%%

#

#%%


model = SpectralBiclustering(n_clusters=(50, 5), method="log", random_state=0)
model.fit(df_current.values)

#model = SpectralBiclustering(n_clusters=(20, 10), method="log", random_state=0)
#model.fit(df_current.values[0:100000, 0:41])


fit_data = df_current.values[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]


#fit_data = df_current.values[0:100000, 0:41][np.argsort(model.row_labels_)]
#fit_data = fit_data[:, np.argsort(model.column_labels_)]

#plt.matshow(fit_data, cmap=plt.cm.Blues)
plt.matshow(fit_data, cmap='Spectral')

plt.gca().set_aspect('auto')

#plt.title("After biclustering; rearranged to show biclusters")





#plt.matshow(
#    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
#    cmap=plt.cm.Blues,
#)


plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap='Spectral',
)





plt.gca().set_aspect('auto')

#plt.title("Checkerboard structure of rearranged data")

plt.show()





#%%