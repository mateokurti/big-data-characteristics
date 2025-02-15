import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

data_sample = st.session_state.data

st.subheader("🔍 Interactive Data Exploration")
    
# Allow user to filter dataset dynamically
st.write("### Filter Dataset")
col_to_filter = st.selectbox("Select a column to filter by", data_sample.columns)
unique_values = data_sample[col_to_filter].dropna().unique()
selected_value = st.selectbox("Select a value", unique_values)
filtered_data = data_sample[data_sample[col_to_filter] == selected_value]
st.write(f"### Showing records where {col_to_filter} is {selected_value}")
st.dataframe(filtered_data)

# Correlation Matrix Visualization
st.write("### 📊 Correlation Matrix")
numeric_data = data_sample.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()
fig = px.imshow(corr_matrix, text_auto=True, aspect='auto', title="Correlation Matrix of Numeric Features")
st.plotly_chart(fig, use_container_width=True)

