import streamlit as st
st.title('Explore a dataset')
st.write('A general purpose data exploration app')
file = st.file_uploader("Upload file", type=['csv'])
st.write(file)
