import streamlit as st
import requests

# Set up the Streamlit app
st.title("Heart Disease Prediction App")

# FastAPI endpoint URL
API_URL = "https://fastapi-service-811695623962.us-central1.run.app/predict/"

# Input form for user to enter features
st.header("Enter Patient Details")
age = st.number_input("Age (years)", min_value=1, max_value=120, value=30, step=1)
education = st.number_input("Education (years)", min_value=0, max_value=25, value=12, step=1)  # Whole number input for years of education
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
is_smoking = st.selectbox("Smoking Status", options=[0, 1], format_func=lambda x: "Non-Smoker" if x == 0 else "Smoker")
cigsPerDay = st.number_input("Cigarettes Per Day (whole number)", min_value=0, value=0, step=1)  # Whole number input
BPMeds = st.number_input("Blood Pressure Medication (0=No, 1=Yes)", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
prevalentStroke = st.selectbox("Prevalent Stroke (0=No, 1=Yes)", options=[0, 1])
prevalentHyp = st.selectbox("Prevalent Hypertension (0=No, 1=Yes)", options=[0, 1])
diabetes = st.selectbox("Diabetes (0=No, 1=Yes)", options=[0, 1])
totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=0.0, value=200.0, step=1.0)
BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0, value=25.0, step=1.0)  # Direct entry for BMI
heartRate = st.number_input("Heart Rate (bpm)", min_value=0.0, value=70.0, step=1.0)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.0, value=90.0, step=1.0)
Mean_bp = st.number_input("Mean Blood Pressure (mmHg)", min_value=0.0, value=80.0, step=1.0)  # Direct entry for Mean_bp

# Submit button
if st.button("Predict"):
    # Prepare input data for the API
    input_data = {
        "age": age,
        "education": education,
        "sex": sex,
        "is_smoking": is_smoking,
        "cigsPerDay": cigsPerDay,
        "BPMeds": BPMeds,
        "prevalentStroke": prevalentStroke,
        "prevalentHyp": prevalentHyp,
        "diabetes": diabetes,
        "totChol": totChol,
        "BMI": BMI,
        "heartRate": heartRate,
        "glucose": glucose,
        "Mean_bp": Mean_bp,
    }

    # Send the request to the FastAPI endpoint
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {'Positive' if result['prediction'] == 1 else 'Negative'}")
            if result["probability"] is not None:
                st.write(f"Prediction Probabilities: {result['probability']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
