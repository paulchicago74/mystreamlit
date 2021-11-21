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
Tref = st.number_input('Enter the reference temperature', min_value=20)

Zref = st.number_input('Enter the reference Zvalue', min_value=1)

Dvalue = st.number_input('Enter the reference Dvalue', min_value=None, step=0.1)

Temp = st.slider('Enter the temperature', 1, 130, 25)

Time = st.slider('Enter the Time', 1, 130, 25)

BMI = (10 ** ((Temp - Tref)/Zref))/1 * Time

D= BMI / Dvalue


st.metric('Temp', millify(BMI, precision=2), delta=None, delta_color="normal")

st.metric('D value', millify(D, precision=2), delta=None, delta_color="normal")

col1, col2, col3 = st.columns(3)

col1.metric('Temp', BMI, delta=None, delta_color="normal")

col2.write (BMI)

col3.write (D)



option = st.selectbox('choose',
 ('Email', 'Home phone', 'Mobile phone'))
if option == 'Email': st.write('Good')
#st.write('You selected:', option)
          
#else:

#st.write('You selected NOT')

  
    
# st.button('Calculate BMI'):
 # st.write(Temp)
  
 # chart_data = Temp,
#  st.bar_chart(chart_data)
     
  
    


      
