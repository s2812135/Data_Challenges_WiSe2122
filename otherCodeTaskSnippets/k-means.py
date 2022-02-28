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

reduced_data = X_transformed
db = DBSCAN(eps=0.5, min_samples=10).fit(reduced_data)


                                                  
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
labels_true = df_current["SepsisLabel"].tolist()
labels_true = labels_true[0:sample_size]
X = reduced_data[0:sample_size]


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
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

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

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
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



###########################




import os, sys
import csv
from os.path import isfile, join
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import sklearn
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans




class SubGroups():
    def __init__(self, dataPath=""):
        self.dataPath = dataPath
        # hasAllFileNamesInAnArray
        self.fileNames = []
        # currentFileData Array
        self.currentFileDataArray = []
        # endResultArray
        self.endResultArray = []

    def getFileNames(self):
        """ returns list of all files in the path"""
        dirs = os.listdir(self.dataPath)
        # für alle Files in Directory
        for file in dirs:
            self.fileNames.append(file);
            # liest die File
            self.readFiles(file)

    # print(self.fileNames)

    def readFiles(self, file):
        """Opens every file and read it. It is Main extraction method"""
        path = self.dataPath
        backslash = "\\"
        filename = self.dataPath + backslash + file
        print("Das ist die zu extrahierende File" + file)
        fp = open(filename)
        resultArray = []
        for line in fp:
            res = line.split('|')
            resultArray.append(res)
        # jetzigeFile
        self.currentFileDataArray = resultArray
        # 1
        self.extractHr(file)
        # 2
        self.extractO2Sat(file)
        self.extractTemp(file)
        self.extractSBP(file)
        self.extractMAP(file)
        self.extractDBP(file)
        self.extractResp(file)
        self.extractEtCO2(file)
        self.extractBaseExcess(file)
        self.extractHCO3(file)
        self.extractFiO2(file)
        self.extractpH(file)
        self.extractPaCO2(file)
        self.extractSaO2(file)
        self.extractAST(file)
        self.extractBUN(file)
        self.extractAlkalinephos(file)
        self.extractCalcium(file)
        self.extractChloride(file)
        self.extractCreatinine(file)
        self.extractBilirubin_direct(file)
        self.extractGlucose(file)
        self.extractLactate(file)
        self.extractMagnesium(file)
        self.extractPhosphate(file)
        self.extractPotassium(file)
        self.extractBilirubin_total(file)
        self.extractTroponinI(file)
        self.extractHct(file)
        self.extractHgb(file)
        self.extractPTT(file)
        self.extractWBC(file)
        self.extractFibrinogen(file)
        self.extractPlatelets(file)
        self.extractAge(file)
        self.extractGender(file)
        self.extractUnit1(file)
        self.extractUnit2(file)
        self.extractHospAdmTime(file)
        self.extractICULOS(file)
        self.extractSepsisLabel(file)

    def extractHr(self, file):
        """ extract important Hr """
        allHeartRatePerPerson = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][0] != "NaN"):
                allHeartRatePerPerson.append(float(self.currentFileDataArray[i][0]))
            if (self.currentFileDataArray[i][0] == "NaN"):
                allHeartRatePerPerson.append(0)

        allHeartRatePerPerson = list(dict.fromkeys(allHeartRatePerPerson))

        for i in range(0, len(allHeartRatePerPerson)):
            self.endResultArray.append([1, allHeartRatePerPerson[i]])

    def extractO2Sat(self, file):
        """ extract important O2Sat """
        allO2Sat = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][1] != "NaN"):
                allO2Sat.append(float(self.currentFileDataArray[i][1]))
            if (self.currentFileDataArray[i][1] == "NaN"):
                allO2Sat.append(0)

        allO2Sat = list(dict.fromkeys(allO2Sat))
        for i in range(0, len(allO2Sat)):
            self.endResultArray.append([2, allO2Sat[i]])

    def extractTemp(self, file):
        """ extract important O2Sat """
        allTemp = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][2] != "NaN"):
                allTemp.append(float(self.currentFileDataArray[i][2]))
            if (self.currentFileDataArray[i][2] == "NaN"):
                allTemp.append(float(0))

        allTemp = list(dict.fromkeys(allTemp))

        for i in range(0, len(allTemp)):
            self.endResultArray.append([3, allTemp[i]])

    def extractSBP(self, file):
        """ extract important SBP """
        allSBP = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][3] != "NaN"):
                allSBP.append(float(self.currentFileDataArray[i][3]))
            if (self.currentFileDataArray[i][3] == "NaN"):
                allSBP.append(float(0))

        allSBP = list(dict.fromkeys(allSBP))

        for i in range(0, len(allSBP)):
            self.endResultArray.append([4, allSBP[i]])

    def extractMAP(self, file):
        """ extract important MAP """
        allMAP = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][4] != "NaN"):
                allMAP.append(float(self.currentFileDataArray[i][4]))
            if (self.currentFileDataArray[i][4] == "NaN"):
                allMAP.append(float(0))

        allMAP = list(dict.fromkeys(allMAP))

        for i in range(0, len(allMAP)):
            self.endResultArray.append([5, allMAP[i]])

    def extractDBP(self, file):
        """ extract important DBP """
        allDBP = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][5] != "NaN"):
                allDBP.append(float(self.currentFileDataArray[i][5]))
            if (self.currentFileDataArray[i][5] == "NaN"):
                allDBP.append(float(0))

        allDBP = list(dict.fromkeys(allDBP))

        for i in range(0, len(allDBP)):
            self.endResultArray.append([6, allDBP[i]])

    def extractResp(self, file):
        """ extract important Resp """
        allResp = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][6] != "NaN"):
                allResp.append(float(self.currentFileDataArray[i][6]))
            if (self.currentFileDataArray[i][6] == "NaN"):
                allResp.append(float(0))

        allResp = list(dict.fromkeys(allResp))

        for i in range(0, len(allResp)):
            self.endResultArray.append([7, allResp[i]])

    # 7
    def extractEtCO2(self, file):
        """ extract important Hr """
        allEtCO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][7] != "NaN"):
                allEtCO2.append(float(self.currentFileDataArray[i][7]))
            if (self.currentFileDataArray[i][7] == "NaN"):
                allEtCO2.append(float(0))

        allEtCO2 = list(dict.fromkeys(allEtCO2))

        for i in range(0, len(allEtCO2)):
            self.endResultArray.append([8, allEtCO2[i]])

    def extractBaseExcess(self, file):
        """ extract important allBaseExcess """
        allBaseExcess = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][8] != "NaN"):
                allBaseExcess.append(float(self.currentFileDataArray[i][8]))
            if (self.currentFileDataArray[i][8] == "NaN"):
                allBaseExcess.append(float(0))

        allBaseExcess = list(dict.fromkeys(allBaseExcess))

        for i in range(0, len(allBaseExcess)):
            self.endResultArray.append([9, allBaseExcess[i]])

    def extractHCO3(self, file):
        """ extract important O2Sat """
        allHCO3 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][9] != "NaN"):
                allHCO3.append(float(self.currentFileDataArray[i][9]))
            if (self.currentFileDataArray[i][9] == "NaN"):
                allHCO3.append(float(0))

        allHCO3 = list(dict.fromkeys(allHCO3))

        for i in range(0, len(allHCO3)):
            self.endResultArray.append([10, allHCO3[i]])

    def extractFiO2(self, file):
        """ extract important SBP """
        allFiO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][10] != "NaN"):
                allFiO2.append(float(self.currentFileDataArray[i][10]))
            if (self.currentFileDataArray[i][10] == "NaN"):
                allFiO2.append(float(0))

        allFiO2 = list(dict.fromkeys(allFiO2))

        for i in range(0, len(allFiO2)):
            self.endResultArray.append([11, allFiO2[i]])

    def extractpH(self, file):
        """ extract important MAP """
        allpH = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][11] != "NaN"):
                allpH.append(float(self.currentFileDataArray[i][11]))
            if (self.currentFileDataArray[i][11] == "NaN"):
                allpH.append(float(0))

        allpH = list(dict.fromkeys(allpH))

        for i in range(0, len(allpH)):
            self.endResultArray.append([12, allpH[i]])

    def extractPaCO2(self, file):
        """ extract important DBP """
        allPaCO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][12] != "NaN"):
                allPaCO2.append(float(self.currentFileDataArray[i][12]))
            if (self.currentFileDataArray[i][12] == "NaN"):
                allPaCO2.append(float(0))

        allPaCO2 = list(dict.fromkeys(allPaCO2))

        for i in range(0, len(allPaCO2)):
            self.endResultArray.append([13, allPaCO2[i]])

    def extractSaO2(self, file):
        """ extract important Resp """
        allSaO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][13] != "NaN"):
                allSaO2.append(float(self.currentFileDataArray[i][13]))
            if (self.currentFileDataArray[i][13] == "NaN"):
                allSaO2.append(float(0))

        allSaO2 = list(dict.fromkeys(allSaO2))

        for i in range(0, len(allSaO2)):
            self.endResultArray.append([14, allSaO2[i]])

    # 14
    def extractAST(self, file):
        """ extract important Hr """
        allAST = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][14] != "NaN"):
                allAST.append(float(self.currentFileDataArray[i][14]))
            if (self.currentFileDataArray[i][14] == "NaN"):
                allAST.append(float(0))

        allAST = list(dict.fromkeys(allAST))
        for i in range(0, len(allAST)):
            self.endResultArray.append([15, allAST[i]])

    def extractBUN(self, file):
        """ extract important O2Sat """
        allBUN = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][15] != "NaN"):
                allBUN.append(float(self.currentFileDataArray[i][15]))
            if (self.currentFileDataArray[i][15] == "NaN"):
                allBUN.append(float(0))

        allBUN = list(dict.fromkeys(allBUN))

        for i in range(0, len(allBUN)):
            self.endResultArray.append([16, allBUN[i]])

    def extractAlkalinephos(self, file):
        """ extract important O2Sat """
        allAlkalinephos = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][16] != "NaN"):
                allAlkalinephos.append(float(self.currentFileDataArray[i][16]))
            if (self.currentFileDataArray[i][16] == "NaN"):
                allAlkalinephos.append(float(0))

        allAlkalinephos = list(dict.fromkeys(allAlkalinephos))

        for i in range(0, len(allAlkalinephos)):
            self.endResultArray.append([17, allAlkalinephos[i]])

    def extractCalcium(self, file):
        """ extract important SBP """
        allCalcium = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][17] != "NaN"):
                allCalcium.append(float(self.currentFileDataArray[i][17]))
            if (self.currentFileDataArray[i][17] == "NaN"):
                allCalcium.append(float(0))

        allCalcium = list(dict.fromkeys(allCalcium))

        for i in range(0, len(allCalcium)):
            self.endResultArray.append([18, allCalcium[i]])

    def extractChloride(self, file):
        """ extract important MAP """
        allChloride = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][18] != "NaN"):
                allChloride.append(float(self.currentFileDataArray[i][18]))
            if (self.currentFileDataArray[i][18] == "NaN"):
                allChloride.append(float(0))

        allChloride = list(dict.fromkeys(allChloride))
        for i in range(0, len(allChloride)):
            self.endResultArray.append([19, allChloride[i]])

    def extractCreatinine(self, file):
        """ extract important Creatinine """
        allCreatinine = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][19] != "NaN"):
                allCreatinine.append(float(self.currentFileDataArray[i][19]))
            if (self.currentFileDataArray[i][19] == "NaN"):
                allCreatinine.append(float(0))

        allCreatinine = list(dict.fromkeys(allCreatinine))

        for i in range(0, len(allCreatinine)):
            self.endResultArray.append([20, allCreatinine[i]])

    def extractBilirubin_direct(self, file):
        """ extract important Bilirubin_direct """
        allBilirubin_direct = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][20] != "NaN"):
                allBilirubin_direct.append(float(self.currentFileDataArray[i][20]))
            if (self.currentFileDataArray[i][20] == "NaN"):
                allBilirubin_direct.append(float(0))

        allBilirubin_direct = list(dict.fromkeys(allBilirubin_direct))

        for i in range(0, len(allBilirubin_direct)):
            self.endResultArray.append([21, allBilirubin_direct[i]])

    def extractGlucose(self, file):
        """ extract important Glucose """
        allGlucose = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][21] != "NaN"):
                allGlucose.append(float(self.currentFileDataArray[i][21]))
            if (self.currentFileDataArray[i][21] == "NaN"):
                allGlucose.append(float(0))

        allGlucose = list(dict.fromkeys(allGlucose))

        for i in range(0, len(allGlucose)):
            self.endResultArray.append([22, allGlucose[i]])

    def extractLactate(self, file):
        """ extract important allBaseExcess """
        allLactate = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][22] != "NaN"):
                allLactate.append(float(self.currentFileDataArray[i][22]))
            if (self.currentFileDataArray[i][22] == "NaN"):
                allLactate.append(float(0))

        allLactate = list(dict.fromkeys(allLactate))

        for i in range(0, len(allLactate)):
            self.endResultArray.append([23, allLactate[i]])

    def extractMagnesium(self, file):
        """ extract important Magnesium """
        allMagnesium = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][23] != "NaN"):
                allMagnesium.append(float(self.currentFileDataArray[i][23]))
            if (self.currentFileDataArray[i][23] == "NaN"):
                allMagnesium.append(float(0))

        allMagnesium = list(dict.fromkeys(allMagnesium))

        for i in range(0, len(allMagnesium)):
            self.endResultArray.append([24, allMagnesium[i]])

    def extractPhosphate(self, file):
        """ extract important allPhosphate """
        allPhosphate = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][24] != "NaN"):
                allPhosphate.append(float(self.currentFileDataArray[i][24]))
            if (self.currentFileDataArray[i][24] == "NaN"):
                allPhosphate.append(float(0))

        allPhosphate = list(dict.fromkeys(allPhosphate))

        for i in range(0, len(allPhosphate)):
            self.endResultArray.append([25, allPhosphate[i]])

    def extractPotassium(self, file):
        """ extract important Potassium """
        allPotassium = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][25] != "NaN"):
                allPotassium.append(float(self.currentFileDataArray[i][25]))
            if (self.currentFileDataArray[i][25] == "NaN"):
                allPotassium.append(float(0))

        allPotassium = list(dict.fromkeys(allPotassium))

        for i in range(0, len(allPotassium)):
            self.endResultArray.append([26, allPotassium[i]])

    def extractBilirubin_total(self, file):
        """ extract important Bilirubin_total """
        allBilirubin_total = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][26] != "NaN"):
                allBilirubin_total.append(float(self.currentFileDataArray[i][26]))
            if (self.currentFileDataArray[i][26] == "NaN"):
                allBilirubin_total.append(float(0))

        allBilirubin_total = list(dict.fromkeys(allBilirubin_total))

        for i in range(0, len(allBilirubin_total)):
            self.endResultArray.append([27, allBilirubin_total[i]])

    def extractTroponinI(self, file):
        """ extract important TroponinI """
        allTroponinI = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][27] != "NaN"):
                allTroponinI.append(float(self.currentFileDataArray[i][27]))
            if (self.currentFileDataArray[i][27] == "NaN"):
                allTroponinI.append(float(0))

        allTroponinI = list(dict.fromkeys(allTroponinI))

        for i in range(0, len(allTroponinI)):
            self.endResultArray.append([28, allTroponinI[i]])

    # 28
    def extractHct(self, file):
        """ extract important O2Sat """
        allHct = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][28] != "NaN"):
                allHct.append(float(self.currentFileDataArray[i][28]))
            if (self.currentFileDataArray[i][28] == "NaN"):
                allHct.append(float(0))

        allHct = list(dict.fromkeys(allHct))

        for i in range(0, len(allHct)):
            self.endResultArray.append([29, allHct[i]])

    def extractHgb(self, file):
        """ extract important Hgb """
        allHgb = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][29] != "NaN"):
                allHgb.append(float(self.currentFileDataArray[i][29]))
            if (self.currentFileDataArray[i][29] == "NaN"):
                allHgb.append(float(0))

        allHgb = list(dict.fromkeys(allHgb))

        for i in range(0, len(allHgb)):
            self.endResultArray.append([30, allHgb[i]])

    def extractPTT(self, file):
        """ extract important SBP """
        allPTT = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][30] != "NaN"):
                allPTT.append(float(self.currentFileDataArray[i][30]))
            if (self.currentFileDataArray[i][30] == "NaN"):
                allPTT.append(float(0))

        allPTT = list(dict.fromkeys(allPTT))

        for i in range(0, len(allPTT)):
            self.endResultArray.append([31, allPTT[i]])

    def extractWBC(self, file):
        """ extract important allWBC """
        allWBC = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][31] != "NaN"):
                allWBC.append(float(self.currentFileDataArray[i][31]))
            if (self.currentFileDataArray[i][31] == "NaN"):
                allWBC.append(float(0))

        allWBC = list(dict.fromkeys(allWBC))

        for i in range(0, len(allWBC)):
            self.endResultArray.append([32, allWBC[i]])

    def extractFibrinogen(self, file):
        """ extract important Fibrinogen """
        allFibrinogen = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][32] != "NaN"):
                allFibrinogen.append(float(self.currentFileDataArray[i][32]))
            if (self.currentFileDataArray[i][32] == "NaN"):
                allFibrinogen.append(float(0))

        allFibrinogen = list(dict.fromkeys(allFibrinogen))

        for i in range(0, len(allFibrinogen)):
            self.endResultArray.append([33, allFibrinogen[i]])

    def extractPlatelets(self, file):
        """ extract important Platelets """
        allPlatelets = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][33] != "NaN"):
                # Null
                allPlatelets.append(float(self.currentFileDataArray[i][33]))
            if (self.currentFileDataArray[i][33] == "NaN"):
                allPlatelets.append(float(0))

        allPlatelets = list(dict.fromkeys(allPlatelets))

        for i in range(0, len(allPlatelets)):
            self.endResultArray.append([34, allPlatelets[i]])

    def extractAge(self, file):
        """ extract important Glucose """
        allAge = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][34] != "NaN"):
                allAge.append(float(self.currentFileDataArray[i][34]))
            if (self.currentFileDataArray[i][34] == "NaN"):
                allAge.append(float(0))

        allAge = list(dict.fromkeys(allAge))

        for i in range(0, len(allAge)):
            self.endResultArray.append([35, allAge[i]])

    # AB HIIIIIIER: Gender
    def extractGender(self, file):
        """ extract important allBaseExcess """
        allGender = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][35] != "NaN"):
                allGender.append(float(self.currentFileDataArray[i][35]))
            if (self.currentFileDataArray[i][35] == "NaN"):
                allGender.append(float(0))

        allGender = list(dict.fromkeys(allGender))

        for i in range(0, len(allGender)):
            self.endResultArray.append([36, allGender[i]])

    def extractUnit1(self, file):
        """ extract important Magnesium """
        allUnit1 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][36] != "NaN"):
                allUnit1.append(float(self.currentFileDataArray[i][36]))
        # if(self.currentFileDataArray[i][36] == "NaN"):
        #    allUnit1.append(float(0))
        # Geht nicht

        allUnit1 = list(dict.fromkeys(allUnit1))

        for i in range(0, len(allUnit1)):
            self.endResultArray.append([37, allUnit1[i]])

    def extractUnit2(self, file):
        """ extract important allUnit2 """
        allUnit2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][37] != "NaN"):
                allUnit2.append(float(self.currentFileDataArray[i][37]))

        allUnit2 = list(dict.fromkeys(allUnit2))

        for i in range(0, len(allUnit2)):
            self.endResultArray.append([38, allUnit2[i]])

    def extractHospAdmTime(self, file):
        """ extract important allHospAdmTime """
        allHospAdmTime = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][38] != "NaN"):
                allHospAdmTime.append(float(self.currentFileDataArray[i][38]))
            if (self.currentFileDataArray[i][38] == "NaN"):
                allHospAdmTime.append(float(0))

        allHospAdmTime = list(dict.fromkeys(allHospAdmTime))

        for i in range(0, len(allHospAdmTime)):
            self.endResultArray.append([39, allHospAdmTime[i]])

    def extractICULOS(self, file):
        """ extract important Bilirubin_total """
        allICULOS = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][39] != "NaN"):
                allICULOS.append(float(self.currentFileDataArray[i][39]))
            if (self.currentFileDataArray[i][39] == "NaN"):
                allICULOS.append(float(0))

        allICULOS = list(dict.fromkeys(allICULOS))

        for i in range(0, len(allICULOS)):
            self.endResultArray.append([40, allICULOS[i]])

    def extractSepsisLabel(self, file):
        """ extract important TroponinI """
        allSepsisLabel = []
        for i in range(1, len(self.currentFileDataArray)):
            if (self.currentFileDataArray[i][40] != "NaN"):
                allSepsisLabel.append(float(self.currentFileDataArray[i][40]))

        allSepsisLabel = list(dict.fromkeys(allSepsisLabel))
        # print(allSepsisLabel)
        for i in range(0, len(allSepsisLabel)):
            self.endResultArray.append([41, allSepsisLabel[i]])


