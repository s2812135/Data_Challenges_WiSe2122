import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import statProperties as felwholeData
import timeseriesVisualization as darG
import exersice2SepsisGender as simo2SepsisGender
import exersice2SepsisGenderAge as simo2SepsisGenderAge
import exersice2UnitSepsisGenderAge as simo3UnitSepsisGenderAge
import exersice2DimRed as dar1
from PIL import Image




st.title("Visualizations on Sepsis-Subgroup-Relation")
st.write("In Task 2, further visualizations are to be created related to the data set. There should also be visualizations about the subgroups.")

st.header('Visualization of the data set')
st.write("There are multiple visualizations. We will start first with visualizations about the subgroup gender with sepsis. Then we will look at whether age groups can be formed and the relationship between age groups of both genders and sepsis. Last, we look at whether there is a difference in which ICUs the patients were in.  ")

#Visualization 1
st.sidebar.subheader("Data Visualizations on subgroups")
st.sidebar.write("Select visualizations you like to see on subgroups")

features = st.sidebar.multiselect(
     'Select Relations you like to visualize',
     ['Gender-Sepsis-relation', 'Sepsis-Age-Gender-relation', 'Sepsis-ICU-Age-Gender relation'],
     ['Gender-Sepsis-relation'])

#button1 = st.sidebar.button("Create Sepsis-Gender visualization", key = "button1")

if(features):
    st.write("These Relations were chosen: ")
    for i in range(len(features)):
        test = str(i+1)
        test2 = i+1
        st.write(test2, ") ", features[i])
        #if für evtl. explainen


    #for j in range(len(features)):
    #    test = str(j+1)
    #    subheaderstring = "Subgroup Visualization"+ test + ": "+features[i]
    #    st.subheader(subheaderstring)

#select which dataset
option1 =  st.sidebar.selectbox(
     'Choose dataset you want to vizualize',
     ('','dataset 1', 'dataset 2', 'both'), key = "selBox1")
button1 = st.sidebar.button("Create Visualizations based on subgroups", key = "button1")
#evtl. davor schauen wegen Button
if(option1 == "dataset 1" and button1 == True):
    #run the algos
    for k in range(len(features)):
        if(features[k]=="Gender-Sepsis-relation"):
            test = str(k+1)
            #subheaderstring = "Subgroup Visualization"+ test + ": "+features[k]
            subheaderstring = features[k]
            st.subheader(subheaderstring)
            st.write("With the help of this vizualization, it can be seen how many men and women have sepsis and do not have sepsis in dataset 1.")
            simo2SepsisGender.decideDiagram(1)
            st.write("There are 8502 women and 11834 men in dataset 1. Converted into percentages, there would be 41.81% of women and 58.19% of men. Out of 8502 women, 698 were infected with sepsis, while out of 11834 men, 1092 were infected with sepsis. Converted, the value of diseased women measured among all women is 8, 21 percent (regardless of gender would be 3.43 percent in total). The value of men infected with sepsis among all men would be: 9.23% (regardless of gender it would be: 5.37 %).")


        if(features[k]=="Sepsis-Age-Gender-relation"):
            test = str(k+1)
            subheaderstring = "Visualization on " ": "+features[k]
            st.subheader(subheaderstring)
            st.write("For both upcoming visualizations on dataset 1, we have divided women and men into 8 age groups of our own. For each of these age groups, the first visualization is about the number of people who have and do not have sepsis. The second visualization will describe the age groups and whether they have sepsis or not as a percentage. ")
            simo2SepsisGenderAge.decideDiagram(1)

        if(features[k]=="Sepsis-ICU-Age-Gender relation"):
            test = str(k+1)
            subheaderstring = "Visualization on "+ test + ": "+features[k]
            st.subheader(subheaderstring)
            st.write("Four diagrams are shown below for this relation. The first chart is about the number of people with different age groups who visited different ICUs and people who did not visit any ICU. The other three charts are the percentage of how many people with sepsis were among the different ICUs and were not in any ICU.")
            simo3UnitSepsisGenderAge.decideDiagram(1)
            #simo3UnitSepsisGenderAge.decideDiagram(1)

