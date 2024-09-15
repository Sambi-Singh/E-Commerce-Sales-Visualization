# Day 1 Aug.31, 2024 - Setting up environment and git environment.

import streamlit as st
import pandas as pd
#import datatime 
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title = 'E-COMMERCE Sales Data')
st.header('Retail Results 2020')
st.subheader('Which product sold the most?')


# Replace this with the path to your CSV file
csv_file = 'business.retailsales.csv'

# Read the CSV file using pandas
df = pd.read_csv(csv_file)

# Display the dataframe in the Streamlit app
st.write(df)

line_graph = px.data.stocks