# Klasse 1: A1
A1 = SubGroups("E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\training")
# A1.makeGenderDiagram()

# A1.makeAgeGenderDiagram()
A2 = SubGroups("E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\training_setB")
#A1.getFileNames()
A1.readFiles("p000004.psv")
totalEndResult = A1.endResultArray
#A2.getFileNames()
#totalEndResult = A1.endResultArray + A2.endResultArray
print(totalEndResult)
# print("Das ist Lände der Liste: "+str(totalEndResult))
# print("Das ist totale Länge der Liste: "+ str(len(totalEndResult)))




#x = totalEndResult

x=totalEndResult[[34,],[41,]]
#visualise data points
plt.scatter(x[34,],x[41,],c='black')
plt.xlabel('Age')
plt.ylabel('xx)')
plt.show()

#kmeans = KMeans(n_clusters=4, random_state=0).fit(x)
#print(kmeans.labels_)
#print("Das sind Label insgesamt"+str(len(kmeans.labels_)))
#n_clusters_ = len(set(kmeans.labels_))
#print("Das sind Cluster in den Labels:"+str(n_clusters_))


# standardizing the data

scaler = StandardScaler()
data_scaled = scaler.fit_transform(totalEndResult)

# statistics of scaled data
pd.DataFrame(data_scaled).describe()

# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=4, init='k-means++',n_init=100, random_state=0)

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)


##########################################
# inertia on the fitted data
#kmeans.inertia_
#print(kmeans.inertia_)


# fitting multiple k-means algorithms and storing the values in an empty list
#SSE = []
#for cluster in range(1,20):
#    kmeans = KMeans( n_clusters = cluster, init='k-means++')
#    kmeans.fit(data_scaled)
#    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
#frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
#plt.figure(figsize=(12,6))
#plt.plot(frame['Cluster'], frame['SSE'], marker='o')
#plt.xlabel('Number of clusters')
#plt.ylabel('Inertia')
#plt.show()

# k means using 5 clusters and k-means++ initialization
#kmeans = KMeans( n_clusters = 4, init='k-means++')
#kmeans.fit(data_scaled)
#pred = kmeans.predict(data_scaled)

#frame = pd.DataFrame(data_scaled)
#frame['cluster'] = pred
#print(frame['cluster'].value_counts())


################################
#Plot kmeans (https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-auto-examples-cluster-plot-kmeans-digits-py)

# Step size of the mesh. Decrease to increase the quality of the VQ.
#h = 0.4  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
#x_min, x_max = data_scaled[:, 0].min() - 1, data_scaled[:, 0].max() + 1
#y_min, y_max = data_scaled[:, 1].min() - 1, data_scaled[:, 1].max() + 1
#xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
#Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
#Z = Z.reshape(xx.shape)
#plt.figure(1)
#plt.clf()
#plt.imshow(
#    Z,
#    interpolation="nearest",
#    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
#    cmap=plt.cm.Paired,
#    aspect="auto",
#    origin="lower",
#)

