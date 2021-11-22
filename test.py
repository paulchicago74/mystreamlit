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

Dvalue = st.number_input('Enter the reference Dvalue', min_value=0.1, step=0.1)

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
if option == 'Email':  st.metric('Pub1', millify(Pub1, precision=2), delta=None, delta_color="normal")
if option == 'Home phone': st.write(Pub2)
st.write (option)
 
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
if selected_options == 'Email':  st.write ('Pub1', millify(Pub1, precision=2), delta=None, delta_color="normal")
st.write (selected_options)
    
options = ("male", "female")
i1 = st.multiselect("multiselect 1", options)
st.text("value 1: %s" % i1)

i2 = st.multiselect("multiselect 2", options, format_func=lambda x: x.capitalize())
st.text("value 2: %s" % i2)

i3 = st.multiselect("multiselect 3", [])
st.text("value 3: %s" % i3)

i4 = st.multiselect("multiselect 4", ["coffee", "tea", "water"], ["tea", "water"])
st.text("value 4: %s" % i4)

i5 = st.multiselect(
    "multiselect 5",
    list(
        map(
            lambda x: f"{x} I am a ridiculously long string to have in a multiselect, so perhaps I should just not wrap and go to the next line.",
            range(5),
        )
    ),
)
st.text("value 5: %s" % i5)

if st._is_running_with_streamlit:

    def on_change():
        st.session_state.multiselect_changed = True

    st.multiselect("multiselect 6", options, key="multiselect6", on_change=on_change)
    st.text("value 6: %s" % st.session_state.multiselect6)
    st.text(f"multiselect changed: {'multiselect_changed' in st.session_state}")



      
