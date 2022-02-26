import os, sys
import csv
from os.path import isfile, join
from collections import Counter
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt



class SubGroups():
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
        #counting ICUs
        #MICU
        self.countAllUnit1Female = 0
        self.countAllUnit1FemaleSepsis = 0
        self.countAllUnit1FemaleNoSepsis = 0
        #SICU
        self.countAllUnit2Female = 0
        self.countAllUnit2FemaleSepsis = 0
        self.countAllUnit2FemaleNoSepsis = 0
        #NaN
        self.countNoUnitFemale = 0
        self.countNoUnitSepFemale = 0
        self.countNoUnitNoSepFemale = 0

        #MICU
        self.countAllUnit1Male = 0
        self.countAllUnit1MaleSepsis = 0
        self.countAllUnit1MaleNoSepsis = 0
        #SICU
        self.countAllUnit2Male = 0
        self.countAllUnit2MaleSepsis = 0
        self.countAllUnit2MaleNoSepsis = 0
        #NaN
        self.countNoUnitMale = 0
        self.countNoUnitSepMale = 0
        self.countNoUnitNoSepMale = 0


        #UNIT1
        #FEMALE, SEPSIS
        self.count1819WSepsisFU1 = 0                                         
        self.count20JahreWSepsisFU1 = 0
        self.count30JahreWSepsisFU1 = 0                    
        self.count40JahreWSepsisFU1 = 0
        self.count50JahreWSepsisFU1 = 0 
        self.count60JahreWSepsisFU1 = 0
        self.count70JahreWSepsisFU1 = 0 
        self.count80JahreWSepsisFU1 = 0
        #Female, NO SEPSIS
        self.count1819WOSepsisFU1 = 0                                          
        self.count20JahreWOSepsisFU1 = 0
        self.count30JahreWOSepsisFU1 = 0               
        self.count40JahreWOSepsisFU1 = 0
        self.count50JahreWOSepsisFU1 = 0  
        self.count60JahreWOSepsisFU1 = 0
        self.count70JahreWOSepsisFU1 = 0
        self.count80JahreWOSepsisFU1 = 0


        #UNIT1, MALE, SEPSIS, NoSepsis
        self.count1819WSepsisMU1 = 0                                      
        self.count20JahreWSepsisMU1 = 0
        self.count30JahreWSepsisMU1 = 0                 
        self.count40JahreWSepsisMU1 = 0
        self.count50JahreWSepsisMU1 = 0
        self.count60JahreWSepsisMU1 = 0
        self.count70JahreWSepsisMU1 = 0
        self.count80JahreWSepsisMU1 = 0
        self.count1819WOSepsisMU1 = 0                             
        self.count20JahreWOSepsisMU1 = 0
        self.count30JahreWOSepsisMU1 = 0                 
        self.count40JahreWOSepsisMU1 = 0
        self.count50JahreWOSepsisMU1 = 0
        self.count60JahreWOSepsisMU1 = 0
        self.count70JahreWOSepsisMU1 = 0
        self.count80JahreWOSepsisMU1 = 0

        #UNIT2
        self.count1819WSepsisFU2 = 0                                   
        self.count20JahreWSepsisFU2 = 0
        self.count30JahreWSepsisFU2 = 0        
        self.count40JahreWSepsisFU2 = 0
        self.count50JahreWSepsisFU2 = 0
        self.count60JahreWSepsisFU2 = 0
        self.count70JahreWSepsisFU2 = 0
        self.count80JahreWSepsisFU2 = 0
        #NoSepsis
        self.count1819WOSepsisFU2 = 0                             
        self.count20JahreWOSepsisFU2 = 0
        self.count30JahreWOSepsisFU2 = 0                 
        self.count40JahreWOSepsisFU2 = 0
        self.count50JahreWOSepsisFU2 = 0
        self.count60JahreWOSepsisFU2 = 0
        self.count70JahreWOSepsisFU2 = 0
        self.count80JahreWOSepsisFU2 = 0
        #MANN
        self.count1819WSepsisMU2 = 0                                     
        self.count20JahreWSepsisMU2 = 0
        self.count30JahreWSepsisMU2 = 0                 
        self.count40JahreWSepsisMU2 = 0
        self.count50JahreWSepsisMU2 = 0
        self.count60JahreWSepsisMU2 = 0
        self.count70JahreWSepsisMU2 =0
        self.count80JahreWSepsisMU2 = 0
        self.count1819WOSepsisMU2 = 0                              
        self.count20JahreWOSepsisMU2 = 0
        self.count30JahreWOSepsisMU2 = 0            
        self.count40JahreWOSepsisMU2 = 0
        self.count50JahreWOSepsisMU2 = 0
        self.count60JahreWOSepsisMU2 = 0
        self.count70JahreWOSepsisMU2 = 0
        self.count80JahreWOSepsisMU2 = 0



        #AgeNaN Frauen Sepsis
        self.count1819WSepsisFNaN = 0                                         
        self.count20JahreWSepsisFNaN = 0
        self.count30JahreWSepsisFNaN =0                  
        self.count40JahreWSepsisFNaN =0
        self.count50JahreWSepsisFNaN = 0
        self.count60JahreWSepsisFNaN = 0
        self.count70JahreWSepsisFNaN = 0
        self.count80JahreWSepsisFNaN = 0

        #AgeNaN Männer Sepsis
        self.count1819WSepsisMNaN = 0                                         
        self.count20JahreWSepsisMNaN = 0
        self.count30JahreWSepsisMNaN =0                  
        self.count40JahreWSepsisMNaN =0
        self.count50JahreWSepsisMNaN = 0
        self.count60JahreWSepsisMNaN = 0
        self.count70JahreWSepsisMNaN = 0
        self.count80JahreWSepsisMNaN = 0

        #AgeNaN Frauen No Sepsis
        self.count1819WOSepsisFNaN = 0                                         
        self.count20JahreWOSepsisFNaN = 0
        self.count30JahreWOSepsisFNaN =0                  
        self.count40JahreWOSepsisFNaN =0
        self.count50JahreWOSepsisFNaN = 0
        self.count60JahreWOSepsisFNaN = 0
        self.count70JahreWOSepsisFNaN = 0
        self.count80JahreWOSepsisFNaN = 0

        #AgeNaN Männer No Sepsis
        self.count1819WOSepsisMNaN = 0                                         
        self.count20JahreWOSepsisMNaN = 0
        self.count30JahreWOSepsisMNaN =0                  
        self.count40JahreWOSepsisMNaN =0
        self.count50JahreWOSepsisMNaN = 0
        self.count60JahreWOSepsisMNaN = 0
        self.count70JahreWOSepsisMNaN = 0
        self.count80JahreWOSepsisMNaN = 0

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
        self.extractAllBothUnits(file)
        #print("das ist file"+file)


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
            self.endResultAllGender.append(self.currentFileDataArray[i][35]);
            gender = self.currentFileDataArray[i][35]
        #delete duplicates
        self.endResultAllGender = list(dict.fromkeys(self.endResultAllGender))
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


    def extractAllBothUnits(self, file):
        allUnit1Female = 0
        allUnit1SepFemale = 0
        allUnit1NoSepFemale = 0
        
        allUnit2Female = 0
        allUnit2SepFemale = 0
        allUnit2NoSepFemale = 0
        
        noUnitFemale = 0
        noUnitSepFemale = 0
        noUnitNoSepFemale = 0

        allUnit1Male = 0
        allUnit1SepMale = 0
        allUnit1NoSepMale = 0

        allUnit2Male = 0
        allUnit2NoSepMale = 0
        allUnit2SepMale = 0
        
        noUnitMale = 0
        noUnitSepMale = 0
        noUnitNoSepMale = 0


        for i in range(1, len(self.currentFileDataArray)-1):
            if((self.currentFileDataArray[i][36] == '1') and (self.currentFileDataArray[i][37] == '0')):
               #print("Patient war in MICU")
               if(self.currentFileDataArray[i][35] =='0'):
                   #Frau
                   allUnit1Female = 1
                   #hasSepsis
                   if(self.currentFileDataArray[i][40]=='1\n'):
                       allUnit1SepFemale = 1
                   #hasNoSepsis
                   #if(self.currentFileDataArray[i][40]=='0\n'):
                       #allUnit1NoSepFemale = 1

               if(self.currentFileDataArray[i][35] =='1'):
                   #Mann
                   allUnit1Male = 1
                   #hasSepsis
                   if(self.currentFileDataArray[i][40]=='1\n'):
                       allUnit1SepMale = 1
                   #hasNoSepsis
                   #if(self.currentFileDataArray[i][40]=='0\n'):
                       #allUnit1NoSepMale = 1

            if((self.currentFileDataArray[i][36] == '0') and (self.currentFileDataArray[i][37] == '1')):
               #print("Patient war in SICU")
               if(self.currentFileDataArray[i][35] =='0'):
                   #Frau
                   allUnit2Female = 1
                   #hasSepsis
                   if(self.currentFileDataArray[i][40]=='1\n'):
                       allUnit2SepFemale = 1
                   #hasNoSepsis
                   #if(self.currentFileDataArray[i][40]=='0\n'):
                   #    allUnit2NoSepFemale = 1


               if(self.currentFileDataArray[i][35] =='1'):

                   #Mann
                   allUnit2Male = 1
                   #hasSepsis
                   if(self.currentFileDataArray[i][40]=='1\n'):
                       allUnit2SepMale = 1
                   #hasNoSepsis
                   #if(self.currentFileDataArray[i][40]=='0\n'):
                   #    allUnit2NoSepMale = 1

            if((self.currentFileDataArray[i][36] == 'NaN') and (self.currentFileDataArray[i][37] == 'NaN')):
               #print("Patient war in keine Intensivstation")
               if(self.currentFileDataArray[i][35] =='0'):
                   #Frau
                   noUnitFemale = 1
                   #Sepsis
                   if(self.currentFileDataArray[i][40]=='1\n'):
                       noUnitSepFemale = 1
                   #NoSepsis
                   #if(self.currentFileDataArray[i][40]=='0\n'):
                   #    noUnitNoSepFemale = 1

               if(self.currentFileDataArray[i][35] =='1'):
                   #Mann
                   noUnitMale = 1
                   #Sepsis
                   if(self.currentFileDataArray[i][40]=='1\n'):
                       noUnitSepMale = 1
                   #NoSepsis
                   #if(self.currentFileDataArray[i][40]=='0\n'):
                   #    noUnitNoSepMale = 1

        #Diagramm 1: Micu
        #Column 2: SICU
        #Column 3 : NaN
        #COLUMN:MICU
        if((self.currentFileDataArray[i][36] == '1') and (self.currentFileDataArray[i][37] == '0')):
            #unterscheide zwischen mann und frau
            #FRAU
            if( allUnit1Female == 1 and self.currentFileDataArray[i][35] == '0'):
                #Unterschied Sepsis
                self.countAllUnit1Female = self.countAllUnit1Female +1
                if(allUnit1SepFemale == 1):
                    self.countAllUnit1FemaleSepsis = self.countAllUnit1FemaleSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WSepsisFU1 = self.count1819WSepsisFU1+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWSepsisFU1 = self.count20JahreWSepsisFU1 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWSepsisFU1 = self.count30JahreWSepsisFU1+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWSepsisFU1 = self.count40JahreWSepsisFU1 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWSepsisFU1 = self.count50JahreWSepsisFU1 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWSepsisFU1 = self.count60JahreWSepsisFU1+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWSepsisFU1 = self.count70JahreWSepsisFU1+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWSepsisFU1 = self.count80JahreWSepsisFU1+1 
                #NoSepsis
                if(allUnit1SepFemale == 0):
                    self.countAllUnit1FemaleNoSepsis = self.countAllUnit1FemaleNoSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WOSepsisFU1 = self.count1819WOSepsisFU1+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWOSepsisFU1 = self.count20JahreWOSepsisFU1 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWOSepsisFU1 = self.count30JahreWOSepsisFU1+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWOSepsisFU1 = self.count40JahreWOSepsisFU1 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWOSepsisFU1 = self.count50JahreWOSepsisFU1 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWOSepsisFU1 = self.count60JahreWOSepsisFU1+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWOSepsisFU1 = self.count70JahreWOSepsisFU1+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWOSepsisFU1 = self.count80JahreWOSepsisFU1+1  

            #MANN
            if( allUnit1Male == 1 and self.currentFileDataArray[i][35] == '1'):
                self.countAllUnit1Male = self.countAllUnit1Male +1
                #Unterschied Sepsis, 
                if(allUnit1SepMale == 1):
                    self.countAllUnit1MaleSepsis = self.countAllUnit1MaleSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WSepsisMU1 = self.count1819WSepsisMU1+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWSepsisMU1 = self.count20JahreWSepsisMU1 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWSepsisMU1 = self.count30JahreWSepsisMU1+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWSepsisMU1 = self.count40JahreWSepsisMU1 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWSepsisMU1 = self.count50JahreWSepsisMU1 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWSepsisMU1 = self.count60JahreWSepsisMU1+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWSepsisMU1 = self.count70JahreWSepsisMU1+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWSepsisMU1 = self.count80JahreWSepsisMU1+1 
                if(noUnitSepMale == 0):
                    self.countAllUnit1MaleNoSepsis = self.countAllUnit1MaleNoSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WOSepsisMU1 = self.count1819WOSepsisMU1+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWOSepsisMU1 = self.count20JahreWOSepsisMU1 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWOSepsisMU1 = self.count30JahreWOSepsisMU1+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWOSepsisMU1 = self.count40JahreWOSepsisMU1 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWOSepsisMU1 = self.count50JahreWOSepsisMU1 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWOSepsisMU1 = self.count60JahreWOSepsisMU1+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWOSepsisMU1 = self.count70JahreWOSepsisMU1+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWOSepsisMU1 = self.count80JahreWOSepsisMU1+1 

        #SICU
        if((self.currentFileDataArray[i][36] == '0') and (self.currentFileDataArray[i][37] == '1')):
            #unterscheide zwischen mann und frau
            #FRAU
            if( allUnit2Female == 1 and self.currentFileDataArray[i][35] == '0'):
                self.countAllUnit2Female = self.countAllUnit2Female +1
                #Unterschied Sepsis, kein Sepsis
                if(allUnit2SepFemale == 1):
                    self.countAllUnit2FemaleSepsis = self.countAllUnit2FemaleSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WSepsisFU2 = self.count1819WSepsisFU2+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWSepsisFU2 = self.count20JahreWSepsisFU2 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWSepsisFU2 = self.count30JahreWSepsisFU2+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWSepsisFU2 = self.count40JahreWSepsisFU2 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWSepsisFU2 = self.count50JahreWSepsisFU2 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWSepsisFU2 = self.count60JahreWSepsisFU2+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWSepsisFU2 = self.count70JahreWSepsisFU2+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWSepsisFU2 = self.count80JahreWSepsisFU2+1 
                #NoSepsis
                if(allUnit2SepFemale == 0):
                    self.countAllUnit2FemaleNoSepsis = self.countAllUnit2FemaleNoSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WOSepsisFU2 = self.count1819WOSepsisFU2+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWOSepsisFU2 = self.count20JahreWOSepsisFU2 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWOSepsisFU2 = self.count30JahreWOSepsisFU2+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWOSepsisFU2 = self.count40JahreWOSepsisFU2 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWOSepsisFU2 = self.count50JahreWOSepsisFU2 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWOSepsisFU2 = self.count60JahreWOSepsisFU2+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWOSepsisFU2 = self.count70JahreWOSepsisFU2+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWOSepsisFU2 = self.count80JahreWOSepsisFU2+1  
                    

            #MANN
            if( allUnit2Male == 1 and self.currentFileDataArray[i][35] == '1'):
                #Unterschied Sepsis, kein Sepsis
                self.countAllUnit2Male = self.countAllUnit2Male +1
                if(allUnit2SepMale == 1):
                    self.countAllUnit2MaleSepsis = self.countAllUnit2MaleSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WSepsisMU2 = self.count1819WSepsisMU2+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWSepsisMU2 = self.count20JahreWSepsisMU2 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWSepsisMU2 = self.count30JahreWSepsisMU2+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWSepsisMU2 = self.count40JahreWSepsisMU2 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWSepsisMU2 = self.count50JahreWSepsisMU2 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWSepsisMU2 = self.count60JahreWSepsisMU2+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWSepsisMU2 = self.count70JahreWSepsisMU2+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWSepsisMU2 = self.count80JahreWSepsisMU2+1 
                if(allUnit2SepMale == 0):
                    self.countAllUnit2MaleNoSepsis = self.countAllUnit2MaleNoSepsis +1
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WOSepsisMU2 = self.count1819WOSepsisMU2+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWOSepsisMU2 = self.count20JahreWOSepsisMU2 +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWOSepsisMU2 = self.count30JahreWOSepsisMU2+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWOSepsisMU2 = self.count40JahreWOSepsisMU2 +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWOSepsisMU2 = self.count50JahreWOSepsisMU2 +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWOSepsisMU2 = self.count60JahreWOSepsisMU2+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWOSepsisMU2 = self.count70JahreWOSepsisMU2+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWOSepsisMU2 = self.count80JahreWOSepsisMU2+1 



        #NaN
        if((self.currentFileDataArray[i][36] == 'NaN') and (self.currentFileDataArray[i][37] == 'NaN')):
            #unterscheide zwischen mann und frau
            #FRAU
            if( noUnitFemale == 1 and self.currentFileDataArray[i][35] == '0'):
                #Unterschied Sepsis, kein Sepsis
                self.countNoUnitFemale = self.countNoUnitFemale +1
                #Sepsis
                if(noUnitSepFemale == 1):
                    self.countNoUnitSepFemale = self.countNoUnitSepFemale +1
                    print("Das ist file Frauen NaN:"+file)
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WSepsisFNaN = self.count1819WSepsisFNaN+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWSepsisFNaN = self.count20JahreWSepsisFNaN +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWSepsisFNaN = self.count30JahreWSepsisFNaN+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWSepsisFNaN = self.count40JahreWSepsisFNaN +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWSepsisFNaN = self.count50JahreWSepsisFNaN +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWSepsisFNaN = self.count60JahreWSepsisFNaN+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWSepsisFNaN = self.count70JahreWSepsisFNaN+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWSepsisFNaN = self.count80JahreWSepsisFNaN+1 
                #NoSepsis
                if(noUnitSepFemale == 0):
                    self.countNoUnitNoSepFemale = self.countNoUnitNoSepFemale +1
                    print("Das ist file Frauen NaN:"+file)
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WOSepsisFNaN = self.count1819WOSepsisFNaN+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWOSepsisFNaN = self.count20JahreWOSepsisFNaN +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWOSepsisFNaN = self.count30JahreWOSepsisFNaN+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWOSepsisFNaN = self.count40JahreWOSepsisFNaN +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWOSepsisFNaN = self.count50JahreWOSepsisFNaN +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWOSepsisFNaN = self.count60JahreWOSepsisFNaN+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWOSepsisFNaN = self.count70JahreWOSepsisFNaN+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWOSepsisFNaN = self.count80JahreWOSepsisFNaN+1  
                    
            #MANN
            if( noUnitMale == 1 and self.currentFileDataArray[i][35] == '1'):
                #Unterschied Sepsis, kein Sepsis
                self.countNoUnitMale = self.countNoUnitMale +1
                if(noUnitSepMale == 1):
                    self.countNoUnitSepMale = self.countNoUnitSepMale +1
                    print("Das ist file Männer NaN:"+file)
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WSepsisMNaN = self.count1819WSepsisMNaN+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWSepsisMNaN = self.count20JahreWSepsisMNaN +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWSepsisMNaN = self.count30JahreWSepsisMNaN+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWSepsisMNaN = self.count40JahreWSepsisMNaN +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWSepsisMNaN = self.count50JahreWSepsisMNaN +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWSepsisMNaN = self.count60JahreWSepsisMNaN+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWSepsisMNaN = self.count70JahreWSepsisMNaN+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWSepsisMNaN = self.count80JahreWSepsisMNaN+1 
                if(noUnitSepMale == 0):
                    self.countNoUnitNoSepMale = self.countNoUnitNoSepMale +1
                    print("Das ist file Männer NaN:"+file)
                    if(float(self.currentFileDataArray[i][34]) < 20):
                        self.count1819WOSepsisMNaN = self.count1819WOSepsisMNaN+1                                           
                    if(30 > float(self.currentFileDataArray[i][34]) >= 20):
                        self.count20JahreWOSepsisMNaN = self.count20JahreWOSepsisMNaN +1
                    if(40 > float(self.currentFileDataArray[i][34]) >= 30):
                        self.count30JahreWOSepsisMNaN = self.count30JahreWOSepsisMNaN+1                    
                    if(50 > float(self.currentFileDataArray[i][34]) >= 40):
                        self.count40JahreWOSepsisMNaN = self.count40JahreWOSepsisMNaN +1
                    if(60 > float(self.currentFileDataArray[i][34]) >= 50):
                        self.count50JahreWOSepsisMNaN = self.count50JahreWOSepsisMNaN +1  
                    if(70 > float(self.currentFileDataArray[i][34]) >= 60):
                        self.count60JahreWOSepsisMNaN = self.count60JahreWOSepsisMNaN+1
                    if(80 > float(self.currentFileDataArray[i][34]) >= 70):
                        self.count70JahreWOSepsisMNaN = self.count70JahreWOSepsisMNaN+1  
                    if(float(self.currentFileDataArray[i][34]) >= 80):
                        self.count80JahreWOSepsisMNaN = self.count80JahreWOSepsisMNaN+1 

    def extractAllIculos(self):
        """ Dauer des Aufenthalts auf der Intensivstation (Stunden seit der Aufnahme auf der Intensivstation)"""
        allIculos = []
        for i in range(1, len(self.currentFileDataArray)-1):
            self.endResultAllAllIculos.append(self.currentFileDataArray[i][39]);
        #delete duplicates
        self.endResultAllAllIculos = list(dict.fromkeys(self.endResultAllAllIculos))
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


            self.endResultAllSepsisLabel.append(self.currentFileDataArray[i][40]);
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


    def makeGenderDiagram(self):
        chart_data = pd.DataFrame(
        np.array([[ 1189, 16581],[ 1738, 20828]]),
        columns=["Sepsis", "no Sepsis"], index=['female','male'])
        st.bar_chart(chart_data)

    def makeAgeGenderDiagram(self):
        chart_data = pd.DataFrame(
        np.array([[ 3, 104, 9, 113],[ 57,769,74, 813], [62,1114, 96, 1165], [129, 1921, 224,2523], [193,2871,342,4286], [264,3634,425,5209], [298, 3513,366, 4392], [183,2655,202,2327]]),
        columns=["Female had Sepsis", "Female had no Sepsis", "Male had Sepsis", "Male had no Sepsis"], index =['under the age of 20', '20-29 year olds', '30-39 year olds', '40-49 year olds', '50-59 year olds', '60-69 year olds', '70-79 year olds','over 80 years'])

        st.bar_chart(chart_data, height=600, width=900)

    