#plt.plot(data_scaled[:, 0], data_scaled[:, 1], "k.", markersize=2)
# Plot the centroids as a white X
#centroids = kmeans.cluster_centers_
#plt.scatter(
#    centroids[:, 0],
#    centroids[:, 1],
#    marker="x",
#    s=169,
#    linewidths=3,
#    color="w",
#   zorder=10,
#)
#plt.title(
#    "K-means clustering on the whole dataset (PCA-reduced data)\n"
#    "Centroids are marked with white cross"
#)
#plt.xlim(x_min, x_max)
#plt.ylim(y_min, y_max)
#plt.xticks(())
#plt.yticks(())
#plt.show()




##################################################################################### age-spesis 
### 
 X["Cluster"]=C
-5.79030735972424
-4.842847223127047
-4.156984913922021
-3.645893134660171
-3.178272157786863
-2.6911147182601063
###################  https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/

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

path = "E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\"

directorys = [
    ['/training/', 'p0'],
    ['/training_setB/', 'p1']
]

dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)

df.head()

X = df[["Age","SepsisLabel"]]
#Visualise data points
plt.scatter(X["Age"],X["SepsisLabel"],c='black')
plt.xlabel('Age')
plt.ylabel('Sepsis')
plt.title('K-means Cluster on the Age-Sepsis')
plt.show()


