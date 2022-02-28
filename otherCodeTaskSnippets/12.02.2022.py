# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:15:05 2022

@author: dariu
"""


import numpy as np
import pandas as pd
import os
from tqdm import tqdm
#import pacmap
import matplotlib.pyplot as plt
#from sklearn.manifold import TSNE
#import umap
#from sklearn.cluster import KMeans
#from sklearn.cluster import DBSCAN
#import sklearn.cluster
#from sklearn.decomposition import PCA
from sklearn import metrics
#from sklearn.cluster import OPTICS, cluster_optics_dbscan
#import matplotlib.gridspec as gridspec
#from sklearn.cluster import SpectralCoclustering
#from sklearn.metrics import consensus_score
#from sklearn.cluster import SpectralBiclustering
#from sklearn import svm
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import NearMiss
from imblearn.pipeline import make_pipeline
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import RocCurveDisplay
#from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from pyts.classification import BOSSVS
import statistics
from scipy import interpolate




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
labels_true = df["SepsisLabel"].tolist()


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
    
#df = df.drop(columns=["SepsisLabel"])

df_current = df.fillna(df.mean())

'''

#%%

df_current = df





dim_current = 'Temp'

T = df_current[[dim_current]]
L = df_current[["SepsisLabel"]]

T_new = []
L_new = []
B = []
C = []
d = -1


for k, row in T.iterrows():  
    if k == 0:
        try:
            B = pd.Series(B).interpolate(method="quadratic")
            B = B.tolist()
        except:
            pass
        T_new.append(B)
        B=[]
        B.append(row[dim_current])
    else:
        B.append(row[dim_current])
    
T_new.append(B)
del T_new[0]   



for k, row in L.iterrows():  
    if k == 0:
        d += 1
        L_new.append(0)
        if row["SepsisLabel"] == 1:
            L_new[d] = 1
    else:
        if row["SepsisLabel"] == 1:
            L_new[d] = 1
            
            
#%%


'''
B=pd.Series(B).interpolate(method="quadratic")
B= B.tolist()

T_new3=[]

for k, row in T_new.iterrows():
    T_new3.append(row.tolist())

'''
#%%

 

T_new2 = T_new
row_lengths = []

for row in T_new2:
    row_lengths.append(len(row))

max_length = max(row_lengths)

for row in T_new2:
    while len(row) < max_length:
        row.append(None)

balanced_array = np.array(T_new2)

#%%


X_train, X_test, y_train, y_test = train_test_split(balanced_array, L_new, test_size=0.2)

X_train_ss = X_train[0:int(1*len(X_train))]
y_train_ss = y_train[0:int(1*len(y_train))]

X_test_ss = X_test[0:int(1*len(X_test))]
y_test_ss = y_test[0:int(1*len(y_test))]

#%%

'''

from tslearn.shapelets import LearningShapelets 

# Define the model using parameters provided by the authors (except that we
# use fewer iterations here)
shp_clf = LearningShapelets(max_iter=100)
                            #n_shapelets_per_size=shapelet_sizes,
                            #optimizer=tf.optimizers.Adam(.01),
                            #batch_size=16,
                            #weight_regularizer=.01,
                            #max_iter=200,
                            #random_state=42,
                            #verbose=0)
                            
shp_clf.fit(X_train_ss, y_train_ss)


print(classification_report_imbalanced(y_test, shp_clf.predict(X_test)))


#
'''

#%%


X_train, X_test, y_train, y_test = train_test_split(balanced_array, L_new, test_size=0.2)

X_train_ss = X_train[0:int(0.07*len(X_train))]
y_train_ss = y_train[0:int(0.07*len(y_train))]

X_test_ss = X_test[0:int(2*len(X_test))]
y_test_ss = y_test[0:int(2*len(y_test))]

#%%


from pyts.classification import LearningShapelets

Z1 = np.array(X_train_ss, dtype=float)
Z2 = np.nan_to_num(Z1, nan = T.mean())

#print(len(min(T_new, key=len)))


#clf = LearningShapelets()
#clf.fit(np.nan_to_num(X_train_ss, nan = T.mean()), y_train_ss)
#clf.fit(Z2, y_train_ss)

Z3 = np.array(X_test_ss, dtype=float)
Z4 = np.nan_to_num(Z3, nan = T.mean())


#print(classification_report_imbalanced(y_test_ss, clf.predict(Z4)))



#%%

from pyts.classification import TimeSeriesForest

# Create a pipeline
pipeline = make_pipeline(
    NearMiss(version=3), LearningShapelets())


# Create a pipeline
#pipeline = make_pipeline(
#    NearMiss(version=3), TimeSeriesForest())


       
# Create a pipeline
#pipeline = make_pipeline(
#    NearMiss(version=3), BOSSVS(window_size=15)) 
#word_size=2, n_bins=3, window_size=80

#%%

pipeline.fit(Z2, y_train_ss)

#pipeline.fit(X_train_transformed_ss, y_train_ss)


print(classification_report_imbalanced(y_test_ss, pipeline.predict(Z4)))

print("##############################################################\n")

print(classification_report(y_test_ss, pipeline.predict(Z4)))

#%%

#
#%%



#X_test_ss = X_test[0:int(0.3*len(X_train))]
#y_test_ss = y_test[0:int(0.3*len(y_train))]

#metrics.plot_roc_curve(shp_clf, X_test_ss, y_test_ss) 

metrics.plot_roc_curve(pipeline, Z4, y_test_ss) 

#metrics.plot_roc_curve(pipeline, X_test_transformed_ss, y_test_ss) 

plt.show()








#%%
'''

fpr, tpr, thresholds = metrics.roc_curve(y_test_ss, pipeline.predict(Z4))
roc_auc = metrics.auc(fpr, tpr)
#display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
#                                  estimator_name='example estimator')
#display.plot()


y_pred = pipeline.decision_function(Z4)
RocCurveDisplay.from_predictions(
    y_test_ss, y_pred)


plt.show()

'''