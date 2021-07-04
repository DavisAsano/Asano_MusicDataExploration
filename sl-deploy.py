#take CSVs and guidelines from ipynb and apply them in streamlit
#NOTE: Label all with correlations that arent significant or are

import streamlit as st
import pandas as pandas


st.write("""
# A Music Data Exploration App

This app lets you explore different correlations in popular songs over the years
""")

st.sidebar.header('User Input Parameters')

#Need to define input and base Y off X using df_popular
#Add mode default to all & same with key
def user_input_features_pop():
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