def decideDiagram(intToDecide, datasetInt):
    #SepsisGender
    if( intToDecide == 1):
        print("Das ist die Entscheidung {}", intToDecide)
        #checkwhichdataset 1
        if(datasetInt == 1):
            print("datasetInt: {}", 1)
            A1 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
            A1.getFileNames()

        #dataset 2
        if(datasetInt == 2):
            print("datasetInt: {}", 2)
            A2 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")

        #both dataset
        if(datasetInt == 3):
            print("datasetInt: {}", 3)
            A1 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
            A2 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")


    #SepsisGenderAge
    if( intToDecide == 2):
        print("Das ist die Entscheidung {}", intToDecide)    
        
    #SepsisGenderAgeUnit
    if( intToDecide == 3):
        print("Das ist die Entscheidung {}", intToDecide)
    #NoSepsisGenderAgeUnit
    if( intToDecide == 4):
        print("Das ist die Entscheidung {}", intToDecide)    

A1 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
#A1.makeGenderDiagram()

#A1.makeAgeGenderDiagram()
A2 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
A1.getFileNames()
A2.getFileNames()
print("Das sind MICU Unit 1 alle Frauen: " + str(A1.countAllUnit1Female+ A2.countAllUnit1Female))
print("Das sind MICU Unit 1 alle Frauen mit Sepsis: " + str(A1.countAllUnit1FemaleSepsis+ A2.countAllUnit1FemaleSepsis))
print("Das sind MICU Unit 1 alle Frauen ohne Sepsis: " + str((A1.countAllUnit1Female+ A2.countAllUnit1Female)-(A1.countAllUnit1FemaleSepsis+ A2.countAllUnit1FemaleSepsis) ) )
print("Das ist MICU Frau unter 20 mit Sepsis: "+ str(A1.count1819WSepsisFU1 + A2.count1819WSepsisFU1))
print("Das ist MICU Frauen  20 - 29 mit Sepsis: "+ str(A1.count20JahreWSepsisFU1 + A2.count20JahreWSepsisFU1))
print("Das ist MICU Frauen 30-39 mit Sepsis: "+str(A1.count30JahreWSepsisFU1 + A2.count30JahreWSepsisFU1))                                
print("Das ist MICU Frauen 40-49 mit Sepsis: "+str(A1.count40JahreWSepsisFU1 + A2.count40JahreWSepsisFU1 ))                                
print("Das ist MICU Frauen 50-59 mit Sepsis: "+str(A1.count50JahreWSepsisFU1 + A2.count50JahreWSepsisFU1) )                                
print("Das ist MICU Frauen 60-69 mit Sepsis: "+str(A1.count60JahreWSepsisFU1 + A2.count60JahreWSepsisFU1 ))                               
print("Das ist MICU Frauen 70-79 mit Sepsis: "+str(A1.count70JahreWSepsisFU1 + A2.count70JahreWSepsisFU1))                                
print("Das ist MICU Frauen 80 größer mit Sepsis: "+str(A1.count80JahreWSepsisFU1 + A2.count80JahreWSepsisFU1))                              
#
print("Das ist MICU Frauen unter 20 ohne Sepsis: "+ str(A1.count1819WOSepsisFU1 + A2.count1819WOSepsisFU1))
print("Das ist MICU Frauen  20 - 29 ohne Sepsis: "+ str(A1.count20JahreWOSepsisFU1 + A2.count20JahreWOSepsisFU1))
print("Das ist MICU Frauen 30-39 ohne Sepsis: "+str(A1.count30JahreWOSepsisFU1 + A2.count30JahreWOSepsisFU1))                                
print("Das ist MICU Frauen 40-49 ohne Sepsis:"+str(A1.count40JahreWOSepsisFU1 + A2.count40JahreWOSepsisFU1))                                
print("Das ist MICU Frauen 50-59 ohne Sepsis: "+str(A1.count50JahreWOSepsisFU1 + A2.count50JahreWOSepsisFU1) )                                
print("Das ist MICU Frauen 60-69 ohne Sepsis: "+str(A1.count60JahreWOSepsisFU1 + A2.count60JahreWOSepsisFU1))                               
print("Das ist MICU Frauen 70-79 ohne Sepsis: "+str(A1.count70JahreWOSepsisFU1 + A2.count70JahreWOSepsisFU1 ))                                
print("Das ist MICU Frauen 80 größer ohne Sepsis: "+str(A1.count80JahreWOSepsisFU1 + A2.count80JahreWOSepsisFU1 ))                                          
#
print("Das sind MICU Unit 1 alle Männer: " + str(A1.countAllUnit1Male+ A2.countAllUnit1Male))
print("Das sind MICU Unit 1 alle Männer mit Sepsis: " + str(A1.countAllUnit1MaleSepsis+ A2.countAllUnit1MaleSepsis))
print("Das sind MICU Unit 1 alle Männer ohne Sepsis: " + str((A1.countAllUnit1Male+ A2.countAllUnit1Male)-(A1.countAllUnit1MaleSepsis+ A2.countAllUnit1MaleSepsis) )   )
print("Das ist MICU Männer unter 20 mit Sepsis: "+ str(A1.count1819WSepsisMU1 + A2.count1819WSepsisMU1))
print("Das ist MICU Männer  20 - 29 mit Sepsis: "+ str(A1.count20JahreWSepsisMU1 + A2.count20JahreWSepsisMU1))
print("Das ist MICU Männer 30-39 mit Sepsis: "+str(A1.count30JahreWSepsisMU1 + A2.count30JahreWSepsisMU1))                                
print("Das ist MICU Männer 40-49 mit Sepsis: "+str(A1.count40JahreWSepsisMU1 + A2.count40JahreWSepsisMU1 ))                                
print("Das ist MICU Männer 50-59 mit Sepsis: "+str(A1.count50JahreWSepsisMU1 + A2.count50JahreWSepsisMU1) )                                
print("Das ist MICU Männer 60-69 mit Sepsis: "+str(A1.count60JahreWSepsisMU1 + A2.count60JahreWSepsisMU1))                               
print("Das ist MICU Männer 70-79 mit Sepsis: "+str(A1.count70JahreWSepsisMU1 + A2.count70JahreWSepsisMU1 ))                                
print("Das ist MICU Männer 80 größer mit Sepsis: "+str(A1.count80JahreWSepsisMU1 + A2.count80JahreWSepsisMU1))                              
#
print("Das ist MICU Männer unter 20 ohne Sepsis: "+ str(A1.count1819WOSepsisMU1 + A2.count1819WOSepsisMU1))
print("Das ist MICU Männer  20 - 29 ohne Sepsis: "+ str(A1.count20JahreWOSepsisMU1 + A2.count20JahreWOSepsisMU1))
print("Das ist MICU Männer 30-39 ohne Sepsis: "+str(A1.count30JahreWOSepsisMU1 + A2.count30JahreWOSepsisMU1))                                
print("Das ist MICU Männer 40-49 ohne Sepsis: "+str(A1.count40JahreWOSepsisMU1 + A2.count40JahreWOSepsisMU1))                                
print("Das ist MICU Männer 50-59 ohne Sepsis: "+str(A1.count50JahreWOSepsisMU1 + A2.count50JahreWOSepsisMU1) )                                
print("Das ist MICU Männer 60-69 ohne Sepsis: "+str(A1.count60JahreWOSepsisMU1 + A2.count60JahreWOSepsisMU1))                               
print("Das ist MICU Männer 70-79 ohne Sepsis: "+str(A1.count70JahreWOSepsisMU1 + A2.count70JahreWOSepsisMU1))                                
print("Das ist MICU Männer 80 größer ohne Sepsis: "+str(A1.count80JahreWOSepsisMU1 + A2.count80JahreWOSepsisMU1))                              
#                              

