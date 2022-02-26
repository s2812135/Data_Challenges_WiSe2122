import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
from PIL import Image




st.title("Results on Exersice No.3")
st.write("Summary of task sheet 3:")
st.write("In task sheet 3, different clustering methods are to be applied on the whole data set. Here we try to identify different clusters based on disease status, age groups, gender etc.). Furthermore, quality measures are to be defined. Clustering methods should also be applied according to dimensionality reduction. ")

st.header('Clustering Methods')
st.write("Two algorithms were chosen:")
st.write("1) DBSCAN")
st.write("2) K-Means algorithm ")

st.subheader("Visualizations on DBSCAN")
st.write("DBSCAN is a slightly more complex algorithm, since it attracts a higher memory complexity. That is why the algo is tried out on a maximum of 10000 people. In the following now the visualizations are presented. To see the visualizations, click on the respective buttons in the sidebar.")
st.write("The algorithm has two parameters to define how dense the clusters needs to be:")
st.write("1) epsilon") 
st.write("2) min_samples")
st.write("Both can be defined by the user.")
st.write("To identify the clusters, first the graph is displayed without applying a cluster algorithm. ")
image1 = Image.open('pics/wholeDatasetwithoutC.jpg')
st.image(image1, caption='Diagramm on the whole dataset without applying a cluster algorithm')




st.sidebar.subheader("DBSCAN Visualization 1: on the whole Dataset")
button1 = st.sidebar.button("Create Visualization on the whole Dataset with DBSCAN", key = "button1")

if(button1):
    image2 = Image.open('pics/DBSCANwholeDataset.jpg')
    st.image(image2, caption='After applying DBSCAN')


st.write("The next DBSCAN visualizations is about subgroups. With the help of sepsis and the Age subgroup data, an attempt will be made to be able to identify different age groups.  ")
st.write("Individuals with sepsis form the lower horizontal line.")
st.write("Individuals with no sepsis form the higher horizontal line.")
st.write("Again, to identify the clusters, first the graph is displayed without applying a cluster algorithm. ")
image3 = Image.open('pics/NoDBSCANAgeSepsis.jpg')
st.image(image3, caption="Before DBSCAN")


st.sidebar.subheader("DBSCAN Visualization 2: on Agegroups")
button2 = st.sidebar.button("Create Visualization on Agegroups with DBSCAN", key = "button2")

if(button2):
    image4 = Image.open('pics/DBSCANAgeSepsis.jpg')
    st.image(image4, caption='After applying DBSCAN')


st.write("By adjusting the epsilon value, a maximum of 4 clusters can be identified.")
st.write("the epsilon value is hereby: ")
st.write("")
st.write("The second DBSCAN visualization is about the subgroup Gender and Age. With the help of Gender and the Age subgroup data, an attempt will be made to be able to to look within the gender groups to see if there are age groups.  ")
st.write("Female individuals form the lower horizontal line.")
st.write("Male individuals form the higher horizontal line.")
st.write("Again, to identify the clusters, first the graph is displayed without applying a cluster algorithm. ")
image5 = Image.open('pics/NoDBSCANAgeGender.jpg')
st.image(image5, caption="Before DBSCAN")


st.sidebar.subheader("DBSCAN Visualization 3: on Agegroups")
button3 = st.sidebar.button("Create Visualization on Agegroups in both gender with DBSCAN", key = "button3")

if(button3):
    image6 = Image.open('pics/DBSCANGenderAge.jpg')
    st.image(image6, caption='After applying DBSCAN')
st.write("It can be seen that no age group can be formed among the two sexes.")

##### KMeans
st.subheader("Visualizations on K-Means")
st.write("K-Means is a centroid-based algorithm, or a distance-based algorithm, where we calculate the distances to assign a point to a cluster. In K-Means, each cluster is associated with a centroid")
st.write("Below you will be shown two diagrams of how to apply kmeans algorithm to the whole data set.")



st.sidebar.subheader("KMeans Visualization 1: on the whole Dataset")
button4 = st.sidebar.button("Create Visualization on the entire dataset", key = "button4")

if(button4):
    image7 = Image.open('pics/K-MeansFullDataset4.jpg')
    st.image(image7, caption='After applying KMEANS')
    st.write("The Reason why we choose k = 4 : ")
    image8 = Image.open('pics/KMEAN6WHOLE.jpg')
    st.image(image8, caption='After applying KMEANS')
    st.write("The Reason why we choose k=6: ")

st.write("The next visualizations are also about Subgroups")
st.write("The first visualization about subgroups we will look at is finding a relationship between Age and Sepsis")

st.sidebar.subheader("KMeans Visualization 2: On the subset: Age-Sepsis")
button5 = st.sidebar.button("Create Visualization on Age-Sepsis", key = "button5")

if(button5):
    image9 = Image.open('pics/KmeansAgeSepsis.jpg')
    st.image(image9, caption='After applying KMEANS')
    st.write("The Reason why we choose k = 4 : ")


st.write("The last visualizations are also about Subgroups")
st.write("The visualization is finding a relationship between Age and Gender")

st.sidebar.subheader("KMeans Visualization 3: On the subset: Age-Gender")
button6 = st.sidebar.button("Create Visualization on Age-Sepsis", key = "button6")

if(button6):
    image10 = Image.open('pics/KmeansAgeGender.jpg')
    st.image(image10, caption='After applying KMEANS')
    st.write("The Reason why we choose k = 4 : ")

#st.subheader("Visualizations on K-Means")
#st.write("K-means.....")



#st.sidebar.subheader("DBSCAN Visualization 1: on the whole Dataset")
#button1 = st.sidebar.button("Create Visualization on the whole Dataset with DBSCAN", key = "button1")

#if(button1):
#    image1 = Image.open('pics/NormalPacMacWithMeanValues.jpg')
#    st.write("Text needs to be included")
#    st.image(image1, caption='PaCMAP on the whole dataset without NaN values')




