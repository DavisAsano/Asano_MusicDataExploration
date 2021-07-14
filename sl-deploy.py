#take CSVs and guidelines from ipynb and apply them in streamlit
#NOTE: Label all with correlations that arent significant or are

import streamlit as st
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns 
import os

#### Read in CSVs ####
path = r'C:\Users\dasan\Documents\GitHub\Music_Data_Asano' #Read multiple CSV by pattern matching

st.write("""
# A Music Data Exploration App

This app lets you explore different correlations in popular songs over the years
""")

st.sidebar.header('User Input Parameters')

#Need to define input and base Y off X using dfp dataframe // Plot X by Y corr
#Add mode default to all & same with key
# "duration_ms","explicit","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"

mode = st.sidebar.selectbox('Mode',('All','Minor','Major'))
key = st.sidebar.selectbox('Key',('All','C','C#','D','D#','E','F','F#','G','G#','A','A#','B'))





#dfm1k0.csv = mode 1 key 0
#dfp.csv = popular
#dfk0.csv = key 0
#dfm1.csv = mode 1

#Popular unfiltered
dfp = pd.read_csv('dfp.csv')
if mode == 'All':
    X = st.sidebar.selectbox('X',('valence', 'loudness', 'explicit', 'energy', 'duration_ms', 'acousticness'))
    if X == 'valence':
        Y = st.sidebar.selectbox('Y',('loudness','danceability'))
        dfm0k11.plot.barh()
    if X == 'loudness':
        Y = st.sidebar.selectbox('Y',('instrumentalness','energy','acousticness'))
        sns.regplot(x=dfp[X],y=dfp[Y])
    if X == 'explicit':
        Y = st.sidebar.selectbox('Y',('speechiness','danceability'))
        sns.regplot(x=dfp[X],y=dfp[Y])
    if X == 'energy':
        Y = st.sidebar.selectbox('Y',('valence'))
        sns.regplot(x=dfp[X],y=dfp[Y])
    if X == 'duration_ms':
        Y = st.sidebar.selectbox('Y',('Year Released'))
        sns.regplot(x=dfp[X],y=dfp[Y])
    if X == 'acousticness':
        Y = st.sidebar.selectbox('Y'('energy'))
        sns.regplot(x=dfp[X],y=dfp[Y])

if mode == 'Minor':
    X = st.sidebar.selectbox('X',('Valence','Speechiness','Loudness','Energy','Duration (Ms)'))
    if X == 'Valence':
        Y = st.sidebar.selectbox('Y',('Loudness','Energy','Danceability'))
    if X == 'Speechiness':
        Y = st.sidebar.selectbox('Explicit')
    if X == 'Loudness':
        Y = st.sidebar.selectbox('Acousticness')
    if X == 'Energy':
        Y = st.sidebar.selectbox('Loudness','Acousticness')
    if X == 'Duration (Ms)':
        Y == 'Year Released'
if mode == 'Major':
    X = st.sidebar.selectbox('X',('Valence','Time Signature','Speechiness','Loudness','Energy','Duration (Ms)','Danceability'))
    if X == 'Valence':
        Y = st.sidebar.selectbox('Y',('Loudness','Energy'))
    if X == 'Time Signature':
        Y = st.sidebar.selectbox('Y',('Instrumentalness'))
    if X == 'Speechiness':
        Y = st.sidebar.selectbox('Y',('Explicit'))
    if X == 'Loudness':
        Y = st.sidebar.selectbox('Y',('Acousticness'))
    if X == 'Energy':
        Y = st.sidebar.selectbox('Y',('Loudness','Acousticness'))
    if X == 'Duration (Ms)':
        Y = st.sidebar.selectbox('Y',('Year Released'))
    if X == 'Danceability':
        Y = st.sidebar.selectbox('Y',('Valence'))





