#!/data/data/com.termux/files/usr/bin/env python3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# Add 'overweight' column, initialise to 0 
df['overweight'] = 0
# height is in cm, so divide  by 100  
bmi = df['weight'] / ((df['height']/100) ** 2)
# if bmi is > 25, set overweight to 1 
df.loc[bmi > 25, 'overweight'] = 1
#print(df['overweight'])

# 3
# Normalize data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0.
# If the value is more than 1, set the value to 1.
gluc = df['gluc']
df.loc[gluc == 1, 'gluc'] = 0
df.loc[gluc > 1, 'gluc'] = 1
chol = df['cholesterol']
df.loc[chol == 1, 'cholesterol'] = 0
df.loc[chol > 1, 'cholesterol'] = 1
#print(df['gluc'])
#print(df['cholesterol'])


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt()
    varbls = df_cat['variable']
    # We need to split in to two groupss:
    # cardio = 0 and cardio = 1 
    cardios = df_cat.loc[varbls == 'cardio']

    actives = df_cat.loc[varbls == 'active']
    alcos = df_cat.loc[varbls == 'alco']
    chols = df_cat.loc[varbls == 'cholesterol']
    glucs = df_cat.loc[varbls == 'gluc']
    overs = df_cat.loc[varbls == 'overweight']    
    smokes = df_cat.loc[varbls == 'smoke']

    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    #fig.savefig('catplot.png')
    #return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
