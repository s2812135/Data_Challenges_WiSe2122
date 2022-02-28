import os, sys
import csv
from os.path import isfile, join
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import sklearn
import numpy
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import statistics

 



class SubGroups():
    def __init__(self, dataPath=""):
        self.dataPath = dataPath
        #hasAllFileNamesInAnArray
        self.fileNames = []
        #currentFileData Array
        self.currentFileDataArray = []
        #endResultArray
        self.endResultArray = []


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
        print("Das ist die zu extrahierende File" + file)
        fp=open(filename)
        resultArray = []
        for line in fp:
            res=line.split('|')
            resultArray.append(res)
        #jetzigeFile
        self.currentFileDataArray = resultArray
        #1
        self.extractHr(file)
        #2
        self.extractO2Sat(file)
        self.extractTemp(file)
        self.extractSBP(file)
        self.extractMAP(file)
        self.extractDBP(file)
        self.extractResp(file)
        self.extractEtCO2(file)
        self.extractBaseExcess(file)
        self.extractHCO3(file)
        self.extractFiO2(file)
        self.extractpH(file)
        self.extractPaCO2(file)
        self.extractSaO2(file)
        self.extractAST(file)
        self.extractBUN(file)
        self.extractAlkalinephos(file)
        self.extractCalcium(file)
        self.extractChloride(file)
        self.extractCreatinine(file)
        self.extractBilirubin_direct(file)
        self.extractGlucose(file)
        self.extractLactate(file)
        self.extractMagnesium(file)
        self.extractPhosphate(file)
        self.extractPotassium(file)
        self.extractBilirubin_total(file)
        self.extractTroponinI(file)
        self.extractHct(file)
        self.extractHgb(file)
        self.extractPTT(file)
        self.extractWBC(file)
        self.extractFibrinogen(file)
        self.extractPlatelets(file)
        self.extractAge(file) 
        self.extractGender(file) 
        self.extractUnit1(file)
        self.extractUnit2(file)
        self.extractHospAdmTime(file)
        self.extractICULOS(file)
        self.extractSepsisLabel(file)


    def extractHr(self, file):
        """ extract important Hr """
        allHeartRatePerPerson = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][0] != "NaN"):
                allHeartRatePerPerson.append(float(self.currentFileDataArray[i][0]))
            #if(self.currentFileDataArray[i][0] == "NaN"):
                #allHeartRatePerPerson.append(0)

        allHeartRatePerPerson = list(dict.fromkeys(allHeartRatePerPerson))

        for i in range(0, len(allHeartRatePerPerson)):
            self.endResultArray.append([1,allHeartRatePerPerson[i]])
        #self.endResultArray.append(['average', 1, statistics.mean(allHeartRatePerPerson)])

    def extractO2Sat(self, file):
        """ extract important O2Sat """
        allO2Sat = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][1] != "NaN"):
                allO2Sat.append(float(self.currentFileDataArray[i][1]))
            #if(self.currentFileDataArray[i][1] == "NaN"):
                #allO2Sat.append(0)

        allO2Sat = list(dict.fromkeys(allO2Sat))
        for i in range(0, len(allO2Sat)):
            self.endResultArray.append([2,allO2Sat[i]])
        #self.endResultArray.append(['average', 2, statistics.mean(allO2Sat)])

    def extractTemp(self, file):
        """ extract important O2Sat """
        allTemp = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][2] != "NaN"):
                allTemp.append(float(self.currentFileDataArray[i][2]))
            #if(self.currentFileDataArray[i][2] == "NaN"):
                #allTemp.append(float(0))

        allTemp = list(dict.fromkeys(allTemp))

        for i in range(0, len(allTemp)):
            self.endResultArray.append([3, allTemp[i]])
        #self.endResultArray.append(['average', 3, statistics.mean(allTemp)])


    def extractSBP(self, file):
        """ extract important SBP """
        allSBP = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][3] != "NaN"):
                allSBP.append(float(self.currentFileDataArray[i][3]))
            #if(self.currentFileDataArray[i][3] == "NaN"):
                #allSBP.append(float(0))


        allSBP = list(dict.fromkeys(allSBP))

        for i in range(0, len(allSBP)):
            self.endResultArray.append([4, allSBP[i]])
        #self.endResultArray.append(['average', 4, statistics.mean(allSBP)])

    def extractMAP(self, file):
        """ extract important MAP """
        allMAP = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][4] != "NaN"):
                allMAP.append(float(self.currentFileDataArray[i][4]))
            #if(self.currentFileDataArray[i][4] == "NaN"):
                #allMAP.append(float(0))

        allMAP = list(dict.fromkeys(allMAP))

        for i in range(0, len(allMAP)):
            self.endResultArray.append([5, allMAP[i]])
        #self.endResultArray.append(['average', 5, statistics.mean(allMAP)])


    def extractDBP(self, file):
        """ extract important DBP """
        allDBP = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][5] != "NaN"):
                allDBP.append(float(self.currentFileDataArray[i][5]))
            #if(self.currentFileDataArray[i][5] == "NaN"):
                #allDBP.append(float(0))

        allDBP = list(dict.fromkeys(allDBP))

        for i in range(0, len(allDBP)):
            self.endResultArray.append([6, allDBP[i]])
        #self.endResultArray.append(['average', 6, statistics.mean(allDBP)])


    def extractResp(self, file):
        """ extract important Resp """
        allResp = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][6] != "NaN"):
                allResp.append(float(self.currentFileDataArray[i][6]))
            #if(self.currentFileDataArray[i][6] == "NaN"):
                #allResp.append(float(0))

        allResp = list(dict.fromkeys(allResp))

        for i in range(0, len(allResp)):
            self.endResultArray.append([7, allResp[i]])
        #self.endResultArray.append(['average', 7, statistics.mean(allResp)])

        #7
    def extractEtCO2(self, file):
        """ extract important Hr """
        allEtCO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][7] != "NaN"):
                allEtCO2.append(float(self.currentFileDataArray[i][7]))
            #if(self.currentFileDataArray[i][7] == "NaN"):
                #allEtCO2.append(float(0))

        allEtCO2 = list(dict.fromkeys(allEtCO2))

        for i in range(0, len(allEtCO2)):
            self.endResultArray.append([8,allEtCO2[i]])
        #self.endResultArray.append(['average', 8, statistics.mean(allEtCO2)])



    def extractBaseExcess(self, file):
        """ extract important allBaseExcess """
        allBaseExcess = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][8] != "NaN"):
                allBaseExcess.append(float(self.currentFileDataArray[i][8]))
            #if(self.currentFileDataArray[i][8] == "NaN"):
                #allBaseExcess.append(float(0))

        allBaseExcess = list(dict.fromkeys(allBaseExcess))

        for i in range(0, len(allBaseExcess)):
            self.endResultArray.append([9,allBaseExcess[i]])
        #self.endResultArray.append(['average', 9, statistics.mean(allBaseExcess)])


    def extractHCO3(self, file):
        """ extract important O2Sat """
        allHCO3 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][9] != "NaN"):
                allHCO3.append(float(self.currentFileDataArray[i][9]))
            #if(self.currentFileDataArray[i][9] == "NaN"):
                #allHCO3.append(float(0))

        allHCO3 = list(dict.fromkeys(allHCO3))

        for i in range(0, len(allHCO3)):
            self.endResultArray.append([10, allHCO3[i]])
        #self.endResultArray.append(['average', 10, statistics.mean(allHCO3)])


    def extractFiO2(self, file):
        """ extract important SBP """
        allFiO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][10] != "NaN"):
                allFiO2.append(float(self.currentFileDataArray[i][10]))
            #if(self.currentFileDataArray[i][10] == "NaN"):
                #allFiO2.append(float(0))

        allFiO2 = list(dict.fromkeys(allFiO2))

        for i in range(0, len(allFiO2)):
            self.endResultArray.append([11, allFiO2[i]])
        #self.endResultArray.append(['average', 11, statistics.mean(allFiO2)])

    def extractpH(self, file):
        """ extract important MAP """
        allpH = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][11] != "NaN"):
                allpH.append(float(self.currentFileDataArray[i][11]))
            #if(self.currentFileDataArray[i][11] == "NaN"):
                #allpH.append(float(0))

        allpH = list(dict.fromkeys(allpH))

        for i in range(0, len(allpH)):
            self.endResultArray.append([12, allpH[i]])
        #self.endResultArray.append(['average', 12, statistics.mean(allpH)])


    def extractPaCO2(self, file):
        """ extract important DBP """
        allPaCO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][12] != "NaN"):
                allPaCO2.append(float(self.currentFileDataArray[i][12]))
            #if(self.currentFileDataArray[i][12] == "NaN"):
                #allPaCO2.append(float(0))

        allPaCO2 = list(dict.fromkeys(allPaCO2))

        for i in range(0, len(allPaCO2)):
            self.endResultArray.append([13, allPaCO2[i]])
        #self.endResultArray.append(['average', 13, statistics.mean(allPaCO2)])




    def extractSaO2(self, file):
        """ extract important Resp """
        allSaO2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][13] != "NaN"):
                allSaO2.append(float(self.currentFileDataArray[i][13]))
            #if(self.currentFileDataArray[i][13] == "NaN"):
                #allSaO2.append(float(0))

        allSaO2 = list(dict.fromkeys(allSaO2))

        for i in range(0, len(allSaO2)):
            self.endResultArray.append([14, allSaO2[i]])
        #self.endResultArray.append(['average', 14, statistics.mean(allSaO2)])


    #14
    def extractAST(self, file):
        """ extract important Hr """
        allAST = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][14] != "NaN"):
                allAST.append(float(self.currentFileDataArray[i][14]))
            #if(self.currentFileDataArray[i][14] == "NaN"):
                #allAST.append(float(0))

        allAST = list(dict.fromkeys(allAST))
        for i in range(0, len(allAST)):
            self.endResultArray.append([15,allAST[i]])
        #self.endResultArray.append(['average', 15, statistics.mean(allAST)])



    def extractBUN(self, file):
        """ extract important O2Sat """
        allBUN = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][15] != "NaN"):
                allBUN.append(float(self.currentFileDataArray[i][15]))
            #if(self.currentFileDataArray[i][15] == "NaN"):
                #allBUN.append(float(0))

        allBUN = list(dict.fromkeys(allBUN))

        for i in range(0, len(allBUN)):
            self.endResultArray.append([16, allBUN[i]])
        #self.endResultArray.append(['average', 16, statistics.mean(allBUN)])


    def extractAlkalinephos(self, file):
        """ extract important O2Sat """
        allAlkalinephos = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][16] != "NaN"):
                allAlkalinephos.append(float(self.currentFileDataArray[i][16]))
            #if(self.currentFileDataArray[i][16] == "NaN"):
                #allAlkalinephos.append(float(0))

        allAlkalinephos = list(dict.fromkeys(allAlkalinephos))

        for i in range(0, len(allAlkalinephos)):
            self.endResultArray.append([17, allAlkalinephos[i]])
        #self.endResultArray.append(['average', 17, statistics.mean(allAlkalinephos)])

    def extractCalcium(self, file):
        """ extract important SBP """
        allCalcium = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][17] != "NaN"):
                allCalcium.append(float(self.currentFileDataArray[i][17]))
            #if(self.currentFileDataArray[i][17] == "NaN"):
                #allCalcium.append(float(0))

        allCalcium = list(dict.fromkeys(allCalcium))

        for i in range(0, len(allCalcium)):
            self.endResultArray.append([18, allCalcium[i]])
        #self.endResultArray.append(['average', 18, statistics.mean(allCalcium)])



    def extractChloride(self, file):
        """ extract important MAP """
        allChloride = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][18] != "NaN"):
                allChloride.append(float(self.currentFileDataArray[i][18]))
            #if(self.currentFileDataArray[i][18] == "NaN"):
                #allChloride.append(float(0))

        allChloride = list(dict.fromkeys(allChloride))
        for i in range(0, len(allChloride)):
            self.endResultArray.append([19, allChloride[i]])
        #self.endResultArray.append(['average', 19, statistics.mean(allChloride)])


    def extractCreatinine(self, file):
        """ extract important Creatinine """
        allCreatinine = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][19] != "NaN"):
                allCreatinine.append(float(self.currentFileDataArray[i][19]))
            #if(self.currentFileDataArray[i][19] == "NaN"):
                #allCreatinine.append(float(0))

        allCreatinine = list(dict.fromkeys(allCreatinine))

        for i in range(0, len(allCreatinine)):
            self.endResultArray.append([20, allCreatinine[i]])
        #self.endResultArray.append(['average', 20, statistics.mean(allCreatinine)])


    def extractBilirubin_direct(self, file):
        """ extract important Bilirubin_direct """
        allBilirubin_direct = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][20] != "NaN"):
                allBilirubin_direct.append(float(self.currentFileDataArray[i][20]))
            #if(self.currentFileDataArray[i][20] == "NaN"):
                #allBilirubin_direct.append(float(0))

        allBilirubin_direct = list(dict.fromkeys(allBilirubin_direct))

        for i in range(0, len(allBilirubin_direct)):
            self.endResultArray.append([21, allBilirubin_direct[i]])
        #self.endResultArray.append(['average', 21, statistics.mean(allBilirubin_direct)])


    def extractGlucose(self, file):
        """ extract important Glucose """
        allGlucose = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][21] != "NaN"):
                allGlucose.append(float(self.currentFileDataArray[i][21]))
            #if(self.currentFileDataArray[i][21] == "NaN"):
                #allGlucose.append(float(0))

        allGlucose = list(dict.fromkeys(allGlucose))

        for i in range(0, len(allGlucose)):
            self.endResultArray.append([22, allGlucose[i]])
        #self.endResultArray.append(['average', 22, statistics.mean(allGlucose)])

    def extractLactate(self, file):
        """ extract important allBaseExcess """
        allLactate = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][22] != "NaN"):
                allLactate.append(float(self.currentFileDataArray[i][22]))
            #if(self.currentFileDataArray[i][22] == "NaN"):
                #allLactate.append(float(0))

        allLactate = list(dict.fromkeys(allLactate))

        for i in range(0, len(allLactate)):
            self.endResultArray.append([23, allLactate[i]])
        #self.endResultArray.append(['average', 23, statistics.mean(allLactate)])


    def extractMagnesium(self, file):
        """ extract important Magnesium """
        allMagnesium = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][23] != "NaN"):
                allMagnesium.append(float(self.currentFileDataArray[i][23]))
            #if(self.currentFileDataArray[i][23] == "NaN"):
                #allMagnesium.append(float(0))

        allMagnesium = list(dict.fromkeys(allMagnesium))

        for i in range(0, len(allMagnesium)):
            self.endResultArray.append([24, allMagnesium[i]])
        #self.endResultArray.append(['average', 24, statistics.mean(allMagnesium)])


    def extractPhosphate(self, file):
        """ extract important allPhosphate """
        allPhosphate = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][24] != "NaN"):
                allPhosphate.append(float(self.currentFileDataArray[i][24]))
            #if(self.currentFileDataArray[i][24] == "NaN"):
                #allPhosphate.append(float(0))

        allPhosphate = list(dict.fromkeys(allPhosphate))

        for i in range(0, len(allPhosphate)):
            self.endResultArray.append([25, allPhosphate[i]])
        #self.endResultArray.append(['average', 25, statistics.mean(allPhosphate)])


    def extractPotassium(self, file):
        """ extract important Potassium """
        allPotassium = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][25] != "NaN"):
                allPotassium.append(float(self.currentFileDataArray[i][25]))
            #if(self.currentFileDataArray[i][25] == "NaN"):
                #allPotassium.append(float(0))

        allPotassium = list(dict.fromkeys(allPotassium))

        for i in range(0, len(allPotassium)):
            self.endResultArray.append([26, allPotassium[i]])
        #self.endResultArray.append(['average', 26, statistics.mean(allPotassium)])


    def extractBilirubin_total(self, file):
        """ extract important Bilirubin_total """
        allBilirubin_total = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][26] != "NaN"):
                allBilirubin_total.append(float(self.currentFileDataArray[i][26]))
            #if(self.currentFileDataArray[i][26] == "NaN"):
                #allBilirubin_total.append(float(0))

        allBilirubin_total = list(dict.fromkeys(allBilirubin_total))

        for i in range(0, len(allBilirubin_total)):
            self.endResultArray.append([27, allBilirubin_total[i]])
        #self.endResultArray.append(['average', 27, statistics.mean(allBilirubin_total)])


    def extractTroponinI(self, file):
        """ extract important TroponinI """
        allTroponinI = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][27] != "NaN"):
                allTroponinI.append(float(self.currentFileDataArray[i][27]))
            #if(self.currentFileDataArray[i][27] == "NaN"):
                #allTroponinI.append(float(0))

        allTroponinI = list(dict.fromkeys(allTroponinI))

        for i in range(0, len(allTroponinI)):
            self.endResultArray.append([28, allTroponinI[i]])

        #self.endResultArray.append(['average', 28, statistics.mean(allTroponinI)])

    #28
    def extractHct(self, file):
        """ extract important O2Sat """
        allHct = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][28] != "NaN"):
                allHct.append(float(self.currentFileDataArray[i][28]))
            #if(self.currentFileDataArray[i][28] == "NaN"):
                #allHct.append(float(0))

        allHct = list(dict.fromkeys(allHct))

        for i in range(0, len(allHct)):
            self.endResultArray.append([29, allHct[i]])
        #self.endResultArray.append(['average', 29, statistics.mean(allHct)])


    def extractHgb(self, file):
        """ extract important Hgb """
        allHgb = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][29] != "NaN"):
                allHgb.append(float(self.currentFileDataArray[i][29]))
            #if(self.currentFileDataArray[i][29] == "NaN"):
                #allHgb.append(float(0))

        allHgb = list(dict.fromkeys(allHgb))

        for i in range(0, len(allHgb)):
            self.endResultArray.append([30, allHgb[i]])
        #self.endResultArray.append(['average', 30, statistics.mean(allHgb)])


    def extractPTT(self, file):
        """ extract important SBP """
        allPTT = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][30] != "NaN"):
                allPTT.append(float(self.currentFileDataArray[i][30]))
            #if(self.currentFileDataArray[i][30] == "NaN"):
                #allPTT.append(float(0))

        allPTT = list(dict.fromkeys(allPTT))

        for i in range(0, len(allPTT)):
            self.endResultArray.append([31, allPTT[i]])
        #self.endResultArray.append(['average', 31, statistics.mean(allPTT)])



    def extractWBC(self, file):
        """ extract important allWBC """
        allWBC = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][31] != "NaN"):
                allWBC.append(float(self.currentFileDataArray[i][31]))
            #if(self.currentFileDataArray[i][31] == "NaN"):
                #allWBC.append(float(0))

        allWBC = list(dict.fromkeys(allWBC))

        for i in range(0, len(allWBC)):
            self.endResultArray.append([32, allWBC[i]])
        #self.endResultArray.append(['average', 32, statistics.mean(allWBC)])


    def extractFibrinogen(self, file):
        """ extract important Fibrinogen """
        allFibrinogen = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][32] != "NaN"):
                allFibrinogen.append(float(self.currentFileDataArray[i][32]))
            #if(self.currentFileDataArray[i][32] == "NaN"):
                #allFibrinogen.append(float(0))

        allFibrinogen = list(dict.fromkeys(allFibrinogen))

        for i in range(0, len(allFibrinogen)):
            self.endResultArray.append([33, allFibrinogen[i]])
        #self.endResultArray.append(['average', 33, statistics.mean(allFibrinogen)])

    def extractPlatelets(self, file):
        """ extract important Platelets """
        allPlatelets = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][33] != "NaN"):
                #Null
                allPlatelets.append(float(self.currentFileDataArray[i][33]))
            #if(self.currentFileDataArray[i][33] == "NaN"):
                #allPlatelets.append(float(0))

        allPlatelets = list(dict.fromkeys(allPlatelets))

        for i in range(0, len(allPlatelets)):
            self.endResultArray.append([34, allPlatelets[i]])
        #self.endResultArray.append(['average', 34, statistics.mean(allPlatelets)])


    def extractAge(self, file):
        """ extract important Glucose """
        allAge = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][34] != "NaN"):
                allAge.append(float(self.currentFileDataArray[i][34]))
            #if(self.currentFileDataArray[i][34] == "NaN"):
                #allAge.append(float(0))

        allAge = list(dict.fromkeys(allAge))

        for i in range(0, len(allAge)):
            self.endResultArray.append([35, allAge[i]])
        #self.endResultArray.append(['average', 35, statistics.mean(allAge)])

    #AB HIIIIIIER: Gender
    def extractGender(self, file):
        """ extract important allBaseExcess """
        allGender = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][35] != "NaN"):
                allGender.append(float(self.currentFileDataArray[i][35]))
            #if(self.currentFileDataArray[i][35] == "NaN"):
                #allGender.append(float(0))

        allGender = list(dict.fromkeys(allGender))

        for i in range(0, len(allGender)):
            self.endResultArray.append([36, allGender[i]])
        #self.endResultArray.append(['average', 36, statistics.mean(allGender)])


    def extractUnit1(self, file):
        """ extract important Magnesium """
        allUnit1 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][36] != "NaN"):
                allUnit1.append(float(self.currentFileDataArray[i][36]))
            #if(self.currentFileDataArray[i][36] == "NaN"):
                #allUnit1.append(float(0))
            # Geht nicht 

        allUnit1 = list(dict.fromkeys(allUnit1))

        for i in range(0, len(allUnit1)):
            self.endResultArray.append([37, allUnit1[i]])
        #self.endResultArray.append(['average', 37, statistics.mean(allUnit1)])


    def extractUnit2(self, file):
        """ extract important allUnit2 """
        allUnit2 = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][37] != "NaN"):
                allUnit2.append(float(self.currentFileDataArray[i][37]))
            #if(self.currentFileDataArray[i][37] == "NaN"):
                #allUnit2.append(float(0))
        allUnit2 = list(dict.fromkeys(allUnit2))

        for i in range(0, len(allUnit2)):
            self.endResultArray.append([38, allUnit2[i]])
        #self.endResultArray.append(['average', 38, statistics.mean(allUnit2)])

    def extractHospAdmTime(self, file):
        """ extract important allHospAdmTime """
        allHospAdmTime = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][38] != "NaN"):
                allHospAdmTime.append(float(self.currentFileDataArray[i][38]))
            #if(self.currentFileDataArray[i][38] == "NaN"):
                #allHospAdmTime.append(float(0))

        allHospAdmTime = list(dict.fromkeys(allHospAdmTime))

        for i in range(0, len(allHospAdmTime)):
            self.endResultArray.append([39, allHospAdmTime[i]])
        #self.endResultArray.append(['average', 39, statistics.mean(allHospAdmTime)])


    def extractICULOS(self, file):
        """ extract important Bilirubin_total """
        allICULOS = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][39] != "NaN"):
                allICULOS.append(float(self.currentFileDataArray[i][39]))
            #if(self.currentFileDataArray[i][39] == "NaN"):
                #allICULOS.append(float(0))

        allICULOS = list(dict.fromkeys(allICULOS))

        for i in range(0, len(allICULOS)):
            self.endResultArray.append([40, allICULOS[i]])
        #self.endResultArray.append(['average', 40, statistics.mean(allICULOS)])

    def extractSepsisLabel(self, file):
        """ extract important TroponinI """
        allSepsisLabel = []
        for i in range(1, len(self.currentFileDataArray)):
            if(self.currentFileDataArray[i][40] != "NaN"):
                allSepsisLabel.append(float(self.currentFileDataArray[i][40]))

        allSepsisLabel = list(dict.fromkeys(allSepsisLabel))
        #print(allSepsisLabel)
        for i in range(0, len(allSepsisLabel)):
            self.endResultArray.append([41, allSepsisLabel[i]])
        #self.endResultArray.append(['average', 41, statistics.mean(allSepsisLabel)])

    def extract41average(self):
        averageArray = []
        popUnimportant = []
        #get All average values
        for i in range(0, len(self.endResultArray)):
            if(self.endResultArray[i][0] == 'average'):
                averageArray.append([self.endResultArray[i][1], self.endResultArray[i][2]])
                popUnimportant.append(i)
        print(popUnimportant)
        #pop unimportant
        for i in sorted(popUnimportant, reverse=True):
                self.endResultArray.pop(i)
        return averageArray


    
