# app.py
import streamlit as st
st.title('Explore a dataset')
st.write('A general purpose data exploration app')
file = st.file_uploader("Upload file", type=['csv'])
st.write(file)

import streamlit as st
import pandas as pd
# def explore(df)...
def transform(df):
  # Select sample size
  frac = st.slider('Random sample (%)', 1, 100, 100)
  if frac < 100:
    df = df.sample(frac=frac/100)
  # Select columns
  cols = st.multiselect('Columns', 
                        df.columns.tolist(),
                        df.columns.tolist())
  df = df[cols]
  return df
def get_df(file)...
def main():
  st.title('Explore a dataset')
  st.write('A general purpose data exploration app')
  file = st.file_uploader("Upload file", type=['csv'])
  if not file:
    st.write("Upload a .csv or .xlsx file to get started")
    return
  df = get_df(file)
  df = transform(df)
  explore(df)
main()
