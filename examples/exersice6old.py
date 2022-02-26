import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import FelixTestPy as felwholeData
import vizualizationComponent as vizComp
import vizualizationComponentGesichtert as vizCompGesichert
import eigeneGridImplementierung as eigenGrid



st.title("Results on Exersice No.6")
st.write("This task sheet is about choosing the right time series features and time series classifier libraries. Furthermore, the webapp should provide a visualization component of the timeseries data and several TS classifiers should be compared.")
st.header('Visualization component for time series')
st.write("To generate a visualization based on Time Series data, certain information is required, which is requested and should be added on the left sitebar. After the required values have been entered, a table is displayed with possible persons corresponding to the criteria entered. ")



st.sidebar.subheader("time series visualization")

option = st.sidebar.selectbox(
     'Choose on which dataset you want to apply the vizualization',
     ('','dataset 1', 'dataset 2', 'both'))

#Soll in session gespeichert werden
st.session_state.option = option

st.sidebar.subheader("Choose one gender")
gender = st.sidebar.checkbox("male")
gender2 = st.sidebar.checkbox("female")

st.sidebar.subheader("Choose patient with or without Sepsis (not both)")
sepsis = st.sidebar.checkbox("Sepsis")
noSepsis = st.sidebar.checkbox("No Sepsis")


ageinput = st.sidebar.number_input("Write down Age of a patient", step = 1, min_value =18, max_value = 80)
#Soll in session gespeichert werden
st.session_state.ageinput = ageinput


#st.sidebar.subheader("Select Features for the visualization")
features = st.sidebar.multiselect(
     'Select Features for the visualization',
     ['HR', 'O2Sat', 'SBP', 'MAP', 'DBP', 'Resp'],
     ['HR', 'O2Sat', 'Resp'])

#Soll in session gespeichert werden
st.session_state.features = features

# habe ich hier geswitched! (also bei personen wird schon visualisierung generiert 
# später ändern
#button2 = st.sidebar.button("Generate possible persons")
button1 = st.sidebar.button("Search for suitable persons")

#vorher die onlypersons abspeichern
onlypersons = []
personlist = []

#if(button1 and gender == True and gender2 == True):
#    st.write("You can only choose one gender! Please redo your input")

#evtl. davor schauen wegen Button
#if(option == "dataset 1" and button1 == True and gender==True and gender2== False and sepsis == True and noSepsis == False):
#personlist = vizComp.getPeople(0,1,1,ageinput,features)
#Soll in session gespeichert werden
#st.session_state.ageinput = ageinput




print("Das ist features")
print(features)
    # Nun liste die returnted Personen auf
print("Das ist personlist")
print(personlist)
    #Now persons grid
eigenGrid.getGridImplementierung(personlist)
    #Wenn eingegeben, auf neue Seite verweisen und speichere alle eingaben#

    #create person tuple
for i in range(len(personlist)):
    onlypersons.append(personlist[i][0])
print("Das ist onlypersons")
print(onlypersons)
persontuple = tuple(onlypersons)



choosePerson = st.sidebar.selectbox('Choose one person you like to vizualize' , options = persontuple)

print("nochmal choosePerson")
#evtl nochmal ein if
#define session variable
#if choosePerson: 



#def saveTesten(choosePerson):
#    st.session_state['choosePerson'] = choosePerson
#    saveInVariable = choosePerson

#st.session_state.choosePerson = choosePerson
#vizualize

#if(option == "dataset 1" and button1 == True and gender==True and gender2== False and sepsis == False and noSepsis == True):
#    st.write("Your Input was: ")
    #speichere in Variable
#    personlist = vizComp.getPeople(0,1,c,ageinput,features)
    # Nun liste die returnted Personen auf
    #print(personlist)

#choosePersonButton = st.sidebar.button("create vizualization")
#if choosePersonButton: 
if button1:
    print("das ist ageinput,features, choosePerson")
    print(choosePerson)
    #print(st.session_state['choosePerson'])
    print(features)
    print(ageinput)
    #vizCompGesichert.getPeople(0,1,1,ageinput,features, choosePerson)
    #abchecken der Eingabe
    if(gender == False and gender2 == False):
        st.subheader("Error!")
        st.write("You forgot to select a gender.")

    if(gender == True and gender2 == True):
        st.subheader("Error!")
        st.write("You cannot choose both genders. ")

    if(ageinput == False):
        st.subheader("Error!")
        st.write("You forgot to enter an age value.")

    if(sepsis==False and noSepsis == False):
        st.subheader("Error!")
        st.write("You forgot to choose if you want patients with or without Sepsis")

    if(sepsis==True and noSepsis == True):
        st.subheader("Error!")
        st.write("You can't choose patients with Sepsis and without Sepsis")

    if(features == False):
        st.subheader("Error!")
        st.write("You didn't select features you want to visualize")    
    
    #Bei richtiger Eingabe: 
    #Frau

    if(option == "dataset 1" and button1 == True and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(0,0,1,ageinput,features, choosePerson)

    if(option == "dataset 1" and button1 == True and gender==False and gender2== True  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
    #vizComp.getPeople(0,0,c,c,f)
        vizCompGesichert.getPeople(0,0,0,ageinput,features, choosePerson)
    #Mann
    if(option == "dataset 1" and button1 == True and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(0,1,1,ageinput,features, choosePerson)

    if(option == "dataset 1" and button1 == True and gender==False and gender2== True  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
    #vizComp.getPeople(0,0,c,c,f)
        vizCompGesichert.getPeople(0,1,0,ageinput,features, choosePerson)

    #Datensatz2
    #Mann
    if(option == "dataset 2"and button1 == True  and gender==True and gender2== False and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
    #vizComp.getPeople(1,1,c,c,f)
        vizCompGesichert.getPeople(1,1,1,ageinput,features, choosePerson)


    if(option == "dataset 2"and button1 == True  and gender==True and gender2== False  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(1,1,0,ageinput,features, choosePerson)
    #Frau
    if(option == "dataset 2"and button1 == True  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(1,0,1,ageinput,features, choosePerson)

    if(option == "dataset 2"and button1 == True  and gender==False and gender2== True and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(1,0,0,ageinput,features, choosePerson)




    #Datensatz beide 
    #Mann
    if(option == "both" and button1 == True and gender==True and gender2== False  and sepsis == False and noSepsis == True):
    #vizComp.getPeople(2,1,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,1,0,ageinput,features, choosePerson)

    if(option == "both" and button1 == True and gender==True and gender2== False  and sepsis == True and noSepsis == False):
    #vizComp.getPeople(2,1,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,1,1,ageinput,features, choosePerson)
    #FRAU
    if(option == "both" and button1 == True and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #vizComp.getPeople(2,0,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,0,1,ageinput,features, choosePerson)
    if(option == "both" and button1 == True and gender==False and gender2== True and sepsis == False and noSepsis == True):
    #vizComp.getPeople(2,0,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,0,0,ageinput,features, choosePerson)
