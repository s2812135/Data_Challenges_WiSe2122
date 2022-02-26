# %%
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import dataframe_image as dfi
import streamlit as st
import altair as alt




@st.cache(suppress_st_warning=True)
def getDiagrammOnWholeDataSet(numberDirectory):
    directorys = []
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

    default_val = 1000000.128957

    number_of_missing_vals = list()
    number_of_total_vals = list()
    min_vals = list()
    max_vals = list()

    for z, (directory, file_head) in enumerate(directorys):
        for i, filename in enumerate(tqdm(os.listdir(directory))):

            if filename.endswith(".psv"): 
                if i == 0 and z == 0: # initialize variables
                    df = pd.read_csv(directory + file_head + '00001.psv', skiprows=0, sep='|')
                    vals = df.T.values

                    missing_vals = df.T.isna().values # transformed df where True == missing value
                    number_of_missing_vals = [0 for x in range(len(missing_vals))]
                    number_of_total_vals = [0 for x in range(len(missing_vals))] # still contains non-missing vals
                    min_vals = [default_val for v in range(len(vals))] 
                    max_vals = [-default_val for v in range(len(vals))]

                df = pd.read_csv(directory + filename, skiprows=0, sep='|')
                vals = df.T.values

                missing_vals = df.T.isna().values
                for j, arr in enumerate(missing_vals):
                    tmp_nr_total_vals = len(arr)
                    tmp_nr_missing_vals = np.count_nonzero(arr)
                    number_of_missing_vals[j] += tmp_nr_missing_vals
                    number_of_total_vals[j] += tmp_nr_total_vals


                for j, arr in enumerate(vals):
                    arr = arr[arr != np.array(None)]
                    min_vals[j] = min(min_vals[j], min(arr))
                    max_vals[j] = max(max_vals[j], max(arr))

    
    
    #print(number_of_missing_vals)
    #print(number_of_total_vals)

    # default value correction
    min_vals = [v if v != default_val else None for v in min_vals]
    max_vals = [v if v != -default_val else None for v in max_vals]

    #print(min_vals)
    #print(max_vals)



    # %%
    df = pd.read_csv(directory + file_head + '00001.psv', skiprows=0, sep='|')
    cols = df.columns
    missing_vals_ratio = [round(number_of_missing_vals[i] / (number_of_total_vals[i] if number_of_total_vals[i] != 0 else 1), 2) for i in range(len(number_of_missing_vals))]


    wholeDatasetArray = []
    #test.append(["Total Number of Values", 1])
    for i, col in enumerate(cols):
        wholeDatasetArray.append([col,1 - round(number_of_missing_vals[i] / (number_of_total_vals[i] if number_of_total_vals[i] != 0 else 1), 2)])
        print(col + ": \nNumber of missing values: " + str(number_of_missing_vals[i]) 
          + "\nNumber of total values: " + str(number_of_total_vals[i]) 
          + "\nMissing value ratio: " + str(round(number_of_missing_vals[i] / (number_of_total_vals[i] if number_of_total_vals[i] != 0 else 1), 2)) 
          + "\nMin Value: " + str(min_vals[i]) 
          + "\nMax Value: " + str(max_vals[i]) 
          +"\n\n")
  
    #df_final = pd.DataFrame()
    #df_final.append(number_of_missing_vals)
    #df_final.columns = cols
    #df_final

    #df_final = pd.DataFrame([number_of_missing_vals, number_of_total_vals, missing_vals_ratio, min_vals, max_vals], columns=cols, index=["missing values", "total values", "missing ratio", "min value", "max value"])

    #pd.set_option('display.max_columns', None)  # or 1000
    #pd.set_option('display.max_rows', None)  # or 1000
    #pd.set_option('display.max_colwidth', None)  # or 199

    df = pd.DataFrame(
        np.array(wholeDatasetArray, dtype="object"),
        columns=['Measurements','number of total values in %'])


    c = alt.Chart(df).mark_bar().encode(
        x='Measurements',
        y='number of total values in %',
    #color=alt.condition(
    #    alt.y == 1,  # If the year is 1810 this test returns True,
    #    alt.value('orange'),     # which sets the bar orange.
    #    alt.value('steelblue'))   # And if it's not true it sets the bar steelblue
    )
    st.altair_chart(c, use_container_width=False)

    #dfi._pandas_accessor.MAX_COLS = 100
    #dfi.export(df_final,"table.png")
    #df_final