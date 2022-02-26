import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode


st.title("Data Challenges WS 21/22")
st.write("In this WebApp we are going to present our result visualizations of the six exersices based on this dataset:")
url = "https://physionet.org/content/challenge-2019/1.0.0/"
st.write("[https://physionet.org/content/challenge-2019/1.0.0/](%s)" % url)

#st.markdown("check out this [link](%s)" % url)
st.write("Look at the sidebar and click on the exersice results you like to see.")
st.write("You can choose which visualization you like to see for each exercise")
st.write("Furthermore, you also have options if you want to apply visualizations on the whole dataset or on a specific dataset")
st.write("For special classifications you can choose your own options.")
st.write("Otherwise have fun with our webapp! :) .")