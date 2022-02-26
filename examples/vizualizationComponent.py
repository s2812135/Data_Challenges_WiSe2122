# %%
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import dataframe_image as dfi
import streamlit as st
import altair as alt
import itertools




@st.cache(suppress_st_warning=True)
def getPeople(numberDirectory, gender, sepsis, age, featurelist):
    #sepsis = str(sepsis) + "\n"
    print(sepsis)
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
    
    #Werte der Timeseries f�r y Achse
    timeseries_werte = []
    #columns sind die features

    #Liste with persons with specific age
    personWerte = []
    for z, (directory, file_head) in enumerate(directorys):
        for i, filename in enumerate(tqdm(os.listdir(directory))):
            #�ffnen der Datei und lesen
            df_temp = pd.read_csv(directory + filename, skiprows=0, sep='|')
            #j f�r dateienzeile appende ins Array
            #row ersetzen mit 
            #if(i == 1000):
            #    break

            for j, row in df_temp.iterrows():
                if(df_temp.at[j,'Gender'] == gender and df_temp.at[j,'SepsisLabel'] == sepsis and round(df_temp.at[j,'Age']) == age):
                    personWerte.append([filename, gender, age, sepsis, "dataset "+str(z)])
    personWerte.sort()
    #list(k for k,_ in itertools.groupby(k))
    return list(personWerte for personWerte,_ in itertools.groupby(personWerte))
    #Anzeigenlassen der Werte

            #if(filename == "p000818.psv"):
            #    df_temp = pd.read_csv(directory + filename, skiprows=0, sep='|')

            #j f�r dateienzeile appende ins Array
            #row ersetzen mit 
                #for j, row in df_temp.iterrows():
                #    tsHelper = []
                #schauen, ob richtige file
                #if(df_temp.at[j,'Gender'] == gender and df_temp.at[j,'SepsisLabel'] == sepsis and round(df_temp.at[j,'Age']) == age):
                #    personWerte.append(filename)

                #    if(np.isnan(df_temp.at[j,'HR'])):
                    #Schauen, was f�r ein Wert man hier eingibt
                #        tsHelper.append(0)

                #if(df_temp.at[j,'HR'] != "nan"):
                #    if(np.isnan(df_temp.at[j,'HR'])!= True):
                #        tsHelper.append(df_temp.at[j,'HR'])


                #    if(np.isnan(df_temp.at[j,'O2Sat'])):
                    #Schauen, was f�r ein Wert man hier eingibt
                #        tsHelper.append(0)

                #if(df_temp.at[j,'HR'] != "nan"):
                #    if(np.isnan(df_temp.at[j,'O2Sat'])!= True):
                #        tsHelper.append(df_temp.at[j,'O2Sat'])                


                #    if(np.isnan(df_temp.at[j,'Resp'])):
                    #Schauen, was f�r ein Wert man hier eingibt
                #        tsHelper.append(0)

                #if(df_temp.at[j,'HR'] != "nan"):
                #    if(np.isnan(df_temp.at[j,'Resp'])!= True):
                #        tsHelper.append(df_temp.at[j,'Resp'])          
                    
                #    timeseries_werte.append(tsHelper)


    print(timeseries_werte)
    #print("Liste der Personen", list(dict.fromkeys(personWerte)))
    #print("timeseries type", type(timeseries_werte))

    chart_data = pd.DataFrame(
    #np.random.randn(20, 3),
    np.array(timeseries_werte, dtype="object"),
    columns=featurelist)

    st.line_chart(chart_data)
    # open file and do first a 
    #for z, (directory, file_head) in enumerate(directorys):
    #    for i, filename in enumerate(tqdm(os.listdir(directory))):
    #        if()
    #        print("Das ist i",i)
    #        print("Das ist z",z)

  


