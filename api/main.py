import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.preprocess import preprocess_features

# ---------------------------
# App initialization
# ---------------------------
app = FastAPI(title="Student Dropout Prediction API")

# ---------------------------
# Load model artifacts
# ---------------------------
model = joblib.load("model/lgbm_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

# ---------------------------
# Pydantic input schema
# ---------------------------
class StudentInput(BaseModel):
    Marital_status: int
    Application_mode: int
    Application_order: int
    Course: int
    Daytime_evening_attendance: int
    Previous_qualification: int
    Previous_qualification_grade: float
    Nacionality: int
    Mothers_qualification: int
    Fathers_qualification: int
    Mothers_occupation: int
    Fathers_occupation: int
    Admission_grade: float
    Displaced: int
    Educational_special_needs: int
    Debtor: int
    Tuition_fees_up_to_date: int
    Gender: int
    Scholarship_holder: int
    Age_at_enrollment: int
    International: int
    Curricular_units_1st_sem_credited: int
    Curricular_units_1st_sem_enrolled: int
    Curricular_units_1st_sem_evaluations: int
    Curricular_units_1st_sem_approved: int
    Curricular_units_1st_sem_grade: float
    Curricular_units_1st_sem_without_evaluations: int
    Curricular_units_2nd_sem_credited: int
    Curricular_units_2nd_sem_enrolled: int
    Curricular_units_2nd_sem_evaluations: int
    Curricular_units_2nd_sem_approved: int
    Curricular_units_2nd_sem_grade: float
    Curricular_units_2nd_sem_without_evaluations: int
    Unemployment_rate: float
    Inflation_rate: float
    GDP: float

# ---------------------------
# Prediction endpoint
# ---------------------------
@app.post("/predict")
def predict(data: StudentInput):
    # Convert validated input to DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Apply preprocessing
    df = preprocess_features(df)

    # Predict
    prediction = model.predict(df)[0]

    # Decode label
    label = label_encoder.inverse_transform([prediction])[0]

    return {"prediction": label}
