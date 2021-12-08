# import the streamlit library
import streamlit as st
import altair as alt
import pandas as pd
from millify import millify
from pandas_profiling import ProfileReport
import numpy as np
import streamlit.components.v1 as stc
#from link_button import link_button
# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# (10^((Temp-Tref)/Zref))/1*Time
# give a title to our app
st.sidebar.title('Predictive Model Calculation')

uploaded_file = st.sidebar.file_uploader("Upload Files",type=['csv'])
if uploaded_file is None:
    st.write("")  

if uploaded_file is not None:
    file_details = uploaded_file.getvalue()

if uploaded_file is not None:
    header_list = ["Time", "Temp"]
    df3 = pd.read_csv(uploaded_file, names=header_list)
    #header_list = ["Name", "Dept"]
    #df3 = pd.read_csv(uploaded_file, names=header_list)
    st.write(df3)

   
   # df3['sums'] = df3.sum(axis=1)
   # st.write(df3)
#else: st.write("")
#bytes_data = uploaded_file.getvalue()
# st.write(bytes_data)
 
# TAKE WEIGHT INPUT in kgs
# Tref = st.number_input('Enter the reference temperature', min_value=20)

Zref = st.sidebar.number_input('Enter the reference Zvalue', value=5.0, min_value=1.0)

Dvalue = st.sidebar.number_input('Enter the reference Dvalue', value=5.0, min_value=0.1, step=0.1)

Tref = st.sidebar.number_input('Enter the reference Tref', value=150.0, min_value=0.1, step=0.1)

st.sidebar.subheader('Parameters', anchor=None)

Temp = st.sidebar.slider('Enter the temperature', min_value=1.00, max_value=250.00, value=120.00, step=0.5)

Time = st.sidebar.slider('Enter the Time', value=10.00, min_value=0.1, max_value=200.0, step=0.5)

genre = st.sidebar.radio(
    "Predict minumum D-value required?",
    ('Yes', 'No'))
if genre == 'Yes': Wanted_D = st.sidebar.number_input('Enter the Dvalue', min_value=0.1, step=0.1)
else:
    st.write("")

#Wanted_D = st.sidebar.number_input('Enter the Dvalue', min_value=0.1, step=0.1)
Fvalue0 = 0
Fvalue1 = (Fvalue0 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/10) - 0))
Fvalue2 = (Fvalue1 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/9) - (Time/10)))
Fvalue3 = (Fvalue2 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/8) - (Time/9)))
Fvalue4 = (Fvalue3 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/7) - (Time/8)))
Fvalue5 = (Fvalue4 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/6) - (Time/7)))
Fvalue6 = (Fvalue5 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/5) - (Time/6)))
Fvalue7 = (Fvalue6 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/4) - (Time/5)))
Fvalue8 = (Fvalue7 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/3) - (Time/4)))
Fvalue9 = (Fvalue8 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/2) - (Time/3)))
Fvalue10 = (Fvalue9 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/1) - (Time/2)))

Dvalue0 = 0
Dvalue1 = Fvalue1 / Dvalue
Dvalue2 = Fvalue2 / Dvalue
Dvalue3 = Fvalue3 / Dvalue
Dvalue4 = Fvalue4 / Dvalue
Dvalue5 = Fvalue5 / Dvalue
Dvalue6 = Fvalue6 / Dvalue
Dvalue7 = Fvalue7 / Dvalue
Dvalue8 = Fvalue8 / Dvalue
Dvalue9 = Fvalue9 / Dvalue
Dvalue10 = Fvalue10 / Dvalue

if uploaded_file is not None:
    #df3["Fo"] = df3["Name"] * Zref
    df3["Fo"] = ((10 ** ((df3["Temp"] - Tref)/Zref) + (10 ** ((df3["Temp"] - Tref)/Zref)))/2*((df3["Time"])-(df3["Time"].shift())))
    st.write(df3)
    
    #df['col'].shift()

df = pd.DataFrame({
    'F-value': [Fvalue0, Fvalue1, Fvalue2, Fvalue3, Fvalue4, Fvalue5, Fvalue6, Fvalue7, Fvalue8, Fvalue9, Fvalue10],
    #'D-value': [Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10]
})

df2 = pd.DataFrame({
    #'F-value': [Fvalue0, Fvalue1, Fvalue2, Fvalue3, Fvalue4, Fvalue5, Fvalue6, Fvalue7, Fvalue8, Fvalue9, Fvalue10],
    'Dvalue': [Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10],
    #'Time': [0, Time/10, Time/9, Time/8, Time/7, Time/6, Time/5, Time/4, Time/3, Time/2, Time/1],
    
})

y = np.array([Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10]).reshape((-1, 1))
#x = np.array([0, Time/10, Time/9, Time/8, Time/7, Time/6, Time/5, Time/4, Time/3, Time/2, Time/1]).reshape((-1, 1))
x_1 = np.array([Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10])
y_1 = np.array([0, Time/10, Time/9, Time/8, Time/7, Time/6, Time/5, Time/4, Time/3, Time/2, Time/1])
#x, y = np.array(x), np.array(y)
#model = LinearRegression()
#model.fit(y, x)
n = np.size(x_1)
n_xy = x_1 * y_1
x_mean = np.mean(x_1)
y_mean = np.mean(y_1)
Sxy = np.sum(x_1*y_1)- n*x_mean*y_mean
Sxx = np.sum(x_1*x_1) - n*x_mean*x_mean
b1 = Sxy/Sxx
b0 = y_mean-b1*x_mean
#st.write('slope b1 is', b1)
#st.write('intercept b0 is', b0)
if genre == 'Yes': st.write('The time you need for a D-value of', Wanted_D ,'is' , millify(b1*Wanted_D + b0, precision=2))



#Tref = 120

#BMI = (10 ** ((Temp - Tref)/Zref))/1 * Time

#D= BMI / Dvalue

#st.metric('Temp', millify(BMI, precision=2), delta=None, delta_color="normal")

#st.metric('D value', millify(D, precision=2), delta=None, delta_color="normal")

col1, col2, col3 = st.columns(3)

col1.metric('F-value', millify(Fvalue10, precision=2), delta=None, delta_color="normal")

col2.metric('D value', millify(Dvalue10, precision=2), delta=None, delta_color="normal")

if genre == 'Yes': col3.metric('Predicted time for the D-value', millify(b1*Wanted_D + b0, precision=2), delta=None, delta_color="normal")
else:
    st.write("")

#st.success (BMI)

Pub1 = (10 ** ((Temp - Tref)/10))/1 * Time / 3
#Tref = st.empty()
#Tref = 200
Pub2 = (10 ** ((Temp - Tref)/10))/1 * Time / 3
#Tref = st.empty()
#Tref = 180
#Pub1.replace (BMI(Tref, 200))
#Pub1 = BMI.replace(Tref, 200)

#option = st.multiselect('choose',
# ('Email', 'Home phone', 'Mobile phone'))
#if option == 'Email': st.write(Pub1) 
#if option == 'Email': Tref = 1200
#if option == 'Email':  st.metric(Pub1, millify(Pub1, precision=2), delta=None, delta_color="normal")
#st.write (option)
#if option == 'Home phone': st.write(BMI)

form = st.form(key='my-form')
name = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')

st.write('Press submit to have your name printed below')

if submit:
    st.success (BMI)
  
#chart_data = Pub1
#st.bar_chart(chart_data)

#container = st.container()
#all = st.checkbox("Select all")
 
#if all:
#    selected_options = container.multiselect("Select one or more options:",
#         ["Email", 'Home phone', 'Mobile phone'],['Email', 'Home phone', 'Mobile phone'])
#else:
#    selected_options =  container.multiselect("Select one or more options:",
#        ['Email', 'Home phone', 'Mobile phone'])
  
#if selected_options == 'Email':  st.success ('Pub1', millify(Pub1, precision=2), delta=None, delta_color="normal")
#st.write (selected_options)

#options = ("male", "female")
#i1 = st.multiselect("selectbox 1", options)
#st.text("value 1: %s" % i1)
#print(BMI)

#_clicked = link_button(name = 'Click Me!', url = 'https://docs.streamlit.io/en/stable/')


col1, col2 = st.columns(2)
chart = col1.line_chart(df)
chart = col2.line_chart(df2)



    
