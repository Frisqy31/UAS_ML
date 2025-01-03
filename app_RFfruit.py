import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os

# Load the trained Random Forest model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'RF_fruit_model.pkl')

with open(model_path, 'rb') as model_file:
    rf_model = pickle.load(model_file)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.selasar.com/wp-content/uploads/2020/06/Buah-Buahan.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
# App title
st.title("Prediksi Jenis Buah")
st.write("Masukkan karakteristik buah.")

# Input fitur
diameter = st.number_input("Diameter (cm)", min_value=0.0)
weight = st.number_input("Weight (g)", min_value=0.0)
red = st.slider("Red Value", 0, 255)
green = st.slider("Green Value", 0, 255)
blue = st.slider("Blue Value", 0, 255)

# Predict button
if st.button("Predict Fruit"):
    # Prepare input data
    input_data = np.array([[diameter, weight, red, green, blue]])
    
    # Make prediction
    prediction = rf_model.predict(input_data)
    
    # Show result
    st.success(f"The predicted fruit type is: {prediction[0]}")