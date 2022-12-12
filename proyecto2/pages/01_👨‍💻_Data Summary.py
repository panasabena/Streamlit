import streamlit as st
import pandas as pd
import io
import missingno as msno
import matplotlib.pyplot as plt
import plotly_express as px

st.title('Data Summary')
st.text('This part contains the statistical info of our data')
#st.markdown('### This is a **markdown**')
## File opener: Muestra un drag and drop de archivos
df = pd.read_csv('./Datasets/Estaciones-bicicletas.csv')
buffer = io.StringIO()
info = df.info(buf = buffer)
s = buffer.getvalue()
fig = msno.matrix(df)


## Funcion creada para cuando se seleccione la opcion de "Data Statistics"
## Muestra df.describe ---> Las descripciones estadísticas básicas de un dataset
def stats(df):
    st.header('Data Statistics')
    st.write(df.head(5))
    st.markdown('**Filas -- Columnas**')
    st.write(df.shape)
    st.markdown('#### The missing values ​​of each "estaciones bicicletas" column are shown')
    st.markdown('**How many missing values ​​are in each column?**')
    st.write(df.isna().sum())
    st.markdown('Data types of each attribute')
    #st.plotly_chart(fig, use_container_width = True)
    return stats

stats(df)


