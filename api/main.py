from fastapi import FastAPI, HTTPException
import pandas as pd

from api.schemas import PassengerData
from api.model_loader import model

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="Predict whether a Titanic passenger survived.",
    version="0.139.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Titanic Survival Prediction API!"
    }

@app.post("/predict")
def predict(passenger: PassengerData):
    try:
        input_data = pd.DataFrame([passenger.model_dump()])

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0]

        confidence = round(max(probability) * 100, 2)

        result = (
            "Survived"
            if prediction == 1
            else "Did Not Survive"
        )

        return {
            "prediction": result,
            "prediction_code": int(prediction),
            "confidence": f"{confidence}%"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )