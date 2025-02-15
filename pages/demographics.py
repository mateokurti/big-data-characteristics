import streamlit as st
import plotly.express as px
import pandas as pd

st.subheader("Patient Demographics Analysis")
st.markdown("---")

# Age Distribution
st.subheader("📊 Age Distribution")

data = st.session_state.data
data["AgeCategory"] = pd.Categorical(data["AgeCategory"], ordered=True)
data = data.sort_values("AgeCategory")

fig = px.histogram(data, x="AgeCategory", title="Patient Age Distribution")
st.plotly_chart(fig, use_container_width=True)

# Sex Distribution
st.subheader("⚧ Sex Distribution")
sex_counts = st.session_state.data["Sex"].value_counts()
fig = px.pie(values=sex_counts.values, names=sex_counts.index, title="Sex Distribution")
st.plotly_chart(fig, use_container_width=True)

# Race/Ethnicity Distribution
st.subheader("🌎 Race/Ethnicity Distribution")
race_counts = st.session_state.data["RaceEthnicityCategory"].value_counts()
fig = px.bar(
    x=race_counts.index,
    y=race_counts.values,
    labels={"x": "Race/Ethnicity", "y": "Count"},
    title="Race/Ethnicity Distribution",
)
st.plotly_chart(fig, use_container_width=True)