print("Das sind MICU Unit 2 alle Frauen: " + str(A1.countAllUnit2Female+ A2.countAllUnit2Female))
print("Das sind SICU Unit 2 alle Frauen mit Sepsis: " + str(A1.countAllUnit2FemaleSepsis+ A2.countAllUnit2FemaleSepsis))
print("Das sind SICU Unit 2 alle Frauen ohne Sepsis: " + str((A1.countAllUnit2Female+ A2.countAllUnit2Female)-(A1.countAllUnit2FemaleSepsis+ A2.countAllUnit2FemaleSepsis) )  )
print("Das ist SICU Frau unter 20 mit Sepsis: "+ str(A1.count1819WSepsisFU2 + A2.count1819WSepsisFU2))
print("Das ist SICU Frauen  20 - 29 mit Sepsis: "+ str(A1.count20JahreWSepsisFU2 + A2.count20JahreWSepsisFU2))
print("Das ist SICU Frauen 30-39 mit Sepsis: "+str(A1.count30JahreWSepsisFU2 + A2.count30JahreWSepsisFU2))                                
print("Das ist SICU Frauen 40-49 mit Sepsis: "+str(A1.count40JahreWSepsisFU2 + A2.count40JahreWSepsisFU2))                                
print("Das ist SICU Frauen 50-59 mit Sepsis: "+str(A1.count50JahreWSepsisFU2 + A2.count50JahreWSepsisFU2) )                                
print("Das ist SICU Frauen 60-69 mit Sepsis: "+str(A1.count60JahreWSepsisFU2 + A2.count60JahreWSepsisFU2))                               
print("Das ist SICU Frauen 70-79 mit Sepsis: "+str(A1.count70JahreWSepsisFU2 + A2.count70JahreWSepsisFU2))                                
print("Das ist SICU Frauen 80 größer mit Sepsis: "+str(A1.count80JahreWSepsisFU2 + A2.count80JahreWSepsisFU2))                              
#
print("Das ist SICU Frauen unter 20 ohne Sepsis: "+ str(A1.count1819WOSepsisFU2 + A2.count1819WOSepsisFU2))
print("Das ist SICU Frauen  20 - 29 ohne Sepsis: "+ str(A1.count20JahreWOSepsisFU2 + A2.count20JahreWOSepsisFU2))
print("Das ist SICU Frauen 30-39 ohne Sepsis: "+str(A1.count30JahreWOSepsisFU2 + A2.count30JahreWOSepsisFU2))                                
print("Das ist SICU Frauen 40-49 ohne Sepsis: "+str(A1.count40JahreWOSepsisFU2 + A2.count40JahreWOSepsisFU2))                                
print("Das ist SICU Frauen 50-59 ohne Sepsis: "+str(A1.count50JahreWOSepsisFU2 + A2.count50JahreWOSepsisFU2) )                                
print("Das ist SICU Frauen 60-69 ohne Sepsis: "+str(A1.count60JahreWOSepsisFU2 + A2.count60JahreWOSepsisFU2))                               
print("Das ist SICU Frauen 70-79 ohne Sepsis: "+str(A1.count70JahreWOSepsisFU2 + A2.count70JahreWOSepsisFU2))                                
print("Das ist SICU Frauen 80 größer ohne Sepsis: "+str(A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2)) 
#

