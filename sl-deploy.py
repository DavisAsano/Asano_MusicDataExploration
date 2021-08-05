# Streamlit GUI for Music Data Correlation Exploration
# TO LAUNCH: streamlit run main.py

import streamlit as st
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns 
import os
import numpy as np
from scipy import stats
import csv
import zipfile


# take in ZIP file for tracks.csv and unzip
if glob.glob("tracks.csv") == []:
    zf = zipfile.ZipFile('tracks.csv.zip','r')
    #print(zf.infolist())
    r = zf.extract("tracks.csv")
    print("Extracted tracks.csv.zip into", r)

# Read in tracks.csv 
df = pd.read_csv("tracks.csv", index_col=None, header=0)


# Use release_date to create Year Released column with only int(year)
df["Year Released"] = pd.to_datetime(df['release_date'])
df["Year Released"] = df["Year Released"].dt.year

### Popularity filter ###
# Filter dataframe to only songs with a popularity score 80+
df_popular = df[df['popularity'] >= 80]
# dfpcorr to do correlations on df_popular
dfpcorr = df_popular
# Filter popular dataframe by key
pk0 = df_popular[df_popular['key'] == 0]
pk1 = df_popular[df_popular['key'] == 1]
pk2 = df_popular[df_popular['key'] == 2]
pk3 = df_popular[df_popular['key'] == 3]
pk4 = df_popular[df_popular['key'] == 4]
pk5 = df_popular[df_popular['key'] == 5]
pk6 = df_popular[df_popular['key'] == 6]
pk7 = df_popular[df_popular['key'] == 7]
pk8 = df_popular[df_popular['key'] == 8]
pk9 = df_popular[df_popular['key'] == 9]
pk10 = df_popular[df_popular['key'] == 10]
pk11 = df_popular[df_popular['key'] == 11]

### Mode and Key filters ###
# Filter popular dataframe to mode 0 
m0 = df_popular[df_popular['mode'] == 0]
# m0corr to do correlations on m0
m0corr = m0
#Filter mode0 dataframe by key
m0k0 = m0[m0['key'] == 0]
m0k1 = m0[m0['key'] == 1]
m0k2 = m0[m0['key'] == 2]
m0k3 = m0[m0['key'] == 3]
m0k4 = m0[m0['key'] == 4]
m0k5 = m0[m0['key'] == 5]
m0k6 = m0[m0['key'] == 6]
m0k7 = m0[m0['key'] == 7]
m0k8 = m0[m0['key'] == 8]
m0k9 = m0[m0['key'] == 9]
m0k10 = m0[m0['key'] == 10]
m0k11 = m0[m0['key'] == 11]
# Filter popular dataframe to mode 1
m1 = df_popular[df_popular['mode'] == 1]
# m1corr to do correlations on m1
m1corr = m1
# Filter mode1 dataframe by key
m1k0 = m1[m1['key'] == 0]
m1k1 = m1[m1['key'] == 1]
m1k2 = m1[m1['key'] == 2]
m1k3 = m1[m1['key'] == 3]
m1k4 = m1[m1['key'] == 4]
m1k5 = m1[m1['key'] == 5]
m1k6 = m1[m1['key'] == 6]
m1k7 = m1[m1['key'] == 7]
m1k8 = m1[m1['key'] == 8]
m1k9 = m1[m1['key'] == 9]
m1k10 = m1[m1['key'] == 10]
m1k11 = m1[m1['key'] == 11]

# Title Text
st.title('Relationships in Music Data (1960-2020)')
# Subheader Text
st.subheader("This app lets you explore different correlations in popular songs (popularity rating of 80+).")
# Bullet Point Text 
st.write("""
* Only relationships with a significant Correlation Coefficent may be selected
** r > 0.30  r < -0.30 **
* The steeper the line the stronger the correlation
""")
###


# Sidebar Label
st.sidebar.header('User Input Parameters')

# Remove error message from Streamlit + Pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)

# Mode Selection
mode = st.sidebar.selectbox('Mode',('All','Minor','Major'))
# Key Selection
key = st.sidebar.selectbox('Key',('All','C','C#','D','D#','E','F','F#','G','G#','A','A#','B'))



