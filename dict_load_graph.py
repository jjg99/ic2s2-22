#!/usr/bin/env python3
'''
Carga de los datos .csv de Safegraph para ver la movilidad entre areas

'''


import json
import os
import pathlib

from matplotlib import pyplot as plt


currentpath = pathlib.Path().resolve()
dict_path = str(currentpath) + "/data/dict/"
dem_path = str(currentpath) + "data/demographics/"

complete_list = []

# Loading the population per demographic area
for filename in os.scandir(dem_path):
    if filename.is_file():
        with open(filename, encoding='us-ascii') as f:
            lines = f.readlines()


# Loading the dictionaries already built
for filename in os.scandir(dict_path):
    if filename.is_file():
        with open(filename) as f:
            line = f.readline()
            json_dict = json.loads(line)

        print(json_dict)
        print(type(json_dict))
        json_list = json_dict.items()
        json_list = sorted(json_list)
        x, y = zip(*json_list)
        plt.plot(x,y, label=filename)
        
plt.legend()
plt.show()