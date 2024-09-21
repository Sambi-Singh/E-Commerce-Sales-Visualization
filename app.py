# Day 1 Aug.31, 2024 - Setting up environment and git environment.

import streamlit as st
import pandas as pd
#import datatime 
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title = 'E-COMMERCE Sales Data')
st.header('Retail Results 2020')
st.subheader('Which product sold the most?')



# Load your CSV data
data = pd.read_csv("business.retailsales.csv")

# Clean the data
clean_data = data.dropna(subset=["Product Type", "Total Net Sales"])

# Create a colorful bar graph using Plotly without text annotations inside the bars
fig = px.bar(clean_data, x="Product Type", y="Total Net Sales", 
             title="Product Type vs Net Sales", 
             color="Product Type", 
             labels={"Total Net Sales": "Net Sales", "Product Type": "Product Type"},
             template="plotly")

# Adjust axis labels and remove grid lines
fig.update_layout(
    xaxis_title="Product Type",
    yaxis_title="Total Net Sales",
    xaxis_tickangle=-45,  # Rotate x-axis labels if needed
    xaxis_showgrid=False,  # Remove grid lines for the x-axis
    yaxis_showgrid=False   # Remove grid lines for the y-axis
)
# Remove the lines inside the bars (marker outlines)
fig.update_traces(marker_line_width=0)


# Create a pie chart using Plotly to show the Net Quantity of each Product Type
pie_fig = px.pie(clean_data, values='Net Quantity', names='Product Type', 
                 title='Net Quantity of Each Product Type',
                 color_discrete_sequence=px.colors.qualitative.Set3)


# Display the bar graph in Streamlit
st.title("Product Type vs Net Sales Bar Graph")
st.plotly_chart(fig)


st.title("Net Quantity of Each Product Type")
st.plotly_chart(pie_fig)

