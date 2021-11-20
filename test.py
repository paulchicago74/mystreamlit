# import the streamlit library
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# give a title to our app
st.title('Predictive Model Calculation')
 
# TAKE WEIGHT INPUT in kgs
Tref = st.number_input('Enter the reference temperature')

Zref = st.number_input('Enter the reference Zvalue')

Temp = st.slider('Enter the temperature', 0, 130, 25)

Time = st.slider('Enter the Time', 0, 130, 25)

st.metric('Temp', Temp, delta=None, delta_color="normal")

# st.button('Calculate BMI'):
 # st.write(Temp)
  
 # chart_data = Temp,
#  st.bar_chart(chart_data)
     
  
    


      