#Klasse 1: A1 
A1 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setA\\training")
#A1.makeGenderDiagram()

#A1.makeAgeGenderDiagram()
A2 = SubGroups("D:\\Uni\\MasterSimo\\WiSe2122\\Data Challenges\\Datensatz\\training_setB\\training_setB")
A1.getFileNames()

#A1.readFiles("p000001.psv")
#totalEndResult = A1.endResultArray 
#print("Das ist total Endresult")
#print(totalEndResult)

#for z, (directory, file_head) in enumerate(directorys):
#    for i, filename in enumerate(tqdm(os.listdir(path + directory))):
#        df_temp = pd.read_csv(path + directory + filename, skiprows=0, sep='|')
#        patient_gender = df_temp["Gender"][1]
#        if df_temp["Age"][1] >= 40:
#        dfs.append(df_temp)



A2.getFileNames()
totalEndResult = A1.endResultArray + A2.endResultArray
#print(endResult)

#print("Das ist average Array:")
#print(A1.extract41average())
#print("Das ist Länge der Liste: "+str( A1.endResultArray ))
#print("Das ist totale Länge der Liste: "+ str(len( A1.endResultArray )))

#Load Data
xWerte = []
yWerte = []

for i in range(0, len(totalEndResult)):
    xWerte.append(totalEndResult[i][0])
    yWerte.append(totalEndResult[i][1])

