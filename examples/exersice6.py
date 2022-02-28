import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
#import FelixTestPy as felwholeData
import vizualizationComponent as vizComp
import vizualizationComponentGesichtert as vizCompGesichert
import eigeneGridImplementierung as eigenGrid

#saving Zustand
class savingShit():

    def __init__(self):
        self.gender = 50
        self.sepsislabel = 50
        self.features = []
        self.ageinput = 150
        self.dataset = 200
        self.personlist = []
    
    
    # getter method
    def get_gender(self):
        return self.gender
      
    # setter method
    def set_gender(self, gender):
        self.gender = gender
    # getter method
    def get_sepsislabel(self):
        return self.sepsislabel
    # setter method
    def set_sepsislabel(self, sepsislabel):
        self.sepsislabel = sepsislabel
      
    # setter method
    def set_personlist(self, personlist):
        self.personlist = personlist

    def get_personlist(self):
        return self.personlist

    # getter method
    def get_ageinput(self):
        return self.ageinput
      
    # setter method
    def set_ageinput(self, ageinput):
        self.ageinput = ageinput
    # getter method
    def get_features(self):
        return self.features
    # setter method
    def set_features(self, features):
        self.features = features

    def state_1(self):
        #Anfangszustand
        #return values fur das Diagramm
        print("hello worklds")



A = savingShit()
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

if(gender == True and gender2 == False ):
    A.set_gender(1)

if(gender2 == True and gender == False):
    A.set_gender(0)    


st.sidebar.subheader("Choose patient with or without Sepsis (not both)")
sepsis = st.sidebar.checkbox("Sepsis")
noSepsis = st.sidebar.checkbox("No Sepsis")

if(sepsis == True and noSepsis == False ):
    A.set_sepsislabel(1)

if(noSepsis == True and sepsis == False):
    A.set_sepsislabel(0)     

ageinput = st.sidebar.number_input("Write down Age of a patient", step = 1, min_value =18, max_value = 80)
#Soll in session gespeichert werden
st.session_state.ageinput = ageinput


#st.sidebar.subheader("Select Features for the visualization")
features = st.sidebar.multiselect(
     'Select Features for the visualization',
     ['HR', 'O2Sat', 'SBP', 'MAP', 'DBP', 'Resp'],
     ['HR', 'O2Sat', 'Resp'])

#Soll in session gespeichert werden
#st.session_state.features = features

# habe ich hier geswitched! (also bei personen wird schon visualisierung generiert 
# später ändern
#button2 = st.sidebar.button("Generate possible persons")
#button1 = st.sidebar.button("Search for suitable persons")

#vorher die onlypersons abspeichern
onlypersons = []
personlist = []

#if(button1 and gender == True and gender2 == True):
#    st.subheader("Error!")
#    st.write("You can only choose one gender! Please redo your input")

#evtl. davor schauen wegen Button
#if(option == "dataset 1" and button1 == True and gender==True and gender2== False and sepsis == True and noSepsis == False):
#if(option == "dataset 1" and gender==True and gender2== False and sepsis == True and noSepsis == False):
#    personlist = vizComp.getPeople(0,1,1,ageinput,features)




if(gender == False and gender2 == False):
    st.subheader("Warning!")
    st.write("You forgot to select a gender.")

if(gender == True and gender2 == True):
    st.subheader("Warning!")
    st.write("You cannot choose both genders. ")

if(ageinput == False):
    st.subheader("Warning!")
    st.write("You forgot to enter an age value.")

if(sepsis==False and noSepsis == False):
    st.subheader("Warning!")
    st.write("You forgot to choose if you want patients with or without Sepsis")

if(sepsis==True and noSepsis == True):
    st.subheader("Warning!")
    st.write("You can't choose patients with Sepsis and without Sepsis")

if(features == False):
    st.subheader("Warning!")
    st.write("You didn't select features you want to visualize") 

button10 = st.sidebar.button("Generate possible persons")
#session versuchen
if 'personlist' not in st.session_state:
    st.session_state.personlist = []

