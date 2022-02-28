
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




