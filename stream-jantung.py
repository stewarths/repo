import pickle
import numpy as np
import streamlit as st
import pandas as pd

# load save model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# judul web
st.title('Prediksi Penyakit Jantung - Kelompok 1 TI 5B')

col1, col2, col3 = st.columns(3)

with col1:
    age = pd.to_numeric(st.text_input('Umur'), errors='coerce')
with col2:
    sex = pd.to_numeric(st.text_input('Jenis Kelamin'), errors='coerce')
with col3:
    cp = pd.to_numeric(st.text_input('Jenis Nyeri Dada'), errors='coerce')
with col1:
    trestbps = pd.to_numeric(st.text_input('Tekanan Darah'), errors='coerce')
with col2:
    chol = pd.to_numeric(st.text_input('Nilai Kolestrol'), errors='coerce')
with col3:
    fbs = pd.to_numeric(st.text_input('Gula Darah'), errors='coerce')
with col1:
    restecg = pd.to_numeric(st.text_input('Hasil Elektrokadiografi'), errors='coerce')
with col2:
    thalach = pd.to_numeric(st.text_input('Detak Jantung Maksimum'), errors='coerce')
with col3:
    exang = pd.to_numeric(st.text_input('Induksi Angina'), errors='coerce')
with col1:
    oldpeak = pd.to_numeric(st.text_input('ST Depression'), errors='coerce')
with col2:
    slope = pd.to_numeric(st.text_input('Slope'), errors='coerce')
with col3:
    ca = pd.to_numeric(st.text_input('Nilai CA'), errors='coerce')
with col1:
    thal = pd.to_numeric(st.text_input('Nilai Thal'), errors='coerce')
    
# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    input_data =[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    if all(not pd.isna(val) for val in input_data):
        heart_prediction = model.predict([input_data])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Masukkan nilai yang valid untuk semua atribut'
        
st.success(heart_diagnosis)