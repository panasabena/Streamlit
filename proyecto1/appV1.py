## Importamos librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

## Seteamos un titulo para la pagina 
st.title('Data Exploratory Analysis')
## Insertamos un texto
st.text('This is a data exploratory analysis')
## Creamos el abridor de archivos
uploaded_file = st.file_uploader('Upload your file here')

if uploaded_file:
    st.header('Data Statistics')
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())

    fig, ax = plt.subplots(1,1)
    ax.scatter(x = df.iloc[:, 0], y = df.iloc[:, 1])
    ax.set_xlabel('SepalLength')
    ax.set_ylabel('SepalWidth')

    st.pyplot(fig)
