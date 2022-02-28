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
import numpy
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import statistics

 



class SubGroups():
    def __init__(self, dataPath=""):
        self.dataPath = dataPath
        #hasAllFileNamesInAnArray
        self.fileNames = []
        #currentFileData Array
        self.currentFileDataArray = []
        #endResultArray
        self.endResultArray = []


    def getFileNames(self):
        """ returns list of all files in the path"""
        dirs = os.listdir(self.dataPath)
        #für alle Files in Directory
        for file in dirs:
            self.fileNames.append(file);
            #liest die File
            self.readFiles(file)
        #print(self.fileNames)

    
    def readFiles(self, file):
        """Opens every file and read it. It is Main extraction method"""
        path = self.dataPath
        backslash = "\\"
        filename = self.dataPath+backslash+file
        print("Das ist die zu extrahierende File" + file)
        fp=open(filename)
        resultArray = []
        for line in fp:
            res=line.split('|')
            resultArray.append(res)
        #jetzigeFile
        self.currentFileDataArray = resultArray

        self.extractAge(file) 

    def extractAge(self, file):
        """ extract important Glucose """
        allAge = []
        allSepsis = []
        #sepsis = 50
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][34] != "NaN"):
                allAge.append(float(self.currentFileDataArray[i][34]))
                #check if sepsis
                if(self.currentFileDataArray[i][40] == "0\n"):
                    allSepsis.append(0)
                if(self.currentFileDataArray[i][40] == "1\n"):
                    allSepsis.append(1)

        allAge = list(dict.fromkeys(allAge))
        allSepsis = list(dict.fromkeys(allSepsis))
        sepsis = 50
        if(len(allSepsis)== 1 and allSepsis[0]==0):
            sepsis=0
        if(len(allSepsis)== 1 and allSepsis[0]==1):
            sepsis=1
        if(len(allSepsis)==2):
            sepsis=1
            

        for i in range(0, len(allAge)):
            if(sepsis != 50):
                #self.endResultArray.append([int(allAge[i]), sepsis])
                self.endResultArray.append([allAge[i], sepsis])
        #self.endResultArray.append(['average', 35, statistics.mean(allAge)])



    
#Klasse 1: A1 
A1 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
#A1.makeGenderDiagram()

#A1.makeAgeGenderDiagram()
A2 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
A1.getFileNames()

#A1.readFiles("p000001.psv")
#totalEndResult = A1.endResultArray 
#print("Das ist total Endresult")
#print(totalEndResult)

#for z, (directory, file_head) in enumerate(directorys):
#    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
#        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
#        dfs.append(df_temp)



A2.getFileNames()
totalEndResult = A1.endResultArray + A2.endResultArray
#print(endResult)

#print("Das ist average Array:")
#print(A1.extract41average())
#print("Das ist Länge der Liste: "+str( A1.endResultArray ))
#print("Das ist totale Länge der Liste: "+ str(len( A1.endResultArray )))

#Load Data
xWerte = []
yWerte = []

for i in range(0, len(totalEndResult)):
    xWerte.append(totalEndResult[i][0])
    yWerte.append(totalEndResult[i][1])

#print(xWerte)
#print(yWerte)
print("Das sind die x-Werte")
print(len(list(dict.fromkeys(xWerte))))
print(list(dict.fromkeys(xWerte)))

#X, _ = make_blobs(n_samples= len(A1.endResultArray), centers=41, random_state=0)

_ = plt.plot(xWerte, yWerte, marker = '.', linewidth=0)
_ = plt.title('Clustering on the Age-Sepsis')
_ = plt.xlabel('All Ages of the dataset')
_ = plt.ylabel('Sepsis value')
plt.show()


#AB HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIER ist es experimentiell
####YOUTUBE ANFANG
#Prepare data for Model
dbscan_data = A1.endResultArray
#convert to numpy array
dbscan_data = np.array(dbscan_data, dtype=np.float32)
#convert to df
indexDF = []
for i in range(len(dbscan_data)):
    indexDF.append(str(i))

dbscan_data = pd.DataFrame(data=dbscan_data, 
                           index =indexDF, 
                           columns=["xWerte", "yWerte"])
#print(dbscan_data)
#Normalize Data
dbscan_data_scaler = StandardScaler().fit(dbscan_data)
dbscan_data = dbscan_data_scaler.transform(dbscan_data)

#model = DBSCAN(eps=0.1, min_samples=1, metric='euclidean').\
#    fit(dbscan_data)
#centers = [[18,1],[19,1],[20,1],[21,1],[22,1],[23,1],[24,1],[25,1],[26,1],[27,1],[28,1],[29,1],[30,1],[31,1],[32,1],[33,1],[34,1],[35,1],[36,1],
#           [37,1],[38,1],[39,1],[40,1],[41,1],[42,1],[43,1],[44,1],[45,1],[46,1],[47,1],[48,1],
#           [49,1],[50,1],[51,1],[52,1],[53,1],[54,1],[55,1],[56,1],[57,1],[58,1],[59,1],[60,1],[61,1],[62,1],[63,1],[64,1],[65,1],[66,1],
#           [67,1],[68,1],[69,1],[70,1],[71,1],[72,1],[73,1],[74,1],[75,1],[76,1],[77,1],[78,1],[79,1],[80,1],[81,1],[82,1],[83,1],[84,1],[85,1],[86,1],
#           [87,1],[88,1],[89,1],[90,1],[91,1],[92,1],[93,1],[94,1],[95,1],[96,1],[97,1],[98,1],[99,1], [100,1]
#           ]
model = DBSCAN(eps=0.05, min_samples=10).fit(dbscan_data)
core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
core_samples_mask[model.core_sample_indices_] = True
labels = model.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)


# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = dbscan_data[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = dbscan_data[class_member_mask & ~core_samples_mask]
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






#############################
#visualize results
#outliers_df = dbscan_data[model.labels_] == -1
#clusters_df = dbscan_data[model.labels_] != -1
#print(model.labels_)
#print("Das ist outliers")
#print(outliers_df)
#print("Dast ist clusters_df")
#print(clusters_df)

#colors = model.labels_
#colors_clusters = colors[colors != -1]
#color_outliers = 'black'
#print("Das ist colors_clusters")
#print(colors_clusters)

#clusters = Counter(model.labels_)
#print(clusters)
#print(dbscan_data[model.labels_ == -1].head())
#print("Number of Clusters {}".format(len(clusters)-1))
#print(dbscan_data)

#fig = plt.figure()
#ax = fig.add_axes([.1,.1,1,1])
#print("Das ist colors_clusters")
#print(colors_clusters)
#print(clusters_df[0])
#print("Das ist clusters_df")
#clustersdfx  =[]
#clustersdfy  =[]
#outliers_dfx =[]
#outliers_dfy =[]


#for i in range(len(clusters_df)):
#    clustersdfx.append(clusters_df[i][0])
#    clustersdfy.append(clusters_df[i][1]) 

#for i in range(len(outliers_df)):
#    outliers_dfx.append(outliers_df[i][0])
#    outliers_dfy.append(outliers_df[i][1]) 
#print("Das ist len clustersdfx")
#print(clustersdfx)
#print(clustersdfy)
#ax.scatter(clustersdfx, clustersdfy, c = colors_clusters, edgecolors='black' )
#ax.scatter(outliers_dfx, outliers_dfy, c = color_outliers, edgecolors='black' )

#ax.set_xlabel('Measurements')
#ax.set_ylabel('values of Measurements')
#plt.title("Clusterings")
#plt.show()


##### YOUTUBE ENDE



















#############################################################################




# #############################################################################
# Generate sample data
#centers = [[1, 1], [-1, -1], [1, -1]]
#X, labels_true = make_blobs(
#    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
#)

#X = StandardScaler().fit_transform(X)

# #############################################################################
# Compute DBSCAN
#db = DBSCAN(eps=0.3, min_samples=10).fit(X)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
#labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)

#print("Estimated number of clusters: %d" % n_clusters_)
#print("Estimated number of noise points: %d" % n_noise_)
#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
#print(
#    "Adjusted Mutual Information: %0.3f"
#    % metrics.adjusted_mutual_info_score(labels_true, labels)
#)
#print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

# #############################################################################
# Plot result
#import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
#unique_labels = set(labels)
#colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
#for k, col in zip(unique_labels, colors):
#    if k == -1:
        # Black used for noise.
#        col = [0, 0, 0, 1]

#    class_member_mask = labels == k

#    xy = X[class_member_mask & core_samples_mask]
#    plt.plot(
#        xy[:, 0],
#        xy[:, 1],
#        "o",
#        markerfacecolor=tuple(col),
#        markeredgecolor="k",
#        markersize=14,
#    )

#    xy = X[class_member_mask & ~core_samples_mask]
#    plt.plot(
#        xy[:, 0],
#        xy[:, 1],
#        "o",
#        markerfacecolor=tuple(col),
#        markeredgecolor="k",
#        markersize=6,
#    )

#plt.title("Estimated number of clusters: %d" % n_clusters_)
#plt.show()





















































#labels are the cluster
#clustering = DBSCAN(eps=1, min_samples=1).fit(X)
#cluster = clustering.labels_
#print("Anzahl Cluster")
#print( len(set(cluster)))


#Prepare data for Model
#dbscan_data = A1.endResultArray
#print(dbscan_data)
#dbscan_data = list(map(numpy.float32, dbscan_data))
#dbscan_data = np.array(dbscan_data, dtype=np.float32)
#print(dbscan_data)
#dbscan_data = dbscan_data.values.astype('float32', copy=False)
#dbscan_data_scaler = StandardScaler().fit(dbscan_data)
#dbscan_data = dbscan_data_scaler.transform(dbscan_data)
#print("Das ist zweiter DBSCAN")
#print(dbscan_data)
#model = DBSCAN(eps=1, min_samples=1, metric='euclidean').\
#    fit(dbscan_data)

#visualize results
#outliers_df = dbscan_data[model.labels_] == -1
#clusters_df = dbscan_data[model.labels_] != -1
#print(model.labels_)
#print(outliers_df)
#print(clusters_df)

#colors = model.labels_
#colors_clusters = colors[colors != -1]
#color_outliers = 'black'
#print("Das ist colors_clusters")
#print(colors_clusters)

#clusters = Counter(model.labels_)
#print(clusters)
#print(A1.endResultArray[model.labels == -1].head())
#print("Number of Clusters".format(len(clusters)-1))

#fig = plt.figure()
#ax = fig.add_axes([.1,.1,1,1])
#print("Das ist colors_clusters")
#print(colors_clusters)
#print(clusters_df[0])
#print("Das ist clusters_df")


#ax.scatter(clusters_df[0], clusters_df[1], c = colors_clusters/255, edgecolors='black' )
#ax.scatter(outliers_df[0], outliers_df[1], c = color_outliers/255, edgecolors='black' )

#ax.set_xlabel('Measurements')
#ax.set_ylabel('values of Measurements')
#plt.title("Clusterings")
#plt.show()


































