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



#path = "C:\\Users\dariu\\Documents\\Master Wirtschaftsinformatik\\Data Challenges\Data\\"
path = "D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Teamtreffen\\Aufgabenblatt5\\Aufgabenblatt51aCode\\"

directorys = [
    ['training_setA/training/', 'p0'],
    ['training_setB/training/', 'p1']
]

dfs = []

for z, (directory, file_head) in enumerate(directorys):
    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
        if(i == 100):
            break
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

print(classification_report(y_train, pred_train, output_dict=True, labels=labels, target_names=label_names))
print(classification_report(y_test, pred_test, output_dict=True, labels=labels, target_names=label_names))

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#F1-score
print("F1-score",f1_score(y_test, y_pred, average='weighted'))
print("F1-score",f1_score(y_test, y_pred, average='micro'))



#plot
clf = clf.fit(df_current, labels_true)
tree.plot_tree(clf, max_depth=20)
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