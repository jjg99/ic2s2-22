#!/usr/bin/env python3
'''
Carga de los datos .csv de Safegraph para ver la movilidad entre areas

'''

import pathlib
import os
import matplotlib.pyplot as plt
import json


currentpath = pathlib.Path().resolve()
mobility_path = str(currentpath) + "/data/mobility/"
cases_path = str(currentpath) + "/data/cases/"
demographics_path = str(currentpath) + "/data/demographics/"
saved_dict_path = str(currentpath) + "/data/dict/"



mob_dict = {}
sum = 0

# Analuyzing all regions in DIR
for dirname in os.scandir(mobility_path):

    if dirname.is_dir() and ".DS_Store" not in str(dirname):
        # Analyzing all .csv mobility files
        for filename in os.scandir(dirname):
            print(str(filename))
            if filename.is_file() and ".DS_Store" not in str(filename) and "TractID_List.csv" not in str(filename):
                with open(filename, encoding='us-ascii') as f:
                    fileLines = f.readlines()

                for line in fileLines:
                    split_line = line.split(",")
                    for el in split_line:
                        sum = sum + int(el)

                mob_dict.update({str(filename): sum})
                sum = 0


    json_dict = json.dumps(mob_dict)

    # open file for writing, "w" 
    with open((saved_dict_path + str(dirname)),"w") as f:
        # write json object to file
        f.write(json_dict)


