# impotação de bibliotecas

import streamlit as st 
import pandas as pd 
import numpy as np 

#Textos:

st.header('Meu dashboard')
st.sidebar.header("Escolha o que deseja filtrar")

st.markdown("# Meu título")
st.caption("minha legenda")

pessoas = (
    {'Nome':'Caio', 'Idade': 22},
    {'Nome': 'Marcos', 'Idade': 33}
          )

# Exibição de dados:

if st.sidebar.button("Exibir Gráfico"):
    df = pd.DataFrame(
         np.random.rand(10, 4),
         columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência', 'Pessoas por casa']

)

st.bar_chart(df)




