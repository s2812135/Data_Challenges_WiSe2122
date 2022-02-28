# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:28:48 2021

@author: dariu
"""

import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

path = "C:\\Users\\dariu\\Documents\\Master Wirtschaftsinformatik\\Data Challenges\\Data\\training_setA\\training\\"
#path = "C:\\Users\\dariu\\Documents\\Master Wirtschaftsinformatik\\Data Challenges\\Data\\training_setB\\training_setB\\"

files = os.listdir(path)

timeseries_length = []


for patientfile in files:    
    reader = csv.reader(open(path + patientfile, 'r'), delimiter='|')
    rows_in_file=0
    for row in enumerate(reader):            
        rows_in_file += 1            
    timeseries_length.append(rows_in_file - 1)    
    

mean = statistics.mean(timeseries_length)
median = statistics.median(timeseries_length)
median_low = statistics.median_low(timeseries_length)
median_high = statistics.median_high(timeseries_length)
quantiles = statistics.quantiles(timeseries_length)
standard_deviation = statistics.stdev(timeseries_length)
variance = statistics.variance(timeseries_length)
min_value = min(timeseries_length)
max_value = max(timeseries_length)

print("mean=",mean, "\n" 
      "median=", median, "\n"
      "median_low=", median_low, "\n"
      "median_high=", median_high, "\n"
      "standard_deviation=", standard_deviation, "\n"
      "min_value=", min_value, "\n"
      "max_value=", max_value, "\n"
      "quantiles", quantiles
      )


#Histogram
sns.distplot(timeseries_length, bins=30, kde=False)

#Boxplot
#sns.boxplot(data=timeseries_length, orient="h")
#plt.ylim(5, 250)
#plt.show()

##################
#sns.swarmplot(data=timeseries_length, orient="v")
#plt.ylim(5, 150)
#plt.show()
