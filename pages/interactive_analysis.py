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

# Dynamic Histogram
st.write("### 📈 Dynamic Histogram")
hist_col = st.selectbox("Select a column for histogram", numeric_data.columns)
fig = px.histogram(data_sample, x=hist_col, title=f"Distribution of {hist_col}")
st.plotly_chart(fig, use_container_width=True)

# Scatter Plot with User Selection
st.write("### 📌 Scatter Plot")
scatter_x = st.selectbox("Select X-axis", numeric_data.columns, index=0)
scatter_y = st.selectbox("Select Y-axis", numeric_data.columns, index=1)
fig = px.scatter(data_sample, x=scatter_x, y=scatter_y, title=f"Scatter Plot: {scatter_x} vs {scatter_y}")
st.plotly_chart(fig, use_container_width=True)

# Word Cloud for Text Analysis
st.write("### ☁ Word Cloud for Common Terms")
text_col = st.selectbox("Select a text column for word cloud", data_sample.select_dtypes(include=[object]).columns)
all_text = " ".join(data_sample[text_col].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
st.image(wordcloud.to_array(), use_container_width=True)