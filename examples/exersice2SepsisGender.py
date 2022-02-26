import os, sys
import csv
from os.path import isfile, join
from collections import Counter
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt



class CheckForSepsisGender():
    def __init__(self, dataPath=""):
        self.dataPath = dataPath
        #hasAllFileNamesInAnArray
        self.fileNames = []
        #currentFileData Array
        self.currentFileDataArray = []
        #has all the data from every file in the dataset A
        self.endResultAllAges = ["All Ages:"]
        #has only the data for 2b
        self.endResultAllGender = ["All Gender"]
        self.endResultAllUnit1 = ["All Unit1:"]
        self.endResultAllUnit2 = ["All Unit2:"]
        self.endResultAllHospAdmTime = ["All HospAdmTime:"]
        self.endResultAllAllIculos = ["All AllIculos:"]
        self.endResultAllSepsisLabel = ["All Sepsislabel: "]
        #female
        self.countFemale = 0;
        self.countFemaleNoSepsis = 0;
        self.countFemaleSepsis = 0;
        #male
        self.countMale = 0;
        self.countMaleNoSepsis = 0;
        self.countMaleSepsis = 0;

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
        self.extractAllGender()
        #self.extractAllSepsislabel(file)


    def extractAllGender(self):
        """ 0 for women and 1 for men"""
        gender = 50
        sepsis = 0
        for i in range(1, len(self.currentFileDataArray)-1):
            self.endResultAllGender.append(self.currentFileDataArray[i][35]);
            gender = self.currentFileDataArray[i][35]
            if(self.currentFileDataArray[i][40]== "1\n"):
                sepsis = 1
        #delete duplicates
        self.endResultAllGender = list(dict.fromkeys(self.endResultAllGender))
        if(gender == '0'):
            self.countFemale = self.countFemale + 1
            if(sepsis == 0):
                self.countFemaleNoSepsis = self.countFemaleNoSepsis + 1
            if(sepsis == 1):
                self.countFemaleSepsis = self.countFemaleSepsis + 1
        if(gender == '1'):
            self.countMale = self.countMale + 1
            if(sepsis == 0):
                self.countMaleNoSepsis = self.countMaleNoSepsis + 1
            if(sepsis == 1):
                self.countMaleSepsis = self.countMaleSepsis + 1 
                
    def makeGenderDiagramm(self, countFemaleSepsis, countFemaleNoSepsis, countMaleSepsis, countMaleNoSepsis):
        #chart_data = pd.DataFrame(
        #np.array([[ 1189, 16581],[ 1738, 20828]]),
        #columns=["Sepsis", "no Sepsis"], index=['female','male'])
        #st.bar_chart(chart_data)
        chart_data = pd.DataFrame(
        np.array([[countFemaleSepsis, countFemaleNoSepsis],[ countMaleSepsis, countMaleNoSepsis]]),
        columns=["Sepsis", "no Sepsis"], index=['female','male'])
        st.bar_chart(chart_data)    

 
    
