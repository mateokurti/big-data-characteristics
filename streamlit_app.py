import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("patients_data.csv", sep=";")  # Ensure correct delimiter
    return df


# Set page configuration
st.set_page_config(page_title="Big Data Characteristics", page_icon="📊", layout="wide")

if "data" not in st.session_state:
    st.session_state.data = load_data()

if "team_members" not in st.session_state:
    st.session_state.team_members = [
        "Mateo Kurti",
        "Dea Peka",
        "Klea Halili",
        "Andri Peti",
    ]


pages = {
    "Overview": [
        st.Page("pages/introduction.py", title="Introduction"),
        st.Page("pages/big_data_characteristics.py", title="Big Data Characteristics"),
    ],
    "Patient Data": [
        st.Page("pages/demographics.py", title="📊 Demographics"),
    ],
}

pg = st.navigation(pages)
pg.run()
