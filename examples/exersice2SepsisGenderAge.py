import os, sys
import csv
from os.path import isfile, join
from collections import Counter
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px


class CheckForSepsisGenderAge():
    def __init__(self, dataPath=""):
        self.dataPath = dataPath
        #hasAllFileNamesInAnArray
        self.fileNames = []
        #currentFileData Array
        self.currentFileDataArray = []

        self.countMale = 0
        self.countFemale = 0
        self.countSepsisPatient = 0
        self.countNonSepsisPatient = 0
        self.countSICU = 0
        self.countMICU = 0
        self.countNaNMICU = 0
        self.countNaNSICU = 0
        self.count1819 = 0
        self.count20Jahre = 0
        self.count30Jahre = 0
        self.count40Jahre = 0
        self.count50Jahre = 0
        self.count60Jahre = 0
        self.count70Jahre = 0
        self.count80Jahre = 0

        self.countMaleWSepsis = 0
        self.countFemaleWSepsis = 0
        self.countFemaleWOSepsis = 0       
        self.countMaleW0Sepsis= 0
        self.count1819WSepsisF = 0 
        self.count1819WOSepsisF = 0 
        self.count20JahreWSepsisF = 0
        self.count20JahreWOSepsisF = 0
        self.count30JahreWSepsisF = 0
        self.count30JahreWOSepsisF = 0
        self.count40JahreWSepsisF = 0
        self.count40JahreWOSepsisF = 0
        self.count50JahreWSepsisF = 0
        self.count50JahreWOSepsisF = 0
        self.count60JahreWSepsisF = 0
        self.count60JahreWOSepsisF = 0
        self.count70JahreWSepsisF = 0
        self.count70JahreWOSepsisF = 0
        self.count80JahreWSepsisF = 0
        self.count80JahreWOSepsisF = 0

        self.count1819WSepsisM = 0 
        self.count1819WOSepsisM = 0 
        self.count20JahreWSepsisM = 0
        self.count20JahreWOSepsisM = 0
        self.count30JahreWSepsisM = 0
        self.count30JahreWOSepsisM = 0
        self.count40JahreWSepsisM = 0
        self.count40JahreWOSepsisM = 0
        self.count50JahreWSepsisM = 0
        self.count50JahreWOSepsisM = 0
        self.count60JahreWSepsisM = 0
        self.count60JahreWOSepsisM = 0
        self.count70JahreWSepsisM = 0
        self.count70JahreWOSepsisM = 0
        self.count80JahreWSepsisM = 0
        self.count80JahreWOSepsisM = 0




    def getFileNames(self):
        """ returns list of all files in the path"""
        dirs = os.listdir(self.dataPath)
        #für alle Files in Directory
        for file in dirs:
            self.fileNames.append(file);
            #liest die File
            self.readFiles(file)
        #print(self.fileNames)




    
    def readFiles(self, file):
        """Opens every file and read it. It is Main extraction method"""
        path = self.dataPath
        backslash = "\\"
        filename = self.dataPath+backslash+file
        #print("Das ist die zu extrahierende File" + file)
        fp=open(filename)
        resultArray = []
        for line in fp:
            res=line.split('|')
            resultArray.append(res)
        #jetzigeFile
        self.currentFileDataArray = resultArray
        #self.extractAllAges()
        #self.extractAllGender()
        #self.extractAllSepsislabel(file)
        #self.extractAllBothUnits(file)
        print("das ist file"+file)
        self.extractAllSepsislabel(file)


    def extractAllAges(self):
        """ extract important columns from rows and gives back an Array"""
        age = 50
        
        for i in range(1, len(self.currentFileDataArray)-1):
            #allPatientsAges.append(self.currentFileDataArray[i][34]);
           self.endResultAllAges.append(self.currentFileDataArray[i][34])
           #age = int(self.currentFileDataArray[i][34])
           age = float(self.currentFileDataArray[i][34])
        #delete duplicates
        self.endResultAllAges = list(dict.fromkeys(self.endResultAllAges))
        #sort
        self.endResultAllAges = sorted(self.endResultAllAges)
        if(age <20):
            self.count1819 = self.count1819 +1
        if(20 <= age <30):
            self.count20Jahre = self.count20Jahre +1        
        if(30 <= age <40):
            self.count30Jahre = self.count30Jahre +1
        if(40 <= age <50):
            self.count40Jahre = self.count40Jahre +1        
        if(50 <= age <60):
            self.count50Jahre = self.count50Jahre +1
        if(60 <= age <70):
            self.count60Jahre = self.count60Jahre +1        
        if(70<= age <80):
            self.count70Jahre = self.count70Jahre +1
        if(age >= 80):
            self.count80Jahre = self.count80Jahre +1
        #self.endResultAllAges.append(allPatientsAges)


    def extractAllGender(self):
        """ 0 for women and 1 for men"""
        gender = 50
        for i in range(1, len(self.currentFileDataArray)-1):
            #self.endResultAllGender.append(self.currentFileDataArray[i][35]);
            gender = self.currentFileDataArray[i][35]
        #delete duplicates
        #self.endResultAllGender = list(dict.fromkeys(self.endResultAllGender))
        if(gender == '0'):
            self.countFemale = self.countFemale + 1
        if(gender == '1'):
            self.countMale = self.countMale + 1
        
    
    def extractAllUnits1(self, file):
        """Administrative Kennung für die Intensivstation (MICU); falsch (0) oder wahr (1)"""
        allUnits1 = 50
        
        for i in range(1, len(self.currentFileDataArray)-1):
            #allUnits1.append(self.currentFileDataArray[i][36]);
            self.endResultAllUnit1.append(self.currentFileDataArray[i][36]);
            allUnits1 = self.currentFileDataArray[i][36]
            #if(self.currentFileDataArray[i][36]=="NaN"):
                #print("Das ist file mit NaN"+file)
                #break
        if(allUnits1 == '0'):
            self.countSICU = self.countSICU + 1
        if(allUnits1 == '1'):
            self.countMICU = self.countMICU + 1
        if(allUnits1 == 'NaN'):
            self.countNaNMICU = self.countNaNMICU + 1

        #delete duplicates
        self.endResultAllUnit1 = list(dict.fromkeys(self.endResultAllUnit1))
        #self.endResultAllUnit1.append(allUnits1)


        

    def extractAllUnits2(self, file):
        """ Administrative Kennung für die Intensivstation (SICU); falsch (0) oder wahr (1)"""
        allUnits2 = 50
        for i in range(1, len(self.currentFileDataArray)-1):
            #allUnits2.append(self.currentFileDataArray[i][37])
            self.endResultAllUnit2.append(self.currentFileDataArray[i][37])
            allUnits2 = self.currentFileDataArray[i][37]
            #if(self.currentFileDataArray[i][37] == "NaN"):
                #print("Das ist file mit NaN"+file)
                #break
        if(allUnits2 == 'NaN'):
            self.countNaNSICU = self.countNaNSICU + 1
        self.endResultAllUnit2 = list(dict.fromkeys(self.endResultAllUnit2))
        #self.endResultAllUnit2.append(allUnits2)



        #self.endResultAllAllIculos.append(allIculos)

    def extractAllSepsislabel(self, file):
        """ Bei septischen Patienten ist SepsisLabel 1, wenn t ≥ tsepsis -6 und 0, wenn t < tsepsis -6. Bei nicht septischen Patienten ist SepsisLabel 0."""
        sepsisLabel = 0
        womenPositive = 0
        womenPos1819 =0
        womenPos20 =0
        womenPos30 =0
        womenPos40 =0
        womenPos50 =0
        womenPos60 =0
        womenPos70 =0
        womenPos80 =0
        menPos1819 =0
        menPos20 =0
        menPos30 =0
        menPos40 =0
        menPos50 =0
        menPos60 =0
        menPos70 =0
        menPos80 =0


        menPos = 0

        #print("Das ist die File"+file)
        for i in range(1, len(self.currentFileDataArray)-1):
            #print("Das ist self.currentFileDataArray"+ self.currentFileDataArray[i][40])

            #Wenn es eine Frau ist
            #if(self.currentFileDataArray[i][35] == "0"):
               # womenTrue = 1
            #Wenn es ein Mann ist
            #if(self.currentFileDataArray[i][35] == "1"):
                #menTrue = 1            
                #Wenn Sepsis vorliegt
            if(self.currentFileDataArray[i][40] == "1\n"):
                sepsisLabel = 1
                #woman
                if(self.currentFileDataArray[i][35] == "0"):
                    menPos = 0;
                    womenPositive = 1
                    #hier kommt if else für 20
                    if(float(self.currentFileDataArray[i][34]) <20):
                        womenPos1819 =1
                    if(20 <= float(self.currentFileDataArray[i][34]) <30):
                        womenPos20 =1       
                    if(30 <= float(self.currentFileDataArray[i][34]) <40):
                        womenPos30 =1 
                    if(40 <= float(self.currentFileDataArray[i][34]) <50):
                        womenPos40 =1        
                    if(50 <= float(self.currentFileDataArray[i][34]) <60):
                        womenPos50 =1   
                    if(60 <= float(self.currentFileDataArray[i][34]) <70):
                        womenPos60 =1         
                    if(70<= float(self.currentFileDataArray[i][34]) <80):
                        womenPos70 =1   
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        womenPos80 =1
                     
                #Male
                if(self.currentFileDataArray[i][35]=="1"):
                    menPos = 1
                    womenPositive = 0
                    if(float(self.currentFileDataArray[i][34]) <20):
                        menPos1819 =1
                    if(20 <= float(self.currentFileDataArray[i][34]) <30):
                        menPos20 =1       
                    if(30 <= float(self.currentFileDataArray[i][34]) <40):
                        menPos30 =1 
                    if(40 <= float(self.currentFileDataArray[i][34]) <50):
                        menPos40 =1        
                    if(50 <= float(self.currentFileDataArray[i][34]) <60):
                        menPos50 =1   
                    if(60 <= float(self.currentFileDataArray[i][34]) <70):
                        menPos60 =1         
                    if(70<= float(self.currentFileDataArray[i][34]) <80):
                        menPos70 =1   
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        menPos80 =1


            #self.endResultAllSepsisLabel.append(self.currentFileDataArray[i][40]);
            #sepsisLabel = self.currentFileDataArray[i][40]
            
        #Anzahl der Sepsis
        if(sepsisLabel == 0):
            self.countNonSepsisPatient = self.countNonSepsisPatient + 1
        if(sepsisLabel == 1):
            self.countSepsisPatient = self.countSepsisPatient + 1

        if(sepsisLabel == 0 and self.currentFileDataArray[1][35] == "0"):
            self.countFemaleWOSepsis = self.countFemaleWOSepsis +1
        if(sepsisLabel ==0 and self.currentFileDataArray[1][35] == "1"):
            self.countMaleW0Sepsis = self.countMaleW0Sepsis +1

        if(womenPositive == 1 and self.currentFileDataArray[1][35] == "0" ):
            self.countFemaleWSepsis = self.countFemaleWSepsis +1
            if(womenPos1819 ==1):
                self.count1819WSepsisF = self.count1819WSepsisF+1
            if(womenPos20 ==1):
                self.count20JahreWSepsisF = self.count20JahreWSepsisF+1
            if(womenPos30 ==1):
                self.count30JahreWSepsisF = self.count30JahreWSepsisF+1
            if(womenPos40 ==1):
                self.count40JahreWSepsisF = self.count40JahreWSepsisF+1
            if(womenPos50 ==1):
                self.count50JahreWSepsisF = self.count50JahreWSepsisF+1
            if(womenPos60 ==1):
                self.count60JahreWSepsisF = self.count60JahreWSepsisF+1
            if(womenPos70 ==1):
                self.count70JahreWSepsisF = self.count70JahreWSepsisF+1
            if(womenPos80 ==1):
                self.count80JahreWSepsisF = self.count80JahreWSepsisF+1

            
        if(menPos == 1 and self.currentFileDataArray[1][35] == "1"):
            self.countMaleWSepsis= self.countMaleWSepsis + 1
            if(menPos1819 ==1):
                self.count1819WSepsisM = self.count1819WSepsisM+1
            if(menPos20 ==1):
                self.count20JahreWSepsisM = self.count20JahreWSepsisM+1
            if(menPos30 ==1 ):
                self.count30JahreWSepsisM = self.count30JahreWSepsisM+1
            if(menPos40 ==1 ):
                self.count40JahreWSepsisM = self.count40JahreWSepsisM+1
            if(menPos50 ==1 ):
                self.count50JahreWSepsisM = self.count50JahreWSepsisM+1
            if(menPos60 ==1 ):
                self.count60JahreWSepsisM = self.count60JahreWSepsisM+1
            if(menPos70 ==1 ):
                self.count70JahreWSepsisM = self.count70JahreWSepsisM+1
            if(menPos80 ==1 ):
                self.count80JahreWSepsisM = self.count80JahreWSepsisM+1

        if(self.currentFileDataArray[1][35] == "0"):
            self.countFemale = self.countFemale +1   

        if(womenPositive == 0 and self.currentFileDataArray[1][35] == "0"):
            if(womenPos1819 ==0 and (float(self.currentFileDataArray[1][34]) <20)):
                self.count1819WOSepsisF = self.count1819WOSepsisF+1
            if(womenPos20 ==0 and (20 <= float(self.currentFileDataArray[1][34]) <30)):
                self.count20JahreWOSepsisF = self.count20JahreWOSepsisF+1
            if(womenPos30 ==0 and (30 <= float(self.currentFileDataArray[1][34]) <40)):
                self.count30JahreWOSepsisF = self.count30JahreWOSepsisF+1
            if(womenPos40 ==0 and (40 <= float(self.currentFileDataArray[1][34]) <50)):
                self.count40JahreWOSepsisF = self.count40JahreWOSepsisF+1
            if(womenPos50 ==0 and (50 <= float(self.currentFileDataArray[1][34]) <60)):
                self.count50JahreWOSepsisF = self.count50JahreWOSepsisF+1
            if(womenPos60 ==0 and (60 <= float(self.currentFileDataArray[1][34]) <70)):
                self.count60JahreWOSepsisF = self.count60JahreWOSepsisF+1
            if(womenPos70 ==0 and (70 <= float(self.currentFileDataArray[1][34]) <80)):
                self.count70JahreWOSepsisF = self.count70JahreWOSepsisF+1
            if(womenPos80 ==0 and (float(self.currentFileDataArray[1][34]) >= 80)):
                self.count80JahreWOSepsisF = self.count80JahreWOSepsisF+1

        if(self.currentFileDataArray[1][35] == "1"):
            self.countMale= self.countMale + 1  

        if(menPos == 0 and self.currentFileDataArray[1][35] == "1"):
            if(menPos1819 ==0  and (float(self.currentFileDataArray[1][34]) <20)):
                self.count1819WOSepsisM = self.count1819WOSepsisM+1
            if(menPos20 ==0 and (20 <= float(self.currentFileDataArray[1][34]) <30)):
                self.count20JahreWOSepsisM = self.count20JahreWOSepsisM+1
            if(menPos30 ==0 and (30 <= float(self.currentFileDataArray[1][34]) <40)):
                self.count30JahreWOSepsisM = self.count30JahreWOSepsisM+1
            if(menPos40 ==0 and (40 <= float(self.currentFileDataArray[1][34]) <50)):
                self.count40JahreWOSepsisM = self.count40JahreWOSepsisM+1
            if(menPos50 ==0  and (50 <= float(self.currentFileDataArray[1][34]) <60)):
                self.count50JahreWOSepsisM = self.count50JahreWOSepsisM+1
            if(menPos60 ==0 and (60 <= float(self.currentFileDataArray[1][34]) <70)):
                self.count60JahreWOSepsisM = self.count60JahreWOSepsisM+1
            if(menPos70 ==0 and (70 <= float(self.currentFileDataArray[1][34]) <80)):
                self.count70JahreWOSepsisM = self.count70JahreWOSepsisM+1
            if(menPos80 ==0  and (float(self.currentFileDataArray[1][34]) >= 80)):
                self.count80JahreWOSepsisM = self.count80JahreWOSepsisM+1



    def makeSepsisAgeGenderDiagram(self, verarbeitetesListList):
        #chart_data = pd.DataFrame(
        #np.array([[ 3, 104, 9, 113],[ 57,769,74, 813], [62,1114, 96, 1165], [129, 1921, 224,2523], [193,2871,342,4286], [264,3634,425,5209], [298, 3513,366, 4392], [183,2655,202,2327]]),
        #columns=["Female had Sepsis", "Female had no Sepsis", "Male had Sepsis", "Male had no Sepsis"], index =['under the age of 20', '20-29 year olds', '30-39 year olds', '40-49 year olds', '50-59 year olds', '60-69 year olds', '70-79 year olds','over 80 years'])

        #st.bar_chart(chart_data, height=600, width=900)
        chart_data = pd.DataFrame(
        np.array(verarbeitetesListList),
        columns=["Female had Sepsis", "Female had no Sepsis", "Male had Sepsis", "Male had no Sepsis"], 
        index =['under the age of 20', '20-29 year olds', '30-39 year olds', '40-49 year olds', '50-59 year olds', '60-69 year olds', '70-79 year olds','over 80 years'])

        st.bar_chart(chart_data, height=600, width=900)
    