if(option1 == "dataset 2"and button1 == True):
    #simo3UnitSepsisGenderAge.decideDiagram(2)
    #run the algos
    for k in range(len(features)):
        if(features[k]=="Gender-Sepsis-relation"):
            test = str(k+1)
            subheaderstring = "Subgroup Visualization"+ test + ": "+features[k]
            st.subheader(subheaderstring)
            st.write("With the help of this vizualization, it can be seen how many men and women have sepsis and do not have sepsis in dataset 2.")
            simo2SepsisGender.decideDiagram(2)
        
        if(features[k]=="Sepsis-Age-Gender-relation"):
            test = str(k+1)
            subheaderstring = "Visualizations on: "+features[k]
            st.subheader(subheaderstring)
            st.write("For both upcoming visualizations on dataset 2, we have divided women and men into 8 age groups of our own. For each of these age groups, the first visualization is about the number of people who have and do not have sepsis. The second visualization will describe the age groups and whether they have sepsis or not as a percentage. ")
            simo2SepsisGenderAge.decideDiagram(2)

        if(features[k]=="Sepsis-ICU-Age-Gender relation"):
            test = str(k+1)
            subheaderstring = "Subgroup Visualization"+ test + ": "+features[k]
            st.subheader(subheaderstring)
            st.write("Four diagrams are shown below for this relation. The first chart is about the number of people with different age groups who visited different ICUs and people who did not visit any ICU. The other three charts are the percentage of how many people with sepsis were among the different ICUs and were not in any ICU.")
            simo3UnitSepsisGenderAge.decideDiagram(2)


if(option1  == "both" and button1 == True):
    #run the algos
    for k in range(len(features)):
        if(features[k]=="Gender-Sepsis-relation"):
            test = str(k+1)
            subheaderstring = " Visualization on "": "+features[k]
            st.subheader(subheaderstring)
            st.write("With the help of this vizualization, it can be seen how many men and women have sepsis and do not have sepsis in both datasets.")
            simo2SepsisGender.decideDiagram(3)

        if(features[k]=="Sepsis-Age-Gender-relation"):
            test = str(k+1)
            subheaderstring = "Visualizations on the "+features[k]
            st.subheader(subheaderstring)
            st.write("For both upcoming visualizations on both datasets, we have divided women and men into 8 age groups of our own. For each of these age groups, the first visualization is about the number of people who have and do not have sepsis. The second visualization will describe the age groups and whether they have sepsis or not as a percentage. ")
            simo2SepsisGenderAge.decideDiagram(3)

        if(features[k]=="Sepsis-ICU-Age-Gender relation"):
            test = str(k+1)
            subheaderstring = "Visualizations on the "+features[k]
            st.subheader(subheaderstring)
            st.write("Four diagrams are shown below for this relation. The first chart is about the number of people with different age groups who visited different ICUs and people who did not visit any ICU. The other three charts are the percentage of how many people with sepsis were among the different ICUs and were not in any ICU.")
            simo3UnitSepsisGenderAge.decideDiagram(3)



    
        #if für evtl. explainen


    #simo3UnitSepsisGenderAge.decideDiagram(3)

#evtl. davor schauen wegen Button 1 und welcher Datensatz
#if(option == "dataset 1" and button1 == True):
#    simo2SepsisGender.decideDiagram(1)
#    st.write("You chose a vizualisation on the first dataset")
#    st.write("Description of the result")

#if(option == "dataset 2"and button1 == True):
#    simo2SepsisGender.decideDiagram(2)
#    st.write("You chose a vizualisation on the second dataset")
#    st.write("Description of the result")

#if(option == "both" and button1 == True):
#    simo2SepsisGender.decideDiagram(3)
#    st.write("You chose a vizualisation on both datasets")
#    st.write("Description of the result")

