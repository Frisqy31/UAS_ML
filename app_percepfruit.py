import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import os

# Fungsi untuk mendapatkan path file berdasarkan lokasi file saat ini
def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)

# Load model dan encoder
@st.cache_data
def load_model(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)

def predict_fruit(model, input_data):
    return model.predict([input_data]) 

# Load model dan encoder dengan path dinamis
model_path = get_file_path('p_model_fruit.sav')
encoder_path = get_file_path('p_encode_fruit.sav')

model = load_model(model_path)
encoder = load_model(encoder_path)

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
st.title("Aplikasi Prediksi Buah")
st.subheader("Masukkan Input untuk Prediksi Buah")

# Input user
diameter = st.number_input("Diameter (cm)", min_value=0.0, step=0.1)
weight = st.number_input("Weight (grams)", min_value=0.0, step=0.1)
red = st.number_input("Red Value", min_value=0, max_value=255, step=1)
green = st.number_input("Green Value", min_value=0, max_value=255, step=1)
blue = st.number_input("Blue Value", min_value=0, max_value=255, step=1)

# Susun input data ke dalam array
input_data = np.array([diameter, weight, red, green, blue])

# Tombol prediksi
if st.button("Prediksi Buah"):
    try:
        # Prediksi berdasarkan input
        prediction = predict_fruit(model, input_data)

        # Validasi encoder
        if hasattr(encoder, 'inverse_transform'):
            # Dekode hasil prediksi menjadi label
            fruit_type = encoder.inverse_transform(prediction)
            st.success(f"Prediksi: {fruit_type[0]}")
        else:
            st.error("Encoder tidak valid atau tidak mendukung inverse_transform.")
    except Exception as e:
        # Tangani kesalahan
        st.error(f"Terjadi kesalahan saat memprediksi: {e}")
