import streamlit as st



st.set_page_config(layout='wide')
st.sidebar.title('Thermal Matrix Calculation')

product = st.sidebar.selectbox(
     'Product',
     ('Acid or acidified', 'Juice', 'Intermediate foods'))
if product == 'Juice' : st.sidebar.selectbox(
     'Storage',
     ('Refrigerated', 'Frozen'))
if product == 'Acid or acidified' : st.sidebar.selectbox(
     'Storage',
     ('Shelf Stable', 'Refrigerated', 'Frozen'))
#storage = st.sidebar.selectbox(
#     'Storage',
#     ('Shelf Stable', 'Refrigerated', 'Frozen'))
ph = st.sidebar.slider(
     'Select the pH',
     0.00, 14.00)
st.write('Values:', ph)

values2 = st.sidebar.slider(
     'Select the temperaeture in celsius',
     0, 200)
st.write('Values:', values2)

values3 = st.sidebar.slider(
     'Select the time in minutes',
     0, 240)
st.write('Values:', values3)



number = st.sidebar.number_input('Fahrenheit to Celsius conversion')
celsius = (number-32)*5/9
if number > 0: st.sidebar.write('Temp in C:')
if number > 0: st.sidebar.subheader(celsius)

J = 5 * (10**((80 - values2)/5.75))
R = 10 * (10**((90 - values2)/9))
ph1 = 0.1 * (10**((93.3 - values2)/8.9))
ph2 = 1 * (10**((93.3 - values2)/8.9))
ph3 = 2.5 * (10**((93.3 - values2)/8.9))
ph4 = 5 * (10**((93.3 - values2)/8.9))
ph5 = 10 * (10**((93.3 - values2)/8.9))
ph6 = 20 * (10**((93.3 - values2)/8.9))

if product == 'Acid or acidified' and ph < 3.9 : (st.metric(label = "Treatment Time", value=ph1, delta=values3-ph1))
if product == 'Acid or acidified' and 3.9 <= ph < 4.1 : (st.metric(label = "Treatment Time", value=ph2, delta=values3-ph2))
if product == 'Acid or acidified' and 4.1 <= ph < 4.2 : (st.metric(label = "Treatment Time", value=ph3, delta=values3-ph3))
if product == 'Acid or acidified' and 4.2 <= ph < 4.3 : (st.metric(label = "Treatment Time", value=ph4, delta=values3-ph4))
if product == 'Acid or acidified' and 4.3 <= ph < 4.4 : (st.metric(label = "Treatment Time", value=ph5, delta=values3-ph5))
if product == 'Acid or acidified' and 4.4 <= ph <= 4.6 : (st.metric(label = "Treatment Time", value=ph6, delta=values3-ph6))

     
if product == 'Juice' : (st.metric(label = "Treatment Time", value=J, delta=values3-J))
if product == 'Juice' and J < values3: st.success('This is a success message!')
if product == 'Juice' and J > values3: st.error('This is an error message!')
#else:
#    st.error('This is an error message!')

if product == 'Intermediate foods' : st.metric(label = "Treatment Time", value=R)
if product == 'Acid or acidified' and ph < 4.00 : st.write(J)
#G22*(10^((H22-L22)/I22))
texto = '''Temp'''
data= (texto, str(J))


#text_contents = str(J)
st.download_button('Download some text', texto)
#st.download_button('Download some text', 'Temperature' str(J))