print("Das sind SICU Unit 2 alle Männer: " + str(A1.countAllUnit2Male+ A2.countAllUnit2Male))
print("Das sind SICU Unit 2 alle Männer mit Sepsis: " + str(A1.countAllUnit2MaleSepsis+ A2.countAllUnit2MaleSepsis))
print("Das sind SICU Unit 2 alle Männer ohne Sepsis: " + str((A1.countAllUnit2Male+ A2.countAllUnit2Male)-(A1.countAllUnit2MaleSepsis+ A2.countAllUnit2MaleSepsis) )   )
#
print("Das ist SICU Mann unter 20 mit Sepsis: "+ str(A1.count1819WSepsisMU2 + A2.count1819WSepsisMU2))
print("Das ist SICU Männer  20 - 29 mit Sepsis: "+ str(A1.count20JahreWSepsisMU2 + A2.count20JahreWSepsisMU2))
print("Das ist SICU Männer 30-39 mit Sepsis: "+str(A1.count30JahreWSepsisMU2 + A2.count30JahreWSepsisMU2))                                
print("Das ist SICU Männer 40-49 mit Sepsis: "+str(A1.count40JahreWSepsisMU2 + A2.count40JahreWSepsisMU2))                                
print("Das ist SICU Männer 50-59 mit Sepsis: "+str(A1.count50JahreWSepsisMU2 + A2.count50JahreWSepsisMU2) )                                
print("Das ist SICU Männer 60-69 mit Sepsis: "+str(A1.count60JahreWSepsisMU2 + A2.count60JahreWSepsisMU2))                               
print("Das ist SICU Männer 70-79 mit Sepsis: "+str(A1.count70JahreWSepsisMU2 + A2.count70JahreWSepsisMU2))                                
print("Das ist SICU Männer 80 größer mit Sepsis: "+str(A1.count80JahreWSepsisMU2 + A2.count80JahreWSepsisMU2))                              
#
print("Das ist SICU Männer unter 20 ohne Sepsis: "+ str(A1.count1819WOSepsisMU2 + A2.count1819WOSepsisMU2))
print("Das ist SICU Männer  20 - 29 ohne Sepsis: "+ str(A1.count20JahreWOSepsisMU2 + A2.count20JahreWOSepsisMU2))
print("Das ist SICU Männer 30-39 ohne Sepsis: "+str(A1.count30JahreWOSepsisMU2 + A2.count30JahreWOSepsisMU2))                                
print("Das ist SICU Männer 40-49 ohne Sepsis: "+str(A1.count40JahreWOSepsisMU2 + A2.count40JahreWOSepsisMU2))                                
print("Das ist SICU Männer 50-59 ohne Sepsis: "+str(A1.count50JahreWOSepsisMU2 + A2.count50JahreWOSepsisMU2) )                                
print("Das ist SICU Männer 60-69 ohne Sepsis: "+str(A1.count60JahreWOSepsisMU2 + A2.count60JahreWOSepsisMU2))                               
print("Das ist SICU Männer 70-79 ohne Sepsis: "+str(A1.count70JahreWOSepsisMU2 + A2.count70JahreWOSepsisMU2))                                
print("Das ist SICU Männer 80 größer ohne Sepsis: "+str(A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2)) 

