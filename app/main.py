from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model once when server starts
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Iris class names
class_names = ["Setosa", "Versicolor", "Virginica"]

# Define input structure
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Create FastAPI app
app = FastAPI(title="ML Deployment Platform", version="1.0")

@app.get("/")
def home():
    return {"message": "ML Deployment Platform is running ✅"}

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0].max()
    return {
        "prediction": class_names[prediction],
        "confidence": round(float(confidence) * 100, 2)
    }
