# import the streamlit library
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# give a title to our app
st.title('Welcome to BMI Calculator')
 
# TAKE WEIGHT INPUT in kgs
weight = st.number_input('Enter your weight (in kgs)')

dvalue = st.slider('How old are you?', 0, 130, 25)
 
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.selectbox('Select your height format: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
     
    try:
        bmi = weight*dvalue / ((height/100)**2)
    except:
        st.text("Enter some value of height")
         
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
     
    try:
        bmi = weight*dvalue / (height ** 2)
    except:
        st.text("Enter some value of height")
         
else:
    # take height input in feet
    height = st.number_input('Feet')
     
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
 
# check if the button is pressed or not
if(st.button('Calculate BMI')):
     
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
    
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
      
    


      
