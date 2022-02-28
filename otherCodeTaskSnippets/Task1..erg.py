# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:28:01 2021

@author: dariu
"""
import csv

data = []
data_individual = []

for i in range(1,20643+1):
    filename = "p"+ (10-len(str(i))) * "0" + str(i)
#    print(filename)
        
    with open('p000001.psv', 'r') as patientfile:
        reader = csv.reader(patientfile, delimiter='|')
        j=1
        for row in enumerate(reader):
#            print(row)
            data_individual.append(row)
            j += 1
            
    data.append(data_individual)
    
print(data[23])
        
