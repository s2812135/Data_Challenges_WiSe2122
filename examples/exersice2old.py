import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import FelixTestPy as felwholeData
import DariusGeschicktes as darG
import exersice2SepsisGender as simo2SepsisGender
import exersice2SepsisGenderAge as simo2SepsisGenderAge
import exersice2UnitSepsisGenderAge as simo3UnitSepsisGenderAge
import exersice2Darius1 as dar1
from PIL import Image




st.title("Results on Exersice No.2")
st.write("Summary of task sheet 2:")
st.write("In Task 2, further visualizations are to be created related to the data set. There should also be visualizations about the subgroups. Furthermore, a dimensionality reduction should be applied to the data sets. The last task describes that Data Imputation should be performed on the dataset. After the data imputation, dimensionality reduction should be applied again. ")

st.header('Visualization of the data set')
st.write("There are multiple visualizations. We will start first with visualizations about the subgroup gender with sepsis. Then we will look at whether age groups can be formed and the relationship between age groups of both genders and sepsis. Last, we look at whether there is a difference in which ICUs the patients were in.  ")
st.subheader("Data Visualization 1: Sepsis-Gender visualization")

#Visualization 1
st.sidebar.subheader("Data Visualization 1: Sepsis-Gender")

option = st.sidebar.selectbox(
     'Choose on which dataset you want to apply Sepsis-Gender',
     ('','dataset 1', 'dataset 2', 'both'), key="selBox1")

button1 = st.sidebar.button("Create Sepsis-Gender visualization", key = "button1")
#evtl. davor schauen wegen Button 1 und welcher Datensatz
if(option == "dataset 1" and button1 == True):
    simo2SepsisGender.decideDiagram(1)
    st.write("You chose a vizualisation on the first dataset")
    st.write("Description of the result")

if(option == "dataset 2"and button1 == True):
    simo2SepsisGender.decideDiagram(2)
    st.write("You chose a vizualisation on the second dataset")
    st.write("Description of the result")

if(option == "both" and button1 == True):
    simo2SepsisGender.decideDiagram(3)
    st.write("You chose a vizualisation on both datasets")
    st.write("Description of the result")


#Vizualization 2
st.subheader('Data Visualization 2: Sepsis-Age-Gender-relation')
st.write("In this section you will find the illustration about statistical properties based on Timestamps")
st.sidebar.subheader("Data Visualization 2: Sepsis-Age-Gender-Relation")
option2 = st.sidebar.selectbox(
     'Choose on which dataset you want to vizualize',
     ('','dataset 1', 'dataset 2', 'both'), key = "selBox2")
button2 = st.sidebar.button("Create Visualization about Sepsis-Age-Gender relation", key ="button2")
#evtl. davor schauen wegen Button
if(option2 == "dataset 1" and button2 == True):
    simo2SepsisGenderAge.decideDiagram(1)

if(option2 == "dataset 2"and button2 == True):
    simo2SepsisGenderAgedecideDiagram(2)

if(option2 == "both" and button2 == True):
    simo2SepsisGenderAge.decideDiagram(3)


#Visualization 3
st.subheader('Data Visualization 3: Sepsis-ICU-Age-Gender relation')
st.write("In this section you will find the illustration about statistical properties based on Timestamps")
st.sidebar.subheader("Data Visualization 3: Sepsis-ICU-Age-Female-Male")
option3 = st.sidebar.selectbox(
     'Choose on which dataset you want to vizualize',
     ('','dataset 1', 'dataset 2', 'both'), key = "selBox3")
button3 = st.sidebar.button("Create Visualization on  Sepsis-ICU-Age-Female-Male", key = "button3")
#evtl. davor schauen wegen Button
if(option3 == "dataset 1" and button3 == True):
    simo3UnitSepsisGenderAge.decideDiagram(1)

if(option3 == "dataset 2"and button3 == True):
    simo3UnitSepsisGenderAge.decideDiagram(2)

if(option3 == "both" and button3 == True):
    simo3UnitSepsisGenderAge.decideDiagram(3)


