from src import operacion
import streamlit as st

st.title("Calculadora")

x = st.number_input('Valor 1')
y = st.number_input('Valor 2')

op = st.selectbox('Operacion',options=['suma',
                                  'resta',
                                  'division',
                                  'multiplicacion'])

st.header(f'Resultado: {operacion(op,x,y)}')