#print(xWerte)
#print(yWerte)

#X, _ = make_blobs(n_samples= len(A1.endResultArray), centers=41, random_state=0)

_ = plt.plot(xWerte, yWerte, marker = '.', linewidth=0)
_ = plt.title('Values over the whole Dataset')
_ = plt.xlabel('41 Features')
_ = plt.ylabel('Values of each Features')
plt.show()


#AB HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIER ist es experimentiell
####YOUTUBE ANFANG
#Prepare data for Model
dbscan_data = A1.endResultArray
#convert to numpy array
dbscan_data = np.array(dbscan_data, dtype=np.float32)
#convert to df
indexDF = []
for i in range(len(dbscan_data)):
    indexDF.append(str(i))

dbscan_data = pd.DataFrame(data=dbscan_data, 
                           index =indexDF, 
                           columns=["xWerte", "yWerte"])
#print(dbscan_data)
#Normalize Data
dbscan_data_scaler = StandardScaler().fit(dbscan_data)
dbscan_data = dbscan_data_scaler.transform(dbscan_data)

#model = DBSCAN(eps=0.1, min_samples=1, metric='euclidean').\
#    fit(dbscan_data)
model = DBSCAN(eps=0.1, min_samples=1).fit(dbscan_data)
core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
core_samples_mask[model.core_sample_indices_] = True
labels = model.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)


# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = dbscan_data[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = dbscan_data[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title("Estimated number of clusters: %d" % n_clusters_)
plt.show()






#############################
#visualize results
#outliers_df = dbscan_data[model.labels_] == -1
#clusters_df = dbscan_data[model.labels_] != -1
#print(model.labels_)
#print("Das ist outliers")
#print(outliers_df)
#print("Dast ist clusters_df")
#print(clusters_df)

#colors = model.labels_
#colors_clusters = colors[colors != -1]
#color_outliers = 'black'
#print("Das ist colors_clusters")
#print(colors_clusters)

#clusters = Counter(model.labels_)
#print(clusters)
#print(dbscan_data[model.labels_ == -1].head())
#print("Number of Clusters {}".format(len(clusters)-1))
#print(dbscan_data)

#fig = plt.figure()
#ax = fig.add_axes([.1,.1,1,1])
#print("Das ist colors_clusters")
#print(colors_clusters)
#print(clusters_df[0])
#print("Das ist clusters_df")
#clustersdfx  =[]
#clustersdfy  =[]
#outliers_dfx =[]
#outliers_dfy =[]


#for i in range(len(clusters_df)):
#    clustersdfx.append(clusters_df[i][0])
#    clustersdfy.append(clusters_df[i][1]) 

#for i in range(len(outliers_df)):
#    outliers_dfx.append(outliers_df[i][0])
#    outliers_dfy.append(outliers_df[i][1]) 
#print("Das ist len clustersdfx")
#print(clustersdfx)
#print(clustersdfy)
#ax.scatter(clustersdfx, clustersdfy, c = colors_clusters, edgecolors='black' )
#ax.scatter(outliers_dfx, outliers_dfy, c = color_outliers, edgecolors='black' )

