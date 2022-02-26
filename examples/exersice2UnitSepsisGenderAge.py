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


class CheckForUnitSepsisGenderAge():
    def __init__(self, dataPath=""):
        self.dataPath = dataPath
        #hasAllFileNamesInAnArray
        self.fileNames = []
        #currentFileData Array
        self.currentFileDataArray = []

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
        self.extractAllBothUnits(file)


        
   

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
                if(allUnit1SepMale == 0):
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




    def makeUnitSepsisAgeGenderDiagram(self, verarbeitetesListList):
        #Chart
        #Sepsis
        #[
        #    [1, 3, 23, 21, 30, 35, 43, 63, 77,101, 90, 137, 102, 110, 62, 67],
        #    [0, 2, 12, 8, 10, 16, 28, 54, 36, 76, 65, 110, 62, 88, 37, 43],
        #    [2, 4, 22, 45, 22, 45, 58, 107, 80, 165, 109, 178, 134, 168, 84, 92]
        #    ]


        chart_data = pd.DataFrame(
            np.array(verarbeitetesListList),
        columns=['female under 20 Sepsis','male under 20 Sepsis', 'female between 20 -29 Sepsis', 'male between 20-29 Sepsis', 'female between 30-39 Sepsis', 'male between 30-39 Sepsis','female between 40 -49 Sepsis', 'male between 40 -49 Sepsis','female between 50-59 Sepsis' ,'male between 50-59 Sepsis', 'female between 60-69 Sepsis','male between 60-69 Sepsis', 'female between 70-79 Sepsis','male between 70-79 Sepsis', 'over 80 female Sepsis', 'over 80 male Sepsis'], 
        index=["M-ICU", "S-ICU", "NaN-ICU"])
        st.bar_chart(chart_data)

    def makeUnitNoSepsisAgeGenderDiagram(self, verarbeitetesListList):
        #Chart
        #Sepsis
        #[
        #    [1, 3, 23, 21, 30, 35, 43, 63, 77,101, 90, 137, 102, 110, 62, 67],
        #    [0, 2, 12, 8, 10, 16, 28, 54, 36, 76, 65, 110, 62, 88, 37, 43],
        #    [2, 4, 22, 45, 22, 45, 58, 107, 80, 165, 109, 178, 134, 168, 84, 92]
        #    ]
        chart_data = pd.DataFrame(
            np.array(verarbeitetesListList),
        columns=['female under 20 No Sepsis','male under 20 No Sepsis', 'female between 20 -29 No Sepsis', 'male between 20-29 No Sepsis', 'female between 30-39 No Sepsis', 'male between 30-39 No Sepsis','female between 40 -49 No Sepsis', 'male between 40 -49 No Sepsis','female between 50-59 No Sepsis' ,'male between 50-59 No Sepsis', 'female between 60-69 No Sepsis','male between 60-69 No Sepsis', 'female between 70-79 No Sepsis','male between 70-79 No Sepsis', 'over 80 female No Sepsis', 'over 80 male No Sepsis'], 
        index=["M-ICU", "S-ICU", "NaN-ICU"])
        st.bar_chart(chart_data)


    def makeMICUDiagram(self, sizes):

                # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'MICU: Woman under the Age of 20 With Sepsis', 'MICU: Woman under the Age of 20 Without Sepsis', 'MICU: Woman between 20-29 With Sepsis', 'MICU: Woman between 20-29 without Sepsis','MICU: Woman between 30-39 With Sepsis', 'MICU: Woman between 30-39 without Sepsis','MICU: Woman between 40-49 With Sepsis', 'MICU: Woman between 40-49 without Sepsis','MICU: Woman between 50-59 With Sepsis', 'MICU: Woman between 50-59 without Sepsis','MICU: Woman between 60-69 With Sepsis', 'MICU: Woman between 60-69 without Sepsis','MICU: Woman between 70-79 With Sepsis', 'MICU: Woman between 70-79 without Sepsis','MICU: Woman older 80 With Sepsis', 'MICU: Woman older 80 without Sepsis','Man under the Age of 20 With Sepsis', 'MICU: Men under the Age of 20 Without Sepsis', 'MICU: Men between 20-29 With Sepsis', 'MICU: Men between 20-29 without Sepsis','MICU: Men between 30-39 With Sepsis', 'MICU: Men between 30-39 without Sepsis','MICU: Men between 40-49 With Sepsis', 'MICU: Men between 40-49 without Sepsis','MICU: Men between 50-59 With Sepsis', 'MICU: Men between 50-59 without Sepsis','MICU: Men between 60-69 With Sepsis', 'MICU: Men between 60-69 without Sepsis','MICU: Men between 70-79 With Sepsis', 'MICU: Men between 70-79 without Sepsis','MICU: Men older 80 With Sepsis', 'MICU: Men older 80 without Sepsis',

        fig1, ax1 = st.columns(2)
        fig2 = px.pie(sizes, labels=labels, values=sizes, names=labels)
        ax1.write(fig2)

    def makeSICUDiagram(self, sizes):

                # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'SICU: Woman under the Age of 20 With Sepsis', 'SICU: Woman under the Age of 20 Without Sepsis', 'SICU: Woman between 20-29 With Sepsis', 'SICU: Woman between 20-29 without Sepsis','SICU: Woman between 30-39 With Sepsis', 'SICU: Woman between 30-39 without Sepsis','SICU: Woman between 40-49 With Sepsis', 'SICU: Woman between 40-49 without Sepsis','SICU: Woman between 50-59 With Sepsis', 'SICU: Woman between 50-59 without Sepsis','SICU: Woman between 60-69 With Sepsis', 'SICU: Woman between 60-69 without Sepsis','SICU: Woman between 70-79 With Sepsis', 'SICU: Woman between 70-79 without Sepsis','SICU: Woman older 80 With Sepsis', 'SICU: Woman older 80 without Sepsis','Man under the Age of 20 With Sepsis', 'SICU: Men under the Age of 20 Without Sepsis', 'SICU: Men between 20-29 With Sepsis', 'SICU: Men between 20-29 without Sepsis','SICU: Men between 30-39 With Sepsis', 'SICU: Men between 30-39 without Sepsis','SICU: Men between 40-49 With Sepsis', 'SICU: Men between 40-49 without Sepsis','SICU: Men between 50-59 With Sepsis', 'SICU: Men between 50-59 without Sepsis','SICU: Men between 60-69 With Sepsis', 'SICU: Men between 60-69 without Sepsis','SICU: Men between 70-79 With Sepsis', 'SICU: Men between 70-79 without Sepsis','SICU: Men older 80 With Sepsis', 'SICU: Men older 80 without Sepsis',

        fig1, ax1 = st.columns(2)
        fig2 = px.pie(sizes, labels=labels, values=sizes, names=labels)
        ax1.write(fig2)

    def makeNaNDiagram(self, sizes):

                # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'NaN: Woman under the Age of 20 With Sepsis', 'NaN: Woman under the Age of 20 Without Sepsis', 'NaN: Woman between 20-29 With Sepsis', 'NaN: Woman between 20-29 without Sepsis','NaN: Woman between 30-39 With Sepsis', 'NaN: Woman between 30-39 without Sepsis','NaN: Woman between 40-49 With Sepsis', 'NaN: Woman between 40-49 without Sepsis','NaN: Woman between 50-59 With Sepsis', 'NaN: Woman between 50-59 without Sepsis','NaN: Woman between 60-69 With Sepsis', 'NaN: Woman between 60-69 without Sepsis','NaN: Woman between 70-79 With Sepsis', 'NaN: Woman between 70-79 without Sepsis','NaN: Woman older 80 With Sepsis', 'NaN: Woman older 80 without Sepsis','Man under the Age of 20 With Sepsis', 'NaN: Men under the Age of 20 Without Sepsis', 'NaN: Men between 20-29 With Sepsis', 'NaN: Men between 20-29 without Sepsis','NaN: Men between 30-39 With Sepsis', 'NaN: Men between 30-39 without Sepsis','NaN: Men between 40-49 With Sepsis', 'NaN: Men between 40-49 without Sepsis','NaN: Men between 50-59 With Sepsis', 'NaN: Men between 50-59 without Sepsis','NaN: Men between 60-69 With Sepsis', 'NaN: Men between 60-69 without Sepsis','NaN: Men between 70-79 With Sepsis', 'NaN: Men between 70-79 without Sepsis','NaN: Men older 80 With Sepsis', 'NaN: Men older 80 without Sepsis',

        fig1, ax1 = st.columns(2)
        fig2 = px.pie(sizes, labels=labels, values=sizes, names=labels)
        ax1.write(fig2)
    
