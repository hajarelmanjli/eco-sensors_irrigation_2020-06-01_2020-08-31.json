import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open('eco-sensors_irrigation_2020-06-01_2020-08-31.json') as fichier:
    data_dict = json.load(fichier)
    #print(data_dict)   
humidity_dataframe = pd.DataFrame(data_dict)
humidity_dataframe



def clean_data2(data):
    for n in range(len(data)):
         if data[n]==200:
                data[n]=np.nan
    return data