#ax.set_xlabel('Measurements')
#ax.set_ylabel('values of Measurements')
#plt.title("Clusterings")
#plt.show()


##### YOUTUBE ENDE



















#############################################################################




# #############################################################################
# Generate sample data
#centers = [[1, 1], [-1, -1], [1, -1]]
#X, labels_true = make_blobs(
#    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
#)

#X = StandardScaler().fit_transform(X)

# #############################################################################
# Compute DBSCAN
#db = DBSCAN(eps=0.3, min_samples=10).fit(X)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
#labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)

#print("Estimated number of clusters: %d" % n_clusters_)
#print("Estimated number of noise points: %d" % n_noise_)
#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
#print(
#    "Adjusted Mutual Information: %0.3f"
#    % metrics.adjusted_mutual_info_score(labels_true, labels)
#)
#print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

# #############################################################################
# Plot result
#import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
#unique_labels = set(labels)
#colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
#for k, col in zip(unique_labels, colors):
#    if k == -1:
        # Black used for noise.
#        col = [0, 0, 0, 1]

#    class_member_mask = labels == k

#    xy = X[class_member_mask & core_samples_mask]
#    plt.plot(
#        xy[:, 0],
#        xy[:, 1],
#        "o",
#        markerfacecolor=tuple(col),
#        markeredgecolor="k",
#        markersize=14,
#    )