#number of clusters
K=4

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Age"],X["SepsisLabel"],c='black')
plt.scatter(Centroids["Age"],Centroids["SepsisLabel"],c='red')
plt.title('K-means Cluster on the Age-Sepsis')
plt.xlabel('Age')
plt.ylabel('Sepsis')
plt.show()


diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Age"]-row_d["Age"])**2
            d2=(row_c["SepsisLabel"]-row_d["SepsisLabel"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Age","SepsisLabel"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['SepsisLabel'] - Centroids['SepsisLabel']).sum() + (Centroids_new['Age'] - Centroids['Age']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["SepsisLabel","Age"]]

    color = ['blue', 'green', 'cyan','yellow']
    for k in range(K):
        data = X[X["Cluster"] == k + 1]
        plt.scatter(data["Age"], data["SepsisLabel"], c=color[k])
    plt.scatter(Centroids["Age"], Centroids["SepsisLabel"], c='red')
    plt.xlabel('Age')
    plt.ylabel('Sepsis')
    plt.title('K-means Cluster on the Age-Sepsis')
    plt.show()
####################################################

#df_current = df.fillna(0)





############################################################################ Gender-Sepsis
 X["Cluster"]=C
0.980920466810966
0.0

########################################


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

path = "E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\"

directorys = [
    ['/training/', 'p0'],
    ['/training_setB/', 'p1']
]

dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)

df.head()

X = df[["Gender","SepsisLabel"]]
#Visualise data points
plt.scatter(X["Gender"],X["SepsisLabel"],c='black')
plt.xlabel('Gender')
plt.ylabel('Sepsis')
plt.title('K-means Cluster on the Gender-Sepsis')
plt.show()


#number of clusters
K=4

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Gender"],X["SepsisLabel"],c='black')
plt.scatter(Centroids["Gender"],Centroids["SepsisLabel"],c='red')
plt.title('K-means Cluster on the Gender-Sepsis')
plt.xlabel('Gender')
plt.ylabel('Sepsis')
plt.show()


diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Gender"]-row_d["Gender"])**2
            d2=(row_c["SepsisLabel"]-row_d["SepsisLabel"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Gender","SepsisLabel"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['SepsisLabel'] - Centroids['SepsisLabel']).sum() + (Centroids_new['Gender'] - Centroids['Gender']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["SepsisLabel","Gender"]]

    color = ['blue', 'green', 'cyan','yellow']
    for k in range(K):
        data = X[X["Cluster"] == k + 1]
        plt.scatter(data["Gender"], data["SepsisLabel"], c=color[k])
    plt.scatter(Centroids["Gender"], Centroids["SepsisLabel"], c='red')
    plt.xlabel('Gender')
    plt.ylabel('Sepsis')
    plt.title('K-means Cluster on the Gender-Sepsis')
    plt.show()
####################################################

#df_current = df.fillna(0)




#####################################################
Gender-Age




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

path = "E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\"

directorys = [
    ['/training/', 'p0'],
    ['/training_setB/', 'p1']
]

dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)

df.head()

X = df[["Age","Gender"]]
#Visualise data points
plt.scatter(X["Age"],X["Gender"],c='black')
plt.xlabel('Age')
plt.ylabel('Gender')
plt.title('K-means Cluster on the Gender-Age')
plt.show()


#number of clusters
K=4

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Age"],X["Gender"],c='black')
plt.scatter(Centroids["Age"],Centroids["Gender"],c='red')
plt.title('K-means Cluster on the Gender-Age')
plt.xlabel('Age')
plt.ylabel('Gender')
plt.show()


diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Age"]-row_d["Age"])**2
            d2=(row_c["Gender"]-row_d["Gender"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Age","Gender"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['Gender'] - Centroids['Gender']).sum() + (Centroids_new['Age'] - Centroids['Age']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Gender","Age"]]

    color = ['blue', 'green', 'cyan','yellow']
    for k in range(K):
        data = X[X["Cluster"] == k + 1]
        plt.scatter(data["Age"], data["Gender"], c=color[k])
    plt.scatter(Centroids["Age"], Centroids["Gender"], c='red')
    plt.xlabel('Age')
    plt.ylabel('Gender')
    plt.title('K-means Cluster on the Gender-Age')
    plt.show()
####################################################

#df_current = df.fillna(0)





100%|██████████| 20336/20336 [02:52<00:00, 117.63it/s]
100%|██████████| 20000/20000 [11:56<00:00, 27.90it/s]
Traceback (most recent call last):
  File "C:/Users/user/PycharmProjects/DC/main.py", line 43, in <module>
    clf = clf.fit(X_train,y_train)
  File "C:\Users\user\PycharmProjects\DC\venv\lib\site-packages\sklearn\tree\tree.py", line 816, in fit
    X_idx_sorted=X_idx_sorted)
  File "C:\Users\user\PycharmProjects\DC\venv\lib\site-packages\sklearn\tree\tree.py", line 130, in fit
    X = check_array(X, dtype=DTYPE, accept_sparse="csc")
  File "C:\Users\user\PycharmProjects\DC\venv\lib\site-packages\sklearn\utils\validation.py", line 521, in check_array
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got 1D array instead:
array=[ 83.42  34.98 100.   ...  83.71  47.98  65.79].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.



###################################################################### Decision Tree


from sklearn import metrics
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import os
import numpy as np

path = "E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\"

directorys = [
    ['/training/', 'p0'],
    ['/training_setB/', 'p1']
]

dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
        dfs.append(df_temp)

df = pd.concat(dfs)

df.head()






#split dataset in features and target variable

X = df[["Age"]]
y = df.SepsisLabel       #target_Var


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) # 80% train and 20% test

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = "Age",class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())




