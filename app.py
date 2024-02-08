import streamlit as st
import pandas as pd 
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')

st.header('Informacion general de vehiculos para la venta')
st.subheader('Data Viewer')
st.write(car_data.head(20))
st.subheader('Histograma')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Tipos de vehiculos por estilo')
    fig = px.histogram(car_data, x='model', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)
st.subheader('Histograma de condicion vs modelo')
fig = px.histogram(car_data, x='model_year',color='condition')
st.plotly_chart(fig, use_container_width=True)
st.subheader('Grafico de dispersion')
scatter_button = st.button('Grafico de dispersion')
if scatter_button:
    st.write('Grafico de dispersion para conocer la informacionde vehiculos en venta')
    fig = px.scatter(car_data, x='odometer', y='price',color='model', size_max=60, size='price')
    st.plotly_chart(fig,use_container_width=True, theme='streamlit' )


    