#    xy = X[class_member_mask & ~core_samples_mask]
#    plt.plot(
#        xy[:, 0],
#        xy[:, 1],
#        "o",
#        markerfacecolor=tuple(col),
#        markeredgecolor="k",
#        markersize=6,
#    )

#plt.title("Estimated number of clusters: %d" % n_clusters_)
#plt.show()





















































#labels are the cluster
#clustering = DBSCAN(eps=1, min_samples=1).fit(X)
#cluster = clustering.labels_
#print("Anzahl Cluster")
#print( len(set(cluster)))


#Prepare data for Model
#dbscan_data = A1.endResultArray
#print(dbscan_data)
#dbscan_data = list(map(numpy.float32, dbscan_data))
#dbscan_data = np.array(dbscan_data, dtype=np.float32)
#print(dbscan_data)
#dbscan_data = dbscan_data.values.astype('float32', copy=False)
#dbscan_data_scaler = StandardScaler().fit(dbscan_data)
#dbscan_data = dbscan_data_scaler.transform(dbscan_data)
#print("Das ist zweiter DBSCAN")
#print(dbscan_data)
#model = DBSCAN(eps=1, min_samples=1, metric='euclidean').\
#    fit(dbscan_data)

#visualize results
#outliers_df = dbscan_data[model.labels_] == -1
#clusters_df = dbscan_data[model.labels_] != -1
#print(model.labels_)
#print(outliers_df)
#print(clusters_df)

#colors = model.labels_
#colors_clusters = colors[colors != -1]
#color_outliers = 'black'
#print("Das ist colors_clusters")
#print(colors_clusters)

#clusters = Counter(model.labels_)
#print(clusters)
#print(A1.endResultArray[model.labels == -1].head())
#print("Number of Clusters".format(len(clusters)-1))

#fig = plt.figure()
#ax = fig.add_axes([.1,.1,1,1])
#print("Das ist colors_clusters")
#print(colors_clusters)
#print(clusters_df[0])
#print("Das ist clusters_df")


#ax.scatter(clusters_df[0], clusters_df[1], c = colors_clusters/255, edgecolors='black' )
#ax.scatter(outliers_df[0], outliers_df[1], c = color_outliers/255, edgecolors='black' )

#ax.set_xlabel('Measurements')
#ax.set_ylabel('values of Measurements')
#plt.title("Clusterings")
#plt.show()

































