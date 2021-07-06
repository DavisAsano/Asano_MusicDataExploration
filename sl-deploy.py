#take CSVs and guidelines from ipynb and apply them in streamlit
#NOTE: Label all with correlations that arent significant or are

import streamlit as st
import pandas as pd
import numpy as np
import glob

#### Read in CSVs ####
path = r'C:\Users\dasan\Documents\GitHub\Music_Data_Asano' #Read multiple CSV by pattern matching
all_files = glob.glob(path +"/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
st.write("""
# A Music Data Exploration App

This app lets you explore different correlations in popular songs over the years
""")

st.sidebar.header('User Input Parameters')

#Need to define input and base Y off X using dfp dataframe // Plot X by Y corr
#Add mode default to all & same with key
# "duration_ms","explicit","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"

mode = st.sidebar.selectbox('Mode',('All','Minor','Major'))
key = st.sidebar.selectbox('Key',('C','C#','D','D#','E','F','F#','G','G#','A','A#','B'))



#df_mode_0
#df_mode_1
if mode == 'All':
    X = st.sidebar.selectbox('X',('Valence', 'Loudness', 'Explicit', 'Energy', 'Duration (Ms)', 'Acousticness'))
    if X == 'Valence':
        Y = st.sidebar.selectbox('Y',('Loudness','Danceability'))
    if X == 'Loudness':
        Y = st.sidebar.selectbox('Y',('Instrumentalness','Energy','Acousticness'))
    if X == 'Explicit':
        Y = st.sidebar.selectbox('Y',('Speechiness','Danceability'))
    if X == 'Energy':
        Y = st.sidebar.selectbox('Y',('Valence'))
    if X == 'Duration (Ms)':
        Y = st.sidebar.selectbox('Y',('Year Released'))
    if X == 'Acousticness':
        Y = st.sidebar.selectbox('Y'('Energy'))

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





