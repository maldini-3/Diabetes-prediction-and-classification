# -*- coding: utf-8 -*-
"""diabetes_prediction.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11VzadbXbx2F3JZ55OtSEchlWNelQF8fw
"""

pip install import-ipynb

import streamlit as st
from importlib import import_module
import import_ipynb

def main():
    st.title("Diabetes Risk Prediction App")

    # Import the notebook containing the prediction function
    diabetes_prediction_model = import_module('diabetes_prediction_model')
    st.title("Diabetes Risk Prediction App")

    # Collect user input
    age = st.slider("Age", min_value=1, max_value=120, value=30)
    hypertension = st.selectbox("Hypertension (0 for No, 1 for Yes)", options=[0, 1])
    heart_disease = st.selectbox("Heart Disease (0 for No, 1 for Yes)", options=[0, 1])
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    hba1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, value=100)

    # Button to trigger prediction
    if st.button("Predict"):
        # Call your prediction function
        prediction =pipe.predict(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level)

        # Display prediction
        st.write("Prediction:", prediction)

if __name__ == "__main__":
    main()

