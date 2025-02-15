import streamlit as st


data = st.session_state.data

st.markdown(
    """
            <div style="display: flex; flex-direction: row; justify-content: space-between;">
                <div style="display: flex; flex-direction: row; align-items: center;">
                    <div>
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/University_of_Tirana_logo.svg/1200px-University_of_Tirana_logo.svg.png" style="width: 80px; height: 80px; margin-right: 15px;">
                    </div>
                    <div>
                        <p style="font-size: 14px">
                            <span style="font-weight: bold">University of Tirana</span> <br>
                            <span style="font-weight: bold">Faculty of Natural Sciences</span> <br>
                            <span>Department of Informatics</span> <br>
                        </p>
                    </div>
                </div>
                <div>
                    <p style="font-size: 14px; text-align: right;">
                        <span style="font-weight: bold">M.Sc. Information Systems Engineering</span> <br>
                        <span style="font-weight: bold">Data Analytics</span> <br>
                        <span>Dr. Alba Çomo</span> <br>
                    </p>
                </div>
            </div>
        """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.title("📊 Big Data Characteristics: A Python Analysis")
st.subheader("Data of Patients ( For Medical Field )")

st.write(
    """
In this Big Data Characteristics Analysis, we explore a large-scale medical dataset to uncover insights into health conditions, disabilities, lifestyle factors, medical tests, and physical measurements. Using interactive visualizations, we analyze the prevalence of chronic diseases such as heart attacks, asthma, and diabetes, while also examining risk factors such as smoking, alcohol consumption, and obesity. Additionally, we investigate the impact of vaccinations and medical tests, shedding light on preventive healthcare trends.

This analysis leverages Big Data principles—Volume, Variety, and Veracity—to ensure a comprehensive and accurate representation of patient health. Through intuitive charts, graphs, and structured insights, this dashboard enables data-driven decision-making in the field of public health and medical research.
"""
)

st.subheader("The Team")


st.markdown(
    """
    <div style="display: flex; flex-direction: row; gap: 8px; margin-bottom: 12px;">
    """
    + "".join(
        [
            f'<span style="background-color: rgba(61, 157, 243, 0.2); padding: 5px 10px; border-radius: 10px; font-size: 18px;">{member}</span>'
            for member in st.session_state.team_members
        ]
    )
    + "</div>",
    unsafe_allow_html=True,
)

st.subheader("Data Source")

st.write(
    """
The dataset consists of patient information, including demographic details like age, sex, and state, along with health-related factors such as general health, BMI, and medical history. It covers conditions like heart disease, stroke, diabetes, and asthma, as well as lifestyle choices like smoking, alcohol consumption, and vaccination status.

Source: [Kaggle - Data of Patients ( For Medical Field )](https://www.kaggle.com/datasets/tarekmuhammed/patients-data-for-medical-field)
"""
)
