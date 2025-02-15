import streamlit as st
import pandas as pd
import plotly.express as px

data = st.session_state.data

st.subheader("Patient Health Conditions Analysis")
st.markdown("---")

# Health Conditions Distribution
st.subheader("🩺 Health Conditions Distribution")

conditions = {
    "HadHeartAttack": "Heart Attack",
    "HadAngina": "Angina",
    "HadStroke": "Stroke",
    "HadAsthma": "Asthma",
    "HadSkinCancer": "Skin Cancer",
    "HadCOPD": "COPD",
    "HadDepressiveDisorder": "Depressive Disorder",
    "HadKidneyDisease": "Kidney Disease",
    "HadArthritis": "Arthritis",
}

conditions_counts = data[list(conditions.keys())].sum()

fig = px.bar(
    x=[conditions[condition] for condition in conditions_counts.index],
    y=conditions_counts.values,
    labels={"x": "Health Condition", "y": "Count"},
    title="Chronic Health Conditions Distribution",
)

st.plotly_chart(fig)

# Disabilities
st.subheader("♿ Disabilities Distribution")
disabilities = {
    "DeafOrHardOfHearing": "Hearing Impairment",
    "BlindOrVisionDifficulty": "Vision Impairment",
    "DifficultyConcentrating": "Cognitive Difficulty",
    "DifficultyWalking": "Mobility Difficulty",
    "DifficultyDressingBathing": "Self-care Difficulty",
    "DifficultyErrands": "Independent Living Difficulty",
}

disabilities_counts = data[list(disabilities.keys())].sum()

fig = px.bar(
    x=[disabilities[disability] for disability in disabilities_counts.index],
    y=disabilities_counts.values,
    labels={"x": "Disability", "y": "Count"},
    title="Disabilities Distribution",
)

st.plotly_chart(fig)
