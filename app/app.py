import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="MediLens AI", layout="centered")

st.title("🏥 MediLens AI")
st.write("AI-based Diabetes Risk Prediction System")

# Load model
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "logistic_model.pkl"

model = joblib.load(MODEL_PATH)

st.header("Enter Patient Details")

preg = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 250, 120)
bp = st.number_input("Blood Pressure", 0, 150, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):

    data = np.array([[preg,
                      glucose,
                      bp,
                      skin,
                      insulin,
                      bmi,
                      dpf,
                      age]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")

    st.write(f"Probability : {probability:.2f}")

    st.subheader("Plain English Summary")

    if prediction == 1:
        st.write(
            "The AI model predicts that the patient may be at high risk of diabetes. Please consult a healthcare professional for further diagnosis."
        )
    else:
        st.write(
            "The AI model predicts that the patient is at low risk of diabetes. Maintaining a healthy lifestyle is recommended."
        )