if(button10):
    print("Das ist a gender Klasse: ", A.get_gender() )
    print("Das ist a sepsislabel Klasse ", A.get_sepsislabel())
    print("Das hier ist, was selbst ohne Klasse gespeichert ist")
    print(gender)
    print(gender2)
    print(sepsis)
    print(noSepsis)
    print(option)
    print(features)
    print(ageinput)
    A.set_ageinput(ageinput)
    A.set_features(features)
    print("button wurde gedrückt")
    if(option == "dataset 1"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        personlist = vizComp.getPeople(0,0,1,ageinput,features)
        A.set_personlist(personlist)

    if(option == "dataset 1"  and gender==False and gender2== True  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
    #personlist = vizComp.getPeople(0,0,c,c,f)
        st.session_state.personlist = vizComp.getPeople(0,0,0,ageinput,features)
        A.set_personlist(personlist)
    
    #Mann
    if(option == "dataset 1"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
        st.session_state.personlist = vizComp.getPeople(0,1,1,ageinput,features)
        A.set_personlist(personlist)
    if(option == "dataset 1"  and gender==False and gender2== True  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
    #personlist = vizComp.getPeople(0,0,c,c,f)
        st.session_state.personlist = vizComp.getPeople(0,1,0,ageinput,features)
        A.set_personlist(personlist)

    #Datensatz2
    #Mann
    if(option == "dataset 2"  and gender==True and gender2== False and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
    #personlist = vizComp.getPeople(1,1,c,c,f)
        st.session_state.personlist = vizComp.getPeople(1,1,1,ageinput,features)
        A.set_personlist(personlist)

    if(option == "dataset 2"  and gender==True and gender2== False  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(1,1,0,ageinput,features)
        A.set_personlist(personlist)
    #Frau
    if(option == "dataset 2"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(1,0,1,ageinput,features)
        A.set_personlist(personlist)
    if(option == "dataset 2"  and gender==False and gender2== True and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(1,0,0,ageinput,features)
        A.set_personlist(personlist)



    #Datensatz beide 
    #Mann
    if(option == "both"  and gender==True and gender2== False  and sepsis == False and noSepsis == True):
    #personlist = vizComp.getPeople(2,1,c,c,f)
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(2,1,0,ageinput,features)
        A.set_personlist(st.session_state.personlist)

    if(option == "both"  and gender==True and gender2== False  and sepsis == True and noSepsis == False):
    #personlist = vizComp.getPeople(2,1,c,c,f)
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(2,1,1,ageinput,features)
        A.set_personlist(st.session_state.personlist)
    #FRAU
    if(option == "both"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #personlist = vizComp.getPeople(2,0,c,c,f)
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(2,0,1,ageinput,features)
        A.set_personlist(st.session_state.personlist)
    if(option == "both"  and gender==False and gender2== True and sepsis == False and noSepsis == True):
    #personlist = vizComp.getPeople(2,0,c,c,f)
    #st.write("Your Input was: ")
        st.session_state.personlist = vizComp.getPeople(2,0,0,ageinput,features)
        A.set_personlist(st.session_state.personlist)

print("Das ist personlist", st.session_state.personlist)
#Soll in session gespeichert werden
#st.session_state.ageinput = ageinput

#print("Das ist features")
#print(features)
    # Nun liste die returnted Personen auf
#print("Das ist personlist")
#print(personlist)
    #Now persons grid
#eigenGrid.getGridImplementierung(personlist)
    #Wenn eingegeben, auf neue Seite verweisen und speichere alle eingaben#

    #create person tuple
for i in range(len(st.session_state.personlist)):
    onlypersons.append(st.session_state.personlist[i][0])
print("Das ist onlypersons")
print(onlypersons)
persontuple = tuple(onlypersons)




choosePerson = st.sidebar.selectbox('Choose one person you like to vizualize' , options = persontuple)
#sessionCount evtl. bei choosePerson machen
if 'chooseP' not in st.session_state:
    st.session_state.chooseP = choosePerson

    print("Initialisierungs-choosePerson = ", st.session_state.chooseP)
if(choosePerson):
    st.session_state.chooseP = choosePerson
    print("Das ist ChoosePerson von choosePerson", choosePerson) #HIER in Klasse
    print("Das ist ChoosePerson von st.session_state.chooseP", st.session_state.chooseP) #HIER in Klasse
    




#def saveTesten(choosePerson):
#    st.session_state['choosePerson'] = choosePerson
#    saveInVariable = choosePerson

#st.session_state.choosePerson = choosePerson
#vizualize
choosePersonButton = st.sidebar.button("create vizualization")
if choosePersonButton: 
    print("das ist ageinput,features, choosePerson")
    print("Das ist choosePerson: ", choosePerson)#isthierNull
    #print(st.session_state['choosePerson'])
    print("Das ist features nicht Klasse: ", features)
    print("Das ist ageinput nicht Klasse: ", ageinput)

    print("Das ist features in Klasse: ", A.get_features())
    print("Das ist ageinput in Klasse: ", A.get_ageinput())
    #print(features)
    #print(ageinput)
    #vizCompGesichert.getPeople(0,1,1,ageinput,features, choosePerson)

    if(option == "dataset 1"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(0,0,1,ageinput,features, choosePerson)

    if(option == "dataset 1"  and gender==False and gender2== True  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
    #vizComp.getPeople(0,0,c,c,f)
        vizCompGesichert.getPeople(0,0,0,ageinput,features, choosePerson)
    #Mann
    if(option == "dataset 1"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(0,1,1,ageinput,features, choosePerson)

    if(option == "dataset 1"  and gender==False and gender2== True  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
    #vizComp.getPeople(0,0,c,c,f)
        vizCompGesichert.getPeople(0,1,0,ageinput,features, choosePerson)

    #Datensatz2
    #Mann
    if(option == "dataset 2"  and gender==True and gender2== False and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
    #vizComp.getPeople(1,1,c,c,f)
        vizCompGesichert.getPeople(1,1,1,ageinput,features, choosePerson)


    if(option == "dataset 2"  and gender==True and gender2== False  and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(1,1,0,ageinput,features, choosePerson)
    #Frau
    if(option == "dataset 2"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(1,0,1,ageinput,features, choosePerson)

    if(option == "dataset 2"  and gender==False and gender2== True and sepsis == False and noSepsis == True):
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(1,0,0,ageinput,features, choosePerson)




    #Datensatz beide 
    #Mann
    if(option == "both"  and gender==True and gender2== False  and sepsis == False and noSepsis == True):
    #vizComp.getPeople(2,1,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,1,0,ageinput,features, choosePerson)

    if(option == "both"  and gender==True and gender2== False  and sepsis == True and noSepsis == False):
    #vizComp.getPeople(2,1,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,1,1,ageinput,features, choosePerson)
    #FRAU
    if(option == "both"  and gender==False and gender2== True and sepsis == True and noSepsis == False):
    #vizComp.getPeople(2,0,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,0,1,ageinput,features, choosePerson)
    if(option == "both"  and gender==False and gender2== True and sepsis == False and noSepsis == True):
    #vizComp.getPeople(2,0,c,c,f)
    #st.write("Your Input was: ")
        vizCompGesichert.getPeople(2,0,0,ageinput,features, choosePerson)






