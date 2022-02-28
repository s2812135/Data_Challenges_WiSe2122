
"""
Created on Sat Oct 30 19:28:48 2021
"""

import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import numpy as np
import streamlit as st
from collections import Counter
import altair as alt
import streamlit as st
from tqdm import tqdm
import collections

@st.cache(suppress_st_warning=True)
def getAllTimeSeries(numberDirectory):



    if(numberDirectory == 0):
        directorys = [
        ['training_setA/training/', 'p0']
        ]

    if(numberDirectory == 1):
        directorys = [
        ['training_setB/training/', 'p1']
        ]
    if(numberDirectory == 2):
        directorys = [
        ['training_setA/training/', 'p0'],
        ['training_setB/training/', 'p1']
        ]

    #files = os.listdir(path)
    #files2 = os.listdir(path2)
    timeseries_length = []
    #timeseries_length2 = []


    for z, (directory, file_head) in enumerate(directorys):
        for i, filename in enumerate(tqdm(os.listdir(directory))):
            #print("Das ist i")
            #print(i)
            rows_in_file=0
            df = pd.read_csv(directory + filename, skiprows=0, sep='|')
            #print("Das ist df")
            #print(df)
            for row in range(len(df)):
                rows_in_file = rows_in_file + 1
            timeseries_length.append(rows_in_file)
            #if(i == 1):
            #    break

    print("Das ist timeseries_length")
    #print(timeseries_length)
    my_dict = {i:timeseries_length.count(i) for i in timeseries_length}
    print("das ist my_dict")
    #print(my_dict)
    print("nun sortiert")
    tuple = sorted(my_dict.items())
    #print( tuple)
    endlist = []
    for tuple_elem in tuple:
        endlist.append([tuple_elem[0], tuple_elem[1]])

    #print(endlist)
    #for i in range(len(tuple)):
    #    endlist.append([tuple[i]])
    #   print(endlist)
    df = pd.DataFrame(
    np.array(endlist, dtype="object"),
    columns=['Number of Timestamps','Number of Patients'])

    c = alt.Chart(df).mark_bar().encode(
        x='Number of Timestamps',
        y='Number of Patients'
    )
    st.altair_chart(c, use_container_width=False)