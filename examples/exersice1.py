import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import statProperties as felwholeData
import timeseriesVisualization as darG





st.title("Visualisations on the whole dataset")
st.write("The first task sheet was about looking at the data sets and to provide statistical properties. Furthermore, subgroups should be found and there should be an analysis of the time series data. Visualizations were made in relation to the statistical properties and the time series. You will see them in the following if you have entered the required data in the sidebar. ")

st.header('Statistical properties of the entire dataset')
st.write("In this section you will find the illustration about statistical properties based on the whole dataset")


st.sidebar.subheader("statistical properties of the entire dataset")

option = st.sidebar.selectbox(
     'Choose on which dataset you want to apply statistical proporties',
     ('','dataset 1', 'dataset 2', 'both'), key="selBox1")

button1 = st.sidebar.button("Create statistical proporties visualization")
#evtl. davor schauen wegen Button
if(option == "dataset 1" and button1 == True):
    felwholeData.getDiagrammOnWholeDataSet(0)
    st.write("In this visualization, all features that are present in the first dataset are mapped on the x-axis. The y-axis shows the percentage of the respective feature that is available in the data set. This makes it easy to see which features always provide data and which features can be imputed.  ")

if(option == "dataset 2"and button1 == True):
    felwholeData.getDiagrammOnWholeDataSet(1)
    st.write("In this visualization, all features that are present in the second dataset are mapped on the x-axis. The y-axis shows the percentage of the respective feature that is available in the data set. This makes it easy to see which features always provide data and which features can be imputed.  ")


if(option == "both" and button1 == True):
    felwholeData.getDiagrammOnWholeDataSet(2)
    st.write("In this visualization, all features that are present in both datasets (luckily they have the same column numbers) are mapped on the x-axis. The y-axis shows the percentage of the respective feature that is available in the data set. This makes it easy to see which features always provide data and which features can be imputed.  ")



st.header('Statistical properties on Timestamps')
st.write("In this section you will find the illustration about statistical properties based on Timestamps")
st.sidebar.subheader("statistical properties on timestamps")
option2 = st.sidebar.selectbox(
     'Choose on which dataset you want to apply statistical proporties',
     ('','dataset 1', 'dataset 2', 'both'), key = "selBox2")
button2 = st.sidebar.button("Create Visualization on timestamps")
#evtl. davor schauen wegen Button
if(option2 == "dataset 1" and button2 == True):
    darG.getAllTimeSeries(0)
    st.write("This timestamp visualization is about timestamps in relation to patients. The x-axis describes the number of timestamps, while the y-axis describes how many people have the same number of timestamps. Here we can see that the minimum number of a timestamp is 8 hours, while the longest number of timestamps is between 330 and 340. The most frequent number of timestamps is around 40.")


if(option2 == "dataset 2"and button2 == True):
    darG.getAllTimeSeries(1)
    st.write("This timestamp visualization is about timestamps in relation to patients. The x-axis describes the number of timestamps, while the y-axis describes how many people have the same number of timestamps. Here we can see that the minimum number of a timestamp is 8 hours, while the longest number of timestamps is between 330 and 340. The most frequent number of timestamps is around 40.")

if(option2 == "both" and button2 == True):
    darG.getAllTimeSeries(2)
    st.write("This timestamp visualization is about timestamps in relation to patients. The x-axis describes the number of timestamps, while the y-axis describes how many people have the same number of timestamps. Here we can see that the minimum number of a timestamp is 8 hours, while the longest number of timestamps is between 330 and 340. The most frequent number of timestamps is around 40.")
