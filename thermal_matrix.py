import streamlit as st

st.set_page_config(layout='wide')
st.sidebar.title('Thermal Matrix Calculation')

product = st.sidebar.selectbox(
     'Product',
     ('Acid or acidified', 'Juice', 'Intermediate foods'))

st.sidebar.selectbox(
     'Sorage',
     ('Shelf Stable', 'Refrigerated', 'Frozen'))
values = st.sidebar.slider(
     'Select the pH',
     0.00, 14.00)
st.write('Values:', values)

if product == 'Juice' : st.write("Juice")