print("Das sind keine Units alle Frauen: " + str(A1.countNoUnitFemale+ A2.countNoUnitFemale))
print("Das sind keine Units alle Frauen mit Sepsis: " + str(A1.countNoUnitSepFemale + A2.countNoUnitSepFemale))
print("Das sind keine Units alle Frauen ohne Sepsis: " + str((A1.countNoUnitFemale + A2.countNoUnitFemale)-(A1.countNoUnitSepFemale+ A2.countNoUnitSepFemale))   )
#
print("Das ist keine Units Frau unter 20 mit Sepsis: "+ str(A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN))
print("Das ist keine Units Frauen  20 - 29 mit Sepsis: "+ str(A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN))
print("Das ist keine Units Frauen 30-39 mit Sepsis: "+str(A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN))                                
print("Das ist keine Units Frauen 40-49 mit Sepsis: "+str(A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN))                                
print("Das ist keine Units Frauen 50-59 mit Sepsis: "+str(A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN) )                                
print("Das ist keine Units Frauen 60-69 mit Sepsis: "+str(A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN))                               
print("Das ist keine Units Frauen 70-79 mit Sepsis: "+str(A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN))                                
print("Das ist keine Units Frauen 80 größer mit Sepsis: "+str(A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN))                              
#
print("Das ist keine Units Frauen unter 20 ohne Sepsis: "+ str(A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN))
print("Das ist keine Units Frauen  20 - 29 ohne Sepsis: "+ str(A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN))
print("Das ist keine Units Frauen 30-39 ohne Sepsis: "+str(A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN))                                
print("Das ist keine Units Frauen 40-49 ohne Sepsis: "+str(A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN))                                
print("Das ist keine Units Frauen 50-59 ohne Sepsis: "+str(A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN) )                                
print("Das ist keine Units Frauen 60-69 ohne Sepsis: "+str(A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN))                               
print("Das ist keine Units Frauen 70-79 ohne Sepsis: "+str(A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN))                                
print("Das ist keine Units Frauen 80 größer ohne Sepsis: "+str(A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN))                     
  

