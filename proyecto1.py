import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title("Proyecto 1: Aplicación de Streamlit")
st.write("Esta es una aplicación de ejemplo para aprender a usar Streamlit.")

num = st.slider("num", 0, 100, step=1)
st.write("El numero ingresado es {}".format(num))

appointment = st.slider("Programe la asesoria:", value=(datetime.time(11, 30), datetime.time(12, 45)))
st.write("Esta agendado para:", appointment)

start_time = st.slider("Ver casos ocurridos en", value=datetime.datetime(2020, 1, 1, 9, 30), format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)

d = st.date_input("Fecha de cumpleaños", datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)

option = st.selectbox('¿Cómo desearía ser contactado/a?', ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

