import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("xgb_fraud_model_enhanced.pkl", "rb"))


st.title("Fraud Detection App")

amount = st.number_input("Enter transaction amount:")
oldbalanceOrg = st.number_input("Old balance (Origin):")

if st.button("Predict"):
    result = model.predict([[amount, oldbalanceOrg]])
    st.success("Fraudulent" if result[0] == 1 else "Legit")
