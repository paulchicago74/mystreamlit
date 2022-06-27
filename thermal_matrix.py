import streamlit as st

st.set_page_config(layout='wide')
st.sidebar.title('Thermal Matrix Calculation')

product = st.sidebar.selectbox(
     'Product',
     ('Acid or acidified', 'Juice', 'Intermediate foods'))

st.sidebar.selectbox(
     'Sorage',
     ('Shelf Stable', 'Refrigerated', 'Frozen'))
values = st.sidebar.slider(
     'Select the pH',
     0.00, 14.00)
st.write('Values:', values)

values2 = st.sidebar.slider(
     'Select the temperature in celsius',
     0, 200)
st.write('Values:', values2)

J = 5 * (10**((80 - values2)/5.75))


if product == 'Juice' : st.metric(label = "Treatment Time", value=J)

if product == 'Acid or acidified' and values < 4.00 : st.write(J)
#G22*(10^((H22-L22)/I22))

st.metric(label="Gas price", value=4, delta=-0.5,
     delta_color="inverse")
