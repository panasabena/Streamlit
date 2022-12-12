## Importamos librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())
def data_header(dataframe):
    st.header('Data Header')
    st.write(df.head())
def plot(dataframe):
    fig, ax = plt.subplots(1,1)
    ax.scatter(x = dataframe.iloc[:, 0], y = dataframe.iloc[:, 1])
    ax.set_xlabel('SepalLength')
    ax.set_ylabel('SepalWidth')

    st.pyplot(fig)    

## Seteamos un titulo para la pagina 
st.title('Data Exploratory Analysis')
## Insertamos un texto
st.text('This is a data exploratory analysis')
## Creamos titulo en la barra de exploración izquierda
st.sidebar.title('Navigation')

## Creamos el abridor de archivos en la barra de la izquierda
uploaded_file = st.sidebar.file_uploader('Upload your file here')

## Creamos las opciones
options = st.sidebar.radio('Pages', options=['Home',
                                             'Data Statistics',
                                             'Data Header',
                                             'Plot'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

if options == 'Data Statistics':
    stats(df)
    
elif options == 'Data Header':
    data_header(df)
    
elif options == 'Plot':
    plot(df)