#Visualization 4: Dimensionality Reduction
st.subheader('Data Visualization 4: Dimensionality Reduction on the whole Dataset')
st.write("PaCMAP on the whole dataset with NaN values filled as the mean of the respective values over the whole set")
st.sidebar.subheader("Data Visualization 4: PacMap Dimensionality Reduction (mean values)")
#option4 = st.sidebar.selectbox(
#     'Choose on which dataset you want to vizualize with PacMap',
#     ('','dataset 1', 'dataset 2', 'both'), key = "selBox4")
button4 = st.sidebar.button("Create Visualization on the whole Dataset with PacMap", key = "button4")

if(button4):
    image1 = Image.open('pics/NormalPacMacWithMeanValues.jpg')
    st.write("Text needs to be included")
    st.image(image1, caption='PaCMAP on the whole dataset with NaN values filled as the mean of the respective values over the whole set')

#Visualization 5: Dimensionality Reduction
st.subheader('Data Visualization 5: Dimensionality Reduction on Subgroups')
st.write("PaCMAP on Subgroups without NaN values over the whole dataset")
st.sidebar.subheader("Data Visualization 5: PacMap Dimensionality Reduction on Subgroups")
#option4 = st.sidebar.selectbox(
#     'Choose on which dataset you want to vizualize with PacMap',
#     ('','dataset 1', 'dataset 2', 'both'), key = "selBox4")
button5 = st.sidebar.button("Create Visualization on Subgroups with PacMap", key = "button5")

if(button5):
    #image2
    st.write("This is PacMan algorithm applied on Age")
    image2 = Image.open('pics/PacMacAge.jpg')
    st.write("Text needs to be included")
    st.image(image2, caption='PaCMAP on Subgroups without NaN values over the whole dataset: Sepsis-Age')
    #image3
    st.write("This is PacMan algorithm applied on Gender")
    image3 = Image.open('pics/PacMacGenderNormal.jpg')
    st.write("Text needs to be included")
    st.image(image3, caption='PaCMAP on Subgroups without NaN values over the whole dataset: Sepsis-Gender')

#Visualization 6: Dimensionality Reduction and Imputation 
st.subheader('Data Visualization 6: Dimensionality Reduction and Data Imputation')
st.write("PaCMAP and UMAP without NaN values over the whole dataset")
st.sidebar.subheader("Data Visualization 5:Dimensionality Reduction and Data Imputation")
#option4 = st.sidebar.selectbox(
#     'Choose on which dataset you want to vizualize with PacMap',
#     ('','dataset 1', 'dataset 2', 'both'), key = "selBox4")
button6 = st.sidebar.button("Create Visualization with PacMap and UMAP", key = "button6")

if(button6):
    #image2
    st.write("This is PacMan algorithm applied on the whole set")
    image4 = Image.open('pics/PacMapDimensionalityReductionAndImputation.jpg')
    st.write("Text needs to be included")
    st.image(image4, caption='PaCMAP on imputated values over the whole dataset')
    #image3
    st.write("This is PacMan algorithm applied on Gender")
    image5 = Image.open('pics/UMAPDimensionalityReductionAndImputation.jpg')
    st.write("Text needs to be included")
    st.image(image5, caption='UMAP on imputated values over the whole dataset')

#Visualization 4: Dimensionality Reduction
#st.subheader('Data Visualization 4: Dimensionality Reduction ')
#st.write("Its a visualization on mean values in NaN-values PacMan")
#st.sidebar.subheader("Data Visualization: PacMap Dimensionality Reduction")
#option4 = st.sidebar.selectbox(
#     'Choose on which dataset you want to vizualize with PacMap',
#     ('','dataset 1', 'dataset 2', 'both'), key = "selBox4")
#button4 = st.sidebar.button("Create Visualization on with PacMap", key = "button4")

#if(button4):
#    image1 = Image.open('NormalPacMacWithMeanValues.jpg')
#    st.write("Text needs to be included")
#    st.image(image1, caption='PaCMAP on the whole dataset with NaN values filled as the mean of the respective values over the whole set')

#evtl. davor schauen wegen Button
#if(option4 == "dataset 1" and button4 == True):
#    dar1.darius1(1)

#if(option4 == "dataset 2"and button4 == True):
#    dar1.darius1(2)

#if(option4 == "both" and button4 == True):
#    dar1.darius1(3)
