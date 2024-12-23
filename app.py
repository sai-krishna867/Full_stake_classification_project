from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the .pkl model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize the FastAPI app
app = FastAPI()

# Root endpoint to return a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Define the input schema for the API
class InputData(BaseModel):
    age: int
    education: float
    sex: int
    is_smoking: int
    cigsPerDay: float
    BPMeds: float
    prevalentStroke: int
    prevalentHyp: int
    diabetes: int
    totChol: float
    BMI: float
    heartRate: float
    glucose: float
    Mean_bp: float

# Define the predict endpoint
@app.post("/predict/")
def predict(data: InputData):
    # Prepare the input data as a numpy array
    input_features = np.array([
        [
            data.age,
            data.education,
            data.sex,
            data.is_smoking,
            data.cigsPerDay,
            data.BPMeds,
            data.prevalentStroke,
            data.prevalentHyp,
            data.diabetes,
            data.totChol,
            data.BMI,
            data.heartRate,
            data.glucose,
            data.Mean_bp,
        ]
    ])

    # Make a prediction using the loaded model
    prediction = model.predict(input_features)  # Adjust if the model needs specific preprocessing
    prediction_proba = model.predict_proba(input_features) if hasattr(model, "predict_proba") else None

    # Return the prediction as a response
    return {
        "prediction": int(prediction[0]),  # Assuming a single prediction output
        "probability": prediction_proba.tolist()[0] if prediction_proba is not None else None
    }
