import streamlit as st

st.set_page_config(layout='wide')
st.sidebar.title('Thermal Matrix Calculation')

st.sidebar.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
