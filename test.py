# import the streamlit library
import streamlit as st
import altair as alt
import pandas as pd
from millify import millify


# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# (10^((Temp-Tref)/Zref))/1*Time
# give a title to our app
st.title('Predictive Model Calculation')
 
# TAKE WEIGHT INPUT in kgs
# Tref = st.number_input('Enter the reference temperature', min_value=20)

Zref = st.number_input('Enter the reference Zvalue', min_value=1)

Dvalue = st.number_input('Enter the reference Dvalue', min_value=None, step=0.1)

Temp = st.slider('Enter the temperature', 1, 130, 25)

Time = st.slider('Enter the Time', 1, 130, 25)

Tref = 120

BMI = (10 ** ((Temp - Tref)/Zref))/1 * Time

D= BMI / Dvalue

st.metric('Temp', millify(BMI, precision=2), delta=None, delta_color="normal")

st.metric('D value', millify(D, precision=2), delta=None, delta_color="normal")

col1, col2, col3 = st.columns(3)

col1.metric('Temp', BMI, delta=None, delta_color="normal")

col2.write (BMI)

st.success (BMI)

col3.write (D)

Pub1 = (10 ** ((Temp - Tref)/10))/1 * Time / 3
# if BMI2 == Pub1: st.write(Tref, 200)
Pub2 = (10 ** ((Temp - Tref)/10))/1 * Time / 3



option = st.selectbox('choose',
 ('Email', 'Home phone', 'Mobile phone'))
if option == 'Email': Tref = 200: st.write(Pub1) 
#if option == 'Email': st.write(Pub1) 
if option == 'Home phone': st.write(Pub2)
 
#st.write('You selected:', option)
          
#else:

#st.write('You selected NOT')

  
    
# st.button('Calculate BMI'):
 # st.write(Temp)
  
 #chart_data = Pub1,
#st.bar_chart(chart_data)
     
  
    


      