def decideDiagram(intToDecide):
    #SepsisGender
    if( intToDecide == 1):
        A1 = CheckForUnitSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
        A1.getFileNames()
        
        #Sepsis
        verarbeitetesListList1 = [
            [A1.count1819WSepsisFU1, A1.count1819WSepsisMU1, 
             A1.count20JahreWSepsisFU1, A1.count20JahreWSepsisMU1, 
             A1.count30JahreWSepsisFU1, A1.count30JahreWSepsisMU1, 
             A1.count40JahreWSepsisFU1, A1.count40JahreWSepsisMU1, 
             A1.count50JahreWSepsisFU1, A1.count50JahreWSepsisMU1 ,
             A1.count60JahreWSepsisFU1, A1.count60JahreWSepsisMU1,
             A1.count70JahreWSepsisFU1, A1.count70JahreWSepsisMU1, 
             A1.count80JahreWSepsisFU1, A1.count80JahreWSepsisMU1], #UNIT1
             [A1.count1819WSepsisFU2, A1.count1819WSepsisMU2,                                   
        A1.count20JahreWSepsisFU2, A1.count20JahreWSepsisMU2,
        A1.count30JahreWSepsisFU2, A1.count30JahreWSepsisMU2,        
        A1.count40JahreWSepsisFU2, A1.count40JahreWSepsisMU2,
        A1.count50JahreWSepsisFU2, A1.count50JahreWSepsisMU2,
        A1.count60JahreWSepsisFU2, A1.count60JahreWSepsisMU2,
        A1.count70JahreWSepsisFU2, A1.count70JahreWSepsisMU2,
        A1.count80JahreWSepsisFU2, A1.count80JahreWSepsisMU2], #UNIT2
        [A1.count1819WSepsisFNaN, A1.count1819WSepsisMNaN,                                   
        A1.count20JahreWSepsisFNaN, A1.count20JahreWSepsisMNaN,
        A1.count30JahreWSepsisFNaN, A1.count30JahreWSepsisMNaN,        
        A1.count40JahreWSepsisFNaN, A1.count40JahreWSepsisMNaN,
        A1.count50JahreWSepsisFNaN, A1.count50JahreWSepsisMNaN,
        A1.count60JahreWSepsisFNaN, A1.count60JahreWSepsisMNaN,
        A1.count70JahreWSepsisFNaN, A1.count70JahreWSepsisMNaN,
        A1.count80JahreWSepsisFNaN, A1.count80JahreWSepsisMNaN ]]

       #Without Sepsis
        verarbeitetesListList2 = [
            [A1.count1819WOSepsisFU1, A1.count1819WOSepsisMU1, 
             A1.count20JahreWOSepsisFU1,A1.count20JahreWOSepsisMU1, 
             A1.count30JahreWOSepsisFU1, A1.count30JahreWOSepsisMU1, 
             A1.count40JahreWOSepsisFU1, A1.count40JahreWOSepsisMU1, 
             A1.count50JahreWOSepsisFU1, A1.count50JahreWOSepsisMU1 ,
             A1.count60JahreWOSepsisFU1, A1.count60JahreWOSepsisMU1,
             A1.count70JahreWOSepsisFU1, A1.count70JahreWOSepsisMU1,
             A1.count80JahreWOSepsisFU1, A1.count80JahreWOSepsisMU1], #UNIT1
             [A1.count1819WOSepsisFU2, A1.count1819WOSepsisMU2,                                   
        A1.count20JahreWOSepsisFU2, A1.count20JahreWOSepsisMU2,
        A1.count30JahreWOSepsisFU2, A1.count30JahreWOSepsisMU2,        
        A1.count40JahreWOSepsisFU2, A1.count40JahreWOSepsisMU2,
        A1.count50JahreWOSepsisFU2, A1.count50JahreWOSepsisMU2,
        A1.count60JahreWOSepsisFU2, A1.count60JahreWOSepsisMU2,
        A1.count70JahreWOSepsisFU2, A1.count70JahreWOSepsisMU2,
        A1.count80JahreWOSepsisFU2, A1.count80JahreWOSepsisMU2], #UNIT2
        [A1.count1819WOSepsisFNaN, A1.count1819WOSepsisMNaN,                                   
        A1.count20JahreWOSepsisFNaN, A1.count20JahreWOSepsisMNaN,
        A1.count30JahreWOSepsisFNaN, A1.count30JahreWOSepsisMNaN,        
        A1.count40JahreWOSepsisFNaN, A1.count40JahreWOSepsisMNaN,
        A1.count50JahreWOSepsisFNaN, A1.count50JahreWOSepsisMNaN,
        A1.count60JahreWOSepsisFNaN, A1.count60JahreWOSepsisMNaN,
        A1.count70JahreWOSepsisFNaN, A1.count70JahreWOSepsisMNaN,
        A1.count80JahreWOSepsisFNaN, A1.count80JahreWOSepsisMNaN ]]

        print("Das ist das Array {}", verarbeitetesListList1)
        print("Das ist das Array {}", verarbeitetesListList2)
        print("Werte")




        #counting ICUs
        #print("MICU Female")
        #print("Alle Micu Frauen",A1.countAllUnit1Female)
        #print("Alle MICU Frauen Sepsis",A1.countAllUnit1FemaleSepsis)
        #print("Alle MICU Frauen kein Sepsis",A1.countAllUnit1FemaleNoSepsis)


        #print("HIIIIIIIIIIIIIIIIER")
        #print("FRAU")
        #allgemein
        #print("MICU Anzahl von Frauen: ", A1.countAllUnit1Female)
        #print("MICU Anzahl von Frauen mit Sepsis: ", A1.countAllUnit1FemaleSepsis)
        #print("MICU Anzahl von Frauen ohne Sepsis: ", A1.countAllUnit1FemaleNoSepsis)
        #print("MICU Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in MICU waren (und nicht in SICU und NaN)): F:A: ", ((A1.countAllUnit1Female * 100)/20336))
        #print("MICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von MICU Sepsis haben): F:A  ", ((A1.countAllUnit1FemaleSepsis*100)/20336))
        #print("MICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von MICU nicht Sepsis haben): F:A ",((A1.countAllUnit1FemaleNoSepsis*100)/20336))
        #print("MICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von MICU Sepsis haben): ", ((A1.countAllUnit1FemaleSepsis*100)/A1.countAllUnit1Female))
        #print("MICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von MICU nicht Sepsis haben): ",((A1.countAllUnit1FemaleNoSepsis*100)/A1.countAllUnit1Female))

        #unter 20
        #print("MICU Anzahl von Frauen unter 20: ", A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1)
        #print("MICU Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFU1)
        #print("MICU Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFU1)
        #print("MICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", ((A1.count1819WSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count1819WOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count1819WSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count1819WOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von MICU Sepsis haben): F:F:unter 20: ", ((A1.count1819WSepsisFU1*100)/ (A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1)))
        #print("MICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von MICU nicht Sepsis haben): F:F:unter 20: ", ((A1.count1819WOSepsisFU1*100)/ (A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1)))

        #zwischen 20-29
        #print("MICU Anzahl von Frauen zwischen 20-29: ",A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count20JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count20JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count20JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count20JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F: F:F: 20", ((A1.count20JahreWSepsisFU1*100)/ (A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU nicht Sepsis haben): F:F: 20", ((A1.count20JahreWOSepsisFU1*100)/ (A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1)))

        #zwischen 30-39
        #print("MICU Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", ((A1.count30JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count30JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von MICU Sepsis haben) F:F:A ", ((A1.count30JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von MICU Sepsis haben) F:F:A ", ((A1.count30JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von MICU Sepsis haben): F:F:30", ((A1.count30JahreWSepsisFU1*100)/ (A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von MICU nicht Sepsis haben): F:F:30 ", ((A1.count30JahreWOSepsisFU1*100)/ (A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1)))

        #zwischen 40-49
        #print("MICU Anzahl von Frauen zwischen 40-49: ",A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count40JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count40JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 40-49 von MICU Sepsis haben) F:F:A ", ((A1.count40JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von MICU Sepsis haben) F:F:A ", ((A1.count40JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von MICU Sepsis haben) F:F:40: ", ((A1.count40JahreWSepsisFU1*100)/ (A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von MICU nicht Sepsis haben): F:F:40", ((A1.count40JahreWOSepsisFU1*100)/ (A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1)))

        #zwischen 50-59
        #print("MICU Anzahl von Frauen zwischen 50-59: ",A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count50JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count50JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count50JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count50JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von MICU Sepsis haben) F:F:50: ", ((A1.count50JahreWSepsisFU1*100)/ (A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von MICU nicht Sepsis haben): F:F:50", ((A1.count50JahreWOSepsisFU1*100)/ (A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1)))

        #zwischen 60-69
        #print("MICU Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", ((A1.count60JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count60JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von MICU Sepsis haben) F:F:A ", ((A1.count60JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von MICU Sepsis haben) F:F:A ", ((A1.count60JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von MICU Sepsis haben): F:F:30", ((A1.count60JahreWSepsisFU1*100)/ (A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von MICU nicht Sepsis haben): F:F:30 ", ((A1.count60JahreWOSepsisFU1*100)/ (A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1)))

        #zwischen 70-79
        #print("MICU Anzahl von Frauen zwischen 70-79: ",A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count70JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count70JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 70-79 von MICU Sepsis haben) F:F:A ", ((A1.count70JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von MICU Sepsis haben) F:F:A ", ((A1.count70JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von MICU Sepsis haben) F:F:40: ", ((A1.count70JahreWSepsisFU1*100)/ (A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von MICU nicht Sepsis haben): F:F:40", ((A1.count70JahreWOSepsisFU1*100)/ (A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1)))

        #älter 80
        #print("MICU Anzahl von Frauen älter 80: ",A1.count80JahreWSepsisFU1 +A1.count80JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count80JahreWSepsisFU1 +A1.count80JahreWOSepsisFU1) * 100)/20336))
        #print("MICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count80JahreWSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count80JahreWOSepsisFU1 * 100)/(20336)))
        #print("MICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count80JahreWSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", ((A1.count80JahreWOSepsisFU1*100)/ (A1.countAllUnit1Female)))
        #print("MICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von MICU Sepsis haben) F:F:50: ", ((A1.count80JahreWSepsisFU1*100)/ (A1.count80JahreWSepsisFU1 +A1.count80JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von MICU nicht Sepsis haben): F:F:50", ((A1.count80JahreWOSepsisFU1*100)/ (A1.count80JahreWSepsisFU1 +A1.count80JahreWOSepsisFU1)))


        #SICU Frau
        #print("SICU Female")
        #print("Alle SICU Frauen",A1.countAllUnit2Female)
        #print("Alle SICU Frauen Sepsis", A1.countAllUnit2FemaleSepsis)
        #print("Alle SICU Frauen kein Sepsis",A1.countAllUnit2FemaleNoSepsis)
        #allgemein
        #print("SICU Anzahl von Frauen: ", A1.countAllUnit2Female)
        #print("SICU Anzahl von Frauen mit Sepsis: ", A1.countAllUnit2FemaleSepsis)
        #print("SICU Anzahl von Frauen ohne Sepsis: ", A1.countAllUnit2FemaleNoSepsis)
        #print("SICU Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in SICU waren (und nicht in SICU und NaN)): F:A: ", ((A1.countAllUnit2Female * 100)/20336))
        #print("SICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von SICU Sepsis haben): F:A  ", ((A1.countAllUnit2FemaleSepsis*100)/20336))
        #print("SICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von SICU nicht Sepsis haben): F:A ",((A1.countAllUnit2FemaleNoSepsis*100)/20336))
        #print("SICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von SICU Sepsis haben): ", ((A1.countAllUnit2FemaleSepsis*100)/A1.countAllUnit2Female))
        #print("SICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von SICU nicht Sepsis haben): ",((A1.countAllUnit2FemaleNoSepsis*100)/A1.countAllUnit2Female))

        #unter 20
        #print("SICU Anzahl von Frauen unter 20: ", A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2)
        #print("SICU Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFU2)
        #print("SICU Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFU2)
        #print("SICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", ((A1.count1819WSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count1819WOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count1819WSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count1819WOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von SICU Sepsis haben): F:F:unter 20: ", ((A1.count1819WSepsisFU2*100)/ (A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2)))
        #print("SICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von SICU nicht Sepsis haben): F:F:unter 20: ", ((A1.count1819WOSepsisFU2*100)/ (A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2)))

        #zwischen 20-29
        #print("SICU Anzahl von Frauen zwischen 20-29: ",A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count20JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count20JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count20JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count20JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F: F:F: 20", ((A1.count20JahreWSepsisFU2*100)/ (A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU nicht Sepsis haben): F:F: 20", ((A1.count20JahreWOSepsisFU2*100)/ (A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2)))

        #zwischen 30-39
        #print("SICU Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", ((A1.count30JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count30JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von SICU Sepsis haben) F:F:A ", ((A1.count30JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von SICU Sepsis haben) F:F:A ", ((A1.count30JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von SICU Sepsis haben): F:F:30", ((A1.count30JahreWSepsisFU2*100)/ (A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von SICU nicht Sepsis haben): F:F:30 ", ((A1.count30JahreWOSepsisFU2*100)/ (A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2)))

        #zwischen 40-49
        #print("SICU Anzahl von Frauen zwischen 40-49: ",A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count40JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count40JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 40-49 von SICU Sepsis haben) F:F:A ", ((A1.count40JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von SICU Sepsis haben) F:F:A ", ((A1.count40JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von SICU Sepsis haben) F:F:40: ", ((A1.count40JahreWSepsisFU2*100)/ (A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von SICU nicht Sepsis haben): F:F:40", ((A1.count40JahreWOSepsisFU2*100)/ (A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2)))

        #zwischen 50-59
        #print("SICU Anzahl von Frauen zwischen 50-59: ",A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count50JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count50JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count50JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count50JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von SICU Sepsis haben) F:F:50: ", ((A1.count50JahreWSepsisFU2*100)/ (A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von SICU nicht Sepsis haben): F:F:50", ((A1.count50JahreWOSepsisFU2*100)/ (A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2)))

        #zwischen 60-69
        #print("SICU Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", ((A1.count60JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count60JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von SICU Sepsis haben) F:F:A ", ((A1.count60JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von SICU Sepsis haben) F:F:A ", ((A1.count60JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von SICU Sepsis haben): F:F:30", ((A1.count60JahreWSepsisFU2*100)/ (A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von SICU nicht Sepsis haben): F:F:30 ", ((A1.count60JahreWOSepsisFU2*100)/ (A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2)))

        #zwischen 70-79
        #print("SICU Anzahl von Frauen zwischen 70-79: ",A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count70JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count70JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 70-79 von SICU Sepsis haben) F:F:A ", ((A1.count70JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von SICU Sepsis haben) F:F:A ", ((A1.count70JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von SICU Sepsis haben) F:F:40: ", ((A1.count70JahreWSepsisFU2*100)/ (A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von SICU nicht Sepsis haben): F:F:40", ((A1.count70JahreWOSepsisFU2*100)/ (A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2)))

        #älter 80
        #print("SICU Anzahl von Frauen älter 80: ",A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2) * 100)/20336))
        #print("SICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  F:A ", ((A1.count80JahreWSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", ((A1.count80JahreWOSepsisFU2 * 100)/(20336)))
        #print("SICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count80JahreWSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", ((A1.count80JahreWOSepsisFU2*100)/ (A1.countAllUnit2Female)))
        #print("SICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von SICU Sepsis haben) F:F:50: ", ((A1.count80JahreWSepsisFU2*100)/ (A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von SICU nicht Sepsis haben): F:F:50", ((A1.count80JahreWOSepsisFU2*100)/ (A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2)))

        #NaN Frau      
        #print("NaN Female")
        #print("Alle NaN Frauen",A1.countNoUnitFemale)
        #print("Alle NaN Frauen Sepsis", A1.countNoUnitSepFemale)
        #print("Alle NaN Frauen kein Sepsis",A1.countNoUnitNoSepFemale)
        #allgemein
        ##print("NaN Anzahl von Frauen: ", A1.countNoUnitFemale)
        ##print("NaN Anzahl von Frauen mit Sepsis: ", A1.countNoUnitSepFemale)
        ##print("NaN Anzahl von Frauen ohne Sepsis: ", A1.countNoUnitNoSepFemale)
        #print("NaN Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in NaN waren (und nicht in NaN und NaN)): F:A: ", ((A1.countNoUnitFemale * 100)/20336))
        #print("NaN Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von NaN Sepsis haben): F:A  ", ((A1.countNoUnitSepFemale*100)/20336))
        #print("NaN Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von NaN nicht Sepsis haben): F:A ",((A1.countNoUnitNoSepFemale*100)/20336))
        #print("NaN Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von NaN Sepsis haben): ", ((A1.countNoUnitSepFemale*100)/A1.countNoUnitFemale))
        #print("NaN Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von NaN nicht Sepsis haben): ",((A1.countNoUnitNoSepFemale*100)/A1.countNoUnitFemale))

        #unter 20
        #print("NaN Anzahl von Frauen unter 20: ", A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN)
        #print("NaN Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFNaN)
        #print("NaN Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFNaN)
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", ((A1.count1819WSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count1819WOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count1819WSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count1819WOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben): F:F:unter 20: ", ((A1.count1819WSepsisFNaN*100)/ (A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN)))
        #print("NaN Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von NaN nicht Sepsis haben): F:F:unter 20: ", ((A1.count1819WOSepsisFNaN*100)/ (A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN)))

        #zwischen 20-29
        #print("NaN Anzahl von Frauen zwischen 20-29: ",A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  F:A ", ((A1.count20JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count20JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count20JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count20JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F: F:F: 20", ((A1.count20JahreWSepsisFNaN*100)/ (A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN nicht Sepsis haben): F:F: 20", ((A1.count20JahreWOSepsisFNaN*100)/ (A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN)))

        #zwischen 30-39
        #print("NaN Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", ((A1.count30JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count30JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben) F:F:A ", ((A1.count30JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben) F:F:A ", ((A1.count30JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben): F:F:30", ((A1.count30JahreWSepsisFNaN*100)/ (A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von NaN nicht Sepsis haben): F:F:30 ", ((A1.count30JahreWOSepsisFNaN*100)/ (A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN)))

        #zwischen 40-49
        #print("NaN Anzahl von Frauen zwischen 40-49: ",A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  F:A ", ((A1.count40JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count40JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:A ", ((A1.count40JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:A ", ((A1.count40JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:40: ", ((A1.count40JahreWSepsisFNaN*100)/ (A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von NaN nicht Sepsis haben): F:F:40", ((A1.count40JahreWOSepsisFNaN*100)/ (A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN)))

        #zwischen 50-59
        #print("NaN Anzahl von Frauen zwischen 50-59: ",A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  F:A ", ((A1.count50JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count50JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count50JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count50JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben) F:F:50: ", ((A1.count50JahreWSepsisFNaN*100)/ (A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von NaN nicht Sepsis haben): F:F:50", ((A1.count50JahreWOSepsisFNaN*100)/ (A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN)))

        #zwischen 60-69
        #print("NaN Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", ((A1.count60JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count60JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben) F:F:A ", ((A1.count60JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben) F:F:A ", ((A1.count60JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben): F:F:30", ((A1.count60JahreWSepsisFNaN*100)/ (A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von NaN nicht Sepsis haben): F:F:30 ", ((A1.count60JahreWOSepsisFNaN*100)/ (A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN)))

        #zwischen 70-79
        #print("NaN Anzahl von Frauen zwischen 70-79: ",A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  F:A ", ((A1.count70JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count70JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:A ", ((A1.count70JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:A ", ((A1.count70JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:40: ", ((A1.count70JahreWSepsisFNaN*100)/ (A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von NaN nicht Sepsis haben): F:F:40", ((A1.count70JahreWOSepsisFNaN*100)/ (A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN)))

        #älter 80
        #print("NaN Anzahl von Frauen älter 80: ",A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN) * 100)/20336))
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  F:A ", ((A1.count80JahreWSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", ((A1.count80JahreWOSepsisFNaN * 100)/(20336)))
        #print("NaN Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count80JahreWSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", ((A1.count80JahreWOSepsisFNaN*100)/ (A1.countNoUnitFemale)))
        #print("NaN Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben) F:F:50: ", ((A1.count80JahreWSepsisFNaN*100)/ (A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von NaN nicht Sepsis haben): F:F:50", ((A1.count80JahreWOSepsisFNaN*100)/ (A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN)))

        #Male
        #print("Male")
        #print("MICU Male ")
        #print(A1.countAllUnit1Male)
        #print(A1.countAllUnit1MaleSepsis)
        #print(A1.countAllUnit1MaleNoSepsis)
        #print("SICU Male ")
        #print(A1.countAllUnit2Male)
        #print(A1.countAllUnit2MaleSepsis)#gut
        #print(A1.countAllUnit2MaleNoSepsis)#nicht gut, muss abgezogen werden
        #print("NaN Male")
        #print(A1.countNoUnitMale)
        #print(A1.countNoUnitSepMale)
        #print(A1.countNoUnitNoSepMale)

                #counting ICUs
        print("MICU Male")
        print("Alle Micu Männer",A1.countAllUnit1Male)
        print("Alle MICU Männer Sepsis",A1.countAllUnit1MaleSepsis)
        print("Alle MICU Männer kein Sepsis",A1.countAllUnit1MaleNoSepsis)


        print("HIIIIIIIIIIIIIIIIER")
        print("MANN")
        #allgemein
        print("MICU Anzahl von Männer: ", A1.countAllUnit1Male)
        print("MICU Anzahl von Männer mit Sepsis: ", A1.countAllUnit1MaleSepsis)
        print("MICU Anzahl von Männer ohne Sepsis: ", A1.countAllUnit1MaleNoSepsis)
        print("MICU Prozent von Männer Allgemein (Wie viele Männer insgesamt in MICU waren (und nicht in SICU und NaN)): M:A: ", ((A1.countAllUnit1Male * 100)/20336))
        print("MICU Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von MICU Sepsis haben): M:A  ", ((A1.countAllUnit1MaleSepsis*100)/20336))
        print("MICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von MICU nicht Sepsis haben): M:A ",((A1.countAllUnit1MaleNoSepsis*100)/20336))
        print("MICU Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von MICU Sepsis haben): ", ((A1.countAllUnit1MaleSepsis*100)/A1.countAllUnit1Male))
        print("MICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von MICU nicht Sepsis haben): ",((A1.countAllUnit1MaleNoSepsis*100)/A1.countAllUnit1Male))

        #unter 20
        print("MICU Anzahl von Männer unter 20: ", A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1)
        print("MICU Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMU1)
        print("MICU Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMU1)
        print("MICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: M:A ", ((A1.count1819WSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count1819WOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count1819WSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count1819WOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von MICU Sepsis haben): M:M:unter 20: ", ((A1.count1819WSepsisMU1*100)/ (A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1)))
        print("MICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von MICU nicht Sepsis haben): M:M:unter 20: ", ((A1.count1819WOSepsisMU1*100)/ (A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1)))

        #zwischen 20-29
        print("MICU Anzahl von Männer zwischen 20-29: ",A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count20JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count20JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count20JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count20JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M: M:M: 20", ((A1.count20JahreWSepsisMU1*100)/ (A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU nicht Sepsis haben): M:M: 20", ((A1.count20JahreWOSepsisMU1*100)/ (A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1)))

        #zwischen 30-39
        print("MICU Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: M:A ", ((A1.count30JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count30JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von MICU Sepsis haben) M:M:A ", ((A1.count30JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von MICU Sepsis haben) M:M:A ", ((A1.count30JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von MICU Sepsis haben): M:M:30", ((A1.count30JahreWSepsisMU1*100)/ (A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von MICU nicht Sepsis haben): M:M:30 ", ((A1.count30JahreWOSepsisMU1*100)/ (A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1)))

        #zwischen 40-49
        print("MICU Anzahl von Männer zwischen 40-49: ",A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count40JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count40JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 40-49 von MICU Sepsis haben) M:M:A ", ((A1.count40JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 40-49 von MICU Sepsis haben) M:M:A ", ((A1.count40JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von MICU Sepsis haben) M:M:40: ", ((A1.count40JahreWSepsisMU1*100)/ (A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von MICU nicht Sepsis haben): M:M:40", ((A1.count40JahreWOSepsisMU1*100)/ (A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1)))

        #zwischen 50-59
        print("MICU Anzahl von Männer zwischen 50-59: ",A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count50JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count50JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count50JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count50JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von MICU Sepsis haben) M:M:50: ", ((A1.count50JahreWSepsisMU1*100)/ (A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von MICU nicht Sepsis haben): M:M:50", ((A1.count50JahreWOSepsisMU1*100)/ (A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1)))

        #zwischen 60-69
        print("MICU Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: M:A ", ((A1.count60JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count60JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von MICU Sepsis haben) M:M:A ", ((A1.count60JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von MICU Sepsis haben) M:M:A ", ((A1.count60JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von MICU Sepsis haben): M:M:30", ((A1.count60JahreWSepsisMU1*100)/ (A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von MICU nicht Sepsis haben): M:M:30 ", ((A1.count60JahreWOSepsisMU1*100)/ (A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1)))

        #zwischen 70-79
        print("MICU Anzahl von Männer zwischen 70-79: ",A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count70JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count70JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 70-79 von MICU Sepsis haben) M:M:A ", ((A1.count70JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 70-79 von MICU Sepsis haben) M:M:A ", ((A1.count70JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von MICU Sepsis haben) M:M:40: ", ((A1.count70JahreWSepsisMU1*100)/ (A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von MICU nicht Sepsis haben): M:M:40", ((A1.count70JahreWOSepsisMU1*100)/ (A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1)))

        #älter 80
        print("MICU Anzahl von Männer älter 80: ",A1.count80JahreWSepsisMU1 +A1.count80JahreWOSepsisMU1)
        print("MICU Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMU1)
        print("MICU Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMU1)
        print("MICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count80JahreWSepsisMU1 +A1.count80JahreWOSepsisMU1) * 100)/20336))
        print("MICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count80JahreWSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count80JahreWOSepsisMU1 * 100)/(20336)))
        print("MICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count80JahreWSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) M:M:A ", ((A1.count80JahreWOSepsisMU1*100)/ (A1.countAllUnit1Male)))
        print("MICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von MICU Sepsis haben) M:M:50: ", ((A1.count80JahreWSepsisMU1*100)/ (A1.count80JahreWSepsisMU1 +A1.count80JahreWOSepsisMU1)))
        print("MICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von MICU nicht Sepsis haben): M:M:50", ((A1.count80JahreWOSepsisMU1*100)/ (A1.count80JahreWSepsisMU1 +A1.count80JahreWOSepsisMU1)))


        #SICU Frau
        print("SICU Male")
        print("Alle SICU Männer",A1.countAllUnit2Male)
        print("Alle SICU Männer Sepsis", A1.countAllUnit2MaleSepsis)
        print("Alle SICU Männer kein Sepsis",A1.countAllUnit2MaleNoSepsis)
        #allgemein
        print("SICU Anzahl von Männer: ", A1.countAllUnit2Male)
        print("SICU Anzahl von Männer mit Sepsis: ", A1.countAllUnit2MaleSepsis)
        print("SICU Anzahl von Männer ohne Sepsis: ", A1.countAllUnit2MaleNoSepsis)
        print("SICU Prozent von Männer Allgemein (Wie viele Männer insgesamt in SICU waren (und nicht in SICU und NaN)): M:A: ", ((A1.countAllUnit2Male * 100)/20336))
        print("SICU Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von SICU Sepsis haben): M:A  ", ((A1.countAllUnit2MaleSepsis*100)/20336))
        print("SICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von SICU nicht Sepsis haben): M:A ",((A1.countAllUnit2MaleNoSepsis*100)/20336))
        print("SICU Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von SICU Sepsis haben): ", ((A1.countAllUnit2MaleSepsis*100)/A1.countAllUnit2Male))
        print("SICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von SICU nicht Sepsis haben): ",((A1.countAllUnit2MaleNoSepsis*100)/A1.countAllUnit2Male))

        #unter 20
        print("SICU Anzahl von Männer unter 20: ", A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2)
        print("SICU Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMU2)
        print("SICU Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMU2)
        print("SICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: M:A ", ((A1.count1819WSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count1819WOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count1819WSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count1819WOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von SICU Sepsis haben): M:M:unter 20: ", ((A1.count1819WSepsisMU2*100)/ (A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2)))
        print("SICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von SICU nicht Sepsis haben): M:M:unter 20: ", ((A1.count1819WOSepsisMU2*100)/ (A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2)))

        #zwischen 20-29
        print("SICU Anzahl von Männer zwischen 20-29: ",A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count20JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count20JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count20JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count20JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M: M:M: 20", ((A1.count20JahreWSepsisMU2*100)/ (A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU nicht Sepsis haben): M:M: 20", ((A1.count20JahreWOSepsisMU2*100)/ (A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2)))

        #zwischen 30-39
        print("SICU Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: M:A ", ((A1.count30JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count30JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von SICU Sepsis haben) M:M:A ", ((A1.count30JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von SICU Sepsis haben) M:M:A ", ((A1.count30JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von SICU Sepsis haben): M:M:30", ((A1.count30JahreWSepsisMU2*100)/ (A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von SICU nicht Sepsis haben): M:M:30 ", ((A1.count30JahreWOSepsisMU2*100)/ (A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2)))

        #zwischen 40-49
        print("SICU Anzahl von Männer zwischen 40-49: ",A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count40JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count40JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 40-49 von SICU Sepsis haben) M:M:A ", ((A1.count40JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 40-49 von SICU Sepsis haben) M:M:A ", ((A1.count40JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von SICU Sepsis haben) M:M:40: ", ((A1.count40JahreWSepsisMU2*100)/ (A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von SICU nicht Sepsis haben): M:M:40", ((A1.count40JahreWOSepsisMU2*100)/ (A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2)))

        #zwischen 50-59
        print("SICU Anzahl von Männer zwischen 50-59: ",A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count50JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count50JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count50JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count50JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von SICU Sepsis haben) M:M:50: ", ((A1.count50JahreWSepsisMU2*100)/ (A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von SICU nicht Sepsis haben): M:M:50", ((A1.count50JahreWOSepsisMU2*100)/ (A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2)))

        #zwischen 60-69
        print("SICU Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: M:A ", ((A1.count60JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count60JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von SICU Sepsis haben) M:M:A ", ((A1.count60JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von SICU Sepsis haben) M:M:A ", ((A1.count60JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von SICU Sepsis haben): M:M:30", ((A1.count60JahreWSepsisMU2*100)/ (A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von SICU nicht Sepsis haben): M:M:30 ", ((A1.count60JahreWOSepsisMU2*100)/ (A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2)))

        #zwischen 70-79
        print("SICU Anzahl von Männer zwischen 70-79: ",A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count70JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count70JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 70-79 von SICU Sepsis haben) M:M:A ", ((A1.count70JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 70-79 von SICU Sepsis haben) M:M:A ", ((A1.count70JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von SICU Sepsis haben) M:M:40: ", ((A1.count70JahreWSepsisMU2*100)/ (A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von SICU nicht Sepsis haben): M:M:40", ((A1.count70JahreWOSepsisMU2*100)/ (A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2)))

        #älter 80
        print("SICU Anzahl von Männer älter 80: ",A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2)
        print("SICU Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMU2)
        print("SICU Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMU2)
        print("SICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)): M:A ", (((A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2) * 100)/20336))
        print("SICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis:  M:A ", ((A1.count80JahreWSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: M:A ", ((A1.count80JahreWOSepsisMU2 * 100)/(20336)))
        print("SICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count80JahreWSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) M:M:A ", ((A1.count80JahreWOSepsisMU2*100)/ (A1.countAllUnit2Male)))
        print("SICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von SICU Sepsis haben) M:M:50: ", ((A1.count80JahreWSepsisMU2*100)/ (A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2)))
        print("SICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von SICU nicht Sepsis haben): M:M:50", ((A1.count80JahreWOSepsisMU2*100)/ (A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2)))

        #NaN Frau      
        print("NaN Male")
        print("Alle NaN Männer",A1.countNoUnitMale)
        print("Alle NaN Männer Sepsis", A1.countNoUnitSepMale)
        print("Alle NaN Männer kein Sepsis",A1.countNoUnitNoSepMale)
        #allgemein
        #print("NaN Anzahl von Männer: ", A1.countNoUnitMale)
        #print("NaN Anzahl von Männer mit Sepsis: ", A1.countNoUnitSepMale)
        #print("NaN Anzahl von Männer ohne Sepsis: ", A1.countNoUnitNoSepMale)
        print("NaN Prozent von Männer Allgemein (Wie viele Männer insgesamt in NaN waren (und nicht in NaN und NaN)): M:A: ", ((A1.countNoUnitMale * 100)/20336))
        print("NaN Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von NaN Sepsis haben): M:A  ", ((A1.countNoUnitSepMale*100)/20336))
        print("NaN Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von NaN nicht Sepsis haben): M:A ",((A1.countNoUnitNoSepMale*100)/20336))
        print("NaN Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von NaN Sepsis haben): ", ((A1.countNoUnitSepMale*100)/A1.countNoUnitMale))
        print("NaN Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von NaN nicht Sepsis haben): ",((A1.countNoUnitNoSepMale*100)/A1.countNoUnitMale))

        #unter 20
        print("NaN Anzahl von Männer unter 20: ", A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN)
        print("NaN Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMNaN)
        print("NaN Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMNaN)
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: M:A ", ((A1.count1819WSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count1819WOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count1819WSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count1819WOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben): M:M:unter 20: ", ((A1.count1819WSepsisMNaN*100)/ (A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN)))
        print("NaN Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von NaN nicht Sepsis haben): M:M:unter 20: ", ((A1.count1819WOSepsisMNaN*100)/ (A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN)))

        #zwischen 20-29
        print("NaN Anzahl von Männer zwischen 20-29: ",A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  M:A ", ((A1.count20JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count20JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count20JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count20JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M: M:M: 20", ((A1.count20JahreWSepsisMNaN*100)/ (A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN nicht Sepsis haben): M:M: 20", ((A1.count20JahreWOSepsisMNaN*100)/ (A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN)))

        #zwischen 30-39
        print("NaN Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: M:A ", ((A1.count30JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count30JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben) M:M:A ", ((A1.count30JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben) M:M:A ", ((A1.count30JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben): M:M:30", ((A1.count30JahreWSepsisMNaN*100)/ (A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von NaN nicht Sepsis haben): M:M:30 ", ((A1.count30JahreWOSepsisMNaN*100)/ (A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN)))

        #zwischen 40-49
        print("NaN Anzahl von Männer zwischen 40-49: ",A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  M:A ", ((A1.count40JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count40JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) M:M:A ", ((A1.count40JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) M:M:A ", ((A1.count40JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) M:M:40: ", ((A1.count40JahreWSepsisMNaN*100)/ (A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von NaN nicht Sepsis haben): M:M:40", ((A1.count40JahreWOSepsisMNaN*100)/ (A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN)))

        #zwischen 50-59
        print("NaN Anzahl von Männer zwischen 50-59: ",A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  M:A ", ((A1.count50JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count50JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count50JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count50JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben) M:M:50: ", ((A1.count50JahreWSepsisMNaN*100)/ (A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von NaN nicht Sepsis haben): M:M:50", ((A1.count50JahreWOSepsisMNaN*100)/ (A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN)))

        #zwischen 60-69
        print("NaN Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: M:A ", ((A1.count60JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count60JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben) M:M:A ", ((A1.count60JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben) M:M:A ", ((A1.count60JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben): M:M:30", ((A1.count60JahreWSepsisMNaN*100)/ (A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von NaN nicht Sepsis haben): M:M:30 ", ((A1.count60JahreWOSepsisMNaN*100)/ (A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN)))

        #zwischen 70-79
        print("NaN Anzahl von Männer zwischen 70-79: ",A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  M:A ", ((A1.count70JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count70JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) M:M:A ", ((A1.count70JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) M:M:A ", ((A1.count70JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) M:M:40: ", ((A1.count70JahreWSepsisMNaN*100)/ (A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von NaN nicht Sepsis haben): M:M:40", ((A1.count70JahreWOSepsisMNaN*100)/ (A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN)))

        #älter 80
        print("NaN Anzahl von Männer älter 80: ",A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMNaN)
        print("NaN Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMNaN)
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)): M:A ", (((A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN) * 100)/20336))
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis:  M:A ", ((A1.count80JahreWSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: M:A ", ((A1.count80JahreWOSepsisMNaN * 100)/(20336)))
        print("NaN Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count80JahreWSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) M:M:A ", ((A1.count80JahreWOSepsisMNaN*100)/ (A1.countNoUnitMale)))
        print("NaN Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben) M:M:50: ", ((A1.count80JahreWSepsisMNaN*100)/ (A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von NaN nicht Sepsis haben): M:M:50", ((A1.count80JahreWOSepsisMNaN*100)/ (A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN)))



        st.subheader("Unit-Sepsis-Patients-Age-Gender-Diagramm")
        st.write("Beschreibung Unit-Sepsis-Patients-Age-Gender-Diagramm für Sepsis für Datensatz 1")

        A1.makeUnitSepsisAgeGenderDiagram(verarbeitetesListList1)
        st.subheader("Unit-No-Sepsis-Patients-Age-Gender-Diagramm")
        st.write("Beschreibung Unit-Sepsis-Patients-Age-Gender-Diagramm für No Sepsis für Datensatz 1")
        A1.makeUnitNoSepsisAgeGenderDiagram(verarbeitetesListList2)
        #MICU
        sizes1 = [
            (A1.count1819WSepsisFU1*100)/20336,
            (A1.count1819WOSepsisFU1*100)/20336,
            (A1.count20JahreWSepsisFU1*100)/20336,
            (A1.count20JahreWOSepsisFU1*100)/20336,
            (A1.count30JahreWSepsisFU1*100)/20336,
            (A1.count30JahreWOSepsisFU1*100)/20336,
            (A1.count40JahreWSepsisFU1*100)/20336,
            (A1.count40JahreWOSepsisFU1*100)/20336,
            (A1.count50JahreWSepsisFU1*100)/20336,
            (A1.count50JahreWOSepsisFU1*100)/20336,
            (A1.count60JahreWSepsisFU1*100)/20336,
            (A1.count60JahreWOSepsisFU1*100)/20336,
            (A1.count70JahreWSepsisFU1*100)/20336,
            (A1.count70JahreWOSepsisFU1*100)/20336,
            (A1.count80JahreWSepsisFU1*100)/20336,
            (A1.count80JahreWOSepsisFU1*100)/20336,
            (A1.count1819WSepsisMU1*100)/20336,
            (A1.count1819WOSepsisMU1*100)/20336,   
            (A1.count20JahreWSepsisMU1*100)/20336,
            (A1.count20JahreWOSepsisMU1*100)/20336,
            (A1.count30JahreWSepsisMU1*100)/20336,
            (A1.count30JahreWOSepsisMU1*100)/20336,
            (A1.count40JahreWSepsisMU1*100)/20336,
            (A1.count40JahreWOSepsisMU1*100)/20336,
            (A1.count50JahreWSepsisMU1*100)/20336,
            (A1.count50JahreWOSepsisMU1*100)/20336,
            (A1.count60JahreWSepsisMU1*100)/20336,
            (A1.count60JahreWOSepsisMU1*100)/20336,
            (A1.count70JahreWSepsisMU1*100)/20336,
            (A1.count70JahreWOSepsisMU1*100)/20336,
            (A1.count80JahreWSepsisMU1*100)/20336,
            (A1.count80JahreWOSepsisMU1*100)/20336,            
            ]
        st.subheader("MICU: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        st.write("Das ist MICU-Beschreibung ICU in Prozent für Datensatz1 und dass man hier einwenig beschreibt")

        A1.makeMICUDiagram(sizes1)

        
        #SICU
        sizes1 = [
            (A1.count1819WSepsisFU2*100)/20336,
            (A1.count1819WOSepsisFU2*100)/20336,
            (A1.count20JahreWSepsisFU2*100)/20336,
            (A1.count20JahreWOSepsisFU2*100)/20336,
            (A1.count30JahreWSepsisFU2*100)/20336,
            (A1.count30JahreWOSepsisFU2*100)/20336,
            (A1.count40JahreWSepsisFU2*100)/20336,
            (A1.count40JahreWOSepsisFU2*100)/20336,
            (A1.count50JahreWSepsisFU2*100)/20336,
            (A1.count50JahreWOSepsisFU2*100)/20336,
            (A1.count60JahreWSepsisFU2*100)/20336,
            (A1.count60JahreWOSepsisFU2*100)/20336,
            (A1.count70JahreWSepsisFU2*100)/20336,
            (A1.count70JahreWOSepsisFU2*100)/20336,
            (A1.count80JahreWSepsisFU2*100)/20336,
            (A1.count80JahreWOSepsisFU2*100)/20336,
            (A1.count1819WSepsisMU2*100)/20336,
            (A1.count1819WOSepsisMU2*100)/20336,   
            (A1.count20JahreWSepsisMU2*100)/20336,
            (A1.count20JahreWOSepsisMU2*100)/20336,
            (A1.count30JahreWSepsisMU2*100)/20336,
            (A1.count30JahreWOSepsisMU2*100)/20336,
            (A1.count40JahreWSepsisMU2*100)/20336,
            (A1.count40JahreWOSepsisMU2*100)/20336,
            (A1.count50JahreWSepsisMU2*100)/20336,
            (A1.count50JahreWOSepsisMU2*100)/20336,
            (A1.count60JahreWSepsisMU2*100)/20336,
            (A1.count60JahreWOSepsisMU2*100)/20336,
            (A1.count70JahreWSepsisMU2*100)/20336,
            (A1.count70JahreWOSepsisMU2*100)/20336,
            (A1.count80JahreWSepsisMU2*100)/20336,
            (A1.count80JahreWOSepsisMU2*100)/20336,            
            ]
        #st.subheader("SICU: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        A1.makeSICUDiagram(sizes1)
        #st.write("Das ist SICU-Beschreibung ICU in Prozent für Datensatz1 und dass man hier einwenig beschreibt")


        #makeNaNDiagram
        #SICU
        sizes1 = [
            (A1.count1819WSepsisFNaN*100)/20336,
            (A1.count1819WOSepsisFNaN*100)/20336,
            (A1.count20JahreWSepsisFNaN*100)/20336,
            (A1.count20JahreWOSepsisFNaN*100)/20336,
            (A1.count30JahreWSepsisFNaN*100)/20336,
            (A1.count30JahreWOSepsisFNaN*100)/20336,
            (A1.count40JahreWSepsisFNaN*100)/20336,
            (A1.count40JahreWOSepsisFNaN*100)/20336,
            (A1.count50JahreWSepsisFNaN*100)/20336,
            (A1.count50JahreWOSepsisFNaN*100)/20336,
            (A1.count60JahreWSepsisFNaN*100)/20336,
            (A1.count60JahreWOSepsisFNaN*100)/20336,
            (A1.count70JahreWSepsisFNaN*100)/20336,
            (A1.count70JahreWOSepsisFNaN*100)/20336,
            (A1.count80JahreWSepsisFNaN*100)/20336,
            (A1.count80JahreWOSepsisFNaN*100)/20336,
            (A1.count1819WSepsisMNaN*100)/20336,
            (A1.count1819WOSepsisMNaN*100)/20336,   
            (A1.count20JahreWSepsisMNaN*100)/20336,
            (A1.count20JahreWOSepsisMNaN*100)/20336,
            (A1.count30JahreWSepsisMNaN*100)/20336,
            (A1.count30JahreWOSepsisMNaN*100)/20336,
            (A1.count40JahreWSepsisMNaN*100)/20336,
            (A1.count40JahreWOSepsisMNaN*100)/20336,
            (A1.count50JahreWSepsisMNaN*100)/20336,
            (A1.count50JahreWOSepsisMNaN*100)/20336,
            (A1.count60JahreWSepsisMNaN*100)/20336,
            (A1.count60JahreWOSepsisMNaN*100)/20336,
            (A1.count70JahreWSepsisMNaN*100)/20336,
            (A1.count70JahreWOSepsisMNaN*100)/20336,
            (A1.count80JahreWSepsisMNaN*100)/20336,
            (A1.count80JahreWOSepsisMNaN*100)/20336,            
            ]
        st.subheader("NaN: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        st.write("Das ist NaN-Beschreibung ICU in Prozent für Datensatz1 und dass man hier einwenig beschreibt")

        A1.makeNaNDiagram(sizes1)



        #dataset 2
    if(intToDecide == 2):
        print("datasetInt: {}", 2)
        A2 = CheckForUnitSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
        A2.getFileNames()
        #A2.extractAllSepsislabel
        verarbeitetesListList = [[A2.count1819WSepsisF, A2.count1819WOSepsisF, A2.count1819WSepsisM, A2.count1819WOSepsisM], 
             [A2.count20JahreWSepsisF, A2.count20JahreWOSepsisF, A2.count20JahreWSepsisM, A2.count20JahreWSepsisM], 
             [A2.count30JahreWSepsisF, A2.count30JahreWOSepsisF, A2.count30JahreWSepsisM, A2.count30JahreWSepsisM], 
             [A2.count40JahreWSepsisF, A2.count40JahreWOSepsisF, A2.count40JahreWSepsisM, A2.count40JahreWSepsisM], 
             [A2.count50JahreWSepsisF, A2.count50JahreWOSepsisF, A2.count50JahreWSepsisM, A2.count50JahreWSepsisM], 
             [A2.count60JahreWSepsisF, A2.count60JahreWOSepsisF, A2.count60JahreWSepsisM, A2.count60JahreWSepsisM], 
             [A2.count70JahreWSepsisF, A2.count70JahreWOSepsisF, A2.count70JahreWSepsisM, A2.count70JahreWSepsisM], 
             [A2.count80JahreWSepsisF, A2.count80JahreWOSepsisF, A2.count80JahreWSepsisM, A2.count80JahreWSepsisM]]
        print("Das ist das Array {}", verarbeitetesListList)
        A2.makeUnitSepsisAgeGenderDiagram(verarbeitetesListList)
        #Sepsis
        verarbeitetesListList1 = [
            [A2.count1819WSepsisFU1, A2.count1819WSepsisMU1, 
             A2.count20JahreWSepsisFU1, A2.count20JahreWSepsisMU1, 
             A2.count30JahreWSepsisFU1, A2.count30JahreWSepsisMU1, 
             A2.count40JahreWSepsisFU1, A2.count40JahreWSepsisMU1, 
             A2.count50JahreWSepsisFU1, A2.count50JahreWSepsisMU1 ,
             A2.count60JahreWSepsisFU1, A2.count60JahreWSepsisMU1,
             A2.count70JahreWSepsisFU1, A2.count70JahreWSepsisMU1, 
             A2.count80JahreWSepsisFU1, A2.count80JahreWSepsisMU1], #UNIT1
             [A2.count1819WSepsisFU2, A2.count1819WSepsisMU2,                                   
        A2.count20JahreWSepsisFU2, A2.count20JahreWSepsisMU2,
        A2.count30JahreWSepsisFU2, A2.count30JahreWSepsisMU2,        
        A2.count40JahreWSepsisFU2, A2.count40JahreWSepsisMU2,
        A2.count50JahreWSepsisFU2, A2.count50JahreWSepsisMU2,
        A2.count60JahreWSepsisFU2, A2.count60JahreWSepsisMU2,
        A2.count70JahreWSepsisFU2, A2.count70JahreWSepsisMU2,
        A2.count80JahreWSepsisFU2, A2.count80JahreWSepsisMU2], #UNIT2
        [A2.count1819WSepsisFNaN, A2.count1819WSepsisMNaN,                                   
        A2.count20JahreWSepsisFNaN, A2.count20JahreWSepsisMNaN,
        A2.count30JahreWSepsisFNaN, A2.count30JahreWSepsisMNaN,        
        A2.count40JahreWSepsisFNaN, A2.count40JahreWSepsisMNaN,
        A2.count50JahreWSepsisFNaN, A2.count50JahreWSepsisMNaN,
        A2.count60JahreWSepsisFNaN, A2.count60JahreWSepsisMNaN,
        A2.count70JahreWSepsisFNaN, A2.count70JahreWSepsisMNaN,
        A2.count80JahreWSepsisFNaN, A2.count80JahreWSepsisMNaN ]]

       #Without Sepsis
        verarbeitetesListList2 = [
            [A2.count1819WOSepsisFU1, A2.count1819WOSepsisMU1, 
             A2.count20JahreWOSepsisFU1,A2.count20JahreWOSepsisMU1, 
             A2.count30JahreWOSepsisFU1, A2.count30JahreWOSepsisMU1, 
             A2.count40JahreWOSepsisFU1, A2.count40JahreWOSepsisMU1, 
             A2.count50JahreWOSepsisFU1, A2.count50JahreWOSepsisMU1 ,
             A2.count60JahreWOSepsisFU1, A2.count60JahreWOSepsisMU1,
             A2.count70JahreWOSepsisFU1, A2.count70JahreWOSepsisMU1,
             A2.count80JahreWOSepsisFU1, A2.count80JahreWOSepsisMU1], #UNIT1
             [A2.count1819WOSepsisFU2, A2.count1819WOSepsisMU2,                                   
        A2.count20JahreWOSepsisFU2, A2.count20JahreWOSepsisMU2,
        A2.count30JahreWOSepsisFU2, A2.count30JahreWOSepsisMU2,        
        A2.count40JahreWOSepsisFU2, A2.count40JahreWOSepsisMU2,
        A2.count50JahreWOSepsisFU2, A2.count50JahreWOSepsisMU2,
        A2.count60JahreWOSepsisFU2, A2.count60JahreWOSepsisMU2,
        A2.count70JahreWOSepsisFU2, A2.count70JahreWOSepsisMU2,
        A2.count80JahreWOSepsisFU2, A2.count80JahreWOSepsisMU2], #UNIT2
        [A2.count1819WOSepsisFNaN, A2.count1819WOSepsisMNaN,                                   
        A2.count20JahreWOSepsisFNaN, A2.count20JahreWOSepsisMNaN,
        A2.count30JahreWOSepsisFNaN, A2.count30JahreWOSepsisMNaN,        
        A2.count40JahreWOSepsisFNaN, A2.count40JahreWOSepsisMNaN,
        A2.count50JahreWOSepsisFNaN, A2.count50JahreWOSepsisMNaN,
        A2.count60JahreWOSepsisFNaN, A2.count60JahreWOSepsisMNaN,
        A2.count70JahreWOSepsisFNaN, A2.count70JahreWOSepsisMNaN,
        A2.count80JahreWOSepsisFNaN, A2.count80JahreWOSepsisMNaN ]]

        print("Das ist das Array {}", verarbeitetesListList1)
        print("Das ist das Array {}", verarbeitetesListList2)
        print("Werte")


        st.subheader("Unit-Sepsis-Patients-Age-Gender-Diagramm")
        A2.makeUnitSepsisAgeGenderDiagram(verarbeitetesListList1)
        st.write("Beschreibung Unit-Sepsis-Patients-Age-Gender-Diagramm für Sepsis für Datensatz 2")
        st.subheader("Unit-No-Sepsis-Patients-Age-Gender-Diagramm")
        A2.makeUnitNoSepsisAgeGenderDiagram(verarbeitetesListList2)
        st.write("Beschreibung Unit-Sepsis-Patients-Age-Gender-Diagramm für Nicht Sepsis für Datensatz 2")

        #MICU
        sizes1 = [
            (A2.count1819WSepsisFU1*100)/20000,
            (A2.count1819WOSepsisFU1*100)/20000,
            (A2.count20JahreWSepsisFU1*100)/20000,
            (A2.count20JahreWOSepsisFU1*100)/20000,
            (A2.count30JahreWSepsisFU1*100)/20000,
            (A2.count30JahreWOSepsisFU1*100)/20000,
            (A2.count40JahreWSepsisFU1*100)/20000,
            (A2.count40JahreWOSepsisFU1*100)/20000,
            (A2.count50JahreWSepsisFU1*100)/20000,
            (A2.count50JahreWOSepsisFU1*100)/20000,
            (A2.count60JahreWSepsisFU1*100)/20000,
            (A2.count60JahreWOSepsisFU1*100)/20000,
            (A2.count70JahreWSepsisFU1*100)/20000,
            (A2.count70JahreWOSepsisFU1*100)/20000,
            (A2.count80JahreWSepsisFU1*100)/20000,
            (A2.count80JahreWOSepsisFU1*100)/20000,
            (A2.count1819WSepsisMU1*100)/20000,
            (A2.count1819WOSepsisMU1*100)/20000,   
            (A2.count20JahreWSepsisMU1*100)/20000,
            (A2.count20JahreWOSepsisMU1*100)/20000,
            (A2.count30JahreWSepsisMU1*100)/20000,
            (A2.count30JahreWOSepsisMU1*100)/20000,
            (A2.count40JahreWSepsisMU1*100)/20000,
            (A2.count40JahreWOSepsisMU1*100)/20000,
            (A2.count50JahreWSepsisMU1*100)/20000,
            (A2.count50JahreWOSepsisMU1*100)/20000,
            (A2.count60JahreWSepsisMU1*100)/20000,
            (A2.count60JahreWOSepsisMU1*100)/20000,
            (A2.count70JahreWSepsisMU1*100)/20000,
            (A2.count70JahreWOSepsisMU1*100)/20000,
            (A2.count80JahreWSepsisMU1*100)/20000,
            (A2.count80JahreWOSepsisMU1*100)/20000,            
            ]
        st.subheader("MICU: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        st.write("Das ist MICU-Beschreibung ICU in Prozent für Datensatz 2 und dass man hier einwenig beschreibt")
        A2.makeMICUDiagram(sizes1)

        
        #SICU
        sizes1 = [
            (A2.count1819WSepsisFU2*100)/20000,
            (A2.count1819WOSepsisFU2*100)/20000,
            (A2.count20JahreWSepsisFU2*100)/20000,
            (A2.count20JahreWOSepsisFU2*100)/20000,
            (A2.count30JahreWSepsisFU2*100)/20000,
            (A2.count30JahreWOSepsisFU2*100)/20000,
            (A2.count40JahreWSepsisFU2*100)/20000,
            (A2.count40JahreWOSepsisFU2*100)/20000,
            (A2.count50JahreWSepsisFU2*100)/20000,
            (A2.count50JahreWOSepsisFU2*100)/20000,
            (A2.count60JahreWSepsisFU2*100)/20000,
            (A2.count60JahreWOSepsisFU2*100)/20000,
            (A2.count70JahreWSepsisFU2*100)/20000,
            (A2.count70JahreWOSepsisFU2*100)/20000,
            (A2.count80JahreWSepsisFU2*100)/20000,
            (A2.count80JahreWOSepsisFU2*100)/20000,
            (A2.count1819WSepsisMU2*100)/20000,
            (A2.count1819WOSepsisMU2*100)/20000,   
            (A2.count20JahreWSepsisMU2*100)/20000,
            (A2.count20JahreWOSepsisMU2*100)/20000,
            (A2.count30JahreWSepsisMU2*100)/20000,
            (A2.count30JahreWOSepsisMU2*100)/20000,
            (A2.count40JahreWSepsisMU2*100)/20000,
            (A2.count40JahreWOSepsisMU2*100)/20000,
            (A2.count50JahreWSepsisMU2*100)/20000,
            (A2.count50JahreWOSepsisMU2*100)/20000,
            (A2.count60JahreWSepsisMU2*100)/20000,
            (A2.count60JahreWOSepsisMU2*100)/20000,
            (A2.count70JahreWSepsisMU2*100)/20000,
            (A2.count70JahreWOSepsisMU2*100)/20000,
            (A2.count80JahreWSepsisMU2*100)/20000,
            (A2.count80JahreWOSepsisMU2*100)/20000,            
            ]
        st.subheader("SICU: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        st.write("Das ist SICU-Beschreibung ICU in Prozent für Datensatz 2 und dass man hier einwenig beschreibt")
        A2.makeSICUDiagram(sizes1)

        #makeNaNDiagram
        sizes1 = [
            (A2.count1819WSepsisFNaN*100)/20000,
            (A2.count1819WOSepsisFNaN*100)/20000,
            (A2.count20JahreWSepsisFNaN*100)/20000,
            (A2.count20JahreWOSepsisFNaN*100)/20000,
            (A2.count30JahreWSepsisFNaN*100)/20000,
            (A2.count30JahreWOSepsisFNaN*100)/20000,
            (A2.count40JahreWSepsisFNaN*100)/20000,
            (A2.count40JahreWOSepsisFNaN*100)/20000,
            (A2.count50JahreWSepsisFNaN*100)/20000,
            (A2.count50JahreWOSepsisFNaN*100)/20000,
            (A2.count60JahreWSepsisFNaN*100)/20000,
            (A2.count60JahreWOSepsisFNaN*100)/20000,
            (A2.count70JahreWSepsisFNaN*100)/20000,
            (A2.count70JahreWOSepsisFNaN*100)/20000,
            (A2.count80JahreWSepsisFNaN*100)/20000,
            (A2.count80JahreWOSepsisFNaN*100)/20000,
            (A2.count1819WSepsisMNaN*100)/20000,
            (A2.count1819WOSepsisMNaN*100)/20000,   
            (A2.count20JahreWSepsisMNaN*100)/20000,
            (A2.count20JahreWOSepsisMNaN*100)/20000,
            (A2.count30JahreWSepsisMNaN*100)/20000,
            (A2.count30JahreWOSepsisMNaN*100)/20000,
            (A2.count40JahreWSepsisMNaN*100)/20000,
            (A2.count40JahreWOSepsisMNaN*100)/20000,
            (A2.count50JahreWSepsisMNaN*100)/20000,
            (A2.count50JahreWOSepsisMNaN*100)/20000,
            (A2.count60JahreWSepsisMNaN*100)/20000,
            (A2.count60JahreWOSepsisMNaN*100)/20000,
            (A2.count70JahreWSepsisMNaN*100)/20000,
            (A2.count70JahreWOSepsisMNaN*100)/20000,
            (A2.count80JahreWSepsisMNaN*100)/20000,
            (A2.count80JahreWOSepsisMNaN*100)/20000,            
            ]
        st.subheader("NaN: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        st.write("Das ist NaN-Beschreibung ICU in Prozent für Datensatz 2 und dass man hier einwenig beschreibt")

        A2.makeNaNDiagram(sizes1)





        #both dataset
    if(intToDecide == 3):
        print("datasetInt: {}", 3)
        A1 = CheckForUnitSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
        A2 = CheckForUnitSepsisGenderAge("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
        A1.getFileNames()
        A2.getFileNames()


        #Sepsis
        verarbeitetesListList1 = [
                [A1.count1819WSepsisFU1 + A2.count1819WSepsisFU1, A1.count1819WSepsisMU1+ A2.count1819WSepsisMU1, 
             A1.count20JahreWSepsisFU1 + A2.count20JahreWSepsisFU1, A1.count20JahreWSepsisMU1 + A2.count20JahreWSepsisMU1, 
             A1.count30JahreWSepsisFU1 + A2.count30JahreWSepsisFU1, A1.count30JahreWSepsisMU1 + A2.count30JahreWSepsisMU1, 
             A1.count40JahreWSepsisFU1 + A2.count40JahreWSepsisFU1, A1.count40JahreWSepsisMU1 + A2.count40JahreWSepsisMU1, 
             A1.count50JahreWSepsisFU1 + A2.count50JahreWSepsisFU1, A1.count50JahreWSepsisMU1 + A2.count50JahreWSepsisMU1, 
             A1.count60JahreWSepsisFU1 + A2.count60JahreWSepsisFU1, A1.count60JahreWSepsisMU1 + A2.count60JahreWSepsisMU1, 
             A1.count70JahreWSepsisFU1 + A2.count70JahreWSepsisFU1, A1.count70JahreWSepsisMU1 + A2.count70JahreWSepsisMU1, 
             A1.count80JahreWSepsisFU1 + A2.count80JahreWSepsisFU1, A1.count80JahreWSepsisMU1 + A2.count80JahreWSepsisMU1], #UNIT1
                [A1.count1819WSepsisFU2 + A2.count1819WSepsisFU2, A1.count1819WSepsisMU2+ A2.count1819WSepsisMU2, 
             A1.count20JahreWSepsisFU2 + A2.count20JahreWSepsisFU2, A1.count20JahreWSepsisMU2 + A2.count20JahreWSepsisMU2, 
             A1.count30JahreWSepsisFU2 + A2.count30JahreWSepsisFU2, A1.count30JahreWSepsisMU2 + A2.count30JahreWSepsisMU2, 
             A1.count40JahreWSepsisFU2 + A2.count40JahreWSepsisFU2, A1.count40JahreWSepsisMU2 + A2.count40JahreWSepsisMU2, 
             A1.count50JahreWSepsisFU2 + A2.count50JahreWSepsisFU2, A1.count50JahreWSepsisMU2 + A2.count50JahreWSepsisMU2, 
             A1.count60JahreWSepsisFU2 + A2.count60JahreWSepsisFU2, A1.count60JahreWSepsisMU2 + A2.count60JahreWSepsisMU2, 
             A1.count70JahreWSepsisFU2 + A2.count70JahreWSepsisFU2, A1.count70JahreWSepsisMU2 + A2.count70JahreWSepsisMU2, 
             A1.count80JahreWSepsisFU2 + A2.count80JahreWSepsisFU2, A1.count80JahreWSepsisMU2 + A2.count80JahreWSepsisMU2], #UNIT2
                [A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN, A1.count1819WSepsisMNaN+ A2.count1819WSepsisMNaN, 
             A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN, A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN, 
             A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN, A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN, 
             A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN, A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN, 
             A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN, A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN, 
             A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN, A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN, 
             A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN, A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN, 
             A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN, A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN]] #NaN


        #NoSepsis
        verarbeitetesListList2 = [
                [A1.count1819WOSepsisFU1 + A2.count1819WOSepsisFU1, A1.count1819WOSepsisMU1+ A2.count1819WOSepsisMU1, 
             A1.count20JahreWOSepsisFU1 + A2.count20JahreWOSepsisFU1, A1.count20JahreWOSepsisMU1 + A2.count20JahreWOSepsisMU1, 
             A1.count30JahreWOSepsisFU1 + A2.count30JahreWOSepsisFU1, A1.count30JahreWOSepsisMU1 + A2.count30JahreWOSepsisMU1, 
             A1.count40JahreWOSepsisFU1 + A2.count40JahreWOSepsisFU1, A1.count40JahreWOSepsisMU1 + A2.count40JahreWOSepsisMU1, 
             A1.count50JahreWOSepsisFU1 + A2.count50JahreWOSepsisFU1, A1.count50JahreWOSepsisMU1 + A2.count50JahreWOSepsisMU1, 
             A1.count60JahreWOSepsisFU1 + A2.count60JahreWOSepsisFU1, A1.count60JahreWOSepsisMU1 + A2.count60JahreWOSepsisMU1, 
             A1.count70JahreWOSepsisFU1 + A2.count70JahreWOSepsisFU1, A1.count70JahreWOSepsisMU1 + A2.count70JahreWOSepsisMU1, 
             A1.count80JahreWOSepsisFU1 + A2.count80JahreWOSepsisFU1, A1.count80JahreWOSepsisMU1 + A2.count80JahreWOSepsisMU1], #UNIT1
                [A1.count1819WOSepsisFU2 + A2.count1819WOSepsisFU2, A1.count1819WOSepsisMU2+ A2.count1819WOSepsisMU2, 
             A1.count20JahreWOSepsisFU2 + A2.count20JahreWOSepsisFU2, A1.count20JahreWOSepsisMU2 + A2.count20JahreWOSepsisMU2, 
             A1.count30JahreWOSepsisFU2 + A2.count30JahreWOSepsisFU2, A1.count30JahreWOSepsisMU2 + A2.count30JahreWOSepsisMU2, 
             A1.count40JahreWOSepsisFU2 + A2.count40JahreWOSepsisFU2, A1.count40JahreWOSepsisMU2 + A2.count40JahreWOSepsisMU2, 
             A1.count50JahreWOSepsisFU2 + A2.count50JahreWOSepsisFU2, A1.count50JahreWOSepsisMU2 + A2.count50JahreWOSepsisMU2, 
             A1.count60JahreWOSepsisFU2 + A2.count60JahreWOSepsisFU2, A1.count60JahreWOSepsisMU2 + A2.count60JahreWOSepsisMU2, 
             A1.count70JahreWOSepsisFU2 + A2.count70JahreWOSepsisFU2, A1.count70JahreWOSepsisMU2 + A2.count70JahreWOSepsisMU2, 
             A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2, A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2], #UNIT2
                [A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN, A1.count1819WOSepsisMNaN+ A2.count1819WOSepsisMNaN, 
             A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN, A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN, 
             A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN, A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN, 
             A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN, A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN, 
             A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN, A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN, 
             A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN, A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN, 
             A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN, A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN, 
             A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN, A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN]] #NaN



        print("Das ist das Array {}", verarbeitetesListList1)
        print("Das ist das Array {}", verarbeitetesListList2)
        print("Werte")
        st.subheader("Visualization: Units with Sepsis Patients")
        st.write("This visualization contains the whole data set. On the x-axis there are three different groups (M-ICU, S-ICU and NaN). A person can have been in only one of the three groups, but not both. All persons are marked here who have sepsis. It can be seen that approximately 2/3 persons with sepsis have been in the ICU, while 1/3 persons have only needed the hospital. Meanwhile, 1/3 of the people with sepsis are divided between M-ICU and S-ICU.")

        A2.makeUnitSepsisAgeGenderDiagram(verarbeitetesListList1)
        st.subheader("Visualization: Units without Sepsis Patients")

        st.write("This visualization also contains the whole data set. The x-axis corresponds as in the diagram above. However, the y-axis is different because the purpose here is to identify the distribution of non-sepsis individuals.  Again, a person may have been in only one of the three groups, but not both. All persons are marked here who do not have sepsis. You can see that here the ICU values are higher than in the previous chart.")

        A2.makeUnitNoSepsisAgeGenderDiagram(verarbeitetesListList2)


        #MICU
        sizes1 = [
            ((A2.count1819WSepsisFU1 + A1.count1819WSepsisFU1)*100)/40336,
            ((A2.count1819WOSepsisFU1 + A1.count1819WOSepsisFU1)*100)/40336,
            ((A2.count20JahreWSepsisFU1 + A1.count20JahreWSepsisFU1)*100)/40336,
            ((A2.count20JahreWOSepsisFU1 + A1.count20JahreWOSepsisFU1)*100)/40336,
            ((A2.count30JahreWSepsisFU1 + A1.count30JahreWSepsisFU1)*100)/40336,
            ((A2.count30JahreWOSepsisFU1 + A1.count30JahreWOSepsisFU1)*100)/40336,
            ((A2.count40JahreWSepsisFU1 + A1.count40JahreWSepsisFU1)*100)/40336,
            ((A2.count40JahreWOSepsisFU1 + A1.count40JahreWOSepsisFU1)*100)/40336,
            ((A2.count50JahreWSepsisFU1 + A1.count50JahreWSepsisFU1)*100)/40336,
            ((A2.count50JahreWOSepsisFU1 + A1.count50JahreWOSepsisFU1)*100)/40336,
            ((A2.count60JahreWSepsisFU1 + A1.count60JahreWSepsisFU1)*100)/40336,
            ((A2.count60JahreWOSepsisFU1 + A1.count60JahreWOSepsisFU1)*100)/40336,
            ((A2.count70JahreWSepsisFU1 + A1.count70JahreWSepsisFU1)*100)/40336,
            ((A2.count70JahreWOSepsisFU1 + A1.count70JahreWOSepsisFU1)*100)/40336,
            ((A2.count80JahreWSepsisFU1 + A1.count80JahreWSepsisFU1 )*100)/40336,
            ((A2.count80JahreWOSepsisFU1 + A1.count80JahreWOSepsisFU1 )*100)/40336,
            ((A2.count1819WSepsisMU1 + A1.count1819WSepsisMU1)*100)/40336,
            ((A2.count1819WOSepsisMU1 + A1.count1819WOSepsisMU1)*100)/40336,   
            ((A2.count20JahreWSepsisMU1 + A1.count20JahreWSepsisMU1  )*100)/40336,
            ((A2.count20JahreWOSepsisMU1 + A1.count20JahreWOSepsisMU1  )*100)/40336,
            ((A2.count30JahreWSepsisMU1 + A1.count30JahreWSepsisMU1 )*100)/40336,
            ((A2.count30JahreWOSepsisMU1 + A1.count30JahreWOSepsisMU1  )*100)/40336,
            ((A2.count40JahreWSepsisMU1 + A1.count40JahreWSepsisMU1  )*100)/40336,
            ((A2.count40JahreWOSepsisMU1 + A1.count40JahreWOSepsisMU1  )*100)/40336,
            ((A2.count50JahreWSepsisMU1 + A1.count50JahreWSepsisMU1  )*100)/40336,
            ((A2.count50JahreWOSepsisMU1 + A1.count50JahreWOSepsisMU1  )*100)/40336,
            ((A2.count60JahreWSepsisMU1 + A1.count60JahreWSepsisMU1  )*100)/40336,
            ((A2.count60JahreWOSepsisMU1 + A1.count60JahreWOSepsisMU1  )*100)/40336,
            ((A2.count70JahreWSepsisMU1 + A1.count70JahreWSepsisMU1  )*100)/40336,
            ((A2.count70JahreWOSepsisMU1 + A1.count70JahreWOSepsisMU1  )*100)/40336,
            ((A2.count80JahreWSepsisMU1 + A1.count80JahreWSepsisMU1  )*100)/40336,
            ((A2.count80JahreWOSepsisMU1 + A1.count80JahreWOSepsisMU1  )*100)/40336,            
            ]
        #st.subheader("MICU: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        #st.write("Das ist MICU-Beschreibung ICU in Prozent für beide Datensätze und dass man hier einwenig beschreibt")
        #st.subheader("Percentage Visualization on ")
        st.subheader("Visualizations on MICU, SICU und NaN in Percentages")
        st.write("The following three graphs each show, in percentage, the patients in each group.")
        A2.makeMICUDiagram(sizes1)
        st.write("The graph below shows the patients who were in the MICU.")
        st.write("Here, the largest male age groups are : ")
        st.write("1) 60-69 men with: 1.12% ")
        st.write("2) 70-79 men with: 0.897%")
        st.write("3) 50-59 men with: 0.823%")
        st.write("Here, the largest female age groups are : ")
        st.write("1) 70-69 women with: 0.831% ")
        st.write("2) 60-69 men with: 0.734%")
        st.write("3) 50-59 women with: 0.628")
        #SICU
        sizes1 = [
            ((A2.count1819WSepsisFU2 + A1.count1819WSepsisFU2)*100)/40336,
            ((A2.count1819WOSepsisFU2 + A1.count1819WOSepsisFU2)*100)/40336,
            ((A2.count20JahreWSepsisFU2 + A1.count20JahreWSepsisFU2)*100)/40336,
            ((A2.count20JahreWOSepsisFU2 + A1.count20JahreWOSepsisFU2)*100)/40336,
            ((A2.count30JahreWSepsisFU2 + A1.count30JahreWSepsisFU2)*100)/40336,
            ((A2.count30JahreWOSepsisFU2 + A1.count30JahreWOSepsisFU2)*100)/40336,
            ((A2.count40JahreWSepsisFU2 + A1.count40JahreWSepsisFU2)*100)/40336,
            ((A2.count40JahreWOSepsisFU2 + A1.count40JahreWOSepsisFU2)*100)/40336,
            ((A2.count50JahreWSepsisFU2 + A1.count50JahreWSepsisFU2)*100)/40336,
            ((A2.count50JahreWOSepsisFU2 + A1.count50JahreWOSepsisFU2)*100)/40336,
            ((A2.count60JahreWSepsisFU2 + A1.count60JahreWSepsisFU2)*100)/40336,
            ((A2.count60JahreWOSepsisFU2 + A1.count60JahreWOSepsisFU2)*100)/40336,
            ((A2.count70JahreWSepsisFU2 + A1.count70JahreWSepsisFU2)*100)/40336,
            ((A2.count70JahreWOSepsisFU2 + A1.count70JahreWOSepsisFU2)*100)/40336,
            ((A2.count80JahreWSepsisFU2 + A1.count80JahreWSepsisFU2 )*100)/40336,
            ((A2.count80JahreWOSepsisFU2 + A1.count80JahreWOSepsisFU2 )*100)/40336,
            ((A2.count1819WSepsisMU2 + A1.count1819WSepsisMU2)*100)/40336,
            ((A2.count1819WOSepsisMU2 + A1.count1819WOSepsisMU2)*100)/40336,   
            ((A2.count20JahreWSepsisMU2 + A1.count20JahreWSepsisMU2  )*100)/40336,
            ((A2.count20JahreWOSepsisMU2 + A1.count20JahreWOSepsisMU2  )*100)/40336,
            ((A2.count30JahreWSepsisMU2 + A1.count30JahreWSepsisMU2 )*100)/40336,
            ((A2.count30JahreWOSepsisMU2 + A1.count30JahreWOSepsisMU2  )*100)/40336,
            ((A2.count40JahreWSepsisMU2 + A1.count40JahreWSepsisMU2  )*100)/40336,
            ((A2.count40JahreWOSepsisMU2 + A1.count40JahreWOSepsisMU2  )*100)/40336,
            ((A2.count50JahreWSepsisMU2 + A1.count50JahreWSepsisMU2  )*100)/40336,
            ((A2.count50JahreWOSepsisMU2 + A1.count50JahreWOSepsisMU2  )*100)/40336,
            ((A2.count60JahreWSepsisMU2 + A1.count60JahreWSepsisMU2  )*100)/40336,
            ((A2.count60JahreWOSepsisMU2 + A1.count60JahreWOSepsisMU2  )*100)/40336,
            ((A2.count70JahreWSepsisMU2 + A1.count70JahreWSepsisMU2  )*100)/40336,
            ((A2.count70JahreWOSepsisMU2 + A1.count70JahreWOSepsisMU2  )*100)/40336,
            ((A2.count80JahreWSepsisMU2 + A1.count80JahreWSepsisMU2  )*100)/40336,
            ((A2.count80JahreWOSepsisMU2 + A1.count80JahreWOSepsisMU2  )*100)/40336,                     
            ]
        #st.subheader("SICU: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        #st.write("Das ist SICU-Beschreibung ICU in Prozent für beide Datensätze  und dass man hier einwenig beschreibt")

        A2.makeSICUDiagram(sizes1)
        st.write("This graph below shows the patients who were in the S-ICU.")
        st.write("Here, the largest male age groups are : ")
        st.write("1) 60-69 men with: 0.883% ")
        st.write("2) 70-79 men with: 0.707%")
        st.write("3) 50-59 men with: 0.61%")
        st.write("Here, the largest female age groups are : ")
        st.write("1) 60-69 women with: 0.522% ")
        st.write("2) 70-79 men with: 0.498%")
        st.write("3) women older 80 with: 0.345")

        #makeNaNDiagram
        sizes1 = [
            ((A2.count1819WSepsisFNaN + A1.count1819WSepsisFNaN)*100)/40336,
            ((A2.count1819WOSepsisFNaN + A1.count1819WOSepsisFNaN)*100)/40336,
            ((A2.count20JahreWSepsisFNaN + A1.count20JahreWSepsisFNaN)*100)/40336,
            ((A2.count20JahreWOSepsisFNaN + A1.count20JahreWOSepsisFNaN)*100)/40336,
            ((A2.count30JahreWSepsisFNaN + A1.count30JahreWSepsisFNaN)*100)/40336,
            ((A2.count30JahreWOSepsisFNaN + A1.count30JahreWOSepsisFNaN)*100)/40336,
            ((A2.count40JahreWSepsisFNaN + A1.count40JahreWSepsisFNaN)*100)/40336,
            ((A2.count40JahreWOSepsisFNaN + A1.count40JahreWOSepsisFNaN)*100)/40336,
            ((A2.count50JahreWSepsisFNaN + A1.count50JahreWSepsisFNaN)*100)/40336,
            ((A2.count50JahreWOSepsisFNaN + A1.count50JahreWOSepsisFNaN)*100)/40336,
            ((A2.count60JahreWSepsisFNaN + A1.count60JahreWSepsisFNaN)*100)/40336,
            ((A2.count60JahreWOSepsisFNaN + A1.count60JahreWOSepsisFNaN)*100)/40336,
            ((A2.count70JahreWSepsisFNaN + A1.count70JahreWSepsisFNaN)*100)/40336,
            ((A2.count70JahreWOSepsisFNaN + A1.count70JahreWOSepsisFNaN)*100)/40336,
            ((A2.count80JahreWSepsisFNaN + A1.count80JahreWSepsisFNaN )*100)/40336,
            ((A2.count80JahreWOSepsisFNaN + A1.count80JahreWOSepsisFNaN )*100)/40336,
            ((A2.count1819WSepsisMNaN + A1.count1819WSepsisMNaN)*100)/40336,
            ((A2.count1819WOSepsisMNaN + A1.count1819WOSepsisMNaN)*100)/40336,   
            ((A2.count20JahreWSepsisMNaN + A1.count20JahreWSepsisMNaN  )*100)/40336,
            ((A2.count20JahreWOSepsisMNaN + A1.count20JahreWOSepsisMNaN  )*100)/40336,
            ((A2.count30JahreWSepsisMNaN + A1.count30JahreWSepsisMNaN )*100)/40336,
            ((A2.count30JahreWOSepsisMNaN + A1.count30JahreWOSepsisMNaN  )*100)/40336,
            ((A2.count40JahreWSepsisMNaN + A1.count40JahreWSepsisMNaN  )*100)/40336,
            ((A2.count40JahreWOSepsisMNaN + A1.count40JahreWOSepsisMNaN  )*100)/40336,
            ((A2.count50JahreWSepsisMNaN + A1.count50JahreWSepsisMNaN  )*100)/40336,
            ((A2.count50JahreWOSepsisMNaN + A1.count50JahreWOSepsisMNaN  )*100)/40336,
            ((A2.count60JahreWSepsisMNaN + A1.count60JahreWSepsisMNaN  )*100)/40336,
            ((A2.count60JahreWOSepsisMNaN + A1.count60JahreWOSepsisMNaN  )*100)/40336,
            ((A2.count70JahreWSepsisMNaN + A1.count70JahreWSepsisMNaN  )*100)/40336,
            ((A2.count70JahreWOSepsisMNaN + A1.count70JahreWOSepsisMNaN  )*100)/40336,
            ((A2.count80JahreWSepsisMNaN + A1.count80JahreWSepsisMNaN  )*100)/40336,
            ((A2.count80JahreWOSepsisMNaN + A1.count80JahreWOSepsisMNaN  )*100)/40336,                 
            ]
        #st.subheader("NaN: Unit-Sepsis-Patients-Age-Gender-Diagramm in percentage")
        #st.write("Das ist NaN-Beschreibung ICU in Prozent für beide Datensätze und dass man hier einwenig beschreibt")
        A2.makeNaNDiagram(sizes1)
        st.write("This graph below shows the patients who were in no ICU.")
        st.write("Here, the largest male age groups are : ")
        st.write("1) 60-69 men with: 1.14% ")
        st.write("2) 70-79 men with: 1.08%")
        st.write("3) 50-59 men with: 1.06%")
        st.write("Here, the largest female age groups are : ")
        st.write("1) 70-79 women with: 0.858% ")
        st.write("2) 60-69 women with: 0.698%")
        st.write("3) women older 80 with: 0.589%")

        #print("HIIIIIIIIIIIIIIIIER")
        #print("FRAU")
        #allgemein
        #print("MICU Anzahl von Frauen: ", A1.countAllUnit1Female + A2.countAllUnit1Female)
        #print("MICU Anzahl von Frauen mit Sepsis: ", A1.countAllUnit1FemaleSepsis + A2.countAllUnit1FemaleSepsis)
        #print("MICU Anzahl von Frauen ohne Sepsis: ", A1.countAllUnit1FemaleNoSepsis + A2.countAllUnit1FemaleNoSepsis)
        #print("MICU Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in MICU waren (und nicht in SICU und NaN)): F:A: ", (((A1.countAllUnit1Female + A2.countAllUnit1Female)* 100)/40336))
        #print("MICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von MICU Sepsis haben): F:A  ", (((A1.countAllUnit1FemaleSepsis+ A2.countAllUnit1FemaleSepsis)*100)/40336))
        #print("MICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von MICU nicht Sepsis haben): F:A ",(((A1.countAllUnit1FemaleNoSepsis+ A2.countAllUnit1FemaleNoSepsis)*100)/40336))
        #print("MICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von MICU Sepsis haben): ", (((A1.countAllUnit1FemaleSepsis+ A2.countAllUnit1FemaleSepsis)*100)/(A1.countAllUnit1Female+A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von MICU nicht Sepsis haben): ",(((A1.countAllUnit1FemaleNoSepsis+ A2.countAllUnit1FemaleNoSepsis)*100)/(A1.countAllUnit1Female+ A2.countAllUnit1Female)))

        #unter 20
        #print("MICU Anzahl von Frauen unter 20: ", A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1+A2.count1819WSepsisFU1 +A2.count1819WOSepsisFU1)
        #print("MICU Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFU1 + A2.count1819WSepsisFU1)
        #print("MICU Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFU1 + A2.count1819WOSepsisFU1)
        #print("MICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count1819WSepsisFU1 + A1.count1819WOSepsisFU1 + A2.count1819WSepsisFU1 + A2.count1819WOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisFU1 + A2.count1819WSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisFU1 + A2.count1819WOSepsisFU1) * 100)/(40336)))
        #print("MICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von MICU Sepsis haben) F:F:A ", (((A1.count1819WSepsisFU1+ A2.count1819WSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von MICU Sepsis haben) F:F:A ", (((A1.count1819WOSepsisFU1 + A2.count1819WOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von MICU Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisFU1 + A2.count1819WSepsisFU1)*100)/ (A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1 + A2.count1819WSepsisFU1 + A2.count1819WOSepsisFU1)))
        #print("MICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von MICU nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisFU1 + A2.count1819WOSepsisFU1)*100)/ (A1.count1819WSepsisFU1 +A1.count1819WOSepsisFU1 +A2.count1819WSepsisFU1 + A2.count1819WOSepsisFU1)))

        #zwischen 20-29
        #print("MICU Anzahl von Frauen zwischen 20-29: ", A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1+A2.count20JahreWSepsisFU1 +A2.count20JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFU1 + A2.count20JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFU1 + A2.count20JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count20JahreWSepsisFU1 + A1.count20JahreWOSepsisFU1 + A2.count20JahreWSepsisFU1 + A2.count20JahreWOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisFU1 + A2.count20JahreWSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisFU1 + A2.count20JahreWOSepsisFU1) * 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisFU1+ A2.count20JahreWSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisFU1 + A2.count20JahreWOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von MICU Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisFU1 + A2.count20JahreWSepsisFU1)*100)/ (A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1 + A2.count20JahreWSepsisFU1 + A2.count20JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von MICU nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisFU1 + A2.count20JahreWOSepsisFU1)*100)/ (A1.count20JahreWSepsisFU1 +A1.count20JahreWOSepsisFU1 +A2.count20JahreWSepsisFU1 + A2.count20JahreWOSepsisFU1)))
 
        #zwischen 30-39
        #print("MICU Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1+A2.count30JahreWSepsisFU1 +A2.count30JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFU1 + A2.count30JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFU1 + A2.count30JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count30JahreWSepsisFU1 + A1.count30JahreWOSepsisFU1 + A2.count30JahreWSepsisFU1 + A2.count30JahreWOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisFU1 + A2.count30JahreWSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisFU1 + A2.count30JahreWOSepsisFU1) * 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von MICU Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisFU1+ A2.count30JahreWSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von MICU Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisFU1 + A2.count30JahreWOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von MICU Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisFU1 + A2.count30JahreWSepsisFU1)*100)/ (A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1 + A2.count30JahreWSepsisFU1 + A2.count30JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von MICU nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisFU1 + A2.count30JahreWOSepsisFU1)*100)/ (A1.count30JahreWSepsisFU1 +A1.count30JahreWOSepsisFU1 +A2.count30JahreWSepsisFU1 + A2.count30JahreWOSepsisFU1)))
       
        #zwischen 40-49
        #print("MICU Anzahl von Frauen zwischen 40-49: ", A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1+A2.count40JahreWSepsisFU1 +A2.count40JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFU1 + A2.count40JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFU1 + A2.count40JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count40JahreWSepsisFU1 + A1.count40JahreWOSepsisFU1 + A2.count40JahreWSepsisFU1 + A2.count40JahreWOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisFU1 + A2.count40JahreWSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisFU1 + A2.count40JahreWOSepsisFU1) * 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von MICU Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisFU1+ A2.count40JahreWSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von MICU Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisFU1 + A2.count40JahreWOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von MICU Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisFU1 + A2.count40JahreWSepsisFU1)*100)/ (A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1 + A2.count40JahreWSepsisFU1 + A2.count40JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von MICU nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisFU1 + A2.count40JahreWOSepsisFU1)*100)/ (A1.count40JahreWSepsisFU1 +A1.count40JahreWOSepsisFU1 +A2.count40JahreWSepsisFU1 + A2.count40JahreWOSepsisFU1)))
 
        #zwischen 50-59
        #print("MICU Anzahl von Frauen zwischen 50-59: ", A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1+A2.count50JahreWSepsisFU1 +A2.count50JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFU1 + A2.count50JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFU1 + A2.count50JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count50JahreWSepsisFU1 + A1.count50JahreWOSepsisFU1 + A2.count50JahreWSepsisFU1 + A2.count50JahreWOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisFU1 + A2.count50JahreWSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisFU1 + A2.count50JahreWOSepsisFU1) * 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von MICU Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisFU1+ A2.count50JahreWSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von MICU Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisFU1 + A2.count50JahreWOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von MICU Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisFU1 + A2.count50JahreWSepsisFU1)*100)/ (A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1 + A2.count50JahreWSepsisFU1 + A2.count50JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von MICU nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisFU1 + A2.count50JahreWOSepsisFU1)*100)/ (A1.count50JahreWSepsisFU1 +A1.count50JahreWOSepsisFU1 +A2.count50JahreWSepsisFU1 + A2.count50JahreWOSepsisFU1)))
  
        #zwischen 60-69
        #print("MICU Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1+A2.count60JahreWSepsisFU1 +A2.count60JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFU1 + A2.count60JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFU1 + A2.count60JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count60JahreWSepsisFU1 + A1.count60JahreWOSepsisFU1 + A2.count60JahreWSepsisFU1 + A2.count60JahreWOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisFU1 + A2.count60JahreWSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisFU1 + A2.count60JahreWOSepsisFU1) * 100)/(40336)))
        #print("MICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von MICU Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisFU1+ A2.count60JahreWSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von MICU Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisFU1 + A2.count60JahreWOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von MICU Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisFU1 + A2.count60JahreWSepsisFU1)*100)/ (A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1 + A2.count60JahreWSepsisFU1 + A2.count60JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von MICU nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisFU1 + A2.count60JahreWOSepsisFU1)*100)/ (A1.count60JahreWSepsisFU1 +A1.count60JahreWOSepsisFU1 +A2.count60JahreWSepsisFU1 + A2.count60JahreWOSepsisFU1)))
        #zwischen 70-79
        #print("MICU Anzahl von Frauen zwischen 70-79: ", A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1+A2.count70JahreWSepsisFU1 +A2.count70JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFU1 + A2.count70JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFU1 + A2.count70JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count70JahreWSepsisFU1 + A1.count70JahreWOSepsisFU1 + A2.count70JahreWSepsisFU1 + A2.count70JahreWOSepsisFU1) * 100)/70336))
        #print("MICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisFU1 + A2.count70JahreWSepsisFU1)* 100)/(70336)))
        #print("MICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisFU1 + A2.count70JahreWOSepsisFU1) * 100)/(70336)))
        #print("MICU Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von MICU Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisFU1+ A2.count70JahreWSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von MICU Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisFU1 + A2.count70JahreWOSepsisFU1)*100)/ (A1.countAllUnit1Female + A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von MICU Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisFU1 + A2.count70JahreWSepsisFU1)*100)/ (A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1 + A2.count70JahreWSepsisFU1 + A2.count70JahreWOSepsisFU1)))
        #print("MICU Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von MICU nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisFU1 + A2.count70JahreWOSepsisFU1)*100)/ (A1.count70JahreWSepsisFU1 +A1.count70JahreWOSepsisFU1 +A2.count70JahreWSepsisFU1 + A2.count70JahreWOSepsisFU1)))
 
        #älter 80
        #print("MICU Anzahl von Frauen älter 80: ", A1.count80JahreWSepsisFU1 +A1.count80JahreWOSepsisFU1+A2.count80JahreWSepsisFU1 +A2.count80JahreWOSepsisFU1)
        #print("MICU Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFU1 + A2.count80JahreWSepsisFU1)
        #print("MICU Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFU1 + A2.count80JahreWOSepsisFU1)
        #print("MICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count80JahreWSepsisFU1 + A1.count80JahreWOSepsisFU1 + A2.count80JahreWSepsisFU1 + A2.count80JahreWOSepsisFU1) * 100)/40336))
        #print("MICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisFU1 + A2.count80JahreWSepsisFU1)* 100)/(40336)))
        #print("MICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisFU1 + A2.count80JahreWOSepsisFU1) * 100)/(40336)))
        #print("MICU Anzahl von Frauen: ", A1.countAllUnit1Female + A2.countAllUnit1Female)
        #print("MICU Anzahl von Frauen mit Sepsis: ", A1.countAllUnit1FemaleSepsis + A2.countAllUnit1FemaleSepsis)
        #print("MICU Anzahl von Frauen ohne Sepsis: ", A1.countAllUnit1FemaleNoSepsis + A2.countAllUnit1FemaleNoSepsis)
        #print("MICU Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in MICU waren (und nicht in SICU und NaN)): F:A: ", (((A1.countAllUnit1Female + A2.countAllUnit1Female)* 100)/40336))
        #print("MICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von MICU Sepsis haben): F:A  ", (((A1.countAllUnit1FemaleSepsis+ A2.countAllUnit1FemaleSepsis)*100)/40336))
        #print("MICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von MICU nicht Sepsis haben): F:A ",(((A1.countAllUnit1FemaleNoSepsis+ A2.countAllUnit1FemaleNoSepsis)*100)/40336))
        #print("MICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von MICU Sepsis haben): ", (((A1.countAllUnit1FemaleSepsis+ A2.countAllUnit1FemaleSepsis)*100)/(A1.countAllUnit1Female+A2.countAllUnit1Female)))
        #print("MICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von MICU nicht Sepsis haben): ",(((A1.countAllUnit1FemaleNoSepsis+ A2.countAllUnit1FemaleNoSepsis)*100)/(A1.countAllUnit1Female+ A2.countAllUnit1Female)))


        #allgemein
        #print("SICU Anzahl von Frauen: ", A1.countAllUnit2Female + A2.countAllUnit2Female)
        #print("SICU Anzahl von Frauen mit Sepsis: ", A1.countAllUnit2FemaleSepsis + A2.countAllUnit2FemaleSepsis)
        #print("SICU Anzahl von Frauen ohne Sepsis: ", A1.countAllUnit2FemaleNoSepsis + A2.countAllUnit2FemaleNoSepsis)
        #print("SICU Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in SICU waren (und nicht in SICU und NaN)): F:A: ", (((A1.countAllUnit2Female + A2.countAllUnit2Female)* 100)/40336))
        #print("SICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von SICU Sepsis haben): F:A  ", (((A1.countAllUnit2FemaleSepsis+ A2.countAllUnit2FemaleSepsis)*100)/40336))
        #print("SICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von SICU nicht Sepsis haben): F:A ",(((A1.countAllUnit2FemaleNoSepsis+ A2.countAllUnit2FemaleNoSepsis)*100)/40336))
        #print("SICU Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von SICU Sepsis haben): ", (((A1.countAllUnit2FemaleSepsis+ A2.countAllUnit2FemaleSepsis)*100)/(A1.countAllUnit2Female+A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von SICU nicht Sepsis haben): ",(((A1.countAllUnit2FemaleNoSepsis+ A2.countAllUnit2FemaleNoSepsis)*100)/(A1.countAllUnit2Female+ A2.countAllUnit2Female)))

        #unter 20
        #print("SICU Anzahl von Frauen unter 20: ", A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2+A2.count1819WSepsisFU2 +A2.count1819WOSepsisFU2)
        #print("SICU Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFU2 + A2.count1819WSepsisFU2)
        #print("SICU Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFU2 + A2.count1819WOSepsisFU2)
        #print("SICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count1819WSepsisFU2 + A1.count1819WOSepsisFU2 + A2.count1819WSepsisFU2 + A2.count1819WOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisFU2 + A2.count1819WSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisFU2 + A2.count1819WOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von SICU Sepsis haben) F:F:A ", (((A1.count1819WSepsisFU2+ A2.count1819WSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von SICU Sepsis haben) F:F:A ", (((A1.count1819WOSepsisFU2 + A2.count1819WOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von SICU Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisFU2 + A2.count1819WSepsisFU2)*100)/ (A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2 + A2.count1819WSepsisFU2 + A2.count1819WOSepsisFU2)))
        #print("SICU Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von SICU nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisFU2 + A2.count1819WOSepsisFU2)*100)/ (A1.count1819WSepsisFU2 +A1.count1819WOSepsisFU2 +A2.count1819WSepsisFU2 + A2.count1819WOSepsisFU2)))

        #zwischen 20-29
        #print("SICU Anzahl von Frauen zwischen 20-29: ", A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2+A2.count20JahreWSepsisFU2 +A2.count20JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFU2 + A2.count20JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFU2 + A2.count20JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count20JahreWSepsisFU2 + A1.count20JahreWOSepsisFU2 + A2.count20JahreWSepsisFU2 + A2.count20JahreWOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisFU2 + A2.count20JahreWSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisFU2 + A2.count20JahreWOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisFU2+ A2.count20JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisFU2 + A2.count20JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von SICU Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisFU2 + A2.count20JahreWSepsisFU2)*100)/ (A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2 + A2.count20JahreWSepsisFU2 + A2.count20JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von SICU nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisFU2 + A2.count20JahreWOSepsisFU2)*100)/ (A1.count20JahreWSepsisFU2 +A1.count20JahreWOSepsisFU2 +A2.count20JahreWSepsisFU2 + A2.count20JahreWOSepsisFU2)))
 
        #zwischen 30-39
        #print("SICU Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2+A2.count30JahreWSepsisFU2 +A2.count30JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFU2 + A2.count30JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFU2 + A2.count30JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count30JahreWSepsisFU2 + A1.count30JahreWOSepsisFU2 + A2.count30JahreWSepsisFU2 + A2.count30JahreWOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisFU2 + A2.count30JahreWSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisFU2 + A2.count30JahreWOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von SICU Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisFU2+ A2.count30JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von SICU Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisFU2 + A2.count30JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von SICU Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisFU2 + A2.count30JahreWSepsisFU2)*100)/ (A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2 + A2.count30JahreWSepsisFU2 + A2.count30JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von SICU nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisFU2 + A2.count30JahreWOSepsisFU2)*100)/ (A1.count30JahreWSepsisFU2 +A1.count30JahreWOSepsisFU2 +A2.count30JahreWSepsisFU2 + A2.count30JahreWOSepsisFU2)))
       
        #zwischen 40-49
        #print("SICU Anzahl von Frauen zwischen 40-49: ", A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2+A2.count40JahreWSepsisFU2 +A2.count40JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFU2 + A2.count40JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFU2 + A2.count40JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count40JahreWSepsisFU2 + A1.count40JahreWOSepsisFU2 + A2.count40JahreWSepsisFU2 + A2.count40JahreWOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisFU2 + A2.count40JahreWSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisFU2 + A2.count40JahreWOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von SICU Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisFU2+ A2.count40JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von SICU Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisFU2 + A2.count40JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von SICU Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisFU2 + A2.count40JahreWSepsisFU2)*100)/ (A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2 + A2.count40JahreWSepsisFU2 + A2.count40JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von SICU nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisFU2 + A2.count40JahreWOSepsisFU2)*100)/ (A1.count40JahreWSepsisFU2 +A1.count40JahreWOSepsisFU2 +A2.count40JahreWSepsisFU2 + A2.count40JahreWOSepsisFU2)))
 
        #zwischen 50-59
        #print("SICU Anzahl von Frauen zwischen 50-59: ", A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2+A2.count50JahreWSepsisFU2 +A2.count50JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFU2 + A2.count50JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFU2 + A2.count50JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count50JahreWSepsisFU2 + A1.count50JahreWOSepsisFU2 + A2.count50JahreWSepsisFU2 + A2.count50JahreWOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisFU2 + A2.count50JahreWSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisFU2 + A2.count50JahreWOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von SICU Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisFU2+ A2.count50JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von SICU Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisFU2 + A2.count50JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von SICU Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisFU2 + A2.count50JahreWSepsisFU2)*100)/ (A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2 + A2.count50JahreWSepsisFU2 + A2.count50JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von SICU nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisFU2 + A2.count50JahreWOSepsisFU2)*100)/ (A1.count50JahreWSepsisFU2 +A1.count50JahreWOSepsisFU2 +A2.count50JahreWSepsisFU2 + A2.count50JahreWOSepsisFU2)))
  
        #zwischen 60-69
        #print("SICU Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2+A2.count60JahreWSepsisFU2 +A2.count60JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFU2 + A2.count60JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFU2 + A2.count60JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count60JahreWSepsisFU2 + A1.count60JahreWOSepsisFU2 + A2.count60JahreWSepsisFU2 + A2.count60JahreWOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisFU2 + A2.count60JahreWSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisFU2 + A2.count60JahreWOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von SICU Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisFU2+ A2.count60JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von SICU Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisFU2 + A2.count60JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von SICU Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisFU2 + A2.count60JahreWSepsisFU2)*100)/ (A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2 + A2.count60JahreWSepsisFU2 + A2.count60JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von SICU nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisFU2 + A2.count60JahreWOSepsisFU2)*100)/ (A1.count60JahreWSepsisFU2 +A1.count60JahreWOSepsisFU2 +A2.count60JahreWSepsisFU2 + A2.count60JahreWOSepsisFU2)))
        #zwischen 70-79
        #print("SICU Anzahl von Frauen zwischen 70-79: ", A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2+A2.count70JahreWSepsisFU2 +A2.count70JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFU2 + A2.count70JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFU2 + A2.count70JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count70JahreWSepsisFU2 + A1.count70JahreWOSepsisFU2 + A2.count70JahreWSepsisFU2 + A2.count70JahreWOSepsisFU2) * 100)/70336))
        #print("SICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisFU2 + A2.count70JahreWSepsisFU2)* 100)/(70336)))
        #print("SICU Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisFU2 + A2.count70JahreWOSepsisFU2) * 100)/(70336)))
        #print("SICU Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von SICU Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisFU2+ A2.count70JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von SICU Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisFU2 + A2.count70JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von SICU Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisFU2 + A2.count70JahreWSepsisFU2)*100)/ (A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2 + A2.count70JahreWSepsisFU2 + A2.count70JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von SICU nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisFU2 + A2.count70JahreWOSepsisFU2)*100)/ (A1.count70JahreWSepsisFU2 +A1.count70JahreWOSepsisFU2 +A2.count70JahreWSepsisFU2 + A2.count70JahreWOSepsisFU2)))
 
        #älter 80
        #print("SICU Anzahl von Frauen älter 80: ", A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2+A2.count80JahreWSepsisFU2 +A2.count80JahreWOSepsisFU2)
        #print("SICU Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFU2 + A2.count80JahreWSepsisFU2)
        #print("SICU Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2)
        #print("SICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count80JahreWSepsisFU2 + A1.count80JahreWOSepsisFU2 + A2.count80JahreWSepsisFU2 + A2.count80JahreWOSepsisFU2) * 100)/40336))
        #print("SICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisFU2 + A2.count80JahreWSepsisFU2)* 100)/(40336)))
        #print("SICU Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2) * 100)/(40336)))
        #print("SICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von SICU Sepsis haben) F:F:A ", (((A1.count80JahreWSepsisFU2+ A2.count80JahreWSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von SICU Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von SICU Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisFU2 + A2.count80JahreWSepsisFU2)*100)/ (A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2 + A2.count80JahreWSepsisFU2 + A2.count80JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von SICU nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2)*100)/ (A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2 +A2.count80JahreWSepsisFU2 + A2.count80JahreWOSepsisFU2)))
 
        #print("SICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von SICU Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2)*100)/ (A1.countAllUnit2Female + A2.countAllUnit2Female)))
        #print("SICU Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von SICU Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisFU2 + A2.count80JahreWSepsisFU2)*100)/ (A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2 + A2.count80JahreWSepsisFU2 + A2.count80JahreWOSepsisFU2)))
        #print("SICU Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von SICU nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisFU2 + A2.count80JahreWOSepsisFU2)*100)/ (A1.count80JahreWSepsisFU2 +A1.count80JahreWOSepsisFU2 +A2.count80JahreWSepsisFU2 + A2.count80JahreWOSepsisFU2)))
 
        #Unit2


        #NaN
        #print("NaN")
        #allgemein
        #print("NaN Anzahl von Frauen: ", A1.countNoUnitFemale + A2.countNoUnitFemale)
        #print("NaN Anzahl von Frauen mit Sepsis: ", A1.countNoUnitSepFemale + A2.countNoUnitSepFemale)
        #print("NaN Anzahl von Frauen ohne Sepsis: ", A1.countNoUnitNoSepFemale + A2.countNoUnitNoSepFemale)
        #print("NaN Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in NaN waren (und nicht in NaN und NaN)): F:A: ", (((A1.countNoUnitFemale + A2.countNoUnitFemale)* 100)/40336))
        #print("NaN Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von NaN Sepsis haben): F:A  ", (((A1.countNoUnitSepFemale+ A2.countNoUnitSepFemale)*100)/40336))
        #print("NaN Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von NaN nicht Sepsis haben): F:A ",(((A1.countNoUnitNoSepFemale+ A2.countNoUnitNoSepFemale)*100)/40336))
        #print("NaN Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von NaN Sepsis haben): ", (((A1.countNoUnitSepFemale+ A2.countNoUnitSepFemale)*100)/(A1.countNoUnitFemale+A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von NaN nicht Sepsis haben): ",(((A1.countNoUnitNoSepFemale+ A2.countNoUnitNoSepFemale)*100)/(A1.countNoUnitFemale+ A2.countNoUnitFemale)))

        #unter 20
        #print("NaN Anzahl von Frauen unter 20: ", A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN+A2.count1819WSepsisFNaN +A2.count1819WOSepsisFNaN)
        #print("NaN Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN)
        #print("NaN Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN)
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count1819WSepsisFNaN + A1.count1819WOSepsisFNaN + A2.count1819WSepsisFNaN + A2.count1819WOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WSepsisFNaN+ A2.count1819WSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN)*100)/ (A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN + A2.count1819WSepsisFNaN + A2.count1819WOSepsisFNaN)))
        #print("NaN Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von NaN nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN)*100)/ (A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN +A2.count1819WSepsisFNaN + A2.count1819WOSepsisFNaN)))

        #zwischen 20-29
        #print("NaN Anzahl von Frauen zwischen 20-29: ", A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN+A2.count20JahreWSepsisFNaN +A2.count20JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count20JahreWSepsisFNaN + A1.count20JahreWOSepsisFNaN + A2.count20JahreWSepsisFNaN + A2.count20JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisFNaN+ A2.count20JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN)*100)/ (A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN + A2.count20JahreWSepsisFNaN + A2.count20JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN)*100)/ (A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN +A2.count20JahreWSepsisFNaN + A2.count20JahreWOSepsisFNaN)))
 
        #zwischen 30-39
        #print("NaN Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN+A2.count30JahreWSepsisFNaN +A2.count30JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count30JahreWSepsisFNaN + A1.count30JahreWOSepsisFNaN + A2.count30JahreWSepsisFNaN + A2.count30JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisFNaN+ A2.count30JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN)*100)/ (A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN + A2.count30JahreWSepsisFNaN + A2.count30JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von NaN nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN)*100)/ (A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN +A2.count30JahreWSepsisFNaN + A2.count30JahreWOSepsisFNaN)))
       
        #zwischen 40-49
        #print("NaN Anzahl von Frauen zwischen 40-49: ", A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN+A2.count40JahreWSepsisFNaN +A2.count40JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count40JahreWSepsisFNaN + A1.count40JahreWOSepsisFNaN + A2.count40JahreWSepsisFNaN + A2.count40JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisFNaN+ A2.count40JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN)*100)/ (A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN + A2.count40JahreWSepsisFNaN + A2.count40JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von NaN nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN)*100)/ (A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN +A2.count40JahreWSepsisFNaN + A2.count40JahreWOSepsisFNaN)))
 
        #zwischen 50-59
        #print("NaN Anzahl von Frauen zwischen 50-59: ", A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN+A2.count50JahreWSepsisFNaN +A2.count50JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count50JahreWSepsisFNaN + A1.count50JahreWOSepsisFNaN + A2.count50JahreWSepsisFNaN + A2.count50JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisFNaN+ A2.count50JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN)*100)/ (A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN + A2.count50JahreWSepsisFNaN + A2.count50JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von NaN nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN)*100)/ (A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN +A2.count50JahreWSepsisFNaN + A2.count50JahreWOSepsisFNaN)))
  
        #zwischen 60-69
        #print("NaN Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN+A2.count60JahreWSepsisFNaN +A2.count60JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count60JahreWSepsisFNaN + A1.count60JahreWOSepsisFNaN + A2.count60JahreWSepsisFNaN + A2.count60JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisFNaN+ A2.count60JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN)*100)/ (A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN + A2.count60JahreWSepsisFNaN + A2.count60JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von NaN nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN)*100)/ (A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN +A2.count60JahreWSepsisFNaN + A2.count60JahreWOSepsisFNaN)))
        #zwischen 70-79
        #print("NaN Anzahl von Frauen zwischen 70-79: ", A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN+A2.count70JahreWSepsisFNaN +A2.count70JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count70JahreWSepsisFNaN + A1.count70JahreWOSepsisFNaN + A2.count70JahreWSepsisFNaN + A2.count70JahreWOSepsisFNaN) * 100)/70336))
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN)* 100)/(70336)))
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN) * 100)/(70336)))
        #print("NaN Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisFNaN+ A2.count70JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN)*100)/ (A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN + A2.count70JahreWSepsisFNaN + A2.count70JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von NaN nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN)*100)/ (A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN +A2.count70JahreWSepsisFNaN + A2.count70JahreWOSepsisFNaN)))
 
        #älter 80
        #print("NaN Anzahl von Frauen älter 80: ", A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN+A2.count80JahreWSepsisFNaN +A2.count80JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count80JahreWSepsisFNaN + A1.count80JahreWOSepsisFNaN + A2.count80JahreWSepsisFNaN + A2.count80JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWSepsisFNaN+ A2.count80JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN)*100)/ (A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN + A2.count80JahreWSepsisFNaN + A2.count80JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von NaN nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN)*100)/ (A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN +A2.count80JahreWSepsisFNaN + A2.count80JahreWOSepsisFNaN)))
 
        #print("NaN")
        #allgemein
        #print("NaN Anzahl von Frauen: ", A1.countNoUnitFemale + A2.countNoUnitFemale)
        #print("NaN Anzahl von Frauen mit Sepsis: ", A1.countNoUnitSepFemale + A2.countNoUnitSepFemale)
        #print("NaN Anzahl von Frauen ohne Sepsis: ", A1.countNoUnitNoSepFemale + A2.countNoUnitNoSepFemale)
        #print("NaN Prozent von Frauen Allgemein (Wie viele Frauen insgesamt in NaN waren (und nicht in NaN und NaN)): F:A: ", (((A1.countNoUnitFemale + A2.countNoUnitFemale)* 100)/40336))
        #print("NaN Prozent von Frauen mit Sepsis (Wie Viele Frauen von Allgemein von NaN Sepsis haben): F:A  ", (((A1.countNoUnitSepFemale+ A2.countNoUnitSepFemale)*100)/40336))
        #print("NaN Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Allgemein von NaN nicht Sepsis haben): F:A ",(((A1.countNoUnitNoSepFemale+ A2.countNoUnitNoSepFemale)*100)/40336))
        #print("NaN Prozent von Frauen mit Sepsis (Wie Viele Frauen von Frauen von NaN Sepsis haben): ", (((A1.countNoUnitSepFemale+ A2.countNoUnitSepFemale)*100)/(A1.countNoUnitFemale+A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen ohne Sepsis (Wie Viele Frauen von Frauen von NaN nicht Sepsis haben): ",(((A1.countNoUnitNoSepFemale+ A2.countNoUnitNoSepFemale)*100)/(A1.countNoUnitFemale+ A2.countNoUnitFemale)))

        #unter 20
        #print("NaN Anzahl von Frauen unter 20: ", A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN+A2.count1819WSepsisFNaN +A2.count1819WOSepsisFNaN)
        #print("NaN Anzahl von Frauen unter 20 mit Sepsis: ", A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN)
        #print("NaN Anzahl von Frauen unter 20 ohne Sepsis: ",A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN)
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count1819WSepsisFNaN + A1.count1819WOSepsisFNaN + A2.count1819WSepsisFNaN + A2.count1819WOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen unter 20 Allgemein (Wie viele Frauen unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WSepsisFNaN+ A2.count1819WSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen unter 20 mit Sepsis (Wie Viele Frauen unter 20 von NaN Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisFNaN + A2.count1819WSepsisFNaN)*100)/ (A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN + A2.count1819WSepsisFNaN + A2.count1819WOSepsisFNaN)))
        #print("NaN Prozent von Frauen unter 20 ohne Sepsis (Wie Viele Frauen unter 20 von NaN nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisFNaN + A2.count1819WOSepsisFNaN)*100)/ (A1.count1819WSepsisFNaN +A1.count1819WOSepsisFNaN +A2.count1819WSepsisFNaN + A2.count1819WOSepsisFNaN)))

        #zwischen 20-29
        #print("NaN Anzahl von Frauen zwischen 20-29: ", A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN+A2.count20JahreWSepsisFNaN +A2.count20JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count20JahreWSepsisFNaN + A1.count20JahreWOSepsisFNaN + A2.count20JahreWSepsisFNaN + A2.count20JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 20-29 Allgemein (Wie viele Frauen zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisFNaN+ A2.count20JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 20-29 mit Sepsis (Wie Viele Frauen zwischen 20-29 von NaN Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisFNaN + A2.count20JahreWSepsisFNaN)*100)/ (A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN + A2.count20JahreWSepsisFNaN + A2.count20JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 20-29 ohne Sepsis (Wie Viele Frauen zwischen 20-29 von NaN nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisFNaN + A2.count20JahreWOSepsisFNaN)*100)/ (A1.count20JahreWSepsisFNaN +A1.count20JahreWOSepsisFNaN +A2.count20JahreWSepsisFNaN + A2.count20JahreWOSepsisFNaN)))
 
        #zwischen 30-39
        #print("NaN Anzahl von Frauen zwischen 30-39: ", A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN+A2.count30JahreWSepsisFNaN +A2.count30JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count30JahreWSepsisFNaN + A1.count30JahreWOSepsisFNaN + A2.count30JahreWSepsisFNaN + A2.count30JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 30-39 Allgemein (Wie viele Frauen zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisFNaN+ A2.count30JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 30-39 mit Sepsis (Wie Viele Frauen zwischen 30-39 von NaN Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisFNaN + A2.count30JahreWSepsisFNaN)*100)/ (A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN + A2.count30JahreWSepsisFNaN + A2.count30JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 30-39 ohne Sepsis (Wie Viele Frauen zwischen 30-39 von NaN nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisFNaN + A2.count30JahreWOSepsisFNaN)*100)/ (A1.count30JahreWSepsisFNaN +A1.count30JahreWOSepsisFNaN +A2.count30JahreWSepsisFNaN + A2.count30JahreWOSepsisFNaN)))
       
        #zwischen 40-49
        #print("NaN Anzahl von Frauen zwischen 40-49: ", A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN+A2.count40JahreWSepsisFNaN +A2.count40JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count40JahreWSepsisFNaN + A1.count40JahreWOSepsisFNaN + A2.count40JahreWSepsisFNaN + A2.count40JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 40-49 Allgemein (Wie viele Frauen zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisFNaN+ A2.count40JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 40-49 mit Sepsis (Wie Viele Frauen zwischen 40-49 von NaN Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisFNaN + A2.count40JahreWSepsisFNaN)*100)/ (A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN + A2.count40JahreWSepsisFNaN + A2.count40JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 40-49 ohne Sepsis (Wie Viele Frauen zwischen 40-49 von NaN nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisFNaN + A2.count40JahreWOSepsisFNaN)*100)/ (A1.count40JahreWSepsisFNaN +A1.count40JahreWOSepsisFNaN +A2.count40JahreWSepsisFNaN + A2.count40JahreWOSepsisFNaN)))
 
        #zwischen 50-59
        #print("NaN Anzahl von Frauen zwischen 50-59: ", A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN+A2.count50JahreWSepsisFNaN +A2.count50JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count50JahreWSepsisFNaN + A1.count50JahreWOSepsisFNaN + A2.count50JahreWSepsisFNaN + A2.count50JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 50-59 Allgemein (Wie viele Frauen zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisFNaN+ A2.count50JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 50-59 mit Sepsis (Wie Viele Frauen zwischen 50-59 von NaN Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisFNaN + A2.count50JahreWSepsisFNaN)*100)/ (A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN + A2.count50JahreWSepsisFNaN + A2.count50JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 50-59 ohne Sepsis (Wie Viele Frauen zwischen 50-59 von NaN nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisFNaN + A2.count50JahreWOSepsisFNaN)*100)/ (A1.count50JahreWSepsisFNaN +A1.count50JahreWOSepsisFNaN +A2.count50JahreWSepsisFNaN + A2.count50JahreWOSepsisFNaN)))
  
        #zwischen 60-69
        #print("NaN Anzahl von Frauen zwischen 60-69: ", A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN+A2.count60JahreWSepsisFNaN +A2.count60JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count60JahreWSepsisFNaN + A1.count60JahreWOSepsisFNaN + A2.count60JahreWSepsisFNaN + A2.count60JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 60-69 Allgemein (Wie viele Frauen zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisFNaN+ A2.count60JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 60-69 mit Sepsis (Wie Viele Frauen zwischen 60-69 von NaN Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisFNaN + A2.count60JahreWSepsisFNaN)*100)/ (A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN + A2.count60JahreWSepsisFNaN + A2.count60JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 60-69 ohne Sepsis (Wie Viele Frauen zwischen 60-69 von NaN nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisFNaN + A2.count60JahreWOSepsisFNaN)*100)/ (A1.count60JahreWSepsisFNaN +A1.count60JahreWOSepsisFNaN +A2.count60JahreWSepsisFNaN + A2.count60JahreWOSepsisFNaN)))
        #zwischen 70-79
        #print("NaN Anzahl von Frauen zwischen 70-79: ", A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN+A2.count70JahreWSepsisFNaN +A2.count70JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count70JahreWSepsisFNaN + A1.count70JahreWOSepsisFNaN + A2.count70JahreWSepsisFNaN + A2.count70JahreWOSepsisFNaN) * 100)/70336))
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN)* 100)/(70336)))
        #print("NaN Prozent von Frauen zwischen 70-79 Allgemein (Wie viele Frauen zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN) * 100)/(70336)))
        #print("NaN Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisFNaN+ A2.count70JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen zwischen 70-79 mit Sepsis (Wie Viele Frauen zwischen 70-79 von NaN Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisFNaN + A2.count70JahreWSepsisFNaN)*100)/ (A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN + A2.count70JahreWSepsisFNaN + A2.count70JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen zwischen 70-79 ohne Sepsis (Wie Viele Frauen zwischen 70-79 von NaN nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisFNaN + A2.count70JahreWOSepsisFNaN)*100)/ (A1.count70JahreWSepsisFNaN +A1.count70JahreWOSepsisFNaN +A2.count70JahreWSepsisFNaN + A2.count70JahreWOSepsisFNaN)))
 
        #älter 80
        #print("NaN Anzahl von Frauen älter 80: ", A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN+A2.count80JahreWSepsisFNaN +A2.count80JahreWOSepsisFNaN)
        #print("NaN Anzahl von Frauen älter 80 mit Sepsis: ", A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN)
        #print("NaN Anzahl von Frauen älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN)
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count80JahreWSepsisFNaN + A1.count80JahreWOSepsisFNaN + A2.count80JahreWSepsisFNaN + A2.count80JahreWOSepsisFNaN) * 100)/40336))
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN)* 100)/(40336)))
        #print("NaN Prozent von Frauen älter 80 Allgemein (Wie viele Frauen älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN) * 100)/(40336)))
        #print("NaN Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWSepsisFNaN+ A2.count80JahreWSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN)*100)/ (A1.countNoUnitFemale + A2.countNoUnitFemale)))
        #print("NaN Prozent von Frauen älter 80 mit Sepsis (Wie Viele Frauen älter 80 von NaN Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisFNaN + A2.count80JahreWSepsisFNaN)*100)/ (A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN + A2.count80JahreWSepsisFNaN + A2.count80JahreWOSepsisFNaN)))
        #print("NaN Prozent von Frauen älter 80 ohne Sepsis (Wie Viele Frauen älter 80 von NaN nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisFNaN + A2.count80JahreWOSepsisFNaN)*100)/ (A1.count80JahreWSepsisFNaN +A1.count80JahreWOSepsisFNaN +A2.count80JahreWSepsisFNaN + A2.count80JahreWOSepsisFNaN)))
 

        print("HIIIIIIIIIIIIIIIIER")
        print("FRAU")
        #allgemein
        print("MICU Anzahl von Männer: ", A1.countAllUnit1Male + A2.countAllUnit1Male)
        print("MICU Anzahl von Männer mit Sepsis: ", A1.countAllUnit1MaleSepsis + A2.countAllUnit1MaleSepsis)
        print("MICU Anzahl von Männer ohne Sepsis: ", A1.countAllUnit1MaleNoSepsis + A2.countAllUnit1MaleNoSepsis)
        print("MICU Prozent von Männer Allgemein (Wie viele Männer insgesamt in MICU waren (und nicht in SICU und NaN)): F:A: ", (((A1.countAllUnit1Male + A2.countAllUnit1Male)* 100)/40336))
        print("MICU Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von MICU Sepsis haben): F:A  ", (((A1.countAllUnit1MaleSepsis+ A2.countAllUnit1MaleSepsis)*100)/40336))
        print("MICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von MICU nicht Sepsis haben): F:A ",(((A1.countAllUnit1MaleNoSepsis+ A2.countAllUnit1MaleNoSepsis)*100)/40336))
        print("MICU Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von MICU Sepsis haben): ", (((A1.countAllUnit1MaleSepsis+ A2.countAllUnit1MaleSepsis)*100)/(A1.countAllUnit1Male+A2.countAllUnit1Male)))
        print("MICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von MICU nicht Sepsis haben): ",(((A1.countAllUnit1MaleNoSepsis+ A2.countAllUnit1MaleNoSepsis)*100)/(A1.countAllUnit1Male+ A2.countAllUnit1Male)))

        #unter 20
        print("MICU Anzahl von Männer unter 20: ", A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1+A2.count1819WSepsisMU1 +A2.count1819WOSepsisMU1)
        print("MICU Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMU1 + A2.count1819WSepsisMU1)
        print("MICU Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMU1 + A2.count1819WOSepsisMU1)
        print("MICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count1819WSepsisMU1 + A1.count1819WOSepsisMU1 + A2.count1819WSepsisMU1 + A2.count1819WOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisMU1 + A2.count1819WSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisMU1 + A2.count1819WOSepsisMU1) * 100)/(40336)))
        print("MICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von MICU Sepsis haben) F:F:A ", (((A1.count1819WSepsisMU1+ A2.count1819WSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von MICU Sepsis haben) F:F:A ", (((A1.count1819WOSepsisMU1 + A2.count1819WOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von MICU Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisMU1 + A2.count1819WSepsisMU1)*100)/ (A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1 + A2.count1819WSepsisMU1 + A2.count1819WOSepsisMU1)))
        print("MICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von MICU nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisMU1 + A2.count1819WOSepsisMU1)*100)/ (A1.count1819WSepsisMU1 +A1.count1819WOSepsisMU1 +A2.count1819WSepsisMU1 + A2.count1819WOSepsisMU1)))

        #zwischen 20-29
        print("MICU Anzahl von Männer zwischen 20-29: ", A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1+A2.count20JahreWSepsisMU1 +A2.count20JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMU1 + A2.count20JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMU1 + A2.count20JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count20JahreWSepsisMU1 + A1.count20JahreWOSepsisMU1 + A2.count20JahreWSepsisMU1 + A2.count20JahreWOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisMU1 + A2.count20JahreWSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisMU1 + A2.count20JahreWOSepsisMU1) * 100)/(40336)))
        print("MICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisMU1+ A2.count20JahreWSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisMU1 + A2.count20JahreWOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von MICU Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisMU1 + A2.count20JahreWSepsisMU1)*100)/ (A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1 + A2.count20JahreWSepsisMU1 + A2.count20JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von MICU nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisMU1 + A2.count20JahreWOSepsisMU1)*100)/ (A1.count20JahreWSepsisMU1 +A1.count20JahreWOSepsisMU1 +A2.count20JahreWSepsisMU1 + A2.count20JahreWOSepsisMU1)))
 
        #zwischen 30-39
        print("MICU Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1+A2.count30JahreWSepsisMU1 +A2.count30JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMU1 + A2.count30JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMU1 + A2.count30JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count30JahreWSepsisMU1 + A1.count30JahreWOSepsisMU1 + A2.count30JahreWSepsisMU1 + A2.count30JahreWOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisMU1 + A2.count30JahreWSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisMU1 + A2.count30JahreWOSepsisMU1) * 100)/(40336)))
        print("MICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von MICU Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisMU1+ A2.count30JahreWSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von MICU Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisMU1 + A2.count30JahreWOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von MICU Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisMU1 + A2.count30JahreWSepsisMU1)*100)/ (A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1 + A2.count30JahreWSepsisMU1 + A2.count30JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von MICU nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisMU1 + A2.count30JahreWOSepsisMU1)*100)/ (A1.count30JahreWSepsisMU1 +A1.count30JahreWOSepsisMU1 +A2.count30JahreWSepsisMU1 + A2.count30JahreWOSepsisMU1)))
       
        #zwischen 40-49
        print("MICU Anzahl von Männer zwischen 40-49: ", A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1+A2.count40JahreWSepsisMU1 +A2.count40JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMU1 + A2.count40JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMU1 + A2.count40JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count40JahreWSepsisMU1 + A1.count40JahreWOSepsisMU1 + A2.count40JahreWSepsisMU1 + A2.count40JahreWOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisMU1 + A2.count40JahreWSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisMU1 + A2.count40JahreWOSepsisMU1) * 100)/(40336)))
        print("MICU Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von MICU Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisMU1+ A2.count40JahreWSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von MICU Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisMU1 + A2.count40JahreWOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von MICU Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisMU1 + A2.count40JahreWSepsisMU1)*100)/ (A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1 + A2.count40JahreWSepsisMU1 + A2.count40JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von MICU nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisMU1 + A2.count40JahreWOSepsisMU1)*100)/ (A1.count40JahreWSepsisMU1 +A1.count40JahreWOSepsisMU1 +A2.count40JahreWSepsisMU1 + A2.count40JahreWOSepsisMU1)))
 
        #zwischen 50-59
        print("MICU Anzahl von Männer zwischen 50-59: ", A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1+A2.count50JahreWSepsisMU1 +A2.count50JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMU1 + A2.count50JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMU1 + A2.count50JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count50JahreWSepsisMU1 + A1.count50JahreWOSepsisMU1 + A2.count50JahreWSepsisMU1 + A2.count50JahreWOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisMU1 + A2.count50JahreWSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisMU1 + A2.count50JahreWOSepsisMU1) * 100)/(40336)))
        print("MICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von MICU Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisMU1+ A2.count50JahreWSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von MICU Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisMU1 + A2.count50JahreWOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von MICU Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisMU1 + A2.count50JahreWSepsisMU1)*100)/ (A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1 + A2.count50JahreWSepsisMU1 + A2.count50JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von MICU nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisMU1 + A2.count50JahreWOSepsisMU1)*100)/ (A1.count50JahreWSepsisMU1 +A1.count50JahreWOSepsisMU1 +A2.count50JahreWSepsisMU1 + A2.count50JahreWOSepsisMU1)))
  
        #zwischen 60-69
        print("MICU Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1+A2.count60JahreWSepsisMU1 +A2.count60JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMU1 + A2.count60JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMU1 + A2.count60JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count60JahreWSepsisMU1 + A1.count60JahreWOSepsisMU1 + A2.count60JahreWSepsisMU1 + A2.count60JahreWOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisMU1 + A2.count60JahreWSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisMU1 + A2.count60JahreWOSepsisMU1) * 100)/(40336)))
        print("MICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von MICU Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisMU1+ A2.count60JahreWSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von MICU Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisMU1 + A2.count60JahreWOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von MICU Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisMU1 + A2.count60JahreWSepsisMU1)*100)/ (A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1 + A2.count60JahreWSepsisMU1 + A2.count60JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von MICU nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisMU1 + A2.count60JahreWOSepsisMU1)*100)/ (A1.count60JahreWSepsisMU1 +A1.count60JahreWOSepsisMU1 +A2.count60JahreWSepsisMU1 + A2.count60JahreWOSepsisMU1)))
        #zwischen 70-79
        print("MICU Anzahl von Männer zwischen 70-79: ", A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1+A2.count70JahreWSepsisMU1 +A2.count70JahreWOSepsisMU1)
        print("MICU Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMU1 + A2.count70JahreWSepsisMU1)
        print("MICU Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMU1 + A2.count70JahreWOSepsisMU1)
        print("MICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count70JahreWSepsisMU1 + A1.count70JahreWOSepsisMU1 + A2.count70JahreWSepsisMU1 + A2.count70JahreWOSepsisMU1) * 100)/70336))
        print("MICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisMU1 + A2.count70JahreWSepsisMU1)* 100)/(70336)))
        print("MICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisMU1 + A2.count70JahreWOSepsisMU1) * 100)/(70336)))
        print("MICU Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von MICU Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisMU1+ A2.count70JahreWSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von MICU Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisMU1 + A2.count70JahreWOSepsisMU1)*100)/ (A1.countAllUnit1Male + A2.countAllUnit1Male)))
        print("MICU Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von MICU Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisMU1 + A2.count70JahreWSepsisMU1)*100)/ (A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1 + A2.count70JahreWSepsisMU1 + A2.count70JahreWOSepsisMU1)))
        print("MICU Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von MICU nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisMU1 + A2.count70JahreWOSepsisMU1)*100)/ (A1.count70JahreWSepsisMU1 +A1.count70JahreWOSepsisMU1 +A2.count70JahreWSepsisMU1 + A2.count70JahreWOSepsisMU1)))
 
        #älter 80
        print("MICU Anzahl von Männer älter 80: ", A1.count80JahreWSepsisMU1 +A1.count80JahreWOSepsisMU1+A2.count80JahreWSepsisMU1 +A2.count80JahreWOSepsisMU1)
        print("MICU Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMU1 + A2.count80JahreWSepsisMU1)
        print("MICU Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMU1 + A2.count80JahreWOSepsisMU1)
        print("MICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count80JahreWSepsisMU1 + A1.count80JahreWOSepsisMU1 + A2.count80JahreWSepsisMU1 + A2.count80JahreWOSepsisMU1) * 100)/40336))
        print("MICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisMU1 + A2.count80JahreWSepsisMU1)* 100)/(40336)))
        print("MICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in MICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisMU1 + A2.count80JahreWOSepsisMU1) * 100)/(40336)))
        print("MICU Anzahl von Männer: ", A1.countAllUnit1Male + A2.countAllUnit1Male)
        print("MICU Anzahl von Männer mit Sepsis: ", A1.countAllUnit1MaleSepsis + A2.countAllUnit1MaleSepsis)
        print("MICU Anzahl von Männer ohne Sepsis: ", A1.countAllUnit1MaleNoSepsis + A2.countAllUnit1MaleNoSepsis)
        print("MICU Prozent von Männer Allgemein (Wie viele Männer insgesamt in MICU waren (und nicht in SICU und NaN)): F:A: ", (((A1.countAllUnit1Male + A2.countAllUnit1Male)* 100)/40336))
        print("MICU Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von MICU Sepsis haben): F:A  ", (((A1.countAllUnit1MaleSepsis+ A2.countAllUnit1MaleSepsis)*100)/40336))
        print("MICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von MICU nicht Sepsis haben): F:A ",(((A1.countAllUnit1MaleNoSepsis+ A2.countAllUnit1MaleNoSepsis)*100)/40336))
        print("MICU Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von MICU Sepsis haben): ", (((A1.countAllUnit1MaleSepsis+ A2.countAllUnit1MaleSepsis)*100)/(A1.countAllUnit1Male+A2.countAllUnit1Male)))
        print("MICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von MICU nicht Sepsis haben): ",(((A1.countAllUnit1MaleNoSepsis+ A2.countAllUnit1MaleNoSepsis)*100)/(A1.countAllUnit1Male+ A2.countAllUnit1Male)))


        #allgemein
        print("SICU Anzahl von Männer: ", A1.countAllUnit2Male + A2.countAllUnit2Male)
        print("SICU Anzahl von Männer mit Sepsis: ", A1.countAllUnit2MaleSepsis + A2.countAllUnit2MaleSepsis)
        print("SICU Anzahl von Männer ohne Sepsis: ", A1.countAllUnit2MaleNoSepsis + A2.countAllUnit2MaleNoSepsis)
        print("SICU Prozent von Männer Allgemein (Wie viele Männer insgesamt in SICU waren (und nicht in SICU und NaN)): F:A: ", (((A1.countAllUnit2Male + A2.countAllUnit2Male)* 100)/40336))
        print("SICU Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von SICU Sepsis haben): F:A  ", (((A1.countAllUnit2MaleSepsis+ A2.countAllUnit2MaleSepsis)*100)/40336))
        print("SICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von SICU nicht Sepsis haben): F:A ",(((A1.countAllUnit2MaleNoSepsis+ A2.countAllUnit2MaleNoSepsis)*100)/40336))
        print("SICU Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von SICU Sepsis haben): ", (((A1.countAllUnit2MaleSepsis+ A2.countAllUnit2MaleSepsis)*100)/(A1.countAllUnit2Male+A2.countAllUnit2Male)))
        print("SICU Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von SICU nicht Sepsis haben): ",(((A1.countAllUnit2MaleNoSepsis+ A2.countAllUnit2MaleNoSepsis)*100)/(A1.countAllUnit2Male+ A2.countAllUnit2Male)))

        #unter 20
        print("SICU Anzahl von Männer unter 20: ", A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2+A2.count1819WSepsisMU2 +A2.count1819WOSepsisMU2)
        print("SICU Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMU2 + A2.count1819WSepsisMU2)
        print("SICU Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMU2 + A2.count1819WOSepsisMU2)
        print("SICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count1819WSepsisMU2 + A1.count1819WOSepsisMU2 + A2.count1819WSepsisMU2 + A2.count1819WOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisMU2 + A2.count1819WSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisMU2 + A2.count1819WOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von SICU Sepsis haben) F:F:A ", (((A1.count1819WSepsisMU2+ A2.count1819WSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von SICU Sepsis haben) F:F:A ", (((A1.count1819WOSepsisMU2 + A2.count1819WOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von SICU Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisMU2 + A2.count1819WSepsisMU2)*100)/ (A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2 + A2.count1819WSepsisMU2 + A2.count1819WOSepsisMU2)))
        print("SICU Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von SICU nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisMU2 + A2.count1819WOSepsisMU2)*100)/ (A1.count1819WSepsisMU2 +A1.count1819WOSepsisMU2 +A2.count1819WSepsisMU2 + A2.count1819WOSepsisMU2)))

        #zwischen 20-29
        print("SICU Anzahl von Männer zwischen 20-29: ", A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2+A2.count20JahreWSepsisMU2 +A2.count20JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMU2 + A2.count20JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMU2 + A2.count20JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count20JahreWSepsisMU2 + A1.count20JahreWOSepsisMU2 + A2.count20JahreWSepsisMU2 + A2.count20JahreWOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisMU2 + A2.count20JahreWSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisMU2 + A2.count20JahreWOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisMU2+ A2.count20JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisMU2 + A2.count20JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von SICU Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisMU2 + A2.count20JahreWSepsisMU2)*100)/ (A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2 + A2.count20JahreWSepsisMU2 + A2.count20JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von SICU nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisMU2 + A2.count20JahreWOSepsisMU2)*100)/ (A1.count20JahreWSepsisMU2 +A1.count20JahreWOSepsisMU2 +A2.count20JahreWSepsisMU2 + A2.count20JahreWOSepsisMU2)))
 
        #zwischen 30-39
        print("SICU Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2+A2.count30JahreWSepsisMU2 +A2.count30JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMU2 + A2.count30JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMU2 + A2.count30JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count30JahreWSepsisMU2 + A1.count30JahreWOSepsisMU2 + A2.count30JahreWSepsisMU2 + A2.count30JahreWOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisMU2 + A2.count30JahreWSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisMU2 + A2.count30JahreWOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von SICU Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisMU2+ A2.count30JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von SICU Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisMU2 + A2.count30JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von SICU Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisMU2 + A2.count30JahreWSepsisMU2)*100)/ (A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2 + A2.count30JahreWSepsisMU2 + A2.count30JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von SICU nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisMU2 + A2.count30JahreWOSepsisMU2)*100)/ (A1.count30JahreWSepsisMU2 +A1.count30JahreWOSepsisMU2 +A2.count30JahreWSepsisMU2 + A2.count30JahreWOSepsisMU2)))
       
        #zwischen 40-49
        print("SICU Anzahl von Männer zwischen 40-49: ", A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2+A2.count40JahreWSepsisMU2 +A2.count40JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMU2 + A2.count40JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMU2 + A2.count40JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count40JahreWSepsisMU2 + A1.count40JahreWOSepsisMU2 + A2.count40JahreWSepsisMU2 + A2.count40JahreWOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisMU2 + A2.count40JahreWSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisMU2 + A2.count40JahreWOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von SICU Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisMU2+ A2.count40JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von SICU Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisMU2 + A2.count40JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von SICU Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisMU2 + A2.count40JahreWSepsisMU2)*100)/ (A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2 + A2.count40JahreWSepsisMU2 + A2.count40JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von SICU nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisMU2 + A2.count40JahreWOSepsisMU2)*100)/ (A1.count40JahreWSepsisMU2 +A1.count40JahreWOSepsisMU2 +A2.count40JahreWSepsisMU2 + A2.count40JahreWOSepsisMU2)))
 
        #zwischen 50-59
        print("SICU Anzahl von Männer zwischen 50-59: ", A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2+A2.count50JahreWSepsisMU2 +A2.count50JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMU2 + A2.count50JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMU2 + A2.count50JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count50JahreWSepsisMU2 + A1.count50JahreWOSepsisMU2 + A2.count50JahreWSepsisMU2 + A2.count50JahreWOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisMU2 + A2.count50JahreWSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisMU2 + A2.count50JahreWOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von SICU Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisMU2+ A2.count50JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von SICU Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisMU2 + A2.count50JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von SICU Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisMU2 + A2.count50JahreWSepsisMU2)*100)/ (A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2 + A2.count50JahreWSepsisMU2 + A2.count50JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von SICU nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisMU2 + A2.count50JahreWOSepsisMU2)*100)/ (A1.count50JahreWSepsisMU2 +A1.count50JahreWOSepsisMU2 +A2.count50JahreWSepsisMU2 + A2.count50JahreWOSepsisMU2)))
  
        #zwischen 60-69
        print("SICU Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2+A2.count60JahreWSepsisMU2 +A2.count60JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMU2 + A2.count60JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMU2 + A2.count60JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count60JahreWSepsisMU2 + A1.count60JahreWOSepsisMU2 + A2.count60JahreWSepsisMU2 + A2.count60JahreWOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisMU2 + A2.count60JahreWSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisMU2 + A2.count60JahreWOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von SICU Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisMU2+ A2.count60JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von SICU Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisMU2 + A2.count60JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von SICU Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisMU2 + A2.count60JahreWSepsisMU2)*100)/ (A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2 + A2.count60JahreWSepsisMU2 + A2.count60JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von SICU nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisMU2 + A2.count60JahreWOSepsisMU2)*100)/ (A1.count60JahreWSepsisMU2 +A1.count60JahreWOSepsisMU2 +A2.count60JahreWSepsisMU2 + A2.count60JahreWOSepsisMU2)))
        #zwischen 70-79
        print("SICU Anzahl von Männer zwischen 70-79: ", A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2+A2.count70JahreWSepsisMU2 +A2.count70JahreWOSepsisMU2)
        print("SICU Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMU2 + A2.count70JahreWSepsisMU2)
        print("SICU Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMU2 + A2.count70JahreWOSepsisMU2)
        print("SICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count70JahreWSepsisMU2 + A1.count70JahreWOSepsisMU2 + A2.count70JahreWSepsisMU2 + A2.count70JahreWOSepsisMU2) * 100)/70336))
        print("SICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisMU2 + A2.count70JahreWSepsisMU2)* 100)/(70336)))
        print("SICU Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisMU2 + A2.count70JahreWOSepsisMU2) * 100)/(70336)))
        print("SICU Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von SICU Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisMU2+ A2.count70JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von SICU Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisMU2 + A2.count70JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von SICU Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisMU2 + A2.count70JahreWSepsisMU2)*100)/ (A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2 + A2.count70JahreWSepsisMU2 + A2.count70JahreWOSepsisMU2)))
        print("SICU Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von SICU nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisMU2 + A2.count70JahreWOSepsisMU2)*100)/ (A1.count70JahreWSepsisMU2 +A1.count70JahreWOSepsisMU2 +A2.count70JahreWSepsisMU2 + A2.count70JahreWOSepsisMU2)))
 
        #älter 80
        print("SICU Anzahl von Männer älter 80: ", A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2+A2.count80JahreWSepsisMU2 +A2.count80JahreWOSepsisMU2)
        print("SICU Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMU2 + A2.count80JahreWSepsisMU2)
        print("SICU Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2)
        print("SICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)): F:A ", (((A1.count80JahreWSepsisMU2 + A1.count80JahreWOSepsisMU2 + A2.count80JahreWSepsisMU2 + A2.count80JahreWOSepsisMU2) * 100)/40336))
        print("SICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisMU2 + A2.count80JahreWSepsisMU2)* 100)/(40336)))
        print("SICU Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in SICU waren (und nicht in SICU und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2) * 100)/(40336)))
        print("SICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von SICU Sepsis haben) F:F:A ", (((A1.count80JahreWSepsisMU2+ A2.count80JahreWSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von SICU Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von SICU Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisMU2 + A2.count80JahreWSepsisMU2)*100)/ (A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2 + A2.count80JahreWSepsisMU2 + A2.count80JahreWOSepsisMU2)))
        print("SICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von SICU nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2)*100)/ (A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2 +A2.count80JahreWSepsisMU2 + A2.count80JahreWOSepsisMU2)))
 
        print("SICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von SICU Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2)*100)/ (A1.countAllUnit2Male + A2.countAllUnit2Male)))
        print("SICU Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von SICU Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisMU2 + A2.count80JahreWSepsisMU2)*100)/ (A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2 + A2.count80JahreWSepsisMU2 + A2.count80JahreWOSepsisMU2)))
        print("SICU Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von SICU nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisMU2 + A2.count80JahreWOSepsisMU2)*100)/ (A1.count80JahreWSepsisMU2 +A1.count80JahreWOSepsisMU2 +A2.count80JahreWSepsisMU2 + A2.count80JahreWOSepsisMU2)))
 
        #Unit2


        #NaN
        print("NaN")
        #allgemein
        print("NaN Anzahl von Männer: ", A1.countNoUnitMale + A2.countNoUnitMale)
        print("NaN Anzahl von Männer mit Sepsis: ", A1.countNoUnitSepMale + A2.countNoUnitSepMale)
        print("NaN Anzahl von Männer ohne Sepsis: ", A1.countNoUnitNoSepMale + A2.countNoUnitNoSepMale)
        print("NaN Prozent von Männer Allgemein (Wie viele Männer insgesamt in NaN waren (und nicht in NaN und NaN)): F:A: ", (((A1.countNoUnitMale + A2.countNoUnitMale)* 100)/40336))
        print("NaN Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von NaN Sepsis haben): F:A  ", (((A1.countNoUnitSepMale+ A2.countNoUnitSepMale)*100)/40336))
        print("NaN Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von NaN nicht Sepsis haben): F:A ",(((A1.countNoUnitNoSepMale+ A2.countNoUnitNoSepMale)*100)/40336))
        print("NaN Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von NaN Sepsis haben): ", (((A1.countNoUnitSepMale+ A2.countNoUnitSepMale)*100)/(A1.countNoUnitMale+A2.countNoUnitMale)))
        print("NaN Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von NaN nicht Sepsis haben): ",(((A1.countNoUnitNoSepMale+ A2.countNoUnitNoSepMale)*100)/(A1.countNoUnitMale+ A2.countNoUnitMale)))

        #unter 20
        print("NaN Anzahl von Männer unter 20: ", A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN+A2.count1819WSepsisMNaN +A2.count1819WOSepsisMNaN)
        print("NaN Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN)
        print("NaN Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN)
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count1819WSepsisMNaN + A1.count1819WOSepsisMNaN + A2.count1819WSepsisMNaN + A2.count1819WOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WSepsisMNaN+ A2.count1819WSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN)*100)/ (A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN + A2.count1819WSepsisMNaN + A2.count1819WOSepsisMNaN)))
        print("NaN Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von NaN nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN)*100)/ (A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN +A2.count1819WSepsisMNaN + A2.count1819WOSepsisMNaN)))

        #zwischen 20-29
        print("NaN Anzahl von Männer zwischen 20-29: ", A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN+A2.count20JahreWSepsisMNaN +A2.count20JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count20JahreWSepsisMNaN + A1.count20JahreWOSepsisMNaN + A2.count20JahreWSepsisMNaN + A2.count20JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisMNaN+ A2.count20JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN)*100)/ (A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN + A2.count20JahreWSepsisMNaN + A2.count20JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN)*100)/ (A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN +A2.count20JahreWSepsisMNaN + A2.count20JahreWOSepsisMNaN)))
 
        #zwischen 30-39
        print("NaN Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN+A2.count30JahreWSepsisMNaN +A2.count30JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count30JahreWSepsisMNaN + A1.count30JahreWOSepsisMNaN + A2.count30JahreWSepsisMNaN + A2.count30JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisMNaN+ A2.count30JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN)*100)/ (A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN + A2.count30JahreWSepsisMNaN + A2.count30JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von NaN nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN)*100)/ (A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN +A2.count30JahreWSepsisMNaN + A2.count30JahreWOSepsisMNaN)))
       
        #zwischen 40-49
        print("NaN Anzahl von Männer zwischen 40-49: ", A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN+A2.count40JahreWSepsisMNaN +A2.count40JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count40JahreWSepsisMNaN + A1.count40JahreWOSepsisMNaN + A2.count40JahreWSepsisMNaN + A2.count40JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisMNaN+ A2.count40JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN)*100)/ (A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN + A2.count40JahreWSepsisMNaN + A2.count40JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von NaN nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN)*100)/ (A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN +A2.count40JahreWSepsisMNaN + A2.count40JahreWOSepsisMNaN)))
 
        #zwischen 50-59
        print("NaN Anzahl von Männer zwischen 50-59: ", A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN+A2.count50JahreWSepsisMNaN +A2.count50JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count50JahreWSepsisMNaN + A1.count50JahreWOSepsisMNaN + A2.count50JahreWSepsisMNaN + A2.count50JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisMNaN+ A2.count50JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN)*100)/ (A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN + A2.count50JahreWSepsisMNaN + A2.count50JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von NaN nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN)*100)/ (A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN +A2.count50JahreWSepsisMNaN + A2.count50JahreWOSepsisMNaN)))
  
        #zwischen 60-69
        print("NaN Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN+A2.count60JahreWSepsisMNaN +A2.count60JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count60JahreWSepsisMNaN + A1.count60JahreWOSepsisMNaN + A2.count60JahreWSepsisMNaN + A2.count60JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisMNaN+ A2.count60JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN)*100)/ (A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN + A2.count60JahreWSepsisMNaN + A2.count60JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von NaN nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN)*100)/ (A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN +A2.count60JahreWSepsisMNaN + A2.count60JahreWOSepsisMNaN)))
        #zwischen 70-79
        print("NaN Anzahl von Männer zwischen 70-79: ", A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN+A2.count70JahreWSepsisMNaN +A2.count70JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count70JahreWSepsisMNaN + A1.count70JahreWOSepsisMNaN + A2.count70JahreWSepsisMNaN + A2.count70JahreWOSepsisMNaN) * 100)/70336))
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN)* 100)/(70336)))
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN) * 100)/(70336)))
        print("NaN Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisMNaN+ A2.count70JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN)*100)/ (A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN + A2.count70JahreWSepsisMNaN + A2.count70JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von NaN nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN)*100)/ (A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN +A2.count70JahreWSepsisMNaN + A2.count70JahreWOSepsisMNaN)))
 
        #älter 80
        print("NaN Anzahl von Männer älter 80: ", A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN+A2.count80JahreWSepsisMNaN +A2.count80JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN)
        print("NaN Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN)
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count80JahreWSepsisMNaN + A1.count80JahreWOSepsisMNaN + A2.count80JahreWSepsisMNaN + A2.count80JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWSepsisMNaN+ A2.count80JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN)*100)/ (A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN + A2.count80JahreWSepsisMNaN + A2.count80JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von NaN nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN)*100)/ (A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN +A2.count80JahreWSepsisMNaN + A2.count80JahreWOSepsisMNaN)))
 
        print("NaN")
        #allgemein
        print("NaN Anzahl von Männer: ", A1.countNoUnitMale + A2.countNoUnitMale)
        print("NaN Anzahl von Männer mit Sepsis: ", A1.countNoUnitSepMale + A2.countNoUnitSepMale)
        print("NaN Anzahl von Männer ohne Sepsis: ", A1.countNoUnitNoSepMale + A2.countNoUnitNoSepMale)
        print("NaN Prozent von Männer Allgemein (Wie viele Männer insgesamt in NaN waren (und nicht in NaN und NaN)): F:A: ", (((A1.countNoUnitMale + A2.countNoUnitMale)* 100)/40336))
        print("NaN Prozent von Männer mit Sepsis (Wie Viele Männer von Allgemein von NaN Sepsis haben): F:A  ", (((A1.countNoUnitSepMale+ A2.countNoUnitSepMale)*100)/40336))
        print("NaN Prozent von Männer ohne Sepsis (Wie Viele Männer von Allgemein von NaN nicht Sepsis haben): F:A ",(((A1.countNoUnitNoSepMale+ A2.countNoUnitNoSepMale)*100)/40336))
        print("NaN Prozent von Männer mit Sepsis (Wie Viele Männer von Männer von NaN Sepsis haben): ", (((A1.countNoUnitSepMale+ A2.countNoUnitSepMale)*100)/(A1.countNoUnitMale+A2.countNoUnitMale)))
        print("NaN Prozent von Männer ohne Sepsis (Wie Viele Männer von Männer von NaN nicht Sepsis haben): ",(((A1.countNoUnitNoSepMale+ A2.countNoUnitNoSepMale)*100)/(A1.countNoUnitMale+ A2.countNoUnitMale)))

        #unter 20
        print("NaN Anzahl von Männer unter 20: ", A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN+A2.count1819WSepsisMNaN +A2.count1819WOSepsisMNaN)
        print("NaN Anzahl von Männer unter 20 mit Sepsis: ", A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN)
        print("NaN Anzahl von Männer unter 20 ohne Sepsis: ",A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN)
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count1819WSepsisMNaN + A1.count1819WOSepsisMNaN + A2.count1819WSepsisMNaN + A2.count1819WOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer unter 20 Allgemein (Wie viele Männer unter 20 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WSepsisMNaN+ A2.count1819WSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben) F:F:A ", (((A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer unter 20 mit Sepsis (Wie Viele Männer unter 20 von NaN Sepsis haben): F:F:unter 20: ", (((A1.count1819WSepsisMNaN + A2.count1819WSepsisMNaN)*100)/ (A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN + A2.count1819WSepsisMNaN + A2.count1819WOSepsisMNaN)))
        print("NaN Prozent von Männer unter 20 ohne Sepsis (Wie Viele Männer unter 20 von NaN nicht Sepsis haben): F:F:unter 20: ", (((A1.count1819WOSepsisMNaN + A2.count1819WOSepsisMNaN)*100)/ (A1.count1819WSepsisMNaN +A1.count1819WOSepsisMNaN +A2.count1819WSepsisMNaN + A2.count1819WOSepsisMNaN)))

        #zwischen 20-29
        print("NaN Anzahl von Männer zwischen 20-29: ", A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN+A2.count20JahreWSepsisMNaN +A2.count20JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 20-29 mit Sepsis: ", A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 20-29 ohne Sepsis: ",A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count20JahreWSepsisMNaN + A1.count20JahreWOSepsisMNaN + A2.count20JahreWSepsisMNaN + A2.count20JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 20-29 Allgemein (Wie viele Männer zwischen 20-29 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWSepsisMNaN+ A2.count20JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben) F:F:A ", (((A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 20-29 mit Sepsis (Wie Viele Männer zwischen 20-29 von NaN Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWSepsisMNaN + A2.count20JahreWSepsisMNaN)*100)/ (A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN + A2.count20JahreWSepsisMNaN + A2.count20JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 20-29 ohne Sepsis (Wie Viele Männer zwischen 20-29 von NaN nicht Sepsis haben): F:F:zwischen 20-29: ", (((A1.count20JahreWOSepsisMNaN + A2.count20JahreWOSepsisMNaN)*100)/ (A1.count20JahreWSepsisMNaN +A1.count20JahreWOSepsisMNaN +A2.count20JahreWSepsisMNaN + A2.count20JahreWOSepsisMNaN)))
 
        #zwischen 30-39
        print("NaN Anzahl von Männer zwischen 30-39: ", A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN+A2.count30JahreWSepsisMNaN +A2.count30JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 30-39 mit Sepsis: ", A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 30-39 ohne Sepsis: ",A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count30JahreWSepsisMNaN + A1.count30JahreWOSepsisMNaN + A2.count30JahreWSepsisMNaN + A2.count30JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 30-39 Allgemein (Wie viele Männer zwischen 30-39 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWSepsisMNaN+ A2.count30JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben) F:F:A ", (((A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 30-39 mit Sepsis (Wie Viele Männer zwischen 30-39 von NaN Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWSepsisMNaN + A2.count30JahreWSepsisMNaN)*100)/ (A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN + A2.count30JahreWSepsisMNaN + A2.count30JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 30-39 ohne Sepsis (Wie Viele Männer zwischen 30-39 von NaN nicht Sepsis haben): F:F:zwischen 30-39: ", (((A1.count30JahreWOSepsisMNaN + A2.count30JahreWOSepsisMNaN)*100)/ (A1.count30JahreWSepsisMNaN +A1.count30JahreWOSepsisMNaN +A2.count30JahreWSepsisMNaN + A2.count30JahreWOSepsisMNaN)))
       
        #zwischen 40-49
        print("NaN Anzahl von Männer zwischen 40-49: ", A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN+A2.count40JahreWSepsisMNaN +A2.count40JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 40-49 mit Sepsis: ", A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 40-49 ohne Sepsis: ",A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count40JahreWSepsisMNaN + A1.count40JahreWOSepsisMNaN + A2.count40JahreWSepsisMNaN + A2.count40JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 40-49 Allgemein (Wie viele Männer zwischen 40-49 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWSepsisMNaN+ A2.count40JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben) F:F:A ", (((A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 40-49 mit Sepsis (Wie Viele Männer zwischen 40-49 von NaN Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWSepsisMNaN + A2.count40JahreWSepsisMNaN)*100)/ (A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN + A2.count40JahreWSepsisMNaN + A2.count40JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 40-49 ohne Sepsis (Wie Viele Männer zwischen 40-49 von NaN nicht Sepsis haben): F:F:zwischen 40-49: ", (((A1.count40JahreWOSepsisMNaN + A2.count40JahreWOSepsisMNaN)*100)/ (A1.count40JahreWSepsisMNaN +A1.count40JahreWOSepsisMNaN +A2.count40JahreWSepsisMNaN + A2.count40JahreWOSepsisMNaN)))
 
        #zwischen 50-59
        print("NaN Anzahl von Männer zwischen 50-59: ", A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN+A2.count50JahreWSepsisMNaN +A2.count50JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 50-59 mit Sepsis: ", A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 50-59 ohne Sepsis: ",A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count50JahreWSepsisMNaN + A1.count50JahreWOSepsisMNaN + A2.count50JahreWSepsisMNaN + A2.count50JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 50-59 Allgemein (Wie viele Männer zwischen 50-59 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWSepsisMNaN+ A2.count50JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben) F:F:A ", (((A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 50-59 mit Sepsis (Wie Viele Männer zwischen 50-59 von NaN Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWSepsisMNaN + A2.count50JahreWSepsisMNaN)*100)/ (A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN + A2.count50JahreWSepsisMNaN + A2.count50JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 50-59 ohne Sepsis (Wie Viele Männer zwischen 50-59 von NaN nicht Sepsis haben): F:F:zwischen 50-59: ", (((A1.count50JahreWOSepsisMNaN + A2.count50JahreWOSepsisMNaN)*100)/ (A1.count50JahreWSepsisMNaN +A1.count50JahreWOSepsisMNaN +A2.count50JahreWSepsisMNaN + A2.count50JahreWOSepsisMNaN)))
  
        #zwischen 60-69
        print("NaN Anzahl von Männer zwischen 60-69: ", A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN+A2.count60JahreWSepsisMNaN +A2.count60JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 60-69 mit Sepsis: ", A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 60-69 ohne Sepsis: ",A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count60JahreWSepsisMNaN + A1.count60JahreWOSepsisMNaN + A2.count60JahreWSepsisMNaN + A2.count60JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer zwischen 60-69 Allgemein (Wie viele Männer zwischen 60-69 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWSepsisMNaN+ A2.count60JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben) F:F:A ", (((A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 60-69 mit Sepsis (Wie Viele Männer zwischen 60-69 von NaN Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWSepsisMNaN + A2.count60JahreWSepsisMNaN)*100)/ (A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN + A2.count60JahreWSepsisMNaN + A2.count60JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 60-69 ohne Sepsis (Wie Viele Männer zwischen 60-69 von NaN nicht Sepsis haben): F:F:zwischen 60-69: ", (((A1.count60JahreWOSepsisMNaN + A2.count60JahreWOSepsisMNaN)*100)/ (A1.count60JahreWSepsisMNaN +A1.count60JahreWOSepsisMNaN +A2.count60JahreWSepsisMNaN + A2.count60JahreWOSepsisMNaN)))
        #zwischen 70-79
        print("NaN Anzahl von Männer zwischen 70-79: ", A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN+A2.count70JahreWSepsisMNaN +A2.count70JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 70-79 mit Sepsis: ", A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN)
        print("NaN Anzahl von Männer zwischen 70-79 ohne Sepsis: ",A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN)
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count70JahreWSepsisMNaN + A1.count70JahreWOSepsisMNaN + A2.count70JahreWSepsisMNaN + A2.count70JahreWOSepsisMNaN) * 100)/70336))
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN)* 100)/(70336)))
        print("NaN Prozent von Männer zwischen 70-79 Allgemein (Wie viele Männer zwischen 70-79 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN) * 100)/(70336)))
        print("NaN Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWSepsisMNaN+ A2.count70JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben) F:F:A ", (((A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer zwischen 70-79 mit Sepsis (Wie Viele Männer zwischen 70-79 von NaN Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWSepsisMNaN + A2.count70JahreWSepsisMNaN)*100)/ (A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN + A2.count70JahreWSepsisMNaN + A2.count70JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer zwischen 70-79 ohne Sepsis (Wie Viele Männer zwischen 70-79 von NaN nicht Sepsis haben): F:F:zwischen 70-79: ", (((A1.count70JahreWOSepsisMNaN + A2.count70JahreWOSepsisMNaN)*100)/ (A1.count70JahreWSepsisMNaN +A1.count70JahreWOSepsisMNaN +A2.count70JahreWSepsisMNaN + A2.count70JahreWOSepsisMNaN)))
 
        #älter 80
        print("NaN Anzahl von Männer älter 80: ", A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN+A2.count80JahreWSepsisMNaN +A2.count80JahreWOSepsisMNaN)
        print("NaN Anzahl von Männer älter 80 mit Sepsis: ", A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN)
        print("NaN Anzahl von Männer älter 80 ohne Sepsis: ",A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN)
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)): F:A ", (((A1.count80JahreWSepsisMNaN + A1.count80JahreWOSepsisMNaN + A2.count80JahreWSepsisMNaN + A2.count80JahreWOSepsisMNaN) * 100)/40336))
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) mit Sepsis: F:A ", (((A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN)* 100)/(40336)))
        print("NaN Prozent von Männer älter 80 Allgemein (Wie viele Männer älter 80 insgesamt in NaN waren (und nicht in NaN und NaN)) ohne Sepsis: F:A ", (((A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN) * 100)/(40336)))
        print("NaN Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWSepsisMNaN+ A2.count80JahreWSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben) F:F:A ", (((A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN)*100)/ (A1.countNoUnitMale + A2.countNoUnitMale)))
        print("NaN Prozent von Männer älter 80 mit Sepsis (Wie Viele Männer älter 80 von NaN Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWSepsisMNaN + A2.count80JahreWSepsisMNaN)*100)/ (A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN + A2.count80JahreWSepsisMNaN + A2.count80JahreWOSepsisMNaN)))
        print("NaN Prozent von Männer älter 80 ohne Sepsis (Wie Viele Männer älter 80 von NaN nicht Sepsis haben): F:F:älter 80: ", (((A1.count80JahreWOSepsisMNaN + A2.count80JahreWOSepsisMNaN)*100)/ (A1.count80JahreWSepsisMNaN +A1.count80JahreWOSepsisMNaN +A2.count80JahreWSepsisMNaN + A2.count80JahreWOSepsisMNaN)))
 








##print("Das sind MICU Unit 1 alle Frauen: " + str(A1.countAllUnit1Female+ A2.countAllUnit1Female))
##print("Das sind MICU Unit 1 alle Frauen mit Se##psis: " + str(A1.countAllUnit1FemaleSe##psis+ A2.countAllUnit1FemaleSe##psis))
##print("Das sind MICU Unit 1 alle Frauen ohne Se##psis: " + str((A1.countAllUnit1Female+ A2.countAllUnit1Female)-(A1.countAllUnit1FemaleSe##psis+ A2.countAllUnit1FemaleSe##psis) ) )
##print("Das ist MICU Frau unter 20 mit Se##psis: "+ str(A1.count1819WSe##psisFU1 + A2.count1819WSe##psisFU1))
##print("Das ist MICU Frauen  20 - 29 mit Se##psis: "+ str(A1.count20JahreWSe##psisFU1 + A2.count20JahreWSe##psisFU1))
##print("Das ist MICU Frauen 30-39 mit Se##psis: "+str(A1.count30JahreWSe##psisFU1 + A2.count30JahreWSe##psisFU1))                                
##print("Das ist MICU Frauen 40-49 mit Se##psis: "+str(A1.count40JahreWSe##psisFU1 + A2.count40JahreWSe##psisFU1 ))                                
##print("Das ist MICU Frauen 50-59 mit Se##psis: "+str(A1.count50JahreWSe##psisFU1 + A2.count50JahreWSe##psisFU1) )                                
##print("Das ist MICU Frauen 60-69 mit Se##psis: "+str(A1.count60JahreWSe##psisFU1 + A2.count60JahreWSe##psisFU1 ))                               
##print("Das ist MICU Frauen 70-79 mit Se##psis: "+str(A1.count70JahreWSe##psisFU1 + A2.count70JahreWSe##psisFU1))                                
##print("Das ist MICU Frauen 80 größer mit Se##psis: "+str(A1.count80JahreWSe##psisFU1 + A2.count80JahreWSe##psisFU1))                              
#
##print("Das ist MICU Frauen unter 20 ohne Se##psis: "+ str(A1.count1819WOSe##psisFU1 + A2.count1819WOSe##psisFU1))
##print("Das ist MICU Frauen  20 - 29 ohne Se##psis: "+ str(A1.count20JahreWOSe##psisFU1 + A2.count20JahreWOSe##psisFU1))
##print("Das ist MICU Frauen 30-39 ohne Se##psis: "+str(A1.count30JahreWOSe##psisFU1 + A2.count30JahreWOSe##psisFU1))                                
##print("Das ist MICU Frauen 40-49 ohne Se##psis:"+str(A1.count40JahreWOSe##psisFU1 + A2.count40JahreWOSe##psisFU1))                                
##print("Das ist MICU Frauen 50-59 ohne Se##psis: "+str(A1.count50JahreWOSe##psisFU1 + A2.count50JahreWOSe##psisFU1) )                                
##print("Das ist MICU Frauen 60-69 ohne Se##psis: "+str(A1.count60JahreWOSe##psisFU1 + A2.count60JahreWOSe##psisFU1))                               
##print("Das ist MICU Frauen 70-79 ohne Se##psis: "+str(A1.count70JahreWOSe##psisFU1 + A2.count70JahreWOSe##psisFU1 ))                                
##print("Das ist MICU Frauen 80 größer ohne Se##psis: "+str(A1.count80JahreWOSe##psisFU1 + A2.count80JahreWOSe##psisFU1 ))                                          
#
##print("Das sind MICU Unit 1 alle Männer: " + str(A1.countAllUnit1Male+ A2.countAllUnit1Male))
##print("Das sind MICU Unit 1 alle Männer mit Se##psis: " + str(A1.countAllUnit1MaleSe##psis+ A2.countAllUnit1MaleSe##psis))
##print("Das sind MICU Unit 1 alle Männer ohne Se##psis: " + str((A1.countAllUnit1Male+ A2.countAllUnit1Male)-(A1.countAllUnit1MaleSe##psis+ A2.countAllUnit1MaleSe##psis) )   )
##print("Das ist MICU Männer unter 20 mit Se##psis: "+ str(A1.count1819WSe##psisMU1 + A2.count1819WSe##psisMU1))
##print("Das ist MICU Männer  20 - 29 mit Se##psis: "+ str(A1.count20JahreWSe##psisMU1 + A2.count20JahreWSe##psisMU1))
##print("Das ist MICU Männer 30-39 mit Se##psis: "+str(A1.count30JahreWSe##psisMU1 + A2.count30JahreWSe##psisMU1))                                
##print("Das ist MICU Männer 40-49 mit Se##psis: "+str(A1.count40JahreWSe##psisMU1 + A2.count40JahreWSe##psisMU1 ))                                
##print("Das ist MICU Männer 50-59 mit Se##psis: "+str(A1.count50JahreWSe##psisMU1 + A2.count50JahreWSe##psisMU1) )                                
##print("Das ist MICU Männer 60-69 mit Se##psis: "+str(A1.count60JahreWSe##psisMU1 + A2.count60JahreWSe##psisMU1))                               
##print("Das ist MICU Männer 70-79 mit Se##psis: "+str(A1.count70JahreWSe##psisMU1 + A2.count70JahreWSe##psisMU1 ))                                
##print("Das ist MICU Männer 80 größer mit Se##psis: "+str(A1.count80JahreWSe##psisMU1 + A2.count80JahreWSe##psisMU1))                              
#
##print("Das ist MICU Männer unter 20 ohne Se##psis: "+ str(A1.count1819WOSe##psisMU1 + A2.count1819WOSe##psisMU1))
##print("Das ist MICU Männer  20 - 29 ohne Se##psis: "+ str(A1.count20JahreWOSe##psisMU1 + A2.count20JahreWOSe##psisMU1))
##print("Das ist MICU Männer 30-39 ohne Se##psis: "+str(A1.count30JahreWOSe##psisMU1 + A2.count30JahreWOSe##psisMU1))                                
##print("Das ist MICU Männer 40-49 ohne Se##psis: "+str(A1.count40JahreWOSe##psisMU1 + A2.count40JahreWOSe##psisMU1))                                
##print("Das ist MICU Männer 50-59 ohne Se##psis: "+str(A1.count50JahreWOSe##psisMU1 + A2.count50JahreWOSe##psisMU1) )                                
##print("Das ist MICU Männer 60-69 ohne Se##psis: "+str(A1.count60JahreWOSe##psisMU1 + A2.count60JahreWOSe##psisMU1))                               
##print("Das ist MICU Männer 70-79 ohne Se##psis: "+str(A1.count70JahreWOSe##psisMU1 + A2.count70JahreWOSe##psisMU1))                                
##print("Das ist MICU Männer 80 größer ohne Se##psis: "+str(A1.count80JahreWOSe##psisMU1 + A2.count80JahreWOSe##psisMU1))                              
#                              

##print("Das sind MICU Unit 2 alle Frauen: " + str(A1.countAllUnit2Female+ A2.countAllUnit2Female))
##print("Das sind SICU Unit 2 alle Frauen mit Se##psis: " + str(A1.countAllUnit2FemaleSe##psis+ A2.countAllUnit2FemaleSe##psis))
##print("Das sind SICU Unit 2 alle Frauen ohne Se##psis: " + str((A1.countAllUnit2Female+ A2.countAllUnit2Female)-(A1.countAllUnit2FemaleSe##psis+ A2.countAllUnit2FemaleSe##psis) )  )
##print("Das ist SICU Frau unter 20 mit Se##psis: "+ str(A1.count1819WSe##psisFU2 + A2.count1819WSe##psisFU2))
##print("Das ist SICU Frauen  20 - 29 mit Se##psis: "+ str(A1.count20JahreWSe##psisFU2 + A2.count20JahreWSe##psisFU2))
##print("Das ist SICU Frauen 30-39 mit Se##psis: "+str(A1.count30JahreWSe##psisFU2 + A2.count30JahreWSe##psisFU2))                                
##print("Das ist SICU Frauen 40-49 mit Se##psis: "+str(A1.count40JahreWSe##psisFU2 + A2.count40JahreWSe##psisFU2))                                
##print("Das ist SICU Frauen 50-59 mit Se##psis: "+str(A1.count50JahreWSe##psisFU2 + A2.count50JahreWSe##psisFU2) )                                
##print("Das ist SICU Frauen 60-69 mit Se##psis: "+str(A1.count60JahreWSe##psisFU2 + A2.count60JahreWSe##psisFU2))                               
##print("Das ist SICU Frauen 70-79 mit Se##psis: "+str(A1.count70JahreWSe##psisFU2 + A2.count70JahreWSe##psisFU2))                                
##print("Das ist SICU Frauen 80 größer mit Se##psis: "+str(A1.count80JahreWSe##psisFU2 + A2.count80JahreWSe##psisFU2))                              
#
##print("Das ist SICU Frauen unter 20 ohne Se##psis: "+ str(A1.count1819WOSe##psisFU2 + A2.count1819WOSe##psisFU2))
##print("Das ist SICU Frauen  20 - 29 ohne Se##psis: "+ str(A1.count20JahreWOSe##psisFU2 + A2.count20JahreWOSe##psisFU2))
##print("Das ist SICU Frauen 30-39 ohne Se##psis: "+str(A1.count30JahreWOSe##psisFU2 + A2.count30JahreWOSe##psisFU2))                                
##print("Das ist SICU Frauen 40-49 ohne Se##psis: "+str(A1.count40JahreWOSe##psisFU2 + A2.count40JahreWOSe##psisFU2))                                
##print("Das ist SICU Frauen 50-59 ohne Se##psis: "+str(A1.count50JahreWOSe##psisFU2 + A2.count50JahreWOSe##psisFU2) )                                
##print("Das ist SICU Frauen 60-69 ohne Se##psis: "+str(A1.count60JahreWOSe##psisFU2 + A2.count60JahreWOSe##psisFU2))                               
##print("Das ist SICU Frauen 70-79 ohne Se##psis: "+str(A1.count70JahreWOSe##psisFU2 + A2.count70JahreWOSe##psisFU2))                                
##print("Das ist SICU Frauen 80 größer ohne Se##psis: "+str(A1.count80JahreWOSe##psisFU2 + A2.count80JahreWOSe##psisFU2)) 
#

##print("Das sind SICU Unit 2 alle Männer: " + str(A1.countAllUnit2Male+ A2.countAllUnit2Male))
##print("Das sind SICU Unit 2 alle Männer mit Se##psis: " + str(A1.countAllUnit2MaleSe##psis+ A2.countAllUnit2MaleSe##psis))
##print("Das sind SICU Unit 2 alle Männer ohne Se##psis: " + str((A1.countAllUnit2Male+ A2.countAllUnit2Male)-(A1.countAllUnit2MaleSe##psis+ A2.countAllUnit2MaleSe##psis) )   )
#
##print("Das ist SICU Mann unter 20 mit Se##psis: "+ str(A1.count1819WSe##psisMU2 + A2.count1819WSe##psisMU2))
##print("Das ist SICU Männer  20 - 29 mit Se##psis: "+ str(A1.count20JahreWSe##psisMU2 + A2.count20JahreWSe##psisMU2))
##print("Das ist SICU Männer 30-39 mit Se##psis: "+str(A1.count30JahreWSe##psisMU2 + A2.count30JahreWSe##psisMU2))                                
##print("Das ist SICU Männer 40-49 mit Se##psis: "+str(A1.count40JahreWSe##psisMU2 + A2.count40JahreWSe##psisMU2))                                
##print("Das ist SICU Männer 50-59 mit Se##psis: "+str(A1.count50JahreWSe##psisMU2 + A2.count50JahreWSe##psisMU2) )                                
##print("Das ist SICU Männer 60-69 mit Se##psis: "+str(A1.count60JahreWSe##psisMU2 + A2.count60JahreWSe##psisMU2))                               
##print("Das ist SICU Männer 70-79 mit Se##psis: "+str(A1.count70JahreWSe##psisMU2 + A2.count70JahreWSe##psisMU2))                                
##print("Das ist SICU Männer 80 größer mit Se##psis: "+str(A1.count80JahreWSe##psisMU2 + A2.count80JahreWSe##psisMU2))                              
#
##print("Das ist SICU Männer unter 20 ohne Se##psis: "+ str(A1.count1819WOSe##psisMU2 + A2.count1819WOSe##psisMU2))
##print("Das ist SICU Männer  20 - 29 ohne Se##psis: "+ str(A1.count20JahreWOSe##psisMU2 + A2.count20JahreWOSe##psisMU2))
##print("Das ist SICU Männer 30-39 ohne Se##psis: "+str(A1.count30JahreWOSe##psisMU2 + A2.count30JahreWOSe##psisMU2))                                
##print("Das ist SICU Männer 40-49 ohne Se##psis: "+str(A1.count40JahreWOSe##psisMU2 + A2.count40JahreWOSe##psisMU2))                                
##print("Das ist SICU Männer 50-59 ohne Se##psis: "+str(A1.count50JahreWOSe##psisMU2 + A2.count50JahreWOSe##psisMU2) )                                
##print("Das ist SICU Männer 60-69 ohne Se##psis: "+str(A1.count60JahreWOSe##psisMU2 + A2.count60JahreWOSe##psisMU2))                               
##print("Das ist SICU Männer 70-79 ohne Se##psis: "+str(A1.count70JahreWOSe##psisMU2 + A2.count70JahreWOSe##psisMU2))                                
##print("Das ist SICU Männer 80 größer ohne Se##psis: "+str(A1.count80JahreWOSe##psisMU2 + A2.count80JahreWOSe##psisMU2)) 

##print("Das sind keine Units alle Frauen: " + str(A1.countNoUnitFemale+ A2.countNoUnitFemale))
##print("Das sind keine Units alle Frauen mit Se##psis: " + str(A1.countNoUnitSe##pFemale + A2.countNoUnitSe##pFemale))
##print("Das sind keine Units alle Frauen ohne Se##psis: " + str((A1.countNoUnitFemale + A2.countNoUnitFemale)-(A1.countNoUnitSe##pFemale+ A2.countNoUnitSe##pFemale))   )
#
##print("Das ist keine Units Frau unter 20 mit Se##psis: "+ str(A1.count1819WSe##psisFNaN + A2.count1819WSe##psisFNaN))
##print("Das ist keine Units Frauen  20 - 29 mit Se##psis: "+ str(A1.count20JahreWSe##psisFNaN + A2.count20JahreWSe##psisFNaN))
##print("Das ist keine Units Frauen 30-39 mit Se##psis: "+str(A1.count30JahreWSe##psisFNaN + A2.count30JahreWSe##psisFNaN))                                
##print("Das ist keine Units Frauen 40-49 mit Se##psis: "+str(A1.count40JahreWSe##psisFNaN + A2.count40JahreWSe##psisFNaN))                                
##print("Das ist keine Units Frauen 50-59 mit Se##psis: "+str(A1.count50JahreWSe##psisFNaN + A2.count50JahreWSe##psisFNaN) )                                
##print("Das ist keine Units Frauen 60-69 mit Se##psis: "+str(A1.count60JahreWSe##psisFNaN + A2.count60JahreWSe##psisFNaN))                               
##print("Das ist keine Units Frauen 70-79 mit Se##psis: "+str(A1.count70JahreWSe##psisFNaN + A2.count70JahreWSe##psisFNaN))                                
##print("Das ist keine Units Frauen 80 größer mit Se##psis: "+str(A1.count80JahreWSe##psisFNaN + A2.count80JahreWSe##psisFNaN))                              
#
##print("Das ist keine Units Frauen unter 20 ohne Se##psis: "+ str(A1.count1819WOSe##psisFNaN + A2.count1819WOSe##psisFNaN))
##print("Das ist keine Units Frauen  20 - 29 ohne Se##psis: "+ str(A1.count20JahreWOSe##psisFNaN + A2.count20JahreWOSe##psisFNaN))
##print("Das ist keine Units Frauen 30-39 ohne Se##psis: "+str(A1.count30JahreWOSe##psisFNaN + A2.count30JahreWOSe##psisFNaN))                                
##print("Das ist keine Units Frauen 40-49 ohne Se##psis: "+str(A1.count40JahreWOSe##psisFNaN + A2.count40JahreWOSe##psisFNaN))                                
##print("Das ist keine Units Frauen 50-59 ohne Se##psis: "+str(A1.count50JahreWOSe##psisFNaN + A2.count50JahreWOSe##psisFNaN) )                                
##print("Das ist keine Units Frauen 60-69 ohne Se##psis: "+str(A1.count60JahreWOSe##psisFNaN + A2.count60JahreWOSe##psisFNaN))                               
##print("Das ist keine Units Frauen 70-79 ohne Se##psis: "+str(A1.count70JahreWOSe##psisFNaN + A2.count70JahreWOSe##psisFNaN))                                
##print("Das ist keine Units Frauen 80 größer ohne Se##psis: "+str(A1.count80JahreWOSe##psisFNaN + A2.count80JahreWOSe##psisFNaN))                     
  

##print("Das sind keine Units alle Männer: " + str(A1.countNoUnitMale+ A2.countNoUnitMale))
##print("Das sind keine Units alle Männer mit Se##psis: " + str(A1.countNoUnitSe##pMale+ A2.countNoUnitSe##pMale))
##print("Das sind keine Units alle Männer ohne Se##psis: " + str((A1.countNoUnitMale+ A2.countNoUnitMale) - (A1.countNoUnitSe##pMale+ A2.countNoUnitSe##pMale))   )
#
##print("Das ist keine Units Mann unter 20 mit Se##psis: "+ str(A1.count1819WSe##psisMNaN + A2.count1819WSe##psisMNaN))
##print("Das ist keine Units Männer  20 - 29 mit Se##psis: "+ str(A1.count20JahreWSe##psisMNaN + A2.count20JahreWSe##psisMNaN))
##print("Das ist keine Units Männer 30-39 mit Se##psis: "+str(A1.count30JahreWSe##psisMNaN + A2.count30JahreWSe##psisMNaN))                                
##print("Das ist keine Units Männer 40-49 mit Se##psis: "+str(A1.count40JahreWSe##psisMNaN + A2.count40JahreWSe##psisMNaN))                                
##print("Das ist keine Units Männer 50-59 mit Se##psis: "+str(A1.count50JahreWSe##psisMNaN + A2.count50JahreWSe##psisMNaN ) )                                
##print("Das ist keine Units Männer 60-69 mit Se##psis: "+str(A1.count60JahreWSe##psisMNaN + A2.count60JahreWSe##psisMNaN))                               
##print("Das ist keine Units Männer 70-79 mit Se##psis: "+str(A1.count70JahreWSe##psisMNaN + A2.count70JahreWSe##psisMNaN))                                
##print("Das ist keine Units Männer 80 größer mit Se##psis: "+str(A1.count80JahreWSe##psisMNaN + A2.count80JahreWSe##psisMNaN))                              
#
##print("Das ist keine Units Männer unter 20 ohne Se##psis: "+ str(A1.count1819WOSe##psisMNaN + A2.count1819WOSe##psisMNaN))
##print("Das ist keine Units Männer  20 - 29 ohne Se##psis: "+ str(A1.count20JahreWOSe##psisMNaN + A2.count20JahreWOSe##psisMNaN))
##print("Das ist keine Units Männer 30-39 ohne Se##psis: "+str(A1.count30JahreWOSe##psisMNaN + A2.count30JahreWOSe##psisMNaN))                                
##print("Das ist keine Units Männer 40-49 ohne Se##psis: "+str(A1.count40JahreWOSe##psisMNaN + A2.count40JahreWOSe##psisMNaN))                                
##print("Das ist keine Units Männer 50-59 ohne Se##psis: "+str(A1.count50JahreWOSe##psisMNaN + A2.count50JahreWOSe##psisMNaN) )                                
##print("Das ist keine Units Männer 60-69 ohne Se##psis: "+str(A1.count60JahreWOSe##psisMNaN + A2.count60JahreWOSe##psisMNaN))                               
##print("Das ist keine Units Männer 70-79 ohne Se##psis: "+str(A1.count70JahreWOSe##psisMNaN + A2.count70JahreWOSe##psisMNaN))                                
##print("Das ist keine Units Männer 80 größer ohne Se##psis: "+str(A1.count80JahreWOSe##psisMNaN + A2.count80JahreWOSe##psisMNaN))   


