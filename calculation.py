import pandas as pd
import os
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

def sakana_wight_list(filename,species):
    df_2 = pd.read_csv(os.path.join('./static/csv', filename), encoding="shift-jis",heade=False,index=False)
    try:
        max_i = int(len(df_2))
        df_1 = df[df["和名"] == species ]
        kesu1 = float(df_1["a"])
        kesu2 = float(df_1["b"])
        for i in range(0,max_i):
            if length > 0:
             df_1 = df[df["和名"] == species ]
             kesu1 = float(df_1["a"])
             kesu2 = float(df_1["b"])
             length=  float(df_2.iloc[i,0])
             df_2["weight"] = int(kesu1*(length[i,1]**kesu2)/100)
             df_2.to_csv(os.path.join('./static/csv', filename))
            return os.path.join('./static/csv', filename)
        else:
            raise Exception # exceptに飛ばす
    except:
        return False