### Process as follows:
# Choose Mode, Choose Key 
# Based on Mode and Key display X options with significant correlations
# Based on X option show Y options that lead to significant correlations

# Mode All
# dfpcorr
if mode == 'All': 
    # Key All
    if key == 'All':
        # X options with significant correlations
        X = st.sidebar.selectbox('X',('valence', 'loudness', 'explicit', 'energy', 'duration_ms', 'acousticness'))
        if X == 'valence':
            # Y options with Significant Correlations to Valence
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
## pk0 /// Mode all + key C/0 
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
### pk1 /// Mode All + key C#
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
### pk2 Mode all + key D
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
    ### pk3 Mode all + Key D#
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
    ### pk4 Mode all + Key E
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
                if Y == 'acousticness':
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

    ### pk5 Mode all + Key F
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
    ### pk6 Mode all + Key F#
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
    ### pk7 Mode all + Key G
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
    ### pk8 Mode all + Key G#
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
    ### pk9 Mode all + Key A
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
    ### pk10 Mode all + Key A#
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
    ### pk11 Mode all + Key B
    if key == 'B':
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


### m0 Mode Minor + Key All
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
### m0k0 Mode Minor + Key C
    if key == 'C':
        X = st.sidebar.selectbox('X',('explicit','loudness'))
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=m0k0['explicit'],y=m0k0['danceability'])
                st.pyplot()  
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k0['loudness'],y=m0k0['energy'])    
                st.pyplot()  
### m0k1 Mode Minor + Key C#      
    if key == 'C#':
        X = st.sidebar.selectbox('X',('acousticness','loudness','valence'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k1['acousticness'],y=m0k1['energy'])
                st.pyplot()  
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k1['valence'],y=m0k1['energy']) 
                st.pyplot()  
### m0k2 Mode Minor + Key D      
    if key == 'D':
        X = st.sidebar.selectbox('X',('Year Released','danceability','energy','explicit'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('liveness',''))
            if Y == 'liveness':
                sns.regplot(x=m0k2['Year Released'],y=m0k2['liveness'])
                st.pyplot()  
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('duration_ms','explicit'))
            if Y == 'duration_ms':
                sns.regplot(x=m0k2['danceability'],y=m0k2['duration_ms']) 
                st.pyplot()  
            if Y == 'explicit':
                sns.regplot(x=m0k2['danceability'],y=m0k2['explicit']) 
                st.pyplot()  
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('liveness','valence'))
            if Y == 'liveness':
                sns.regplot(x=m0k2['energy'],y=m0k2['liveness']) 
                st.pyplot()  
            if Y == 'valence':
                sns.regplot(x=m0k2['energy'],y=m0k2['valence']) 
                st.pyplot()  
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('loudness','speechiness'))
            if Y == 'loudness':
                sns.regplot(x=m0k2['explicit'],y=m0k2['loudness']) 
                st.pyplot()  
            if Y == 'speechiness':
                sns.regplot(x=m0k2['explicit'],y=m0k2['speechiness']) 
                st.pyplot()  
        if X == 'liveness':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=m0k2['liveness'],y=m0k2['duration_ms']) 
                st.pyplot()  
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k2['loudness'],y=m0k2['energy']) 
                st.pyplot()  
        if X == 'popularity':
            Y = st.sidebar.selectbox('Y',('energy','liveness'))
            if Y == 'energy':
                sns.regplot(x=m0k2['popularity'],y=m0k2['energy']) 
                st.pyplot()  
            if Y == 'liveness':
                sns.regplot(x=m0k2['popularity'],y=m0k2['liveness']) 
                st.pyplot() 
        if X == 'tempo':
            Y = st.sidebar.selectbox('Y',('danceability','explicit'))
            if Y == 'danceability':
                sns.regplot(x=m0k2['tempo'],y=m0k2['danceability']) 
                st.pyplot()  
            if Y == 'explicit':
                sns.regplot(x=m0k2['tempo'],y=m0k2['explicit']) 
                st.pyplot()  
