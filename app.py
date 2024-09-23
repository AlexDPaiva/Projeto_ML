import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

df=pd.read_csv("./pizzas.csv")
modelo = LinearRegression()
x = df [["diametro"]]
y = df [["preco"]]

modelo.fit(x,y)

st.title('Prevendo o valor de uma Pizza :pizza:')
st.divider()
diametro = st.number_input('Digite o Diametro da Pizza: ',
                           value=None, placeholder="Digite Seu numero...",
                           min_value=0.0, max_value=100.00,
                           label_visibility="visible",
                           help="Digite um numro para saber sua pizza")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'O valor da pizza com diametro de {diametro :.2f} é de R${preco_previsto :.2f} reais')