100%|██████████| 20336/20336 [03:04<00:00, 109.98it/s]
100%|██████████| 20000/20000 [12:41<00:00, 26.25it/s]
Accuracy: 0.9822801038519272
C:\Users\user\PycharmProjects\DC\venv\lib\site-packages\sklearn\externals\six.py:31: DeprecationWarning: The module is deprecated in version 0.21 and will be removed in version 0.23 since we've dropped support for Python 2.7. Please rely on the official version of six (https://pypi.org/project/six/).
  "(https://pypi.org/project/six/).", DeprecationWarning)



################################################################################
decision-tree-imputed data



import matplotlib.pyplot as plt
from sklearn import metrics
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import os
from sklearn import tree
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
import numpy as np


path = "E:\\Goethe 11-4-2021\\Zweites Semester\\Data Challenges\\project\\"

directorys = [
    ['/training/', 'p0'],
    ['/training_setB/', 'p1']
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


# %%

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
    mean = round(df[d].sum() / df.shape[0], 2)
    df.loc[df[d].isna(), d] = mean



df = df.drop(columns=["SepsisLabel"])

df_current = df.fillna(df.mean())

#split dataset in features and target variable

#X = df[["Age"]]
#y = df.SepsisLabel       #target_Var

label_names = ["no_sepsis", "sepsis"]
labels = [0, 1]
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(df_current, labels_true, test_size=0.2, random_state=1) # 80% train and 20% test

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

pred_test = clf.predict(X_test)
pred_train = clf.predict(X_train)


# Model Accuracy, how often is the classifier correct?
print(classification_report(y_test, y_pred, target_names=label_names))

#print(classification_report(y_train, pred_train, output_dict=True, labels=labels, target_names=label_names))
#print(classification_report(y_test, pred_test, output_dict=True, labels=labels, target_names=label_names))

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#F1-score
print("F1-score",f1_score(y_test, y_pred, average='weighted'))
print("F1-score",f1_score(y_test, y_pred, average='micro'))



#plot
clf = clf.fit(df_current, labels_true)
tree.plot_tree(clf, max_depth=5)
plt.show()



#from sklearn.tree import export_graphviz
#from sklearn.externals.six import StringIO
#from IPython.display import Image
#import pydotplus

#dot_data = StringIO()
#export_graphviz(clf, out_file=dot_data,
#                filled=True, rounded=True,
#                special_characters=True,feature_names = df_current,class_names=['0','1'])
#graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#graph.write_png('Sepsis.png')
#Image(graph.create_png())