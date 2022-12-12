## Importamos librerias
import streamlit as st
import pandas as pd
## Importamos librerias de machine learning
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

## Cambiando el fondo de color con lo siguiente:
st.markdown('''<style>
            .main {
            background-color: #f5f5f5;
            }
            </style>''',
            unsafe_allow_html = True
            )

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

def get_data(filename):
    bicycle_data = pd.read_csv(filename)
    return bicycle_data

with header:
    ## Seteamos titulo para en la pagina del proyecto
    st.title('Welcome to this Data Exploratory Analysis')
    ## Seteamos breve texto introductorio
    st.text('In this project we are going to look the bicycles movements in the city Buenos Aires')

with dataset:
    ## Seteamos encabezado al proyecto
    st.header('Bicycle trips')
    ## Explicamos de donde obtuvimos nuestro dataset
    st.text('This dataset is from https://data.buenosaires.gob.ar/dataset/')
    ## Abrimos dataset
    bicycle_data = get_data('./Datasets/EstacionesBicicletaModificado.csv')
    ## Imprimimos cabecera del dataset
    st.write(bicycle_data.head())

    st.subheader('Bicycle Stations')
    pulocation_dist = (bicycle_data['id_estacion'].value_counts().head(15))
    st.bar_chart(pulocation_dist)

with features:
    st.header('The features I created')
    st.markdown('**First feature** This feature was created for doing this: example')
    st.markdown('**Second feature** This feature was created for doing this: example')

with model_training:
    st.header('Time to train the model')
    st.text('Here you get the hyperparameters of the model and see how the performance change')
    
    sel_col,disp_col = st.columns(2)
    ## Seteamos el deslizador de valores
    max_depth = sel_col.slider('What should be the max depth of the model?', min_value = 10, max_value = 100, value = 20, step = 2)
    ## Definimos la cantidad de estimadores que queremos que tenga nuestro modelo
    n_estimators = sel_col.selectbox('How many trees should there be?', options = [100,200,300,'No limit'], index = 0) # lo que hace el index 0, es empezar la lista desde 0
    ## Lista de features
    sel_col.text('Here is a list of features: ')
    sel_col.write(bicycle_data.columns)
    ## Input feature
    input_feature = sel_col.text_input('Which feature should be used as the input feature', 'id_estacion')

    ## Creando un random forest regressor

    regr = RandomForestRegressor(max_depth = max_depth, n_estimators = n_estimators)
    
    X = bicycle_data[[input_feature]]
    y = bicycle_data[['id_estacion']]
    #print(X,y)
    # Funciona,pero son un monton de parámetros distintos y no sirve de esa manera
    #regr.fit(X,y.values.ravel())
    #prediction = regr.predict(y)

    disp_col.subheader('Mean Absolute Error of the model is: ')
    #disp_col.write(mean_absolute_error(y, prediction))
    disp_col.subheader('Mean Squared Error of the model is: ')
    #disp_col.write(mean_squared_error(y, prediction))
    disp_col.subheader('R Squared Score of the model is: ')
    #disp_col.write(r2_score(y, prediction))
    
