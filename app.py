# Day 1 Aug.31, 2024 - Setting up environment and git environment.

import streamlit as st
import pandas as pd
import datatime
import plotly.express as px
import plotly.graph_objects as go

# read the data from cvs file
data_file = pd.read_csv("/E-COMMERCE DATA/business.retailsales.csv")