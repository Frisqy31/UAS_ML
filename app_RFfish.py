import streamlit as st
import pickle
import pandas as pd
import os

# Load Random Forest model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'RF_fish_model.pkl')

with open(model_path, 'rb') as model_file:
    rf_model = pickle.load(model_file)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://asset.kompas.com/crops/H_0XFt6n1ztJF8rqgbG_XFJChaA=/100x99:900x632/1200x800/data/photo/2022/12/19/63a03b83a97e3.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title("Aplikasi Klasifikasi Jenis Ikan")
st.write("Masukkan data ikan untuk mengetahui spesiesnya.")

# Input fitur
length = st.number_input("Masukkan panjang ikan (cm):", min_value=0.0)
weight = st.number_input("Masukkan berat ikan (g):", min_value=0.0)
w_l_ratio = st.number_input("Masukkan rasio lebar-panjang ikan:", min_value=0.0, max_value=1.0)

# Prediksi
if st.button("Prediksi"):
    # Data input dari pengguna
    input_data = pd.DataFrame([[length, weight, w_l_ratio]], columns=['length', 'weight', 'w_l_ratio'])
    
    try:
        # Prediksi menggunakan model
        prediction = rf_model.predict(input_data)
        st.write(f"Spesies Ikan: {prediction[0]}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")