### m0k3 Mode Minor + Key D#      
    if key == 'D#':
        X = st.sidebar.selectbox('X',('Year Released','danceability','energy','explicit','liveness','loudness','popularity','speechiness'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms','energy'))
            if Y == 'duration_ms':
                sns.regplot(x=m0k3['Year Released'],y=m0k3['duration_ms'])
                st.pyplot()  
            if Y == 'energy':
                sns.regplot(x=m0k3['Year Released'],y=m0k3['energy'])
                st.pyplot() 
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('acousticness','energy'))
            if Y == 'acousticness':
                sns.regplot(x=m0k3['danceability'],y=m0k3['acousticness'])
                st.pyplot()    
            if Y == 'energy':
                sns.regplot(x=m0k3['danceability'],y=m0k3['energy'])
                st.pyplot() 
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=m0k3['energy'],y=m0k3['explicit'])
                st.pyplot()   
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m0k3['explicit'],y=m0k3['loudness'])
                st.pyplot()    
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('acousticness','danceability'))
            if Y == 'acousticness':
                sns.regplot(x=m0k3['liveness'],y=m0k3['acousticness'])
                st.pyplot()    
            if Y == 'danceability':
                sns.regplot(x=m0k3['liveness'],y=m0k3['danceability'])
                st.pyplot()  
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('speechiness','valence'))
            if Y == 'speechiness':
                sns.regplot(x=m0k3['loudness'],y=m0k3['speechiness'])
                st.pyplot()    
            if Y == 'valence':
                sns.regplot(x=m0k3['loudness'],y=m0k3['valence'])
                st.pyplot() 
        if X == 'popularity':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=m0k3['popularity'],y=m0k3['duration_ms'])
                st.pyplot()   
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('duration_ms','explicit'))
            if Y == 'duration_ms':
                sns.regplot(x=m0k3['speechiness'],y=m0k3['duration_ms'])
                st.pyplot()    
            if Y == 'explicit':
                sns.regplot(x=m0k3['speechiness'],y=m0k3['explicit'])
                st.pyplot()     
            if Y == 'popularity':
                sns.regplot(x=m0k3['speechiness'],y=m0k3['popularity'])
                st.pyplot()     
### m0k4 Mode Minor + Key E      
    if key == 'E':
        X = st.sidebar.selectbox('X',('acousticness','duration_ms','energy','valence'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k4['acousticness'],y=m0k4['energy'])
                st.pyplot() 
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=m0k4['duration_ms'],y=m0k4['Year Released'])
                st.pyplot()  
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m0k4['energy'],y=m0k4['loudness'])
                st.pyplot() 
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('energy','loudness'))
            if Y == 'energy':
                sns.regplot(x=m0k4['valence'],y=m0k4['energy'])
                st.pyplot() 
            if Y == 'loudness':
                sns.regplot(x=m0k4['valence'],y=m0k4['loudness'])
                st.pyplot() 
### m0k5 Mode Minor + Key F      
    if key == 'F':
        X = st.sidebar.selectbox('X',('energy','time_signature','valence'))
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m0k5['energy'],y=m0k5['loudness'])
                st.pyplot() 
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m0k5['time_signature'],y=m0k5['acousticness'])
                st.pyplot() 
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k5['valence'],y=m0k5['energy'])
                st.pyplot() 
### m0k6 Mode Minor + Key F#      
    if key == 'F#':
        X = st.sidebar.selectbox('X',('energy',''))
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','loudness','valence'))
            if Y == 'acousticness':
                sns.regplot(x=m0k6['energy'],y=m0k6['acousticness'])
                st.pyplot() 
            if Y == 'loudness':
                sns.regplot(x=m0k6['energy'],y=m0k6['loudness'])
                st.pyplot() 
            if Y == 'valence':
                sns.regplot(x=m0k6['energy'],y=m0k6['valence'])
                st.pyplot() 
### m0k7 Mode Minor + Key G      
    if key == 'G':
        X = st.sidebar.selectbox('X',('energy','valence'))
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m0k7['energy'],y=m0k7['loudness'])
                st.pyplot() 
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=m0k7['valence'],y=m0k7['danceability'])
                st.pyplot() 
### m0k8 Mode Minor + Key G#      
    if key == 'G#':
        X = st.sidebar.selectbox('X',('acousticness','instrumentalness','loudness','tempo'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('liveness',''))
            if Y == 'liveness':
                sns.regplot(x=m0k8['acousticness'],y=m0k8['liveness'])
                st.pyplot() 
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m0k8['instrumentalness'],y=m0k8['loudness'])
                st.pyplot() 
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m0k8['loudness'],y=m0k8['energy'])
                st.pyplot() 
        if X == 'tempo':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=m0k8['tempo'],y=m0k8['danceability'])
                st.pyplot() 
