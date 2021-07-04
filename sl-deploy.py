#take CSVs and guidelines from ipynb and apply them in streamlit
#NOTE: Label all with correlations that arent significant or are

import streamlit as st
import pandas as pandas


st.write("""
# A Music Data Exploration App

This app lets you explore different correlations in popular songs over the years
""")

st.sidebar.header('User Input Parameters')

#Need to define input and base Y off X using dfp dataframe // Plot X by Y corr
#Add mode default to all & same with key
# "duration_ms","explicit","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"
def user_input_features_pop():
   X = st.sidebar.selectbox('X',('Valence', 'Loudness', 'Explicit', 'Energy', 'Duration (Ms)', 'Acousticness'))
   Y = st.sidebar.selectbox('Y',())
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

#df_mode_0
#df_mode_1
mode = st.sidebar.selectbox('Mode',('Major','Minor'))
if mode == 'Major':
    X = st.sidebar.selectbox('X',('Valence','Speechiness','Loudness','Energy','Duration (Ms)'))
    if X == 'Valence':
        Y = st.selectbar.selectbox('Y',('Loudness','Energy','Danceability'))
    if X == 'Speechiness':
        Y = st.selectbar.selectbox('Explicit')
    if X == 'Loudness':
        Y = st.selectbar.selectbox('Acousticness')
    if X == 'Energy':
        Y = st.selectbar.selectbox('Loudness','Acousticness')
    if X == 'Duration (Ms)':
        Y == 'Year Released'
if mode == 'Minor':
    X = st.sidebar.selectbox('X',('Valence','Time Signature','Speechiness','Loudness','Energy','Duration (Ms)','Danceability'))
    if X == 'Valence':
        Y = st.selectbar.selectbox('Y',('Loudness','Energy'))
    if X == 'Time Signature':
        Y = st.selectbar.selectbox('Y',('Instrumentalness'))
    if X == 'Speechiness':
        Y = st.selectbar.selectbox('Y',('Explicit'))
    if X == 'Loudness':
        Y = st.selectbar.selectbox('Y',('Acousticness'))
    if X == 'Energy':
        Y = st.selectbar.selectbox('Y',('Loudness','Acousticness'))
    if X == 'Duration (Ms)':
        Y = st.selectbar.selectbox('Y',('Year Released'))
    if X == 'Danceability':
        Y = st.selectbar.selectbox('Y',('Valence'))


key = st.sidebar.selectbox('Key',())

