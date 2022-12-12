import streamlit as st
import pandas as pd
st.title('Data Summary')
st.text('This part contains the statistical info of our data')
#st.markdown('### This is a **markdown**')
## File opener: Muestra un drag and drop de archivos
df = pd.read_csv('./Datasets/Recorrido_de_bicicletas_2015-2019.csv')

## Funcion creada para cuando se seleccione la opcion de "Data Statistics"
## Muestra df.describe ---> Las descripciones estadísticas básicas de un dataset
def stats(df):
    st.header('Data Statistics')
    st.write(df.describe())
