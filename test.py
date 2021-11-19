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

 
 #TAKE HEIGHT INPUT
 #radio button to choose height format
#status = st.selectbox('Select temperature format: ',
#                 ('F', 'C', 'feet'))
 
# compare status value
#if(status == 'F'):
    # take height input in centimeters
 #   Tref = st.number_input('Enter the reference temperature')
#and
#if(status == 'F'):
   # Zref = st.number_input('Enter the reference Zvalue')
     
 # try:
        bmi = Time
#   else:
#       st.text("Enter some value of height")
         
#elif(status == 'meters'):
    # take height input in meters
#    height = st.number_input('Meters')
     
#   try:
#        bmi = weight*dvalue / (height ** 2)
#    except:
 #       st.text("Enter some value of height")
         
#else:
    # take height input in feet
#    height = st.number_input('Feet')
     
    # 1 meter = 3.28
#    try:
#        bmi = weight / (((height/3.28))**2)
#    except:
#        st.text("Enter some value of height")
 
# check if the button is pressed or not
#if st.button('Calculate BMI'):
 #st.write(Temp)
#     else:
#   st.write('Goodbye')
    # print the BMI INDEX
     #st.text("Your BMI Index is {}.".print(bmi))
  print(bmi)  
  chart_data = bmi,
  st.bar_chart(chart_data)
     
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")       
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")
      
    


      