print("Das sind keine Units alle Männer: " + str(A1.countNoUnitMale+ A2.countNoUnitMale))
print("Das sind keine Units alle Männer mit Sepsis: " + str(A1.countNoUnitSepMale+ A2.countNoUnitSepMale))
print("Das sind keine Units alle Männer ohne Sepsis: " + str((A1.countNoUnitMale+ A2.countNoUnitMale) - (A1.countNoUnitSepMale+ A2.countNoUnitSepMale))   )
#
print("Das ist keine Units Mann unter 20 mit Sepsis: "+ str(A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN))
print("Das ist keine Units Männer  20 - 29 mit Sepsis: "+ str(A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN))
print("Das ist keine Units Männer 30-39 mit Sepsis: "+str(A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN))                                
print("Das ist keine Units Männer 40-49 mit Sepsis: "+str(A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN))                                
print("Das ist keine Units Männer 50-59 mit Sepsis: "+str(A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN ) )                                
print("Das ist keine Units Männer 60-69 mit Sepsis: "+str(A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN))                               
print("Das ist keine Units Männer 70-79 mit Sepsis: "+str(A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN))                                
print("Das ist keine Units Männer 80 größer mit Sepsis: "+str(A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN))                              
#
print("Das ist keine Units Männer unter 20 ohne Sepsis: "+ str(A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN))
print("Das ist keine Units Männer  20 - 29 ohne Sepsis: "+ str(A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN))
print("Das ist keine Units Männer 30-39 ohne Sepsis: "+str(A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN))                                
print("Das ist keine Units Männer 40-49 ohne Sepsis: "+str(A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN))                                
print("Das ist keine Units Männer 50-59 ohne Sepsis: "+str(A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN) )                                
print("Das ist keine Units Männer 60-69 ohne Sepsis: "+str(A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN))                               
print("Das ist keine Units Männer 70-79 ohne Sepsis: "+str(A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN))                                
print("Das ist keine Units Männer 80 größer ohne Sepsis: "+str(A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN))   