### m0k9 Mode Minor + Key A      
    if key == 'A':
        X = st.sidebar.selectbox('X',('Year Released','acousticness','loudness','speechiness','tempo','time_signature'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=m0k9['Year Released'],y=m0k9['duration_ms'])
                st.pyplot() 
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('loudness','time_signature'))
            if Y == 'loudness':
                sns.regplot(x=m0k9['acousticness'],y=m0k9['loudness'])
                st.pyplot() 
            if Y == 'time_signature':
                sns.regplot(x=m0k9['acousticness'],y=m0k9['time_signature'])
                st.pyplot() 
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','loudness'))
            if Y == 'acousticness':
                sns.regplot(x=m0k9['energy'],y=m0k9['acousticness'])
                st.pyplot() 
            if Y == 'loudness':
                sns.regplot(x=m0k9['energy'],y=m0k9['loudness'])
                st.pyplot() 
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('time_signature',''))
            if Y == 'time_signature':
                sns.regplot(x=m0k9['loudness'],y=m0k9['time_signature'])
                st.pyplot() 
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('time_signature',''))
            if Y == 'time_signature':
                sns.regplot(x=m0k9['loudness'],y=m0k9['time_signature'])
                st.pyplot() 
        if X == 'tempo':
            Y = st.sidebar.selectbox('Y',('explicit','time_signature'))
            if Y == 'explicit':
                sns.regplot(x=m0k9['tempo'],y=m0k9['explicit'])
                st.pyplot() 
            if Y == 'time_signature':
                sns.regplot(x=m0k9['tempo'],y=m0k9['time_signature'])
                st.pyplot() 
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('explicit','danceability'))
            if Y == 'danceability':
                sns.regplot(x=m0k9['time_signature'],y=m0k9['danceability'])
                st.pyplot() 
