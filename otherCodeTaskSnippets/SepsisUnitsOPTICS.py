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

        #self.extractAge(file) 
        #self.extractGender(file) 
        self.extractUnit1(file)
        #self.extractUnit2(file)


    #AB HIIIIIIER: Gender
    def extractGender(self, file):
        """ extract important allBaseExcess """
        allGender = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][35] != "NaN"):
                allGender.append(float(self.currentFileDataArray[i][35]))
            #if(self.currentFileDataArray[i][35] == "NaN"):
                #allGender.append(float(0))

        allGender = list(dict.fromkeys(allGender))

        for i in range(0, len(allGender)):
            self.endResultArray.append([36, allGender[i]])
        #self.endResultArray.append(['average', 36, statistics.mean(allGender)])


    def extractUnit1(self, file):
        """ extract important Magnesium """
        allUnit1 = []
        #allUnit2 = []
        #noUnit = []
        allSepsis = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][36] != "NaN" and self.currentFileDataArray[i][37] != "NaN"):
                if(self.currentFileDataArray[i][36] == "1" ):
                    allUnit1.append(1)
                    if(self.currentFileDataArray[i][40] == "1\n" ):
                        allSepsis.append(1)
                    if(self.currentFileDataArray[i][40] == "0\n" ):
                        allSepsis.append(0)
                if(self.currentFileDataArray[i][37] == "1" ):
                    allUnit1.append(2)
                    if(self.currentFileDataArray[i][40] == "1\n" ):
                        allSepsis.append(1)
                    if(self.currentFileDataArray[i][40] == "0\n" ):
                        allSepsis.append(0)
            if(self.currentFileDataArray[i][36] == "NaN" and self.currentFileDataArray[i][37]):
                allUnit1.append(float(0))
                if(self.currentFileDataArray[i][40] == "1\n" ):
                    allSepsis.append(1)
                if(self.currentFileDataArray[i][40] == "0\n" ):
                    allSepsis.append(0)
            # Geht nicht 

        allUnit1 = list(dict.fromkeys(allUnit1))
        allSepsis = list(dict.fromkeys(allSepsis))
        
        if(len(allUnit1)==1):
            if(len(allSepsis) == 1 and allSepsis[0]==1):
                self.endResultArray.append([1, allUnit1[0]])
            if(len(allSepsis) == 1 and allSepsis[0]== 0):
                self.endResultArray.append([0, allUnit1[0]])
            if(len(allSepsis) == 2):
                self.endResultArray.append([1, allUnit1[0]])


    


    
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

#X, _ = make_blobs(n_samples= len(A1.endResultArray), centers=41, random_state=0)

_ = plt.plot(xWerte, yWerte, marker = '.', linewidth=0)
_ = plt.title('DBSCAN over ICUs and people with and without Sepsis')
_ = plt.xlabel('0 has no Sepsis, 1 has Sepsis')
_ = plt.ylabel('0 is no ICU, 1 is MICU, 2 is SICU')
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
model = DBSCAN(eps=0.1, min_samples=1).fit(dbscan_data)
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


