#Chart
#Sepsis
chart_data = pd.DataFrame(
    np.array([
        [1, 3, 23, 21, 30, 35, 43, 63, 77,101, 90, 137, 102, 110, 62, 67],
        [0, 2, 12, 8, 10, 16, 28, 54, 36, 76, 65, 110, 62, 88, 37, 43],
        [2, 4, 22, 45, 22, 45, 58, 107, 80, 165, 109, 178, 134, 168, 84, 92]
        ]),
    columns=['female under 20 Sepsis','male under 20 Sepsis', 'female between 20 -29 Sepsis', 'male between 20-29 Sepsis', 'female between 30-39 Sepsis', 'male between 30-39 Sepsis','female between 40 -49 Sepsis', 'male between 40 -49 Sepsis','female between 50-59 Sepsis' ,'male between 50-59 Sepsis', 'female between 60-69 Sepsis','male between 60-69 Sepsis', 'female between 70-79 Sepsis','male between 70-79 Sepsis', 'over 80 female Sepsis', 'over 80 male Sepsis'], 
    index=["M-ICU", "S-ICU", "NaN-ICU"])

st.bar_chart(chart_data)


#Chart
#NoSepsis
chart_data = pd.DataFrame(
    np.array([
        #MICU
        [37, 27, 332, 287, 407, 471, 626, 853, 921, 1274, 1120, 1387, 1082, 1294, 937, 784],
        #SICU
        [23, 13, 144, 137, 246, 258, 384, 698, 729, 1578, 1132, 2254, 1114, 1765, 631, 699],
        #NaN
        [44, 76, 293, 410, 461, 471, 911, 1035, 1221, 1535, 1382, 1705, 1317, 1443, 1087, 911]
        ]),
    columns=['female under 20 No Sepsis','male under 20 No Sepsis', 'female between 20 -29 No Sepsis', 'male between 20-29 No Sepsis', 'female between 30-39 No Sepsis', 'male between 30-39 No Sepsis','female between 40 -49 No Sepsis', 'male between 40 -49 No Sepsis','female between 50-59 No Sepsis' ,'male between 50-59 No Sepsis', 'female between 60-69 No Sepsis','male between 60-69 No Sepsis', 'female between 70-79 No Sepsis','male between 70-79 No Sepsis', 'over 80 female No Sepsis', 'over 80 male No Sepsis'], 
    index=["M-ICU", "S-ICU", "NaN-ICU"])

st.bar_chart(chart_data)




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

