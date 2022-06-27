import streamlit as st

st.set_page_config(layout='wide')
st.sidebar.title('Thermal Matrix Calculation')

st.sidebar.selectbox(
     'Product',
     ('Acid or acidified', 'Juice', 'Refrigerated Foods'))
