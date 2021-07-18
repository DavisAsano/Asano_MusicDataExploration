from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import glob
import streamlit as st

#####
## df > dfp --- plot all correlations for keys and modes by themselves
## dfp > m0/m1 --- plot all correlations for modes
## mo/m1 > m0k0/m1k0 --- plot all correlations for keys in modes
#####

# Read in all CSV files
path = r'C:\Users\dasan\Desktop\Repo\Music_Data_Asano' #Read multiple CSV by pattern matching
all_files = glob.glob(path +"/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

# Use release_date to create Year Released column with only int(year)
df["Year Released"] = pd.to_datetime(df['release_date'])
df["Year Released"] = df["Year Released"].dt.year

### Popularity filter ###
# Filter dataframe to only songs with a popularity score 80+
df_popular = df[df['popularity'] >= 80]
dfpcorr = df_popular.corr()
# Filter popular dataframe by key
pk0 = df_popular[df_popular['key'] == 0].corr()
pk1 = df_popular[df_popular['key'] == 1].corr()
pk2 = df_popular[df_popular['key'] == 2].corr()
pk3 = df_popular[df_popular['key'] == 3].corr()
pk4 = df_popular[df_popular['key'] == 4].corr()
pk5 = df_popular[df_popular['key'] == 5].corr()
pk6 = df_popular[df_popular['key'] == 6].corr()
pk7 = df_popular[df_popular['key'] == 7].corr()
pk8 = df_popular[df_popular['key'] == 8].corr()
pk9 = df_popular[df_popular['key'] == 9].corr()
pk10 = df_popular[df_popular['key'] == 10].corr()
pk11 = df_popular[df_popular['key'] == 11].corr()

### Mode and Key filters ###
# Filter popular dataframe to mode 0 
m0 = df_popular[df_popular['mode'] == 0]
m0corr = m0.corr()
#Filter mode0 dataframe by key
m0k0 = m0[m0['key'] == 0].corr()
m0k1 = m0[m0['key'] == 1].corr()
m0k2 = m0[m0['key'] == 2].corr()
m0k3 = m0[m0['key'] == 3].corr()
m0k4 = m0[m0['key'] == 4].corr()
m0k5 = m0[m0['key'] == 5].corr()
m0k6 = m0[m0['key'] == 6].corr()
m0k7 = m0[m0['key'] == 7].corr()
m0k8 = m0[m0['key'] == 8].corr()
m0k9 = m0[m0['key'] == 9].corr()
m0k10 = m0[m0['key'] == 10].corr()
m0k11 = m0[m0['key'] == 11].corr()
# Filter popular dataframe to mode 1
m1 = df_popular[df_popular['mode'] == 1]
m1corr = m1.corr()
# Filter mode1 dataframe by key
m1k0 = m1[m1['key'] == 0].corr()
m1k1 = m1[m1['key'] == 1].corr()
m1k2 = m1[m1['key'] == 2].corr()
m1k3 = m1[m1['key'] == 3].corr()
m1k4 = m1[m1['key'] == 4].corr()
m1k5 = m1[m1['key'] == 5].corr()
m1k6 = m1[m1['key'] == 6].corr()
m1k7 = m1[m1['key'] == 7].corr()
m1k8 = m1[m1['key'] == 8].corr()
m1k9 = m1[m1['key'] == 9].corr()
m1k10 = m1[m1['key'] == 10].corr()
m1k11 = m1[m1['key'] == 11].corr()


#####
# Graphs --- Regression plots for every correlation (+/-) 0.3
# sns.regplot(x=m0['loudness'],y=m0['energy'])
#####

# Graphs for Popular (only key filter needed)
