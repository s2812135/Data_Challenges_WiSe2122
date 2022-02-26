import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

st.title("Welcome to our WebApp")
st.write("click on the sidebar to see our results from exersice number 1 to 6")