def decideDiagram(datasetInt):
    #SepsisGender

        #checkwhichdataset 1
    if(datasetInt == 1):
        A1 = CheckForSepsisGender("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
        A1.getFileNames()
        print("Das sind alle Females vom Datensatz ",A1.countFemale)
        print("Das sind alle Males vom Datensatz ",A1.countMale)
        print("Das sind alle Females Sepsis vom Datensatz ",A1.countFemaleSepsis)
        print("Das sind alle Males Sepsis vom Datensatz ",A1.countMaleSepsis)
        print("Das sind alle Females No Sepsis vom Datensatz ",A1.countFemaleNoSepsis)
        print("Das sind alle Males No Sepsis vom Datensatz ",A1.countMaleNoSepsis)
        A1.makeGenderDiagramm(A1.countFemaleSepsis, A1.countFemaleNoSepsis, A1.countMaleSepsis, A1.countMaleNoSepsis)


    #dataset 2
    if(datasetInt == 2):
        A2 = CheckForSepsisGender("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
        A2.getFileNames()
        A2.makeGenderDiagramm(A2.countFemaleSepsis, A2.countFemaleNoSepsis, A2.countMaleSepsis, A2.countMaleNoSepsis)
        #print("Anzahl Frauen ", A2.countFemaleSepsis + A2.countFemaleNoSepsis)
        #print("Anzahl Sepsis Frauen ", (A2.countFemaleSepsis))
        #print("Prozent Sepsis Frauen ", (A2.countFemaleSepsis*100) / (A2.countFemaleSepsis + A2.countFemaleNoSepsis))
        #print("Anzahl No Sepsis Frauen ", (A2.countFemaleNoSepsis))
        #print("Prozent No Sepsis Frauen ", (A2.countFemaleNoSepsis*100) / (A2.countFemaleSepsis + A2.countFemaleNoSepsis))
        #print("Anzahl No Sepsis Frauen Allgemein", (A2.countFemaleNoSepsis))
        #print("Prozent No Sepsis Frauen Allgemein", (A2.countFemaleNoSepsis*100) / (20000))
        #print("Anzahl Sepsis Frauen Allgemein", (A2.countFemaleSepsis))
        #print("Prozent Sepsis Frauen Allgemein", (A2.countFemaleSepsis*100) / (20000))
        #print("Anzahl Männer ", A2.countMaleSepsis + A2.countMaleNoSepsis)
        #print("Prozent Sepsis Männer ", (A2.countMaleSepsis*100) / (A2.countMaleSepsis + A2.countMaleNoSepsis))
        #print("Anzahö Sepsis Männer ", (A2.countMaleSepsis))
        #print("Prozent No Sepsis Männer ", (A2.countMaleNoSepsis*100) / (A2.countMaleSepsis + A2.countMaleNoSepsis))
        #print("Anzahl No Sepsis Männer ", (A2.countMaleNoSepsis*100))
        #print("Prozent No Sepsis Männer Allgemein", (A2.countMaleNoSepsis*100) / (20000))
        #print("Prozent Sepsis Männer Allgemein", (A2.countMaleSepsis*100) / (20000))

        st.write("There are 9268 women and 10732 men in dataset 2. Converted into percentages, there would be 46.34% of women and 53.66% of men. Out of 9268 women, 491 were infected with sepsis, while out of 10732 men, 646 were infected with sepsis. Converted, the value of diseased women measured among all women is 5,3 % (regardless of gender would be 2.455% in total). The value of men infected with sepsis among all men would be:  6.02% (regardless of gender it would be: 3.23 %).")


        #both dataset
    if(datasetInt == 3):
        A1 = CheckForSepsisGender("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
        A2 = CheckForSepsisGender("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
        A1.getFileNames()
        A2.getFileNames()
        
        A3countFemaleSepsis = A1.countFemaleSepsis + A2.countFemaleSepsis
        A3countFemaleNoSepsis = A1.countFemaleNoSepsis + A2.countFemaleNoSepsis
        A3countMaleSepsis = A1.countMaleSepsis + A2.countMaleSepsis
        A3countMaleNoSepsis = A1.countMaleNoSepsis + A2.countMaleNoSepsis
        print("hier")
        A1.makeGenderDiagramm(A3countFemaleSepsis, A3countFemaleNoSepsis, A3countMaleSepsis, A3countMaleNoSepsis)
        print("Anzahl Frauen ", A3countFemaleSepsis + A3countFemaleNoSepsis)
        print("Anzahl Sepsis Frauen ", (A3countFemaleSepsis))
        #print("Prozent Sepsis Frauen ", (A3countFemaleSepsis*100) / (A3countFemaleSepsis + A3countFemaleNoSepsis))
        #print("Anzahl No Sepsis Frauen ", (A3countFemaleNoSepsis))
        #print("Prozent No Sepsis Frauen ", (A3countFemaleNoSepsis*100) / (A3countFemaleSepsis + A3countFemaleNoSepsis))
        print("Anzahl No Sepsis Frauen Allgemein", (A3countFemaleNoSepsis))
        #print("Prozent No Sepsis Frauen Allgemein", (A3countFemaleNoSepsis*100) / (40336))
        #print("Anzahl Sepsis Frauen Allgemein", (A3countFemaleSepsis))
        #print("Prozent Sepsis Frauen Allgemein", (A3countFemaleSepsis*100) / (40336))
        print("Anzahl Männer ", A3countMaleSepsis + A3countMaleNoSepsis)
        #print("Prozent Sepsis Männer ", (A3countMaleSepsis*100) / (A3countMaleSepsis + A3countMaleNoSepsis))
        print("Anzahö Sepsis Männer ", (A3countMaleSepsis))
        #print("Prozent No Sepsis Männer ", (A3countMaleNoSepsis*100) / (A3countMaleSepsis + A3countMaleNoSepsis))
        print("Anzahl No Sepsis Männer ", (A3countMaleNoSepsis*100))
        #print("Prozent No Sepsis Männer Allgemein", (A3countMaleNoSepsis*100) / (40336))
        #print("Prozent Sepsis Männer Allgemein", (A3countMaleSepsis*100) / (40336))

        st.write("There are 17770 women and 22566 men in both datasets. Converted into percentages, there would be 44.05% of women and 55.95% of men. Out of 17770 women, 1189 were infected with sepsis, while out of 22566 men, 1738 were infected with sepsis. Converted, the value of diseased women measured among all women is 6.69 % (regardless of gender would be 2.95% in total). The value of men infected with sepsis among all men would be:  7.70% (regardless of gender it would be: 4.31 %).")


