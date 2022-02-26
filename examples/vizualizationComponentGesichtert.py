import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import dataframe_image as dfi
import streamlit as st
import altair as alt
import streamlit as st


personWerte = []

@st.cache(suppress_st_warning=True)
def getPeople(numberDirectory, gender, sepsis, age, featurelist, chooseperson):
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
            for j, row in df_temp.iterrows():
                #schauen, ob richtige file
                #if(df_temp.at[j,'Gender'] == gender and df_temp.at[j,'SepsisLabel'] == sepsis and round(df_temp.at[j,'Age']) == age):
                #if(df_temp.at[j,'Gender'] == gender and df_temp.at[j,'SepsisLabel'] == sepsis and round(df_temp.at[j,'Age']) == age):
                #    personWerte.append(filename)
                
                if(filename == chooseperson):
                    #print("Das ist filename: ", filename)
                    #für jedes feature
                    rows = []
                    for f in featurelist:
                        if(np.isnan(df_temp.at[j, f])):
                            #Schauen, was f�r ein Wert man hier eingibt
                            rows.append(0)
    
                #if(df_temp.at[j,'HR'] != "nan"):
                        if(np.isnan(df_temp.at[j, f])!= True):
                            rows.append(df_temp.at[j,f])
                    timeseries_werte.append(rows)
                #TODO: Noch ein Break reinbauen
            if(filename == chooseperson):
                break
            #if(i == 0):
                #break

    #print(timeseries_werte)
    #print("Liste der Personen", list(dict.fromkeys(personWerte)))
    #return personWerte
    #print("timeseries type", type(timeseries_werte))
    #print("Das ist timeseries_werte")
    #print(timeseries_werte)
    st.header('Visualization Result on a chosen Person')

    st.write("This diagram gives you values about the selected person as well as about the selected features. The figure represents the Time Series data of a person in a hospital stay. The x-axis describes the time every hour. the y-axis describes the values of the previously selected features.")
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

  


