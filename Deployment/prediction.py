import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import joblib

def app():
    knn_model = joblib.load('model_knn.pkl')
    svm_model = joblib.load('model_svm.pkl')
    logreg_model = joblib.load('model_logreg.pkl')

    features_names = ['limit_balance', 'pay_0','pay_2',	'pay_3',	'pay_4',	'pay_5',	'pay_6']
    input_features = []

    for features_name in features_names:
        input_feature = st.number_input(features_name, step=0.01)
        input_features.append(input_feature)

    pilihan_model = st.selectbox('pilih_model', ['knn_model', 'svm_mode', 'logreg_model'])

    if st.button('buat_prediksi'):
        input_array = [input_features]
        if pilihan_model == 'knn_model':
            prediksi = knn_model.predict(input_array)
        elif pilihan_model == 'svm_model':
            prediksi = svm_model.predict(input_array)
        elif pilihan_model == 'logreg_model':
            prediksi = logreg_model.predict(input_array)
        st.write('prediksi = ', prediksi[0])