### m0k10 Mode Minor + Key A#      
    if key == 'A#':
        X = st.sidebar.selectbox('X',('Year Released','acousticness','energy'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=m0k10['Year Released'],y=m0k10['duration_ms'])
                st.pyplot()
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'duration_ms':
                sns.regplot(x=m0k10['acousticness'],y=m0k10['energy'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=m0k10['energy'],y=m0k10['valence'])
                st.pyplot()
### m0k11 Mode Minor + Key B      
    if key == 'B':
        X = st.sidebar.selectbox('X',('Year Released','danceability','energy','explicit'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=m0k11['Year Released'],y=m0k11['duration_ms'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=m0k11['danceability'],y=m0k11['valence'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m0k11['energy'],y=m0k11['loudness'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=m0k11['explicit'],y=m0k11['speechiness'])
                st.pyplot()

### m1 Mode Major + Key All
if mode == 'Major':
    if key == 'All':
        X = st.sidebar.selectbox('X',('danceability','duration_ms','energy','instrumentalness','loudness','speechiness','time_signature','valence'))
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=m1corr['danceability'],y=m1corr['valence'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=m1corr['duration_ms'],y=m1corr['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','loudness'))
            if Y == 'acousticness':
                sns.regplot(x=m1corr['energy'],y=m1corr['acousticness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1corr['energy'],y=m1corr['loudness'])
                st.pyplot()
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m1corr['instrumentalness'],y=m1corr['loudness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m1corr['loudness'],y=m1corr['acousticness'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=m1corr['speechiness'],y=m1corr['explicit'])
                st.pyplot()
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('instrumentalness',''))
            if Y == 'instrumentalness':
                sns.regplot(x=m1corr['time_signature'],y=m1corr['instrumentalness'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('energy','loudness'))
            if Y == 'energy':
                sns.regplot(x=m1corr['valence'],y=m1corr['energy'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1corr['valence'],y=m1corr['loudness'])
                st.pyplot()
### m1k0 Mode Major + Key C      
    if key == 'C':
        X = st.sidebar.selectbox('X',('acousticness','energy','loudness'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k0['acousticness'],y=m1k0['energy'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m1k0['energy'],y=m1k0['loudness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m1k0['loudness'],y=m1k0['acousticness'])
                st.pyplot()
### m1k1 Mode Major + Key C#      
    if key == 'C#':
        X = st.sidebar.selectbox('X',('energy',''))
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness','loudness'))
            if Y == 'acousticness':
                sns.regplot(x=m1k1['energy'],y=m1k1['acousticness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1k1['energy'],y=m1k1['loudness'])
                st.pyplot()
### m1k2 Mode Major + Key D      
    if key == 'D':
        X = st.sidebar.selectbox('X',('acousticness','loudness'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k2['acousticness'],y=m1k2['energy'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k2['loudness'],y=m1k2['energy'])
                st.pyplot()    
### m1k3 Mode Major + Key D#      
    if key == 'D#':
        X = st.sidebar.selectbox('X',('Year Released','danceability','duration_ms','energy','instrumentalness','loudness'))
        if X == 'Year Released':
            Y = st.sidebar.selectbox('Y',('popularity',''))
            if Y == 'popularity':
                sns.regplot(x=m1k3['Year Released'],y=m1k3['popularity'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=m1k3['danceability'],y=m1k3['valence'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('danceability','loudness','valence'))
            if Y == 'danceability':
                sns.regplot(x=m1k3['duration_ms'],y=m1k3['danceability'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1k3['duration_ms'],y=m1k3['loudness'])
                st.pyplot()
            if Y == 'valence':
                sns.regplot(x=m1k3['duration_ms'],y=m1k3['valence'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m1k3['energy'],y=m1k3['acousticness'])
                st.pyplot()
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=m1k3['instrumentalness'],y=m1k3['explicit'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k3['loudness'],y=m1k3['energy'])
                st.pyplot()
### m1k4 Mode Major + Key E      
    if key == 'E':
        X = st.sidebar.selectbox('X',('duration_ms','energy','duration_ms','loudness','valence'))
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=m1k4['duration_ms'],y=m1k4['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m1k4['energy'],y=m1k4['acousticness'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness','energy'))
            if Y == 'acousticness':
                sns.regplot(x=m1k4['loudness'],y=m1k4['acousticness'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=m1k4['loudness'],y=m1k4['energy'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability','energy'))
            if Y == 'danceability':
                sns.regplot(x=m1k4['valence'],y=m1k4['danceability'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=m1k4['valence'],y=m1k4['energy'])
                st.pyplot()
### m1k5 Mode Major + Key F      
    if key == 'F':
        X = st.sidebar.selectbox('X',('instrumentalness','loudness','time_signature','valence'))
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('time_signature',''))
            if Y == 'time_signature':
                sns.regplot(x=m1k5['instrumentalness'],y=m1k5['time_signature'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k5['loudness'],y=m1k5['energy'])
                st.pyplot()
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=m1k5['time_signature'],y=m1k5['danceability'])
                st.pyplot()
        if X == 'valence':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=m1k5['valence'],y=m1k5['danceability'])
                st.pyplot()
### m1k6 Mode Major + Key F#      
    if key == 'F#':
        X = st.sidebar.selectbox('X',('energy','instrumentalness','loudness'))
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('acousticness',''))
            if Y == 'acousticness':
                sns.regplot(x=m1k6['energy'],y=m1k6['acousticness'])
                st.pyplot()
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=m1k6['instrumentalness'],y=m1k6['Year Released'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('acousticness','energy'))
            if Y == 'acousticness':
                sns.regplot(x=m1k6['loudness'],y=m1k6['acousticness'])
                st.pyplot()
            if Y == 'energy':
                sns.regplot(x=m1k6['loudness'],y=m1k6['energy'])
                st.pyplot()
### m1k7 Mode Major + Key G      
    if key == 'G':
        X = st.sidebar.selectbox('X',('loudness',''))
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k7['loudness'],y=m1k7['energy'])
                st.pyplot()
### m1k8 Mode Major + Key G#      
    if key == 'G#':
        X = st.sidebar.selectbox('X',('danceability','energy','explicit','instrumentalness','loudness','tempo','time_signature'))
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('speechiness','time_signature'))
            if Y == 'speechiness':
                sns.regplot(x=m1k8['danceability'],y=m1k8['speechiness'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=m1k8['danceability'],y=m1k8['time_signature'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('instrumentalness','loudness','valence'))
            if Y == 'instrumentalness':
                sns.regplot(x=m1k8['energy'],y=m1k8['instrumentalness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1k8['energy'],y=m1k8['loudness'])
                st.pyplot() 
            if Y == 'valence':
                sns.regplot(x=m1k8['energy'],y=m1k8['valence'])
                st.pyplot()     
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('danceability',''))
            if Y == 'danceability':
                sns.regplot(x=m1k8['explicit'],y=m1k8['danceability'])
                st.pyplot()
        if X == 'instrumentalness':
            Y = st.sidebar.selectbox('Y',('danceability','time_signature'))
            if Y == 'danceability':
                sns.regplot(x=m1k8['instrumentalness'],y=m1k8['danceability'])
                st.pyplot()
            if Y == 'time_signature':
                sns.regplot(x=m1k8['instrumentalness'],y=m1k8['time_signature'])
                st.pyplot() 
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('instrumentalness','loudness'))
            if Y == 'instrumentalness':
                sns.regplot(x=m1k8['loudness'],y=m1k8['instrumentalness'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1k8['loudness'],y=m1k8['loudness'])
                st.pyplot() 
        if X == 'time_signature':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m1k8['time_signature'],y=m1k8['loudness'])
                st.pyplot()
### m1k9 Mode Major + Key A      
    if key == 'A':
        X = st.sidebar.selectbox('X',('loudness',''))
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k9['loudness'],y=m1k9['energy'])
                st.pyplot()
### m1k10 Mode Major + Key A#      
    if key == 'A#':
        X = st.sidebar.selectbox('X',('acousticness','duration_ms','energy','loudness','speechiness'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy','loudness'))
            if Y == 'energy':
                sns.regplot(x=m1k10['acousticness'],y=m1k10['energy'])
                st.pyplot()
            if Y == 'loudness':
                sns.regplot(x=m1k10['acousticness'],y=m1k10['loudness'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released',''))
            if Y == 'Year Released':
                sns.regplot(x=m1k10['duration_ms'],y=m1k10['Year Released'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=m1k10['energy'],y=m1k10['valence'])
                st.pyplot()
        if X == 'loudness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k10['loudness'],y=m1k10['energy'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('explicit',''))
            if Y == 'explicit':
                sns.regplot(x=m1k10['speechiness'],y=m1k10['explicit'])
                st.pyplot()
### m1k11 Mode Major + Key B      
    if key == 'B':
        X = st.sidebar.selectbox('X',('acousticness','danceability','duration_ms','energy','explicit','speechiness'))
        if X == 'acousticness':
            Y = st.sidebar.selectbox('Y',('energy',''))
            if Y == 'energy':
                sns.regplot(x=m1k11['acousticness'],y=m1k11['energy'])
                st.pyplot()
        if X == 'danceability':
            Y = st.sidebar.selectbox('Y',('duration_ms',''))
            if Y == 'duration_ms':
                sns.regplot(x=m1k11['danceability'],y=m1k11['duration_ms'])
                st.pyplot()
        if X == 'duration_ms':
            Y = st.sidebar.selectbox('Y',('Year Released','instrumentalness'))
            if Y == 'Year Released':
                sns.regplot(x=m1k11['duration_ms'],y=m1k11['Year Released'])
                st.pyplot()
            if Y == 'instrumentalness':
                sns.regplot(x=m1k11['duration_ms'],y=m1k11['instrumentalness'])
                st.pyplot()
        if X == 'energy':
            Y = st.sidebar.selectbox('Y',('loudness',''))
            if Y == 'loudness':
                sns.regplot(x=m1k11['energy'],y=m1k11['loudness'])
                st.pyplot()
        if X == 'explicit':
            Y = st.sidebar.selectbox('Y',('speechiness',''))
            if Y == 'speechiness':
                sns.regplot(x=m1k11['explicit'],y=m1k11['speechiness'])
                st.pyplot()
        if X == 'speechiness':
            Y = st.sidebar.selectbox('Y',('valence',''))
            if Y == 'valence':
                sns.regplot(x=m1k11['speechiness'],y=m1k11['valence'])
                st.pyplot()