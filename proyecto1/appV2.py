import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px


st.title('Data Exploratory Analysis')
st.text('This is a web app to explore our data')
st.markdown('### This is a **markdown**')

## File opener: Muestra un drag and drop de archivos
uploaded_file = st.file_uploader('Upload your file here')
## Seteamos titulo al panel de la izquierda
st.sidebar.title('Navigation')
## Mostramos las opciones
options = st.sidebar.radio('Pages', options = ['Home', 'Data Statistics',
                                               'Data Header', 'Plot',
                                               'Interactive Plot'])


if uploaded_file:
    df = pd.read_csv(uploaded_file)

## Funcion creada para cuando se seleccione la opcion de "Data Statistics"
## Muestra df.describe ---> Las descripciones estadísticas básicas de un dataset
def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())
## Funcion que muestra las primeras 5 filas del dataset que le pasemos a la web
def data_header(dataframe):
    st.header('Data Header')
    st.write(df.head())
## Imprime un gráfico básico de matplot. Con los parámetros fijos por defecto
def plot(dataframe):
    fig, ax = plt.subplots(1,1)
    ax.scatter(x = df.iloc[:, 0], y = df.iloc[:, 1])
    ax.set_xlabel('SepalLength')
    ax.set_ylabel('SepalWidth')
    st.pyplot(fig)
## El gráfico interactivo tiene la ventaja de que se puede jugar en la web
## viendo diferentes maneras de imprimir los gráficos, pero la desventaja que
## tiene, es que cada vez que salimos de la pestaña, se resetea.
def interactive_plot(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options = df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options = df.columns)
    col = st.color_picker('Select a plot colour')
    plot = px.scatter(dataframe, x = x_axis_val, y = y_axis_val)
    plot.update_traces(marker = dict(color = col))
    st.plotly_chart(plot)
    
## Selector de opciones
if options == 'Data Statistics':
    stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Plot':
    plot(df)
elif options == 'Interactive Plot':
    interactive_plot(df)



