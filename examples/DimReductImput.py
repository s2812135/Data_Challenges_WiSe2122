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
import testDarius as tDs
import pacmap_male_female as pmf



st.title("Results on Exersice No.2")
st.write("In Task 2, further visualizations are to be created related to the data set. There should also be visualizations about the subgroups. Furthermore, a dimensionality reduction should be applied to the data sets. The last task describes that Data Imputation should be performed on the dataset. After the data imputation, dimensionality reduction should be applied again. ")

st.header('Visualization of the data set')
st.write("There are multiple visualizations. We will start first with visualizations about the subgroup gender with sepsis. Then we will look at whether age groups can be formed and the relationship between age groups of both genders and sepsis. Last, we look at whether there is a difference in which ICUs the patients were in.  ")

#Visualization 1
st.sidebar.subheader("Data Visualizations with Dimensionality Reduction")


#test
#button1 = st.sidebar.button("Create statistical proporties visualization")
#evtl. davor schauen wegen Button
#if(button1 == True):
#    tDs.pacmapTest()


#################################### TEST ENDE ###########################

st.header('Dimensionality Reduction')
st.write("Beschreibung kommt später ")

#Dimensionality Reduction
st.sidebar.subheader("Dimensionality Reduction")
#st.sidebar.write("Select Results of ")

option =  st.sidebar.selectbox(
     'Choose dataset you want to vizualize',
     ('dataset 1', 'dataset 2', 'both'), key = "selBox1")

featuresDimReduction = st.sidebar.multiselect(
     'Select Dimensionality Reduction Technique',
     ['PaCMAP', 'UMAP'],
     ['PaCMAP'])

#button1 = st.sidebar.button("Create Sepsis-Gender visualization", key = "button1")

if(featuresDimReduction):
    st.write("These Methods were chosen: ")
    for i in range(len(featuresDimReduction)):
        test = str(i+1)
        test2 = i+1
        st.write(test2, ") ", featuresDimReduction[i])

option2 =  st.sidebar.selectbox(
     'Choose one of the three Data Imputations',
     ('mean', 'median'), key = "selBox3")

samplesinput = st.sidebar.number_input("Choose the number of samples", step = 1000, min_value =1000, max_value = 500000)


if 'dimRed' not in st.session_state:
    st.session_state.dimRed = ""

option3 =  st.sidebar.selectbox(
     'Select on which data you want to apply Dimensionality Reduction',
     ('Gender: Male', 'Gender: Female','Age','on the whole Dataset'), key = "selBox2")

if option3:
    st.session_state.dimRed = option3

#Soll in session gespeichert werden
#st.session_state.samplesinput = ageinput

if(option3 == ''):
    st.write("Warning!Please select on which data you want to apply Dimensionality Reduction")

if(option2 == ''):
    st.write("Please select on which data you want to apply Dimensionality Reduction")
    
button = st.sidebar.button("create vizualization")
if button: 
    st.write("es funzt")
    st.write(st.session_state.dimRed)
    pmf.start_pacmac_gender()
    

