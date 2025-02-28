import streamlit as st



st.subheader("Big Data Characteristics Analysis")


st.write("## Data Overview")
st.write(f"Showing the first 10 rows of the dataset.")
st.dataframe(st.session_state.data.head(10))

# Volume Analysis
st.write("## 📦 Volume Analysis")
st.info(
    "The dataset contains a large number of records, making it a substantial dataset for analysis."
)
st.metric(label="Total Records in Dataset", value=f"{len(st.session_state.data):,}")

# Variety Analysis
st.write("## 🎭 Variety Analysis")
st.info(
    "The dataset consists of multiple types of data grouped into different categories."
)

data_types = {
    "👤 Demographics": ["Patient ID", "Sex", "Age Category", "Race/Ethnicity"],
    "🩺 Health Conditions": [
        "Heart Attack",
        "Angina",
        "Stroke",
        "Asthma",
        "Skin Cancer",
        "COPD",
        "Depressive Disorder",
        "Kidney Disease",
        "Arthritis",
        "Diabetes",
    ],
    "♿ Disabilities": [
        "Hearing Impairment",
        "Vision Impairment",
        "Cognitive Difficulty",
        "Mobility Difficulty",
        "Self-care Difficulty",
        "Independent Living Difficulty",
    ],
    "🚬 Lifestyle": ["Smoking Status", "E-Cigarette Usage", "Alcohol Consumption"],
    "🧪 Medical Tests & Vaccines": [
        "Chest Scan",
        "HIV Testing",
        "Flu Vaccine (Last 12 months)",
        "Pneumonia Vaccine",
        "Tetanus Vaccine",
        "High-Risk Last Year",
        "Covid Positive",
    ],
    "📏 Physical Measurements": ["Height (m)", "Weight (kg)", "BMI"],
}

for category, labels in data_types.items():
    with st.expander(category):
        st.markdown(
            """
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
            """
            + "".join(
                [
                    f'<span style="background-color: rgba(61, 157, 243, 0.2); padding: 5px 10px; border-radius: 10px; font-size: 14px;">{label}</span>'
                    for label in labels
                ]
            )
            + """
            </div>
            """,
            unsafe_allow_html=True,
        )

# Veracity Analysis
st.write("## 📉 Veracity Analysis")
missing_values = st.session_state.data.isnull().sum()
missing_values = missing_values[missing_values > 0]
if not missing_values.empty:
    st.warning("The dataset contains missing values in the following columns:")
    st.dataframe(missing_values.rename("Missing Count"))
else:
    st.success("No missing values detected in the dataset.")

# Value Analysis
st.write("## 💡 Value Analysis")
st.success(
    "This dataset provides valuable insights into patient demographics, health conditions, and lifestyle factors. Potential applications include:"
)
st.markdown("- ✅ Identifying high-risk groups for chronic diseases.")
st.markdown(
    "- ✅ Understanding correlations between lifestyle choices and medical conditions."
)
st.markdown("- ✅ Assessing the impact of vaccines and medical tests.")