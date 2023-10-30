import streamlit as st
import pandas as pd
import plotly
import matplotlib.pyplot as plt
# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

def app():
    st.markdown(    
        """
        <h1 style='text-align: center;'>Exploratory Data Analysis (EDA)</h1>
        """,
        unsafe_allow_html=True
    )

    # Menggunakan HTML untuk mengatur teks lebih rapi
    st.markdown(
        """
        <h3 style='text-align: center;'>Informasi Dataset</h3>
        <p  style='text-align: justify;'>Dataset yang digunakan adalah <code>credit_card_default</code>, yang berasal dari <code>Google Cloud Platform</code>. Dataset ini bersifat open source, sehingga dapat diakses oleh siapa pun. Dataset ini bertujuan untuk mengidentifikasi pengguna yang membayar tagihan kartu kredit tepat waktu dan pengguna yang tidak. Data ini membantu dalam upaya memahami perilaku pembayaran pengguna kartu kredit. Dataset ini terdiri dari 2965 entri dengan 29 kolom.</p>
        <hr>
        <h3 style='text-align: center;'>Tujuan Dataset:</h3>
        <p style='text-align: justify;'>Tujuan dari dataset ini adalah untuk membuat model prediktif yang dapat memprediksi apakah seorang pengguna akan membayar tagihan kartu kreditnya tepat waktu atau telat. Ini dapat membantu institusi keuangan untuk mengidentifikasi risiko kredit dan mengambil langkah-langkah yang sesuai dalam manajemen risiko.</p>
        """,
        unsafe_allow_html=True  # Mengizinkan penggunaan HTML
    )

    st.markdown('---')

    st.markdown(
        """
        <h3 style='text-align: center;'>Dataframe Dataset</h3>
        """,
        unsafe_allow_html=True  # Mengizinkan penggunaan HTML
    )

    data = pd.read_csv('P1G5_Set_1_fikri.csv')
    st.dataframe(data)

    st.markdown('---')

    st.markdown(
        """
        <h3 style='text-align: center;'>Dataset Info</h3>
        """,
        unsafe_allow_html=True  # Mengizinkan penggunaan HTML
    )

    # gunakan pip install streamlit-pandas-profiling dan pip install pandas_profiling
    # profile = ProfileReport(data, title="Profiling Report")
    # st_profile_report(profile)

    data_describe = data.describe()
    st.dataframe(data_describe)

    st.markdown(
        """
        <h3 style='text-align: center;'>Mengecek Distribusi Data</h3>
        <h4 style='text-align: center;'>1. Distribusi Data Numeric</h4>
        """,
        unsafe_allow_html=True  # Mengizinkan penggunaan HTML
    )

    # Pilih kolom-kolom numerik
    list_numeric = ['limit_balance', 'age', 'bill_amt_1', 'bill_amt_2', 'bill_amt_3', 'bill_amt_4', 'bill_amt_5', 'bill_amt_6', 'pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6']

    # Widget Select Box untuk memilih kolom
    selected_column = st.selectbox("Pilih kolom feature numerik:", list_numeric)

    # Tampilkan histogram berdasarkan pilihan pengguna
    fig, ax = plt.subplots(figsize=(16, 12))
    df_numeric = data[selected_column]
    ax.hist(df_numeric, bins=100)
    plt.title(f'Histogram dari {selected_column}')
    st.pyplot(fig)
    st.markdown(
        """
        <h4 style='text-align: center;'>2. Distribusi Data Target</h4>
        """,
        unsafe_allow_html=True  # Mengizinkan penggunaan HTML
    )

    #  Hitung jumlah setiap nilai
    value_counts = data['default_payment_next_month'].value_counts()

    # Buat grafik batang menggunakan Plotly Express
    fig = plotly.bar(x=value_counts.index, y=value_counts.values, labels={'x': 'Status Pembayaran Berikutnya', 'y': 'Jumlah'})
    st.plotly_chart(fig)