def decideDiagram(intToDecide):
    #SepsisGender
    if( intToDecide == 1):
        A1 = CheckForSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
        A1.getFileNames()
        #A1.extractAllSepsislabel
        verarbeitetesListList = [[A1.count1819WSepsisF, A1.count1819WOSepsisF, A1.count1819WSepsisM, A1.count1819WOSepsisM], 
             [A1.count20JahreWSepsisF, A1.count20JahreWOSepsisF, A1.count20JahreWSepsisM, A1.count20JahreWOSepsisM], 
             [A1.count30JahreWSepsisF, A1.count30JahreWOSepsisF, A1.count30JahreWSepsisM, A1.count30JahreWOSepsisM], 
             [A1.count40JahreWSepsisF, A1.count40JahreWOSepsisF, A1.count40JahreWSepsisM, A1.count40JahreWOSepsisM], 
             [A1.count50JahreWSepsisF, A1.count50JahreWOSepsisF, A1.count50JahreWSepsisM, A1.count50JahreWOSepsisM], 
             [A1.count60JahreWSepsisF, A1.count60JahreWOSepsisF, A1.count60JahreWSepsisM, A1.count60JahreWOSepsisM], 
             [A1.count70JahreWSepsisF, A1.count70JahreWOSepsisF, A1.count70JahreWSepsisM, A1.count70JahreWOSepsisM], 
             [A1.count80JahreWSepsisF, A1.count80JahreWOSepsisF, A1.count80JahreWSepsisM, A1.count80JahreWOSepsisM]]
        print("Das ist das Array {}", verarbeitetesListList)

        A1.makeSepsisAgeGenderDiagram(verarbeitetesListList)
        st.write("The top graph includes the number of age groups with and without sepsis, while the bottom graph shows in percentages who has the largest sepsis group. The three largest groups with sepsis among men is respectively: ")
        st.write("1) 60-69 men with: 1.24%.")
        st.write("2) 70-79 men with: 1,23%.")
        st.write("3) 50-59 men with: 1.07%.")
        st.write("While the largest groups for females were these: ")
        st.write("1) 70-79 women with: 0.89%")
        st.write("2) 60-69 women with: 0,733%")
        st.write("3) women older 80 with: 0.615%.")
        st.write("Here it may be that there has no difference between the gendern. (TODO: Find out!)")


        print("Personen im Datensatz")
        print("Personen im Datensatz Frau: ", A1.countFemale)
        print("Personen im Datensatz Mann: ", A1.countMale)
        print("HIIIIIIIIIIEEEEEEEER")
        print("FRAUEN")
        #personen allgemein
        print("Personen im Datensatz: ", A1.countFemale + A1.countMale)
        persondatensatz =  A1.countFemale + A1.countMale

        #under 20 years
        print("Anzahl Frauen allgemein unter 20 insgesamt im Datensatz: ", (A1.count1819WSepsisF + A1.count1819WOSepsisF))
        print("Prozent Frauen allgemein unter 20 insgesamt im Datensatz: (F:All)", ((A1.count1819WSepsisF + A1.count1819WOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis unter 20 insgesamt im Datensatz: ", (A1.count1819WSepsisF))
        print("Prozent Frauen mit Sepsis unter 20 insgesamt im Datensatz (F:A): ", (A1.count1819WSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A1.count1819WSepsisF*100) / (A1.count1819WSepsisF + A1.count1819WOSepsisF) )
        print("Anzahl Frauen ohne Sepsis unter 20 insgesamt im Datensatz: ", A1.count1819WOSepsisF)
        print("Prozent Frauen ohne Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A1.count1819WOSepsisF*100)/(A1.count1819WSepsisF + A1.count1819WOSepsisF))
        
        #between 20 years -29 years
        print("Anzahl Frauen zwischen 20-29  insgesamt im Datensatz: ", (A1.count20JahreWSepsisF + A1.count20JahreWOSepsisF))
        print("Prozent Frauen zwischen 20-29 insgesamt im Datensatz: (F:All)", ((A1.count20JahreWSepsisF + A1.count20JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz: ", (A1.count20JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:A): ", (A1.count20JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A1.count20JahreWSepsisF*100) / (A1.count20JahreWSepsisF + A1.count20JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 20-29 insgesamt im Datensatz: ", A1.count20JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A1.count20JahreWOSepsisF*100)/(A1.count20JahreWSepsisF + A1.count20JahreWOSepsisF))

        #between 30 years -39 years
        print("Anzahl Frauen zwischen 30-39  insgesamt im Datensatz: ", (A1.count30JahreWSepsisF + A1.count30JahreWOSepsisF))
        print("Prozent Frauen zwischen 30-39 insgesamt im Datensatz: (F:All)", ((A1.count30JahreWSepsisF + A1.count30JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz: ", (A1.count30JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:A): ", (A1.count30JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A1.count30JahreWSepsisF*100) / (A1.count30JahreWSepsisF + A1.count30JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 30-39 insgesamt im Datensatz: ", A1.count30JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A1.count30JahreWOSepsisF*100)/(A1.count30JahreWSepsisF + A1.count30JahreWOSepsisF))

        #between 40 years -49 years
        print("Anzahl Frauen zwischen 40-49  insgesamt im Datensatz: ", (A1.count40JahreWSepsisF + A1.count40JahreWOSepsisF))
        print("Prozent Frauen zwischen 40-49 insgesamt im Datensatz: (F:All)", ((A1.count40JahreWSepsisF + A1.count40JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz: ", (A1.count40JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:A): ", (A1.count40JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A1.count40JahreWSepsisF*100) / (A1.count40JahreWSepsisF + A1.count40JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 40-49 insgesamt im Datensatz: ", A1.count40JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A1.count40JahreWOSepsisF*100)/(A1.count40JahreWSepsisF + A1.count40JahreWOSepsisF))

        #between 50 years -59 years
        print("Anzahl Frauen zwischen 50-59  insgesamt im Datensatz: ", (A1.count50JahreWSepsisF + A1.count50JahreWOSepsisF))
        print("Prozent Frauen zwischen 50-59 insgesamt im Datensatz: (F:All)", ((A1.count50JahreWSepsisF + A1.count50JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz: ", (A1.count50JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:A): ", (A1.count50JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A1.count50JahreWSepsisF*100) / (A1.count50JahreWSepsisF + A1.count50JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 50-59 insgesamt im Datensatz: ", A1.count50JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A1.count50JahreWOSepsisF*100)/(A1.count50JahreWSepsisF + A1.count50JahreWOSepsisF))

        #between 60 years -69 years
        print("Anzahl Frauen zwischen 60-69  insgesamt im Datensatz: ", (A1.count60JahreWSepsisF + A1.count60JahreWOSepsisF))
        print("Prozent Frauen zwischen 60-69 insgesamt im Datensatz: (F:All)", ((A1.count60JahreWSepsisF + A1.count60JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz: ", (A1.count60JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:A): ", (A1.count60JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A1.count60JahreWSepsisF*100) / (A1.count60JahreWSepsisF + A1.count60JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 60-69 insgesamt im Datensatz: ", A1.count60JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A1.count60JahreWOSepsisF*100)/(A1.count60JahreWSepsisF + A1.count60JahreWOSepsisF))

         #between 70 years -79 years
        print("Anzahl Frauen zwischen 70-79  insgesamt im Datensatz: ", (A1.count70JahreWSepsisF + A1.count70JahreWOSepsisF))
        print("Prozent Frauen zwischen 70-79 insgesamt im Datensatz: (F:All)", ((A1.count70JahreWSepsisF + A1.count70JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz: ", (A1.count70JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:A): ", (A1.count70JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A1.count70JahreWSepsisF*100) / (A1.count70JahreWSepsisF + A1.count70JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 70-79 insgesamt im Datensatz: ", A1.count70JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A1.count70JahreWOSepsisF*100)/(A1.count70JahreWSepsisF + A1.count70JahreWOSepsisF))

        #older 80
        print("Anzahl Frauen älter 80  insgesamt im Datensatz: ", (A1.count80JahreWSepsisF + A1.count80JahreWOSepsisF))
        print("Prozent Frauen älter 80 insgesamt im Datensatz: (F:All)", ((A1.count80JahreWSepsisF + A1.count80JahreWOSepsisF)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Frauen mit Sepsis älter 80 insgesamt im Datensatz: ", (A1.count80JahreWSepsisF))
        print("Prozent Frauen mit Sepsis älter 80 insgesamt im Datensatz (F:A): ", (A1.count80JahreWSepsisF)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Frauen mit Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A1.count80JahreWSepsisF*100) / (A1.count80JahreWSepsisF + A1.count80JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis älter 80 insgesamt im Datensatz: ", A1.count80JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A1.count80JahreWOSepsisF*100)/(A1.count80JahreWSepsisF + A1.count80JahreWOSepsisF))

        #MÄNNER
        print("MÄNNER")
        #under 20 years
        print("Anzahl Männer allgemein unter 20 insgesamt im Datensatz: ", (A1.count1819WSepsisM + A1.count1819WOSepsisM))
        print("Prozent Männer allgemein unter 20 insgesamt im Datensatz: (F:All)", ((A1.count1819WSepsisM + A1.count1819WOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis unter 20 insgesamt im Datensatz: ", (A1.count1819WSepsisM))
        print("Prozent Männer mit Sepsis unter 20 insgesamt im Datensatz (F:A): ", (A1.count1819WSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A1.count1819WSepsisM*100) / (A1.count1819WSepsisM + A1.count1819WOSepsisM) )
        print("Anzahl Männer ohne Sepsis unter 20 insgesamt im Datensatz: ", A1.count1819WOSepsisM)
        print("Prozent Männer ohne Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A1.count1819WOSepsisM*100)/(A1.count1819WSepsisM + A1.count1819WOSepsisM))
        
        #between 20 years -29 years
        print("Anzahl Männer zwischen 20-29  insgesamt im Datensatz: ", (A1.count20JahreWSepsisM + A1.count20JahreWOSepsisM))
        print("Prozent Männer zwischen 20-29 insgesamt im Datensatz: (F:All)", ((A1.count20JahreWSepsisM + A1.count20JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz: ", (A1.count20JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:A): ", (A1.count20JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A1.count20JahreWSepsisM*100) / (A1.count20JahreWSepsisM + A1.count20JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 20-29 insgesamt im Datensatz: ", A1.count20JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A1.count20JahreWOSepsisM*100)/(A1.count20JahreWSepsisM + A1.count20JahreWOSepsisM))

        #between 30 years -39 years
        print("Anzahl Männer zwischen 30-39  insgesamt im Datensatz: ", (A1.count30JahreWSepsisM + A1.count30JahreWOSepsisM))
        print("Prozent Männer zwischen 30-39 insgesamt im Datensatz: (F:All)", ((A1.count30JahreWSepsisM + A1.count30JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz: ", (A1.count30JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:A): ", (A1.count30JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A1.count30JahreWSepsisM*100) / (A1.count30JahreWSepsisM + A1.count30JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 30-39 insgesamt im Datensatz: ", A1.count30JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A1.count30JahreWOSepsisM*100)/(A1.count30JahreWSepsisM + A1.count30JahreWOSepsisM))

        #between 40 years -49 years
        print("Anzahl Männer zwischen 40-49  insgesamt im Datensatz: ", (A1.count40JahreWSepsisM + A1.count40JahreWOSepsisM))
        print("Prozent Männer zwischen 40-49 insgesamt im Datensatz: (F:All)", ((A1.count40JahreWSepsisM + A1.count40JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz: ", (A1.count40JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:A): ", (A1.count40JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A1.count40JahreWSepsisM*100) / (A1.count40JahreWSepsisM + A1.count40JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 40-49 insgesamt im Datensatz: ", A1.count40JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A1.count40JahreWOSepsisM*100)/(A1.count40JahreWSepsisM + A1.count40JahreWOSepsisM))

        #between 50 years -59 years
        print("Anzahl Männer zwischen 50-59  insgesamt im Datensatz: ", (A1.count50JahreWSepsisM + A1.count50JahreWOSepsisM))
        print("Prozent Männer zwischen 50-59 insgesamt im Datensatz: (F:All)", ((A1.count50JahreWSepsisM + A1.count50JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz: ", (A1.count50JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:A): ", (A1.count50JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A1.count50JahreWSepsisM*100) / (A1.count50JahreWSepsisM + A1.count50JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 50-59 insgesamt im Datensatz: ", A1.count50JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A1.count50JahreWOSepsisM*100)/(A1.count50JahreWSepsisM + A1.count50JahreWOSepsisM))

        #between 60 years -69 years
        print("Anzahl Männer zwischen 60-69  insgesamt im Datensatz: ", (A1.count60JahreWSepsisM + A1.count60JahreWOSepsisM))
        print("Prozent Männer zwischen 60-69 insgesamt im Datensatz: (F:All)", ((A1.count60JahreWSepsisM + A1.count60JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz: ", (A1.count60JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:A): ", (A1.count60JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A1.count60JahreWSepsisM*100) / (A1.count60JahreWSepsisM + A1.count60JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 60-69 insgesamt im Datensatz: ", A1.count60JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A1.count60JahreWOSepsisM*100)/(A1.count60JahreWSepsisM + A1.count60JahreWOSepsisM))

         #between 70 years -79 years
        print("Anzahl Männer zwischen 70-79  insgesamt im Datensatz: ", (A1.count70JahreWSepsisM + A1.count70JahreWOSepsisM))
        print("Prozent Männer zwischen 70-79 insgesamt im Datensatz: (F:All)", ((A1.count70JahreWSepsisM + A1.count70JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz: ", (A1.count70JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:A): ", (A1.count70JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A1.count70JahreWSepsisM*100) / (A1.count70JahreWSepsisM + A1.count70JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 70-79 insgesamt im Datensatz: ", A1.count70JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A1.count70JahreWOSepsisM*100)/(A1.count70JahreWSepsisM + A1.count70JahreWOSepsisM))

        #older 80
        print("Anzahl Männer älter 80  insgesamt im Datensatz: ", (A1.count80JahreWSepsisM + A1.count80JahreWOSepsisM))
        print("Prozent Männer älter 80 insgesamt im Datensatz: (F:All)", ((A1.count80JahreWSepsisM + A1.count80JahreWOSepsisM)*100 )/  (A1.countFemale + A1.countMale))
        print("Anzahl Männer mit Sepsis älter 80 insgesamt im Datensatz: ", (A1.count80JahreWSepsisM))
        print("Prozent Männer mit Sepsis älter 80 insgesamt im Datensatz (F:A): ", (A1.count80JahreWSepsisM)*100 /  (A1.countFemale + A1.countMale) )
        print("Prozent Männer mit Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A1.count80JahreWSepsisM*100) / (A1.count80JahreWSepsisM + A1.count80JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis älter 80 insgesamt im Datensatz: ", A1.count80JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A1.count80JahreWOSepsisM*100)/(A1.count80JahreWSepsisM + A1.count80JahreWOSepsisM))

        #print("Anzahl Männer unter 20 insgesamt im Datensatz: ", (A1.count1819WSepsisM + A1.count1819WOSepsisM))
        #ein Diagramm nur mit Sepsis

                # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Woman under the Age of 20 With Sepsis', 'Woman under the Age of 20 Without Sepsis', 'Woman between 20-29 With Sepsis', 'Woman between 20-29 without Sepsis','Woman between 30-39 With Sepsis', 'Woman between 30-39 without Sepsis','Woman between 40-49 With Sepsis', 'Woman between 40-49 without Sepsis','Woman between 50-59 With Sepsis', 'Woman between 50-59 without Sepsis','Woman between 60-69 With Sepsis', 'Woman between 60-69 without Sepsis','Woman between 70-79 With Sepsis', 'Woman between 70-79 without Sepsis','Woman older 80 With Sepsis', 'Woman older 80 without Sepsis','Man under the Age of 20 With Sepsis', 'Men under the Age of 20 Without Sepsis', 'Men between 20-29 With Sepsis', 'Men between 20-29 without Sepsis','Men between 30-39 With Sepsis', 'Men between 30-39 without Sepsis','Men between 40-49 With Sepsis', 'Men between 40-49 without Sepsis','Men between 50-59 With Sepsis', 'Men between 50-59 without Sepsis','Men between 60-69 With Sepsis', 'Men between 60-69 without Sepsis','Men between 70-79 With Sepsis', 'Men between 70-79 without Sepsis','Men older 80 With Sepsis', 'Men older 80 without Sepsis',

        #Prozente
        sizes = [ (verarbeitetesListList[0][0])*100 /  (persondatensatz) , 
                 (verarbeitetesListList[0][1]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][1]*100) / (persondatensatz),
                 (verarbeitetesListList[2][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[2][1]*100) / (persondatensatz),
                 (verarbeitetesListList[3][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[3][1]*100) / (persondatensatz),
                 (verarbeitetesListList[4][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[4][1]*100) / (persondatensatz),
                 (verarbeitetesListList[5][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[5][1]*100) / (persondatensatz),
                 (verarbeitetesListList[6][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[6][1]*100) / (persondatensatz),
                 (verarbeitetesListList[7][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[7][1]*100) / (persondatensatz),
                 (verarbeitetesListList[0][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[0][3]*100) / (persondatensatz),
                 (verarbeitetesListList[1][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][3]*100) / (persondatensatz),
                 (verarbeitetesListList[2][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[2][3]*100) / (persondatensatz),
                 (verarbeitetesListList[3][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[3][3]*100) / (persondatensatz),
                 (verarbeitetesListList[4][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[4][3]*100) / (persondatensatz),
                 (verarbeitetesListList[5][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[5][3]*100) / (persondatensatz),
                 (verarbeitetesListList[6][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[6][3]*100) / (persondatensatz),
                 (verarbeitetesListList[7][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[7][3]*100) / (persondatensatz),
                 ]
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        #fig1, ax1 = plt.subplots()
        #ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
        #fig1.subplots_adjust(left,bottom,right,top)
        #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        #fig1.update_layout(height=800, width=1100)


        #st.pyplot(fig1, height=10000)
        #fig1, ax1 = plt.subplots()
        fig1, ax1 = st.columns(2)
        fig2 = px.pie(sizes, labels=labels, values=sizes, names=labels)
        ax1.write(fig2)

        #dataset 2
    if(intToDecide == 2):
        print("datasetInt: {}", 2)
        A2 = CheckForSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
        A2.getFileNames()
        #A2.extractAllSepsislabel
        verarbeitetesListList = [[A2.count1819WSepsisF, A2.count1819WOSepsisF, A2.count1819WSepsisM, A2.count1819WOSepsisM], 
             [A2.count20JahreWSepsisF, A2.count20JahreWOSepsisF, A2.count20JahreWSepsisM, A2.count20JahreWOSepsisM], 
             [A2.count30JahreWSepsisF, A2.count30JahreWOSepsisF, A2.count30JahreWSepsisM, A2.count30JahreWOSepsisM], 
             [A2.count40JahreWSepsisF, A2.count40JahreWOSepsisF, A2.count40JahreWSepsisM, A2.count40JahreWOSepsisM], 
             [A2.count50JahreWSepsisF, A2.count50JahreWOSepsisF, A2.count50JahreWSepsisM, A2.count50JahreWOSepsisM], 
             [A2.count60JahreWSepsisF, A2.count60JahreWOSepsisF, A2.count60JahreWSepsisM, A2.count60JahreWOSepsisM], 
             [A2.count70JahreWSepsisF, A2.count70JahreWOSepsisF, A2.count70JahreWSepsisM, A2.count70JahreWOSepsisM], 
             [A2.count80JahreWSepsisF, A2.count80JahreWOSepsisF, A2.count80JahreWSepsisM, A2.count80JahreWOSepsisM]]
        print("Das ist das Array {}", verarbeitetesListList)
        A2.makeSepsisAgeGenderDiagram(verarbeitetesListList)
        st.write("TODO ")
        st.write("The top graph includes the number of age groups with and without sepsis, while the bottom graph shows in percentages who has the largest sepsis group. The three largest groups with sepsis among men is respectively: ")
        st.write("1) 60-69 men with: 1.24%.")
        st.write("2) 70-79 men with: 1,23%.")
        st.write("3) 50-59 men with: 1.07%.")
        st.write("While the largest groups for females were these: ")
        st.write("1) 70-79 women with: 0.89%")
        st.write("2) 60-69 women with: 0,733%")
        st.write("3) women older 80 with: 0.615%.")
        st.write("Here it may be that there has no difference between the gendern. (TODO: Find out!)")

        print("Personen im Datensatz")
        print("Personen im Datensatz Frau: ", A2.countFemale)
        print("Personen im Datensatz Mann: ", A2.countMale)
        print("HIIIIIIIIIIEEEEEEEER")
        print("FRAUEN")
        #personen allgemein
        print("Personen im Datensatz: ", A2.countFemale + A2.countMale)
        persondatensatz =  A2.countFemale + A2.countMale
        #under 20 years
        print("Anzahl Frauen allgemein unter 20 insgesamt im Datensatz: ", (A2.count1819WSepsisF + A2.count1819WOSepsisF))
        print("Prozent Frauen allgemein unter 20 insgesamt im Datensatz: (F:All)", ((A2.count1819WSepsisF + A2.count1819WOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis unter 20 insgesamt im Datensatz: ", (A2.count1819WSepsisF))
        print("Prozent Frauen mit Sepsis unter 20 insgesamt im Datensatz (F:A): ", (A2.count1819WSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A2.count1819WSepsisF*100) / (A2.count1819WSepsisF + A2.count1819WOSepsisF) )
        print("Anzahl Frauen ohne Sepsis unter 20 insgesamt im Datensatz: ", A2.count1819WOSepsisF)
        print("Prozent Frauen ohne Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A2.count1819WOSepsisF*100)/(A2.count1819WSepsisF + A2.count1819WOSepsisF))
        
        #between 20 years -29 years
        print("Anzahl Frauen zwischen 20-29  insgesamt im Datensatz: ", (A2.count20JahreWSepsisF + A2.count20JahreWOSepsisF))
        print("Prozent Frauen zwischen 20-29 insgesamt im Datensatz: (F:All)", ((A2.count20JahreWSepsisF + A2.count20JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz: ", (A2.count20JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:A): ", (A2.count20JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A2.count20JahreWSepsisF*100) / (A2.count20JahreWSepsisF + A2.count20JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 20-29 insgesamt im Datensatz: ", A2.count20JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A2.count20JahreWOSepsisF*100)/(A2.count20JahreWSepsisF + A2.count20JahreWOSepsisF))

        #between 30 years -39 years
        print("Anzahl Frauen zwischen 30-39  insgesamt im Datensatz: ", (A2.count30JahreWSepsisF + A2.count30JahreWOSepsisF))
        print("Prozent Frauen zwischen 30-39 insgesamt im Datensatz: (F:All)", ((A2.count30JahreWSepsisF + A2.count30JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz: ", (A2.count30JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:A): ", (A2.count30JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A2.count30JahreWSepsisF*100) / (A2.count30JahreWSepsisF + A2.count30JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 30-39 insgesamt im Datensatz: ", A2.count30JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A2.count30JahreWOSepsisF*100)/(A2.count30JahreWSepsisF + A2.count30JahreWOSepsisF))

        #between 40 years -49 years
        print("Anzahl Frauen zwischen 40-49  insgesamt im Datensatz: ", (A2.count40JahreWSepsisF + A2.count40JahreWOSepsisF))
        print("Prozent Frauen zwischen 40-49 insgesamt im Datensatz: (F:All)", ((A2.count40JahreWSepsisF + A2.count40JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz: ", (A2.count40JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:A): ", (A2.count40JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A2.count40JahreWSepsisF*100) / (A2.count40JahreWSepsisF + A2.count40JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 40-49 insgesamt im Datensatz: ", A2.count40JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A2.count40JahreWOSepsisF*100)/(A2.count40JahreWSepsisF + A2.count40JahreWOSepsisF))

        #between 50 years -59 years
        print("Anzahl Frauen zwischen 50-59  insgesamt im Datensatz: ", (A2.count50JahreWSepsisF + A2.count50JahreWOSepsisF))
        print("Prozent Frauen zwischen 50-59 insgesamt im Datensatz: (F:All)", ((A2.count50JahreWSepsisF + A2.count50JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz: ", (A2.count50JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:A): ", (A2.count50JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A2.count50JahreWSepsisF*100) / (A2.count50JahreWSepsisF + A2.count50JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 50-59 insgesamt im Datensatz: ", A2.count50JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A2.count50JahreWOSepsisF*100)/(A2.count50JahreWSepsisF + A2.count50JahreWOSepsisF))

        #between 60 years -69 years
        print("Anzahl Frauen zwischen 60-69  insgesamt im Datensatz: ", (A2.count60JahreWSepsisF + A2.count60JahreWOSepsisF))
        print("Prozent Frauen zwischen 60-69 insgesamt im Datensatz: (F:All)", ((A2.count60JahreWSepsisF + A2.count60JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz: ", (A2.count60JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:A): ", (A2.count60JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A2.count60JahreWSepsisF*100) / (A2.count60JahreWSepsisF + A2.count60JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 60-69 insgesamt im Datensatz: ", A2.count60JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A2.count60JahreWOSepsisF*100)/(A2.count60JahreWSepsisF + A2.count60JahreWOSepsisF))

         #between 70 years -79 years
        print("Anzahl Frauen zwischen 70-79  insgesamt im Datensatz: ", (A2.count70JahreWSepsisF + A2.count70JahreWOSepsisF))
        print("Prozent Frauen zwischen 70-79 insgesamt im Datensatz: (F:All)", ((A2.count70JahreWSepsisF + A2.count70JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz: ", (A2.count70JahreWSepsisF))
        print("Prozent Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:A): ", (A2.count70JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A2.count70JahreWSepsisF*100) / (A2.count70JahreWSepsisF + A2.count70JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis zwischen 70-79 insgesamt im Datensatz: ", A2.count70JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A2.count70JahreWOSepsisF*100)/(A2.count70JahreWSepsisF + A2.count70JahreWOSepsisF))

        #older 80
        print("Anzahl Frauen älter 80  insgesamt im Datensatz: ", (A2.count80JahreWSepsisF + A2.count80JahreWOSepsisF))
        print("Prozent Frauen älter 80 insgesamt im Datensatz: (F:All)", ((A2.count80JahreWSepsisF + A2.count80JahreWOSepsisF)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Frauen mit Sepsis älter 80 insgesamt im Datensatz: ", (A2.count80JahreWSepsisF))
        print("Prozent Frauen mit Sepsis älter 80 insgesamt im Datensatz (F:A): ", (A2.count80JahreWSepsisF)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Frauen mit Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A2.count80JahreWSepsisF*100) / (A2.count80JahreWSepsisF + A2.count80JahreWOSepsisF) )
        print("Anzahl Frauen ohne Sepsis älter 80 insgesamt im Datensatz: ", A2.count80JahreWOSepsisF)
        print("Prozent Frauen ohne Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A2.count80JahreWOSepsisF*100)/(A2.count80JahreWSepsisF + A2.count80JahreWOSepsisF))

        #MÄNNER
        print("MÄNNER")
        #under 20 years
        print("Anzahl Männer allgemein unter 20 insgesamt im Datensatz: ", (A2.count1819WSepsisM + A2.count1819WOSepsisM))
        print("Prozent Männer allgemein unter 20 insgesamt im Datensatz: (F:All)", ((A2.count1819WSepsisM + A2.count1819WOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis unter 20 insgesamt im Datensatz: ", (A2.count1819WSepsisM))
        print("Prozent Männer mit Sepsis unter 20 insgesamt im Datensatz (F:A): ", (A2.count1819WSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A2.count1819WSepsisM*100) / (A2.count1819WSepsisM + A2.count1819WOSepsisM) )
        print("Anzahl Männer ohne Sepsis unter 20 insgesamt im Datensatz: ", A2.count1819WOSepsisM)
        print("Prozent Männer ohne Sepsis unter 20 insgesamt im Datensatz (F:F): ", (A2.count1819WOSepsisM*100)/(A2.count1819WSepsisM + A2.count1819WOSepsisM))
        
        #between 20 years -29 years
        print("Anzahl Männer zwischen 20-29  insgesamt im Datensatz: ", (A2.count20JahreWSepsisM + A2.count20JahreWOSepsisM))
        print("Prozent Männer zwischen 20-29 insgesamt im Datensatz: (F:All)", ((A2.count20JahreWSepsisM + A2.count20JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz: ", (A2.count20JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:A): ", (A2.count20JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A2.count20JahreWSepsisM*100) / (A2.count20JahreWSepsisM + A2.count20JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 20-29 insgesamt im Datensatz: ", A2.count20JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (A2.count20JahreWOSepsisM*100)/(A2.count20JahreWSepsisM + A2.count20JahreWOSepsisM))

        #between 30 years -39 years
        print("Anzahl Männer zwischen 30-39  insgesamt im Datensatz: ", (A2.count30JahreWSepsisM + A2.count30JahreWOSepsisM))
        print("Prozent Männer zwischen 30-39 insgesamt im Datensatz: (F:All)", ((A2.count30JahreWSepsisM + A2.count30JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz: ", (A2.count30JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:A): ", (A2.count30JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A2.count30JahreWSepsisM*100) / (A2.count30JahreWSepsisM + A2.count30JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 30-39 insgesamt im Datensatz: ", A2.count30JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (A2.count30JahreWOSepsisM*100)/(A2.count30JahreWSepsisM + A2.count30JahreWOSepsisM))

        #between 40 years -49 years
        print("Anzahl Männer zwischen 40-49  insgesamt im Datensatz: ", (A2.count40JahreWSepsisM + A2.count40JahreWOSepsisM))
        print("Prozent Männer zwischen 40-49 insgesamt im Datensatz: (F:All)", ((A2.count40JahreWSepsisM + A2.count40JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz: ", (A2.count40JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:A): ", (A2.count40JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A2.count40JahreWSepsisM*100) / (A2.count40JahreWSepsisM + A2.count40JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 40-49 insgesamt im Datensatz: ", A2.count40JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (A2.count40JahreWOSepsisM*100)/(A2.count40JahreWSepsisM + A2.count40JahreWOSepsisM))

        #between 50 years -59 years
        print("Anzahl Männer zwischen 50-59  insgesamt im Datensatz: ", (A2.count50JahreWSepsisM + A2.count50JahreWOSepsisM))
        print("Prozent Männer zwischen 50-59 insgesamt im Datensatz: (F:All)", ((A2.count50JahreWSepsisM + A2.count50JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz: ", (A2.count50JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:A): ", (A2.count50JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A2.count50JahreWSepsisM*100) / (A2.count50JahreWSepsisM + A2.count50JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 50-59 insgesamt im Datensatz: ", A2.count50JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (A2.count50JahreWOSepsisM*100)/(A2.count50JahreWSepsisM + A2.count50JahreWOSepsisM))

        #between 60 years -69 years
        print("Anzahl Männer zwischen 60-69  insgesamt im Datensatz: ", (A2.count60JahreWSepsisM + A2.count60JahreWOSepsisM))
        print("Prozent Männer zwischen 60-69 insgesamt im Datensatz: (F:All)", ((A2.count60JahreWSepsisM + A2.count60JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz: ", (A2.count60JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:A): ", (A2.count60JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A2.count60JahreWSepsisM*100) / (A2.count60JahreWSepsisM + A2.count60JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 60-69 insgesamt im Datensatz: ", A2.count60JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (A2.count60JahreWOSepsisM*100)/(A2.count60JahreWSepsisM + A2.count60JahreWOSepsisM))

         #between 70 years -79 years
        print("Anzahl Männer zwischen 70-79  insgesamt im Datensatz: ", (A2.count70JahreWSepsisM + A2.count70JahreWOSepsisM))
        print("Prozent Männer zwischen 70-79 insgesamt im Datensatz: (F:All)", ((A2.count70JahreWSepsisM + A2.count70JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz: ", (A2.count70JahreWSepsisM))
        print("Prozent Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:A): ", (A2.count70JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A2.count70JahreWSepsisM*100) / (A2.count70JahreWSepsisM + A2.count70JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis zwischen 70-79 insgesamt im Datensatz: ", A2.count70JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (A2.count70JahreWOSepsisM*100)/(A2.count70JahreWSepsisM + A2.count70JahreWOSepsisM))

        #older 80
        print("Anzahl Männer älter 80  insgesamt im Datensatz: ", (A2.count80JahreWSepsisM + A2.count80JahreWOSepsisM))
        print("Prozent Männer älter 80 insgesamt im Datensatz: (F:All)", ((A2.count80JahreWSepsisM + A2.count80JahreWOSepsisM)*100 )/  (A2.countFemale + A2.countMale))
        print("Anzahl Männer mit Sepsis älter 80 insgesamt im Datensatz: ", (A2.count80JahreWSepsisM))
        print("Prozent Männer mit Sepsis älter 80 insgesamt im Datensatz (F:A): ", (A2.count80JahreWSepsisM)*100 /  (A2.countFemale + A2.countMale) )
        print("Prozent Männer mit Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A2.count80JahreWSepsisM*100) / (A2.count80JahreWSepsisM + A2.count80JahreWOSepsisM) )
        print("Anzahl Männer ohne Sepsis älter 80 insgesamt im Datensatz: ", A2.count80JahreWOSepsisM)
        print("Prozent Männer ohne Sepsis älter 80 insgesamt im Datensatz (F:F): ", (A2.count80JahreWOSepsisM*100)/(A2.count80JahreWSepsisM + A2.count80JahreWOSepsisM))


        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Woman under the Age of 20 With Sepsis', 'Woman under the Age of 20 Without Sepsis', 'Woman between 20-29 With Sepsis', 'Woman between 20-29 without Sepsis','Woman between 30-39 With Sepsis', 'Woman between 30-39 without Sepsis','Woman between 40-49 With Sepsis', 'Woman between 40-49 without Sepsis','Woman between 50-59 With Sepsis', 'Woman between 50-59 without Sepsis','Woman between 60-69 With Sepsis', 'Woman between 60-69 without Sepsis','Woman between 70-79 With Sepsis', 'Woman between 70-79 without Sepsis','Woman older 80 With Sepsis', 'Woman older 80 without Sepsis','Man under the Age of 20 With Sepsis', 'Men under the Age of 20 Without Sepsis', 'Men between 20-29 With Sepsis', 'Men between 20-29 without Sepsis','Men between 30-39 With Sepsis', 'Men between 30-39 without Sepsis','Men between 40-49 With Sepsis', 'Men between 40-49 without Sepsis','Men between 50-59 With Sepsis', 'Men between 50-59 without Sepsis','Men between 60-69 With Sepsis', 'Men between 60-69 without Sepsis','Men between 70-79 With Sepsis', 'Men between 70-79 without Sepsis','Men older 80 With Sepsis', 'Men older 80 without Sepsis',

        #Prozente
        sizes = [ (verarbeitetesListList[0][0])*100 /  (persondatensatz) , 
                 (verarbeitetesListList[0][1]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][1]*100) / (persondatensatz),
                 (verarbeitetesListList[2][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[2][1]*100) / (persondatensatz),
                 (verarbeitetesListList[3][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[3][1]*100) / (persondatensatz),
                 (verarbeitetesListList[4][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[4][1]*100) / (persondatensatz),
                 (verarbeitetesListList[5][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[5][1]*100) / (persondatensatz),
                 (verarbeitetesListList[6][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[6][1]*100) / (persondatensatz),
                 (verarbeitetesListList[7][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[7][1]*100) / (persondatensatz),
                 (verarbeitetesListList[0][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[0][3]*100) / (persondatensatz),
                 (verarbeitetesListList[1][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][3]*100) / (persondatensatz),
                 (verarbeitetesListList[2][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[2][3]*100) / (persondatensatz),
                 (verarbeitetesListList[3][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[3][3]*100) / (persondatensatz),
                 (verarbeitetesListList[4][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[4][3]*100) / (persondatensatz),
                 (verarbeitetesListList[5][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[5][3]*100) / (persondatensatz),
                 (verarbeitetesListList[6][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[6][3]*100) / (persondatensatz),
                 (verarbeitetesListList[7][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[7][3]*100) / (persondatensatz),
                 ]

        fig1, ax1 = st.columns(2)
        fig2 = px.pie(sizes, labels=labels, values=sizes, names=labels)
        ax1.write(fig2)


        #both dataset
    if(intToDecide == 3):
        print("datasetInt: {}", 3)
        A1 = CheckForSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
        A2 = CheckForSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
        A1.getFileNames()
        A2.getFileNames()
        #A2.extractAllSepsislabel
        verarbeitetesListList = [[A1.count1819WSepsisF+A2.count1819WSepsisF, A1.count1819WOSepsisF + A2.count1819WOSepsisF,A1.count1819WSepsisM + A2.count1819WSepsisM, A1.count1819WOSepsisM + A2.count1819WOSepsisM], 
             [A1.count20JahreWSepsisF + A2.count20JahreWSepsisF, A1.count20JahreWOSepsisF + A2.count20JahreWOSepsisF, A1.count20JahreWSepsisM + A2.count20JahreWSepsisM, A1.count20JahreWOSepsisM + A2.count20JahreWOSepsisM], 
             [A1.count30JahreWSepsisF + A2.count30JahreWSepsisF, A1.count30JahreWOSepsisF + A2.count30JahreWOSepsisF, A1.count30JahreWSepsisM + A2.count30JahreWSepsisM, A1.count30JahreWOSepsisM + A2.count30JahreWOSepsisM], 
             [A1.count40JahreWSepsisF + A2.count40JahreWSepsisF, A1.count40JahreWOSepsisF + A2.count40JahreWOSepsisF, A1.count40JahreWSepsisM + A2.count40JahreWSepsisM, A1.count40JahreWOSepsisM + A2.count40JahreWOSepsisM], 
             [A1.count50JahreWSepsisF + A2.count50JahreWSepsisF, A1.count50JahreWOSepsisF + A2.count50JahreWOSepsisF, A1.count50JahreWSepsisM + A2.count50JahreWSepsisM, A1.count50JahreWOSepsisM + A2.count50JahreWOSepsisM], 
             [A1.count60JahreWSepsisF + A2.count60JahreWSepsisF, A1.count60JahreWOSepsisF + A2.count60JahreWOSepsisF, A1.count60JahreWSepsisM + A2.count60JahreWSepsisM, A1.count60JahreWOSepsisM + A2.count60JahreWOSepsisM], 
             [A1.count70JahreWSepsisF + A2.count70JahreWSepsisF, A1.count70JahreWOSepsisF + A2.count70JahreWOSepsisF, A1.count70JahreWSepsisM + A2.count70JahreWSepsisM, A1.count70JahreWOSepsisM + A2.count70JahreWOSepsisM], 
             [A1.count80JahreWSepsisF + A2.count80JahreWSepsisF, A1.count80JahreWOSepsisF + A2.count80JahreWOSepsisF, A1.count80JahreWSepsisM + A2.count80JahreWSepsisM, A1.count80JahreWOSepsisM + A2.count80JahreWOSepsisM]]
        print("Das ist das Array {}", verarbeitetesListList)

        A2.makeSepsisAgeGenderDiagram(verarbeitetesListList)
        #st.write("TODO")
        st.write("The top graph includes the number of age groups with and without sepsis, while the bottom graph shows in percentages who has the largest sepsis group.")

        #st.write("Here it may be that there has no difference between the gendern. (TODO: Find out!)")

        print("Personen im Datensatz: BOTH")
        print("Personen im Datensatz Frau: ", A1.countFemale+ A2.countFemale)
        print("Personen im Datensatz Mann: ", A1.countMale + A2.countMale)
        print("HIIIIIIIIIIEEEEEEEER")
        print("FRAUEN")
        #personen allgemein
        persondatensatz =  A1.countFemale + A1.countMale+ A2.countFemale + A2.countMale
        print("Personen im Datensatz: ", persondatensatz)
        #under 20 years
        print("Anzahl Frauen allgemein unter 20 insgesamt im Datensatz: ", (verarbeitetesListList[0][0] + verarbeitetesListList[0][1]))
        print("Prozent Frauen allgemein unter 20 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[0][0] + verarbeitetesListList[0][1])*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis unter 20 insgesamt im Datensatz: ", (verarbeitetesListList[0][0]))
        print("Prozent Frauen mit Sepsis unter 20 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[0][0])*100 /  (persondatensatz) )
        print("Prozent Frauen ohne Sepsis unter 20 insgesamt im Datensatz (F:A): ", ((verarbeitetesListList[0][1]*100) / persondatensatz) )
        print("Anzahl Frauen ohne Sepsis unter 20 insgesamt im Datensatz: ", verarbeitetesListList[0][1])
        print("Prozent Frauen ohne Sepsis unter 20 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[0][1]*100)/(verarbeitetesListList[0][0] + verarbeitetesListList[0][1]))
        
        #between 20 years -29 years
        print("Anzahl Frauen zwischen 20-29  insgesamt im Datensatz: ", (verarbeitetesListList[1][0]  + verarbeitetesListList[1][1] ))
        print("Prozent Frauen zwischen 20-29 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[1][0]  + verarbeitetesListList[1][1] )*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz: ", (verarbeitetesListList[1][0] ))
        print("Prozent Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[1][0] )*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[1][0] *100) / (verarbeitetesListList[1][0]  + verarbeitetesListList[1][1] ) )
        print("Anzahl Frauen ohne Sepsis zwischen 20-29 insgesamt im Datensatz: ", verarbeitetesListList[1][1] )
        print("Prozent Frauen ohne Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[1][1] *100)/(verarbeitetesListList[1][0]  + verarbeitetesListList[1][1] ))

        #between 30 years -39 years
        print("Anzahl Frauen zwischen 30-39  insgesamt im Datensatz: ", (verarbeitetesListList[2][0]  + verarbeitetesListList[2][1] ))
        print("Prozent Frauen zwischen 30-39 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[2][0]  + verarbeitetesListList[2][1] )*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz: ", (verarbeitetesListList[2][0] ))
        print("Prozent Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[2][0] )*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[2][0] *100) / (verarbeitetesListList[2][0]  + verarbeitetesListList[2][1] ) )
        print("Anzahl Frauen ohne Sepsis zwischen 30-39 insgesamt im Datensatz: ", verarbeitetesListList[2][1] )
        print("Prozent Frauen ohne Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[2][1] *100)/(verarbeitetesListList[2][0]  + verarbeitetesListList[2][1] ))

        #between 40 years -49 years
        print("Anzahl Frauen zwischen 40-49  insgesamt im Datensatz: ", (verarbeitetesListList[3][0] + verarbeitetesListList[3][1]))
        print("Prozent Frauen zwischen 40-49 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[3][0] + verarbeitetesListList[3][1])*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz: ", (verarbeitetesListList[3][0]))
        print("Prozent Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[3][0])*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[3][0]*100) / (verarbeitetesListList[3][0] + verarbeitetesListList[3][1]) )
        print("Anzahl Frauen ohne Sepsis zwischen 40-49 insgesamt im Datensatz: ", verarbeitetesListList[3][1])
        print("Prozent Frauen ohne Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[3][1]*100)/(verarbeitetesListList[3][0] + verarbeitetesListList[3][1]))

        #between 50 years -59 years
        print("Anzahl Frauen zwischen 50-59  insgesamt im Datensatz: ", (verarbeitetesListList[4][0] + verarbeitetesListList[4][1]))
        print("Prozent Frauen zwischen 50-59 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[4][0] + verarbeitetesListList[4][1])*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz: ", (verarbeitetesListList[4][0]))
        print("Prozent Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[4][0])*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[4][0]*100) / (verarbeitetesListList[4][0] + verarbeitetesListList[4][1]) )
        print("Anzahl Frauen ohne Sepsis zwischen 50-59 insgesamt im Datensatz: ", verarbeitetesListList[4][1])
        print("Prozent Frauen ohne Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[4][1]*100)/(verarbeitetesListList[4][0] + verarbeitetesListList[4][1]))

        #between 60 years -69 years
        print("Anzahl Frauen zwischen 60-69  insgesamt im Datensatz: ", (verarbeitetesListList[5][0] + verarbeitetesListList[5][1]))
        print("Prozent Frauen zwischen 60-69 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[5][0] + verarbeitetesListList[5][1])*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz: ", (verarbeitetesListList[5][0]))
        print("Prozent Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[5][0])*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[5][0]*100) / (verarbeitetesListList[5][0] + verarbeitetesListList[5][1]) )
        print("Anzahl Frauen ohne Sepsis zwischen 60-69 insgesamt im Datensatz: ", verarbeitetesListList[5][1])
        print("Prozent Frauen ohne Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[5][1]*100)/(verarbeitetesListList[5][0] + verarbeitetesListList[5][1]))

         #between 70 years -79 years
        print("Anzahl Frauen zwischen 70-79  insgesamt im Datensatz: ", (verarbeitetesListList[6][0] + verarbeitetesListList[6][1]))
        print("Prozent Frauen zwischen 70-79 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[6][0] + verarbeitetesListList[6][1])*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz: ", (verarbeitetesListList[6][0]))
        print("Prozent Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[6][0])*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[6][0]*100) / (verarbeitetesListList[6][0] + verarbeitetesListList[6][1]) )
        print("Anzahl Frauen ohne Sepsis zwischen 70-79 insgesamt im Datensatz: ", verarbeitetesListList[6][1])
        print("Prozent Frauen ohne Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[6][1]*100)/(verarbeitetesListList[6][0] + verarbeitetesListList[6][1]))

        #older 80
        print("Anzahl Frauen älter 80  insgesamt im Datensatz: ", (verarbeitetesListList[7][0] + verarbeitetesListList[7][1]))
        print("Prozent Frauen älter 80 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[7][0] + verarbeitetesListList[7][1])*100 )/  (persondatensatz))
        print("Anzahl Frauen mit Sepsis älter 80 insgesamt im Datensatz: ", (verarbeitetesListList[7][0]))
        print("Prozent Frauen mit Sepsis älter 80 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[7][0])*100 /  (persondatensatz) )
        print("Prozent Frauen mit Sepsis älter 80 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[7][0]*100) / (verarbeitetesListList[7][0] + verarbeitetesListList[7][1]) )
        print("Anzahl Frauen ohne Sepsis älter 80 insgesamt im Datensatz: ", verarbeitetesListList[7][1])
        print("Prozent Frauen ohne Sepsis älter 80 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[7][1]*100)/(verarbeitetesListList[7][0] + verarbeitetesListList[7][1]))

        print("MÄNNER")
        #under 20 years
        print("Anzahl Männer allgemein unter 20 insgesamt im Datensatz: ", (verarbeitetesListList[0][2] + verarbeitetesListList[0][3]))
        print("Prozent Männer allgemein unter 20 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[0][2] + verarbeitetesListList[0][3])*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis unter 20 insgesamt im Datensatz: ", (verarbeitetesListList[0][2]))
        print("Prozent Männer mit Sepsis unter 20 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[0][2])*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis unter 20 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[0][2]*100) / (verarbeitetesListList[0][2] + verarbeitetesListList[0][3]) )
        print("Anzahl Männer ohne Sepsis unter 20 insgesamt im Datensatz: ", verarbeitetesListList[0][3])
        print("Prozent Männer ohne Sepsis unter 20 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[0][3]*100)/(verarbeitetesListList[0][2] + verarbeitetesListList[0][3]))
        
        #between 20 years -29 years
        print("Anzahl Männer zwischen 20-29  insgesamt im Datensatz: ", (verarbeitetesListList[1][2]  + verarbeitetesListList[1][3] ))
        print("Prozent Männer zwischen 20-29 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[1][2]  + verarbeitetesListList[1][3] )*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz: ", (verarbeitetesListList[1][2] ))
        print("Prozent Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[1][2] )*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[1][2] *100) / (verarbeitetesListList[1][2]  + verarbeitetesListList[1][3] ) )
        print("Anzahl Männer ohne Sepsis zwischen 20-29 insgesamt im Datensatz: ", verarbeitetesListList[1][3] )
        print("Prozent Männer ohne Sepsis zwischen 20-29 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[1][3] *100)/(verarbeitetesListList[1][2]  + verarbeitetesListList[1][3] ))

        #between 30 years -39 years
        print("Anzahl Männer zwischen 30-39  insgesamt im Datensatz: ", (verarbeitetesListList[2][2]  + verarbeitetesListList[2][3] ))
        print("Prozent Männer zwischen 30-39 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[2][2]  + verarbeitetesListList[2][3] )*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz: ", (verarbeitetesListList[2][2] ))
        print("Prozent Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[2][2] )*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[2][2] *100) / (verarbeitetesListList[2][2]  + verarbeitetesListList[2][3] ) )
        print("Anzahl Männer ohne Sepsis zwischen 30-39 insgesamt im Datensatz: ", verarbeitetesListList[2][3] )
        print("Prozent Männer ohne Sepsis zwischen 30-39 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[2][3] *100)/(verarbeitetesListList[2][2]  + verarbeitetesListList[2][3] ))

        #between 40 years -49 years
        print("Anzahl Männer zwischen 40-49  insgesamt im Datensatz: ", (verarbeitetesListList[3][2] + verarbeitetesListList[3][3]))
        print("Prozent Männer zwischen 40-49 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[3][2] + verarbeitetesListList[3][3])*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz: ", (verarbeitetesListList[3][2]))
        print("Prozent Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[3][2])*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[3][2]*100) / (verarbeitetesListList[3][2] + verarbeitetesListList[3][3]) )
        print("Anzahl Männer ohne Sepsis zwischen 40-49 insgesamt im Datensatz: ", verarbeitetesListList[3][3])
        print("Prozent Männer ohne Sepsis zwischen 40-49 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[3][3]*100)/(verarbeitetesListList[3][2] + verarbeitetesListList[3][3]))

        #between 50 years -59 years
        print("Anzahl Männer zwischen 50-59  insgesamt im Datensatz: ", (verarbeitetesListList[4][2] + verarbeitetesListList[4][3]))
        print("Prozent Männer zwischen 50-59 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[4][2] + verarbeitetesListList[4][3])*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz: ", (verarbeitetesListList[4][2]))
        print("Prozent Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[4][2])*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[4][2]*100) / (verarbeitetesListList[4][2] + verarbeitetesListList[4][3]) )
        print("Anzahl Männer ohne Sepsis zwischen 50-59 insgesamt im Datensatz: ", verarbeitetesListList[4][3])
        print("Prozent Männer ohne Sepsis zwischen 50-59 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[4][3]*100)/(verarbeitetesListList[4][2] + verarbeitetesListList[4][3]))

        #between 60 years -69 years
        print("Anzahl Männer zwischen 60-69  insgesamt im Datensatz: ", (verarbeitetesListList[5][2] + verarbeitetesListList[5][3]))
        print("Prozent Männer zwischen 60-69 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[5][2] + verarbeitetesListList[5][3])*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz: ", (verarbeitetesListList[5][2]))
        print("Prozent Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[5][2])*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[5][2]*100) / (verarbeitetesListList[5][2] + verarbeitetesListList[5][3]) )
        print("Anzahl Männer ohne Sepsis zwischen 60-69 insgesamt im Datensatz: ", verarbeitetesListList[5][3])
        print("Prozent Männer ohne Sepsis zwischen 60-69 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[5][3]*100)/(verarbeitetesListList[5][2] + verarbeitetesListList[5][3]))

         #between 70 years -79 years
        print("Anzahl Männer zwischen 70-79  insgesamt im Datensatz: ", (verarbeitetesListList[6][2] + verarbeitetesListList[6][3]))
        print("Prozent Männer zwischen 70-79 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[6][2] + verarbeitetesListList[6][3])*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz: ", (verarbeitetesListList[6][2]))
        print("Prozent Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[6][2])*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[6][2]*100) / (verarbeitetesListList[6][2] + verarbeitetesListList[6][3]) )
        print("Anzahl Männer ohne Sepsis zwischen 70-79 insgesamt im Datensatz: ", verarbeitetesListList[6][3])
        print("Prozent Männer ohne Sepsis zwischen 70-79 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[6][3]*100)/(verarbeitetesListList[6][2] + verarbeitetesListList[6][3]))

        #older 80
        print("Anzahl Männer älter 80  insgesamt im Datensatz: ", (verarbeitetesListList[7][2] + verarbeitetesListList[7][3]))
        print("Prozent Männer älter 80 insgesamt im Datensatz: (F:All)", ((verarbeitetesListList[7][2] + verarbeitetesListList[7][3])*100 )/  (persondatensatz))
        print("Anzahl Männer mit Sepsis älter 80 insgesamt im Datensatz: ", (verarbeitetesListList[7][2]))
        print("Prozent Männer mit Sepsis älter 80 insgesamt im Datensatz (F:A): ", (verarbeitetesListList[7][2])*100 /  (persondatensatz) )
        print("Prozent Männer mit Sepsis älter 80 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[7][2]*100) / (verarbeitetesListList[7][2] + verarbeitetesListList[7][3]) )
        print("Anzahl Männer ohne Sepsis älter 80 insgesamt im Datensatz: ", verarbeitetesListList[7][3])
        print("Prozent Männer ohne Sepsis älter 80 insgesamt im Datensatz (F:F): ", (verarbeitetesListList[7][3]*100)/(verarbeitetesListList[7][2] + verarbeitetesListList[7][3]))

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Woman under the Age of 20 With Sepsis', 'Woman under the Age of 20 Without Sepsis', 'Woman between 20-29 With Sepsis', 'Woman between 20-29 without Sepsis','Woman between 30-39 With Sepsis', 'Woman between 30-39 without Sepsis','Woman between 40-49 With Sepsis', 'Woman between 40-49 without Sepsis','Woman between 50-59 With Sepsis', 'Woman between 50-59 without Sepsis','Woman between 60-69 With Sepsis', 'Woman between 60-69 without Sepsis','Woman between 70-79 With Sepsis', 'Woman between 70-79 without Sepsis','Woman older 80 With Sepsis', 'Woman older 80 without Sepsis','Man under the Age of 20 With Sepsis', 'Men under the Age of 20 Without Sepsis', 'Men between 20-29 With Sepsis', 'Men between 20-29 without Sepsis','Men between 30-39 With Sepsis', 'Men between 30-39 without Sepsis','Men between 40-49 With Sepsis', 'Men between 40-49 without Sepsis','Men between 50-59 With Sepsis', 'Men between 50-59 without Sepsis','Men between 60-69 With Sepsis', 'Men between 60-69 without Sepsis','Men between 70-79 With Sepsis', 'Men between 70-79 without Sepsis','Men older 80 With Sepsis', 'Men older 80 without Sepsis',

        #Prozente
        sizes = [ (verarbeitetesListList[0][0])*100 /  (persondatensatz) , 
                 (verarbeitetesListList[0][1]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][1]*100) / (persondatensatz),
                 (verarbeitetesListList[2][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[2][1]*100) / (persondatensatz),
                 (verarbeitetesListList[3][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[3][1]*100) / (persondatensatz),
                 (verarbeitetesListList[4][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[4][1]*100) / (persondatensatz),
                 (verarbeitetesListList[5][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[5][1]*100) / (persondatensatz),
                 (verarbeitetesListList[6][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[6][1]*100) / (persondatensatz),
                 (verarbeitetesListList[7][0]*100) / (persondatensatz), 
                 (verarbeitetesListList[7][1]*100) / (persondatensatz),
                 (verarbeitetesListList[0][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[0][3]*100) / (persondatensatz),
                 (verarbeitetesListList[1][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[1][3]*100) / (persondatensatz),
                 (verarbeitetesListList[2][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[2][3]*100) / (persondatensatz),
                 (verarbeitetesListList[3][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[3][3]*100) / (persondatensatz),
                 (verarbeitetesListList[4][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[4][3]*100) / (persondatensatz),
                 (verarbeitetesListList[5][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[5][3]*100) / (persondatensatz),
                 (verarbeitetesListList[6][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[6][3]*100) / (persondatensatz),
                 (verarbeitetesListList[7][2]*100) / (persondatensatz), 
                 (verarbeitetesListList[7][3]*100) / (persondatensatz),
                 ]
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = st.columns(2)
        fig2 = px.pie(sizes, labels=labels, values=sizes, names=labels)
        ax1.write(fig2)
        st.write("The three largest groups of the second visualization with sepsis among men is respectively: ")
        st.write("1) 60-69 men with: 1.05%.")
        st.write("2) 70-79 men with: 1,91%.")
        st.write("3) 50-59 men with: 0.85%.")
        st.write("While the largest groups for females were: ")
        st.write("1) 70-79 women with: 0.74%")
        st.write("2) 60-69 women with: 0,65%")
        st.write("3) 50-59 women with: 0.48%.")
        






#A1 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
#A1.makeGenderDiagram()

#A1.makeAgeGenderDiagram()
#A2 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
#A1.getFileNames()
#A2.getFileNames()


#Chart
#Sepsis
#chart_data = pd.DataFrame(
#    np.array([
#        [1, 3, 23, 21, 30, 35, 43, 63, 77,101, 90, 137, 102, 110, 62, 67],
#        [0, 2, 12, 8, 10, 16, 28, 54, 36, 76, 65, 110, 62, 88, 37, 43],
#        [2, 4, 22, 45, 22, 45, 58, 107, 80, 165, 109, 178, 134, 168, 84, 92]
#        ]),
#    columns=['female under 20 Sepsis','male under 20 Sepsis', 'female between 20 -29 Sepsis', 'male between 20-29 Sepsis', 'female between 30-39 Sepsis', 'male between 30-39 Sepsis','female between 40 -49 Sepsis', 'male between 40 -49 Sepsis','female between 50-59 Sepsis' ,'male between 50-59 Sepsis', 'female between 60-69 Sepsis','male between 60-69 Sepsis', 'female between 70-79 Sepsis','male between 70-79 Sepsis', 'over 80 female Sepsis', 'over 80 male Sepsis'], 
#    index=["M-ICU", "S-ICU", "NaN-ICU"])

#st.bar_chart(chart_data)


#Chart
#NoSepsis
#chart_data = pd.DataFrame(
#    np.array([
#        #MICU
#        [37, 27, 332, 287, 407, 471, 626, 853, 921, 1274, 1120, 1387, 1082, 1294, 937, 784],
#        #SICU
#        [23, 13, 144, 137, 246, 258, 384, 698, 729, 1578, 1132, 2254, 1114, 1765, 631, 699],
#        #NaN
#        [44, 76, 293, 410, 461, 471, 911, 1035, 1221, 1535, 1382, 1705, 1317, 1443, 1087, 911]
#        ]),
#    columns=['female under 20 No Sepsis','male under 20 No Sepsis', 'female between 20 -29 No Sepsis', 'male between 20-29 No Sepsis', 'female between 30-39 No Sepsis', 'male between 30-39 No Sepsis','female between 40 -49 No Sepsis', 'male between 40 -49 No Sepsis','female between 50-59 No Sepsis' ,'male between 50-59 No Sepsis', 'female between 60-69 No Sepsis','male between 60-69 No Sepsis', 'female between 70-79 No Sepsis','male between 70-79 No Sepsis', 'over 80 female No Sepsis', 'over 80 male No Sepsis'], 
#    index=["M-ICU", "S-ICU", "NaN-ICU"])

#st.bar_chart(chart_data)




#print("Das ist ALLER AnzahlSepsispatient: "+ str(A1.countSepsisPatient + A2.countSepsisPatient))
#print("Das ist ALLER AnzahlNichtSepsispatient: "+str(A1.countNonSepsisPatient + A2.countNonSepsisPatient))

#print("Das ist Anzahl aller Frauen:"+str(A1.countFemale+A2.countFemale))
#print("Das ist ALLER AnzahlFrauen mit Sepsis: "+ str(A1.countFemaleWSepsis + A2.countFemaleWSepsis))
#print("Das ist ALLER AnzahlFrauen ohne Sepsis: "+ str(A1.countFemaleWOSepsis + A2.countFemaleWOSepsis))
#print("Gesamte Anzahl Frauen mit 20-")
#print("Das ist ALLER AnzahlFrauen 20- mit Sepsis: "+ str(A1.count1819WSepsisF + A2.count1819WSepsisF))
#print("Das ist ALLER AnzahlFrauen 20- ohne Sepsis: "+ str(A1.count1819WOSepsisF + A2.count1819WOSepsisF))
#print("Gesamte Anzahl Frauen mit 20+")
#print("Das ist ALLER AnzahlFrauen 20er mit Sepsis: "+ str(A1.count20JahreWSepsisF + A2.count20JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 20er ohne Sepsis: "+ str(A1.count20JahreWOSepsisF + A2.count20JahreWOSepsisF))
#print("Gesamte Anzahl Frauen mit 30+")
#print("Das ist ALLER AnzahlFrauen 30er mit Sepsis: "+ str(A1.count30JahreWSepsisF + A2.count30JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 30er ohne Sepsis: "+ str(A1.count30JahreWOSepsisF + A2.count30JahreWOSepsisF))
#print("Gesamte Anzahl Frauen mit 40+")
#print("Das ist ALLER AnzahlFrauen 40er mit Sepsis: "+ str(A1.count40JahreWSepsisF + A2.count40JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 40er ohne Sepsis: "+ str(A1.count40JahreWOSepsisF + A2.count40JahreWOSepsisF))
#print("Gesamte Anzahl Frauen mit 50+")
#print("Das ist ALLER AnzahlFrauen 50er mit Sepsis: "+ str(A1.count50JahreWSepsisF + A2.count50JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 50er ohne Sepsis: "+ str(A1.count50JahreWOSepsisF + A2.count50JahreWOSepsisF))
#print("Gesamte Anzahl Frauen mit 60+")
#print("Das ist ALLER AnzahlFrauen 60er mit Sepsis: "+ str(A1.count60JahreWSepsisF + A2.count60JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 60er ohne Sepsis: "+ str(A1.count60JahreWOSepsisF + A2.count60JahreWOSepsisF))
#print("Gesamte Anzahl Frauen mit 70+")
#print("Das ist ALLER AnzahlFrauen 70er mit Sepsis: "+ str(A1.count70JahreWSepsisF + A2.count70JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 70er ohne Sepsis: "+ str(A1.count70JahreWOSepsisF + A2.count70JahreWOSepsisF))
#print("Gesamte Anzahl Frauen mit 80+")
#print("Das ist ALLER AnzahlFrauen 80er mit Sepsis: "+ str(A1.count80JahreWSepsisF + A2.count80JahreWSepsisF))
#print("Das ist ALLER AnzahlFrauen 80er ohne Sepsis: "+ str(A1.count80JahreWOSepsisF + A2.count80JahreWOSepsisF))


#print("Das ist Anzahl aller Männer:"+str(A1.countMale+A2.countMale))
#print("Das ist ALLER Anzahl Männer mit Sepsis: "+ str(A1.countMaleWSepsis + A2.countMaleWSepsis))
#print("Das ist ALLER Anzahl Männer ohne Sepsis: "+ str(A1.countMaleW0Sepsis + A2.countMaleW0Sepsis))
#print("Gesamte Anzahl Männer mit 20-")
#print("Das ist ALLER AnzahlMänner 18 mit Sepsis: "+ str(A1.count1819WSepsisM + A2.count1819WSepsisM))
#print("Das ist ALLER AnzahlMänner 18 ohne Sepsis: "+ str(A1.count1819WOSepsisM + A2.count1819WOSepsisM))
#print("Gesamte Anzahl Männer mit 20+")
#print("Das ist ALLER AnzahlMänner 20er mit Sepsis: "+ str(A1.count20JahreWSepsisM + A2.count20JahreWSepsisM))
#print("Das ist ALLER AnzahlMänner 20er ohne Sepsis: "+ str(A1.count20JahreWOSepsisM + A2.count20JahreWOSepsisM))
#print("Gesamte Anzahl Männer mit 30+")
#print("Das ist ALLER AnzahlMänner 30er mit Sepsis: "+ str(A1.count30JahreWSepsisM + A2.count30JahreWSepsisM))
#print("Das ist ALLER Anzahl Männer 30er ohne Sepsis: "+ str(A1.count30JahreWOSepsisM + A2.count30JahreWOSepsisM))
#print("Gesamte Anzahl Männer mit 40+")
#print("Das ist ALLER AnzahlMänner 40er mit Sepsis: "+ str(A1.count40JahreWSepsisM + A2.count40JahreWSepsisM))
#print("Das ist ALLER Anzahl Männer 40er ohne Sepsis: "+ str(A1.count40JahreWOSepsisM + A2.count40JahreWOSepsisM))
#print("Gesamte Anzahl Männer mit 50+")
#print("Das ist ALLER AnzahlMänner 50er mit Sepsis: "+ str(A1.count50JahreWSepsisM + A2.count50JahreWSepsisM))
#print("Das ist ALLER AnzahlMänner 50er ohne Sepsis: "+ str(A1.count50JahreWOSepsisM + A2.count50JahreWOSepsisM))
#print("Gesamte Anzahl Männer mit 60+")
#print("Das ist ALLER AnzahlMänner 60er mit Sepsis: "+ str(A1.count60JahreWSepsisM + A2.count60JahreWSepsisM))
#print("Das ist ALLER AnzahlMänner 60er ohne Sepsis: "+ str(A1.count60JahreWOSepsisM + A2.count60JahreWOSepsisM))
#print("Gesamte Anzahl Männer mit 70+")
#print("Das ist ALLER AnzahlMänner 70er mit Sepsis: "+ str(A1.count70JahreWSepsisM + A2.count70JahreWSepsisM))
#print("Das ist ALLER AnzahlMänner 70er ohne Sepsis: "+ str(A1.count70JahreWOSepsisM + A2.count70JahreWOSepsisM))
#print("Gesamte Anzahl Männer mit 80+")
#print("Das ist ALLER AnzahlMänner 80er mit Sepsis: "+ str(A1.count80JahreWSepsisM + A2.count80JahreWSepsisM))
#print("Das ist ALLER AnzahlMänner 80er ohne Sepsis: "+ str(A1.count80JahreWOSepsisM + A2.count80JahreWOSepsisM))


#Chart1
#chart_data = pd.DataFrame(
#    np.array([[ 1189, 16581],[ 1738, 20828]]),
#    columns=["Sepsis", "no Sepsis"], index=['female','male'])

#st.bar_chart(chart_data)



#Chart2 About Female
#chart_data = pd.DataFrame(
#    np.array([[ 3, 104, 9, 113],[ 57,769,74, 813], [62,1114, 96, 1165], [129, 1921, 224,2523], [193,2871,342,4286], [264,3634,425,5209], [298, 3513,366, 4392], [183,2655,202,2327]]),
#    columns=["Female had Sepsis", "Female had no Sepsis", "Male had Sepsis", "Male had no Sepsis"], index =['under the age of 20', '20-29 year olds', '30-39 year olds', '40-49 year olds', '50-59 year olds', '60-69 year olds', '70-79 year olds','over 80 years'])

#st.bar_chart(chart_data, height=600, width=900)

#Chart3 About Male


#Chat2
#df = pd.DataFrame(
#    np.array([[ 'female',1189, 16581, 17770],[ 'male',1738, 20828, 22566]]),
#    columns=['gender','has Sepsis', 'has no Sepsis', 'total' ])
#c = alt.Chart(df).mark_bar().encode(
#    x='gender,has Sepsis, has no Sepsis',
#    y='total',
    #color='year:N',
#)
#st.altair_chart(c, use_container_width=False)
#alt.Chart(source).mark_bar().encode(
#    x='year:O',
#    y='sum(yield):Q',
#    color='year:N',
#    column='site:N'
#)




#https://docs.streamlit.io/library/api-reference/charts/st.altair_chart

#print("Das ist SICU"+str(A.countSICU))
#print("Das ist MICU"+str(A.countMICU))
#print("Das ist NaN (kein SICU) "+str(A.countNaNSICU))
#print("Das ist NaN (kein MICU)"+str(A.countNaNMICU))
#print("18-19 Jahre:"+str(A.count1819))
#print("Zwanziger:"+str(A.count20Jahre))
#print("Dreißiger:"+str(A.count30Jahre))
#print("Vierziger"+str(A.count40Jahre))
#print("Fünfziger"+str(A.count50Jahre))
#print("sechziger"+str(A.count60Jahre))
#print("siebziger"+str(A.count70Jahre))
#print("achtziger"+str(A.count80Jahre))

#print(A.endResultAllAges), 
#print(A.endResultAllGender),
#print(A.endResultAllUnit1) 
#print(A.endResultAllUnit2)
#print(A.endResultAllHospAdmTime)
#print(A.endResultAllAllIculos)
#print(A.endResultAllSepsisLabel)
#A.readFiles("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training\\p000001.psv");
#A.extractAllAges();
#A.extractAllGender();
#A.extractAllUnits1();
#A.extractAllUnits2();
#A.extractAllHospAdmTime();
#A.extractAllIculos();
#A.extractAllSepsislabel();
#A.getFileNames()



 
    



#A1 = CheckForNaNValues("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
#A2 = CheckForNaNValues("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
#A1.getFileNames()
#A2.getFileNames()

