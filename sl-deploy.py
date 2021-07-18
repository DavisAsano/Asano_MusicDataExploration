#take CSVs and guidelines from ipynb and apply them in streamlit
#NOTE: Label all with correlations that arent significant or are

import streamlit as st
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns 
import os
import numpy as np


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

st.write("""
# A Music Data Exploration App

This app lets you explore different correlations in popular songs over the years
""")

st.sidebar.header('User Input Parameters')

#Need to define input and base Y off X using dfp dataframe // Plot X by Y corr
#Add mode default to all & same with key
# "duration_ms","explicit","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"

# Remove error message
st.set_option('deprecation.showPyplotGlobalUse', False)

mode = st.sidebar.selectbox('Mode',('All','Minor','Major'))
key = st.sidebar.selectbox('Key',('All','C','C#','D','D#','E','F','F#','G','G#','A','A#','B'))

#Popular unfiltered // All = dfpcorr & by key = pk0
if mode == 'All': 
    if key == 'All':
        X = st.sidebar.selectbox('X',('valence', 'loudness', 'explicit', 'energy', 'duration_ms', 'acousticness'))
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('loudness','danceability'))
            if Y == 'loudness':
                sns.regplot(x=dfpcorr['valence'],y=dfpcorr['loudness'])
                st.pyplot()
            if Y == 'danceability':
                sns.regplot(x=dfpcorr['valence'],y=dfpcorr['danceability'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness','energy','instrumentalness'))
            if Y == 'acousticness':
                sns.regplot(x=dfpcorr['loudness'],y=dfpcorr['acousticness'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=dfpcorr['loudness'],y=dfpcorr['energy'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=dfpcorr['loudness'],y=dfpcorr['instrumentalness'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness','danceability'))
            if Y == 'speechiness':
                sns.regplot(x=dfpcorr['explicit'],y=dfpcorr['speechiness'])
                st.pyplot()
            if Y == 'danceability':
                sns.regplot(x=dfpcorr['explicit'],y=dfpcorr['danceability'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('valence'))
            if Y == 'valence':
                sns.regplot(x=dfpcorr['energy'],y=dfpcorr['valence'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released'))
            if Y == 'Year Released':
                sns.regplot(x=dfpcorr['duration_ms'],y=dfpcorr['Year Released'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=dfpcorr['acousticness'],y=dfpcorr['energy'])
                st.pyplot()
## pk0 /// Mode all + key C/0 ### CONTAINS EMPTY CHOICES
    if key == 'C':
        X = st.sidebar.selectbox('X',('Year Released', 'danceability', 'energy', 'loudness'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk0['Year Released'],y=pk0['duration_ms'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('explicit','valence'))
            if Y == 'explicit':
                sns.regplot(x=pk0['danceability'],y=pk0['explicit'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk0['danceability'],y=pk0['valence'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','valence'))
            if Y == 'acousticness':
                sns.regplot(x=pk0['energy'],y=pk0['acousticness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk0['energy'],y=pk0['valence'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness','energy'))
            if Y == 'acousticness':
                sns.regplot(x=pk0['loudness'],y=pk0['acousticness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk0['loudness'],y=pk0['energy'])
                st.pyplot()
### pk1 ### CONTAINS EMPTY CHOICES
    if key == 'C#':
        X = st.sidebar.selectbox('X',('acousticness', 'duration_ms', 'energy', 'explicit','loudness','valence'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk1['acousticness'],y=pk1['energy'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=pk1['duration_ms'],y=pk1['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=pk1['energy'],y=pk1['loudness'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=pk1['explicit'],y=pk1['speechiness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=pk1['loudness'],y=pk1['acousticness'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability','energy'))
            if Y == 'danceability':
                sns.regplot(x=pk1['valence'],y=pk1['danceability'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk1['valence'],y=pk1['energy'])
                st.pyplot()
### pk2 ###
    if key == 'D':
        X = st.sidebar.selectbox('X',('Year Released', 'duration_ms', 'energy', 'explicit','instrumentalness','loudness','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=pk2['Year Released'],y=pk2['loudness'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=pk2['duration_ms'],y=pk2['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=pk2['energy'],y=pk2['acousticness'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=pk2['explicit'],y=pk2['speechiness'])
                st.pyplot()
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('loudness','time_signature','valence'))
            if Y == 'loudness':
                sns.regplot(x=pk2['instrumentalness'],y=pk2['loudness'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=pk2['instrumentalness'],y=pk2['time_signature'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk2['instrumentalness'],y=pk2['valence'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk2['loudness'],y=pk2['energy'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('energy','loudness'))
            if Y == 'energy':
                sns.regplot(x=pk2['valence'],y=pk2['energy'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk2['valence'],y=pk2['loudness'])
                st.pyplot()
### pk3 ###
if key == 'D#':
        X = st.sidebar.selectbox('X',('Year Released', 'danceability', 'duration_ms', 'energy','explicit','loudness','mode','popularity','speechiness','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('popularity','speechiness'))
            if Y == 'popularity':
                sns.regplot(x=pk3['Year Released'],y=pk3['popularity'])
                st.pyplot()
            if Y == 'speechiness':
                sns.regplot(x=pk3['Year Released'],y=pk3['speechiness'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('duration_ms','explicit','mode','speechiness','valence'))
            if Y == 'duration_ms':
                sns.regplot(x=pk3['danceability'],y=pk3['duration_ms'])
                st.pyplot()
            if Y == 'explicit':
                sns.regplot(x=pk3['danceability'],y=pk3['explicit'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk3['danceability'],y=pk3['mode'])
                st.pyplot()
            if Y == 'speechiness':
                sns.regplot(x=pk3['danceability'],y=pk3['speechiness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk3['danceability'],y=pk3['valence'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released','loudness','popularity'))
            if Y == 'Year Released':
                sns.regplot(x=pk3['duration_ms'],y=pk3['Year Released'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk3['duration_ms'],y=pk3['loudness'])
                st.pyplot()
            if Y == 'popularity':
                sns.regplot(x=pk3['duration_ms'],y=pk3['popularity'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','instrumentalness','loudness','mode'))
            if Y == 'acousticness':
                sns.regplot(x=pk3['energy'],y=pk3['acousticness'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=pk3['energy'],y=pk3['instrumentalness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk3['energy'],y=pk3['loudness'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk3['energy'],y=pk3['mode'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('instrumentalness','mode'))
            if Y == 'instrumentalness':
                sns.regplot(x=pk3['explicit'],y=pk3['instrumentalness'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk3['explicit'],y=pk3['mode'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=pk3['loudness'],y=pk3['valence'])
                st.pyplot()
        if X == 'mode':
            Y = st.sidebar.selectbox('Y',('acousticness','duration_ms'))
            if Y == 'acousticness':
                sns.regplot(x=pk3['explicit'],y=pk3['acousticness'])
                st.pyplot()
            if Y == 'duration_ms':
                sns.regplot(x=pk3['explicit'],y=pk3['duration_ms'])
                st.pyplot()  
        if X == 'popularity':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=pk3['popularity'],y=pk3['explicit'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('duration_ms','explicit'))
            if Y == 'duration_ms':
                sns.regplot(x=pk3['speechiness'],y=pk3['duration_ms'])
                st.pyplot()
            if Y == 'explicit':
                sns.regplot(x=pk3['speechiness'],y=pk3['explicit']) 
                st.pyplot()   
            if Y == 'popularity':
                sns.regplot(x=pk3['speechiness'],y=pk3['popularity']) 
                st.pyplot()  
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('duration_ms','energy',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk3['valence'],y=pk3['duration_ms'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk3['valence'],y=pk3['energy']) 
                st.pyplot()   
            if Y == 'mode':
                sns.regplot(x=pk3['valence'],y=pk3['mode']) 
                st.pyplot()  
### pk4 ###
if key == 'E':
        X = st.sidebar.selectbox('X',('Year Released', 'acousticness', 'danceability', 'duration_ms','energy','loudness','popularity','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('acousticness','duration_ms','popularity'))
            if Y == 'acousticness':
                sns.regplot(x=pk4['Year Released'],y=pk4['acousticness'])
                st.pyplot()
            if Y == 'duration_ms':
                sns.regplot(x=pk4['Year Released'],y=pk4['duration_ms'])
                st.pyplot()
            if Y == 'popularity':
                sns.regplot(x=pk4['Year Released'],y=pk4['popularity'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('loudness','valence'))
            if Y == 'loudness':
                sns.regplot(x=pk4['acousticness'],y=pk4['loudness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk4['acousticness'],y=pk4['valence'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=pk4['danceability'],y=pk4['explicit']) 
                st.pyplot() 
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('time_signature',''))
            if Y == 'time_signature':
                sns.regplot(x=pk4['duration_ms'],y=pk4['time_signature'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'v':
                sns.regplot(x=pk4['energy'],y=pk4['acousticness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy','valence'))
            if Y == 'energy':
                sns.regplot(x=pk4['loudness'],y=pk4['energy'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk4['loudness'],y=pk4['valence'])
                st.pyplot()
        if X == 'popularity':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk4['popularity'],y=pk4['duration_ms'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability','energy'))
            if Y == 'danceability':
                sns.regplot(x=pk4['valence'],y=pk4['danceability'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk4['valence'],y=pk4['energy'])
                st.pyplot()

### pk5 ###
if key == 'F':
        X = st.sidebar.selectbox('X',('danceability', 'duration_ms', 'energy', 'explicit','mode','speechiness','time_signature','valence'))
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('mode',''))
            if Y == 'mode':
                sns.regplot(x=pk5['danceability'],y=pk5['mode'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=pk5['duration_ms'],y=pk5['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','explicit'))
            if Y == 'acousticness':
                sns.regplot(x=pk5['energy'],y=pk5['acousticness'])
                st.pyplot()
            if Y == 'explicit':
                sns.regplot(x=pk5['energy'],y=pk5['explicit'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk5['energy'],y=pk5['loudness'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('loudness','mode'))
            if Y == 'loudness':
                sns.regplot(x=pk5['explicit'],y=pk5['loudness'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk5['explicit'],y=pk5['mode'])
                st.pyplot()
        if X == 'mode':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=pk5['mode'],y=pk5['speechiness'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=pk5['speechiness'],y=pk5['explicit'])
                st.pyplot()
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=pk5['time_signature'],y=pk5['danceability'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability','energy','loudness'))
            if Y == 'danceability':
                sns.regplot(x=pk5['valence'],y=pk5['danceability'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk5['valence'],y=pk5['energy'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk5['valence'],y=pk5['loudness'])
                st.pyplot()
### pk6 ###
if key == 'F#':
        X = st.sidebar.selectbox('X',('Year Released', 'acousticness', 'duration_ms', 'energy','explicit','loudness','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk6['Year Released'],y=pk6['duration_ms'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy','valence'))
            if Y == 'energy':
                sns.regplot(x=pk6['acousticness'],y=pk6['energy'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk6['acousticness'],y=pk6['valence'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=pk6['duration_ms'],y=pk6['danceability'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('Year Released','valence'))
            if Y == 'Year Released':
                sns.regplot(x=pk6['energy'],y=pk6['Year Released'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk6['energy'],y=pk6['valence']) 
                st.pyplot()  
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'energy':
                sns.regplot(x=pk6['explicit'],y=pk6['speechiness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness','energy','instrumentalness'))
            if Y == 'acousticness':
                sns.regplot(x=pk6['loudness'],y=pk6['acousticness'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk6['loudness'],y=pk6['energy'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=pk6['loudness'],y=pk6['instrumentalness'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability','loudness'))
            if Y == 'danceability':
                sns.regplot(x=pk6['valence'],y=pk6['danceability'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk6['valence'],y=pk6['loudness'])
                st.pyplot()
### pk7 ###
if key == 'G':
        X = st.sidebar.selectbox('X',('Year Released', 'danceability', 'duration_ms', 'energy','explicit','loudness','mode','speechiness','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('popularity','speechiness'))
            if Y == 'popularity':
                sns.regplot(x=pk7['Year Released'],y=pk7['popularity'])
                st.pyplot()
            if Y == 'speechiness':
                sns.regplot(x=pk7['Year Released'],y=pk7['speechiness'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('duration_ms','explicit','mode','speechiness','valence'))
            if Y == 'duration_ms':
                sns.regplot(x=pk7['danceability'],y=pk7['duration_ms'])
                st.pyplot()
            if Y == 'explicit':
                sns.regplot(x=pk7['danceability'],y=pk7['explicit'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk7['danceability'],y=pk7['mode'])
                st.pyplot()
            if Y == 'speechiness':
                sns.regplot(x=pk7['danceability'],y=pk7['speechiness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk7['danceability'],y=pk7['valence'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released','loudness','popularity'))
            if Y == 'ear Released':
                sns.regplot(x=pk7['duration_ms'],y=pk7['ear Released'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk7['duration_ms'],y=pk7['loudness'])
                st.pyplot()
            if Y == 'popularity':
                sns.regplot(x=pk7['duration_ms'],y=pk7['popularity'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','instrumentalness','loudness','mode'))
            if Y == 'acousticness':
                sns.regplot(x=pk7['energy'],y=pk7['acousticness'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=pk7['energy'],y=pk7['instrumentalness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk7['energy'],y=pk7['loudness'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk7['energy'],y=pk7['mode'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('instrumentalness','mode'))
            if Y == 'instrumentalness':
                sns.regplot(x=pk7['explicit'],y=pk7['instrumentalness'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk7['explicit'],y=pk7['mode'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=pk7['loudness'],y=pk7['valence'])
                st.pyplot()
        if X == 'mode':
            Y = st.sidebar.selectbox('Y',('acousticness','duration_ms'))
            if Y == 'acousticness':
                sns.regplot(x=pk7['mode'],y=pk7['acousticness'])
                st.pyplot()
            if Y == 'duration_ms':
                sns.regplot(x=pk7['mode'],y=pk7['duration_ms'])
                st.pyplot()
        if X == 'popularity':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=pk7['popularity'],y=pk7['explicit'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('duration_ms','explicit','popularity'))
            if Y == 'duration_ms':
                sns.regplot(x=pk7['speechiness'],y=pk7['duration_ms'])
                st.pyplot()
            if Y == 'explicit':
                sns.regplot(x=pk7['speechiness'],y=pk7['explicit'])
                st.pyplot()
            if Y == 'popularity':
                sns.regplot(x=pk7['speechiness'],y=pk7['popularity'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('duration_ms','energy','mode'))
            if Y == 'duration_ms':
                sns.regplot(x=pk7['valence'],y=pk7['duration_ms'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk7['valence'],y=pk7['energy'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk7['valence'],y=pk7['mode'])
                st.pyplot()
### pk8 ###
if key == 'G#':
        X = st.sidebar.selectbox('X',('Year Released', 'acousticness','danceability', 'energy','explicit', 'instrumentalness','loudness','speechiness','tempo','time_signature','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk8['Year Released'],y=pk8['duration_ms'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk8['acousticness'],y=pk8['energy'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('explicit','loudness','speechiness','time_signature','valence'))
            if Y == 'explicit':
                sns.regplot(x=pk8['danceability'],y=pk8['explicit'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk8['danceability'],y=pk8['loudness'])
                st.pyplot()
            if Y == 'speechiness':
                sns.regplot(x=pk8['danceability'],y=pk8['speechiness'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=pk8['danceability'],y=pk8['time_signature'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk8['danceability'],y=pk8['valence'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('instrumentalness','tempo'))
            if Y == 'instrumentalness':
                sns.regplot(x=pk8['energy'],y=pk8['instrumentalness'])
                st.pyplot()
            if Y == 'tempo':
                sns.regplot(x=pk8['energy'],y=pk8['tempo'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=pk8['explicit'],y=pk8['speechiness'])
                st.pyplot()
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('danceability','valence'))
            if Y == 'danceability':
                sns.regplot(x=pk8['instrumentalness'],y=pk8['danceability'])
                st.pyplot()
            if Y == 'duration_ms':
                sns.regplot(x=pk8['instrumentalness'],y=pk8['duration_ms'])
                st.pyplot()   
            if Y == 'valence':
                sns.regplot(x=pk8['instrumentalness'],y=pk8['valence'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness','energy','instrumentalness'))
            if Y == 'acousticness':
                sns.regplot(x=pk8['loudness'],y=pk8['acousticness'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=pk8['loudness'],y=pk8['energy']) 
                st.pyplot()  
            if Y == 'instrumentalness':
                sns.regplot(x=pk8['loudness'],y=pk8['instrumentalness'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('mode',''))
            if Y == 'mode':
                sns.regplot(x=pk8['speechiness'],y=pk8['mode'])
                st.pyplot()
        if X == 'tempo':
            Y = st.sidebar.selectbox('Y',('instrumentalness','loudness','valence'))
            if Y == 'instrumentalness':
                sns.regplot(x=pk8['tempo'],y=pk8['instrumentalness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk8['tempo'],y=pk8['loudness']) 
                st.pyplot()  
            if Y == 'valence':
                sns.regplot(x=pk8['tempo'],y=pk8['valence'])
                st.pyplot()
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('energy','instrumentalness','loudness'))
            if Y == 'energy':
                sns.regplot(x=pk8['time_signature'],y=pk8['energy'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=pk8['time_signature'],y=pk8['instrumentalness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk8['time_signature'],y=pk8['loudness'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('energy','instrumentalness','loudness'))
            if Y == 'energy':
                sns.regplot(x=pk8['valence'],y=pk8['energy'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk8['valence'],y=pk8['loudness'])
                st.pyplot()
### pk9 ###
if key == 'A':
        X = st.sidebar.selectbox('X',('Year Released', 'acousticness','energy', 'loudness','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk9['Year Released'],y=pk9['duration_ms'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('loudness','time_signature','valence'))
            if Y == 'loudness':
                sns.regplot(x=pk9['acousticness'],y=pk9['loudness'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=pk9['acousticness'],y=pk9['time_signature'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk9['acousticness'],y=pk9['valence'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','loudness'))
            if Y == 'acousticness':
                sns.regplot(x=pk9['energy'],y=pk9['acousticness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=pk9['energy'],y=pk9['loudness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('time_signature',''))
            if Y == 'time_signature':
                sns.regplot(x=pk9['loudness'],y=pk9['time_signature'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk9['valence'],y=pk9['energy'])
                st.pyplot()
### pk10 ###
if key == 'A#':
        X = st.sidebar.selectbox('X',('Year Released', 'acousticness','danceability', 'energy','explicit','loudness','mode','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk10['Year Released'],y=pk10['duration_ms'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('loudness','time_signature','valence'))
            if Y == 'loudness':
                sns.regplot(x=pk10['acousticness'],y=pk10['loudness'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=pk10['acousticness'],y=pk10['time_signature'])
            if Y == 'valence':
                sns.regplot(x=pk10['acousticness'],y=pk10['valence'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('acousticness','explicit','mode'))
            if Y == 'acousticness':
                sns.regplot(x=pk10['danceability'],y=pk10['acousticness'])
                st.pyplot()
            if Y == 'explicit':
                sns.regplot(x=pk10['danceability'],y=pk10['explicit'])
                st.pyplot()
            if Y == 'mode':
                sns.regplot(x=pk10['danceability'],y=pk10['mode'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','time_signature','valence'))
            if Y == 'acousticness':
                sns.regplot(x=pk10['energy'],y=pk10['acousticness'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=pk10['energy'],y=pk10['time_signature'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk10['energy'],y=pk10['valence'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=pk10['explicit'],y=pk10['speechiness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk10['loudness'],y=pk10['energy'])
                st.pyplot()
        if X == 'mode':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=pk10['mode'],y=pk10['acousticness'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=pk10['valence'],y=pk10['loudness'])
                st.pyplot()
### pk11 ###
if key == 'A#':
        X = st.sidebar.selectbox('X',('Year Released', 'acousticness','danceability', 'duration_ms','energy','loudness','speechiness','tempo','time_signature','valence'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=pk11['Year Released'],y=pk11['duration_ms'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk11['acousticness'],y=pk11['loudness'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=pk11['danceability'],y=pk11['explicit'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('explicit','instrumentalness'))
            if Y == 'danceability':
                sns.regplot(x=pk11['duration_ms'],y=pk11['danceability'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=pk11['duration_ms'],y=pk11['instrumentalness'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness','valence'))
            if Y == 'loudness':
                sns.regplot(x=pk11['energy'],y=pk11['loudness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk11['energy'],y=pk11['valence'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('tempo','valence'))
            if Y == 'tempo':
                sns.regplot(x=pk11['loudness'],y=pk11['tempo'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk11['loudness'],y=pk11['valence'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('explicit','tempo','valence'))
            if Y == 'explicit':
                sns.regplot(x=pk11['loudness'],y=pk11['explicit'])
                st.pyplot()
            if Y == 'tempo':
                sns.regplot(x=pk11['loudness'],y=pk11['tempo'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=pk11['loudness'],y=pk11['valence'])
                st.pyplot()
        if X == 'tempo':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=pk11['tempo'],y=pk11['energy'])
                st.pyplot()
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=pk11['time_signature'],y=pk11['speechiness'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=pk11['valence'],y=pk11['danceability'])
                st.pyplot()


### m0 ###
if mode == 'Minor':
    if key == 'All':
        X = st.sidebar.selectbox('X',('duration_ms','energy','loudness','speechiness','valence'))
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=m0corr['duration_ms'],y=m0corr['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','loudness'))
            if Y == 'acousticness':
                sns.regplot(x=m0corr['energy'],y=m0corr['acousticness']) 
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m0corr['energy'],y=m0corr['loudness']) 
                st.pyplot() 
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m0corr['loudness'],y=m0corr['acousticness'])
                st.pyplot() 
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability','loudness'))
            if Y == 'danceability':
                sns.regplot(x=m0corr['valence'],y=m0corr['danceability']) 
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=m0corr['valence'],y=m0corr['energy'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m0corr['valence'],y=m0corr['loudness'])
                st.pyplot()  
#if mode == 'Major':