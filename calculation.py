import pandas as pd
import os
##フィッティングに使うもの
from scipy.optimize import curve_fit
import numpy as np
## 図示のために使うもの
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("fish.csv", encoding="shift-jis")


def sakana_weight(species,length):
    try:
        length=  float(length)
        df_1 = df[df["和名"] == species ]
        kesu1 = float(df_1["a"])
        kesu2 = float(df_1["b"])
        weight = int(kesu1*(length**kesu2)/100)
        if length > 0 :
            df_1 = df[df["和名"] == species ]
            kesu1 = float(df_1["a"])
            kesu2 = float(df_1["b"])
            weight = int(kesu1*(length**kesu2)/100)
            return weight

        else:
            raise Exception # exceptに飛ばす
    except:
        return False

#--------------------------------------#

def sakana_weight_list(filename,species):
    df_2 = pd.read_csv(os.path.join('./static/csv', filename), encoding="shift-jis",header = None)
    max_i = int(len(df_2))
    df_1 = df[df["和名"] == species ]
    kesu1 = float(df_1["a"])
    kesu2 = float(df_1["b"])
    a = []
    for i in range(0,max_i):
        length =  float(df_2.iloc[i,1])
        if length > 0:
            weight = float(kesu1*(length**kesu2)/100)
            a.append(weight)
        else:
            raise Exception # exceptに飛ばす
    df_2 = df_2.assign(weight = a)
    df_2.to_csv(os.path.join('./static/csv',filename),header=False,index=False)
    return os.path.join('./static/csv', filename)

#--------------------------------------#
def func1(X, a, b): # １次式近似
    Y = a * X ** b
    return Y

def sakana_weight_line(filename):
     df_3 = pd.read_csv(os.path.join('./static/csv', filename), encoding="shift-jis",header = None)
     length =  float(df_3["length"])
     weight =  float(df_3["weight"])
     popt, pcov = curve_fit(func1,length,weight) 
     return popt,pcov


