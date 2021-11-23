# import the streamlit library
import streamlit as st
import altair as alt
import pandas as pd
from millify import millify
from pandas_profiling import ProfileReport

# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# (10^((Temp-Tref)/Zref))/1*Time
# give a title to our app
st.title('Predictive Model Calculation')
 
# TAKE WEIGHT INPUT in kgs
# Tref = st.number_input('Enter the reference temperature', min_value=20)

Zref = st.sidebar.number_input('Enter the reference Zvalue', min_value=1)

Dvalue = st.sidebar.number_input('Enter the reference Dvalue', min_value=0.1, step=0.1)

Tref = st.sidebar.number_input('Enter the reference Tref', min_value=0.1, step=0.1)

#Temp = st.sidebar.slider('Enter the temperature', min_value=1, max_value=250, value=120, step=0.1)

Time = st.sidebar.slider('Enter the Time', 1, 130, 25, step=0.1)

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
#Tref = st.empty()
#Tref.line_chart({"Pub1": [120]})
Pub1 = (10 ** ((Temp - Tref)/10))/1 * Time / 3
#Tref = st.empty()
#Tref = 200
Pub2 = (10 ** ((Temp - Tref)/10))/1 * Time / 3
#Tref = st.empty()
#Tref = 180
#Pub1.replace (BMI(Tref, 200))
#Pub1 = BMI.replace(Tref, 200)

option = st.multiselect('choose',
 ('Email', 'Home phone', 'Mobile phone'))
#if option == 'Email': st.write(Pub1) 
#if option == 'Email': Tref = 1200
if option == 'Email':  st.metric(Pub1, millify(Pub1, precision=2), delta=None, delta_color="normal")
st.write (option)
if option == 'Home phone': st.write(BMI)
# st.write (option)
 
# df.loc[df['First Season'] > 1990, 'First Season'] = 1
 
#profile = ProfileReport(
#                        title="Agriculture Data"
#        )
#profile
 
#st.write('You selected:', option)
          
#else:

#st.write('You selected NOT')



form = st.form(key='my-form')
name = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')

st.write('Press submit to have your name printed below')

if submit:
    st.success (BMI)
  
#chart_data = Pub1
#st.bar_chart(chart_data)

container = st.container()
all = st.checkbox("Select all")
 
if all:
    selected_options = container.multiselect("Select one or more options:",
         ["Email", 'Home phone', 'Mobile phone'],['Email', 'Home phone', 'Mobile phone'])
else:
    selected_options =  container.multiselect("Select one or more options:",
        ['Email', 'Home phone', 'Mobile phone'])
  
if selected_options == 'Email':  st.success ('Pub1', millify(Pub1, precision=2), delta=None, delta_color="normal")
#st.write (selected_options)

options = ("male", "female")
i1 = st.multiselect("selectbox 1", options)
st.text("value 1: %s" % i1)
print(BMI)

    
