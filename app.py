import pandas as pd
import streamlit as st
import plotly.express as px 

car_data = pd.read_csv("vehicles_us.csv")

st.header('Análisis exploratorio de datos de vehículos en EE.UU. entre 1908 y 2019')

# Tabla de visualización del dataframe
st.subheader("Tabla de datos")
st.dataframe(car_data, use_container_width=True, hide_index=True)

# Histograma de la columna prices
st.subheader("Histograma de precios de vehículos")
hist_prices = px.histogram(
    car_data,
    x='price',
    nbins=80,
    color='type',
    labels={'price': 'Precio (USD)'}
)

hist_prices.update_layout(
    yaxis_title='Cantidad de vehículos'
)
st.plotly_chart(hist_prices, use_container_width=True)

# Gráfico de dispersión entre odómetro y precio
st.subheader("Gráfico de dispersión entre odómetro y precio")
scatter_plot = px.scatter(
    car_data,
    x='odometer',
    y='price',
    color_discrete_sequence=["#b24dff"],
    labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)'},
)
st.plotly_chart(scatter_plot, use_container_width=True)

# Botón para crear un histograma
# agrupar y contar

if st.button('Cantidad de vehículos por año de fabricación'):
    hist_year = px.histogram(
        car_data,
        'model_year',
        nbins=80,
        color_discrete_sequence=["#33cc33"],
        labels={'model_year': 'Año de fabricación', 'y': 'Cantidad de vehículos'}     
    )

hist_year.update_layout(
        yaxis_title='Cantidad de vehículos'
    )
st.plotly_chart(hist_year, use_container_width=True)
