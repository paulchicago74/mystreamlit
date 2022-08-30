import streamlit as st
from simple_colors import *
from pytesseract import image_to_string 
from PIL import Image
from fpdf import FPDF
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
from streamlit.components.v1 import iframe

st.set_page_config(
   page_title="Thermal Matrix Calculator",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
#st.sidebar.title('Thermal Matrix Calculation')



#pdf = PDF(orientation='P', unit='mm', format='A4')

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

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
ph = st.sidebar.number_input(
     'Select the pH',
     0.00, 14.00)
#st.write('Values:', ph)

values2 = st.sidebar.number_input(
     'Select the temperaeture in celsius',
     60.0, 200.0, key='values2')
#st.write('Temperature:', values2)

values3 = st.sidebar.number_input(
     'Select the time in minutes',
     0.0, 240.5)
#st.write('Values:', values3)

if product == 'Intermediate foods' : aw = st.sidebar.number_input(
     'Select the water activity',
     0.60, 0.99)

hotfill = st.sidebar.radio(
     "Is the product hot filled?",
     ('Yes', 'No'))

if hotfill == 'Yes':
     hftemp = st.sidebar.number_input(
     'Select the temperature in celsius',
     60, 200, key=hotfill)
if hotfill == 'Yes':	 
	ph7 = 0.6 * (10**((74.44 - hftemp)/10.833))
	ph8 = 2.5 * (10**((74.44 - hftemp)/9.5))

if hotfill == 'Yes':
	 timehotfill = st.sidebar.number_input(
     'Select the Time (min)', 0.00, 240.00, key='hftime')
if hotfill == 'Yes':
	 phhotfill = st.sidebar.number_input(
     'Select the pH',
     0.00, 4.60, key='hftemp')
else:
     st.sidebar.write(" ")



st.warning('Values Selected for Thermal Processing')

col1, col2 = st.columns(2)
with col1:
    project = st.text_input('Project')

with col2:
    d = str(st.date_input(
    "Date"))
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("pH")
    st.write('Values:', ph)

with col2:
    st.subheader("Temperature")
    st.write('Temperature:', values2, "C")

with col3:
    st.subheader("Time")
    st.write('Values:', values3)

number = st.sidebar.number_input('Fahrenheit to Celsius conversion')
celsius = (number-32)*5/9
if number > 0: st.sidebar.write('Temp in C:')
if number > 0: st.sidebar.subheader(celsius)
round (celsius, 2)

J = 8.5 * (10**((60 - values2)/4.9))
R = 10 * (10**((90 - values2)/9))
#IF = 1 * (10**((72 - hftemp)/7.5))
ph1 = 2.5 * (10**((71.11 - values2)/8.9))
ph2 = 0.75 * (10**((76.67 - values2)/8.9))
ph3 = 1.5 * (10**((76.67 - values2)/8.9))
ph4 = 3 * (10**((76.67 - values2)/8.9))
ph5 = 6 * (10**((76.67 - values2)/8.9))
ph6 = 12 * (10**((76.67 - values2)/8.9))
ph7 = 24 * (10**((76.67 - values2)/8.9))
ph8 = 32 * (10**((76.67 - values2)/8.9))
ph9 = 1 * (10**((93.3 - values2)/8.9))
ph10 = 2.5 * (10**((93.3 - values2)/8.9))
ph11 = 5 * (10**((93.3 - values2)/8.9))
ph12 = 10 * (10**((93.3 - values2)/8.9))
ph13 = 20 * (10**((93.3 - values2)/8.9))


Cs1 = 10 * (10**((90 - values2)/10))
Cs2 = 37 * (10**((86 - values2)/7))

#ph8 = 2.5 * (10**((74.44 - hftemp)/9.5))

#round(ph1, 2)

if product == 'Acid or acidified' and ph <= 3.2 : (st.metric(label = "Treatment Time", value=round(ph1, 2), delta=round((values3-ph1),2)))
if product == 'Acid or acidified' and 3.2 < ph <= 3.3 : (st.metric(label = "Treatment Time", value=round(ph2, 2), delta=round((values3-ph2),2)))
if product == 'Acid or acidified' and 3.3 < ph <= 3.4 : (st.metric(label = "Treatment Time", value=round(ph3, 2), delta=round((values3-ph3),2)))
if product == 'Acid or acidified' and 3.4 < ph <= 3.5 : (st.metric(label = "Treatment Time", value=round(ph4, 2), delta=round((values3-ph4),2)))
if product == 'Acid or acidified' and 3.5 < ph <= 3.6 : (st.metric(label = "Treatment Time", value=round(ph5, 2), delta=round((values3-ph5),2)))
if product == 'Acid or acidified' and 3.6 < ph <= 3.7 : (st.metric(label = "Treatment Time", value=round(ph6, 2), delta=round((values3-ph6),2)))
if product == 'Acid or acidified' and 3.7 < ph <= 3.8 : (st.metric(label = "Treatment Time", value=round(ph7, 2), delta=round((values3-ph7),2)))
if product == 'Acid or acidified' and 3.8 < ph <= 3.9 : (st.metric(label = "Treatment Time", value=round(ph8, 2), delta=round((values3-ph8),2)))
if product == 'Acid or acidified' and 3.9 < ph <= 4.1 : (st.metric(label = "Treatment Time", value=round(ph9, 2), delta=round((values3-ph9),2)))
if product == 'Acid or acidified' and 4.1 < ph <= 4.2 : (st.metric(label = "Treatment Time", value=round(ph10, 2), delta=round((values3-ph10),2)))
if product == 'Acid or acidified' and 4.2 < ph <= 4.3 : (st.metric(label = "Treatment Time", value=round(ph11, 2), delta=round((values3-ph11),2)))    
if product == 'Acid or acidified' and 4.3 < ph <= 4.4 : (st.metric(label = "Treatment Time", value=round(ph12, 2), delta=round((values3-ph12),2)))
if product == 'Acid or acidified' and 4.4 < ph <= 4.6 : (st.metric(label = "Treatment Time", value=round(ph13, 2), delta=round((values3-ph13),2)))

#if product == 'Acid or acidified' and ph <= 3.2 and values3 >= ph1 : a = st.success('Process is Safe') 
#else : a = st.error('Not Safe!')
	
if product == 'Acid or acidified' and ph <= 3.2  : a = ph1
if product == 'Acid or acidified' and 3.2 < ph <= 3.3 : a = ph2
if product == 'Acid or acidified' and 3.3 < ph <= 3.4 : a = ph3
if product == 'Acid or acidified' and 3.4 < ph <= 3.5 : a = ph4
if product == 'Acid or acidified' and 3.5 < ph <= 3.6 : a = ph5
if product == 'Acid or acidified' and 3.6 < ph <= 3.7 : a = ph6
if product == 'Acid or acidified' and 3.7 < ph <= 3.8 : a = ph7
if product == 'Acid or acidified' and 3.8 < ph <= 3.9 : a = ph8
if product == 'Acid or acidified' and 3.9 < ph <= 4.1 : a = ph9
if product == 'Acid or acidified' and 4.1 < ph <= 4.2 : a = ph10
if product == 'Acid or acidified' and 4.2 < ph <= 4.3 : a = ph11   
if product == 'Acid or acidified' and 4.3 < ph <= 4.4 : a = ph12
if product == 'Acid or acidified' and 4.4 < ph <= 4.6 : a = ph13

if product == 'Acid or acidified' and values3 >= a : result = st.success('Process is Safe') 
else : result = st.error('Not Safe!')
#st.write(result)

	
	
if product == 'Juice' : (st.metric(label = "Treatment Time", value=round(J, 2), delta=values3-J))
if product == 'Juice' and ph < 4.41 and J < values3: st.success('Process is Safe')
if product == 'Juice' and ph < 4.41 and J > values3: st.error('Not Safe!')
if product == 'Juice' and ph > 4.40 : st.error('Not Safe! Check for Clostridium')
#if product == 'Juice' : hotfill == st.write("")
#else:
#    st.error('This is an error message!')

#if product == 'Intermediate foods' : st.metric(label = "Treatment Time", value=R)
if product == 'Intermediate foods' and ph >4.6 and values2<65 and  aw<0.80: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-88))
if product == 'Intermediate foods' and ph >4.6 and values2<65 and  0.80 <= aw < 0.9: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-90))
if product == 'Intermediate foods' and ph >4.6 and values2<65 and  aw>=0.9: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-87))

if product == 'Intermediate foods' and ph >4.6 and 65 <= values2 < 72 and  aw<0.80: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-27))
if product == 'Intermediate foods' and ph >4.6 and 65 <= values2 < 72 and  0.80 <= aw < 0.9: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-30))
if product == 'Intermediate foods' and ph >4.6 and 65 <= values2 < 72 and  aw>=0.9: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-27))

if product == 'Intermediate foods' and ph >4.6 and values2>=72 and  aw<0.80: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-8))
if product == 'Intermediate foods' and ph >4.6 and values2>=72 and  0.80 <= aw < 0.9: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-4))
if product == 'Intermediate foods' and ph >4.6 and values2>=72 and  aw>=0.9: (st.metric(label = "Treatment Time for Salmonella", value=values3, delta=values3-2))

if product == 'Intermediate foods' and ph >4.2 and aw>=0.92 and values2>=90: (st.metric(label = "Treatment Time for Clostridium spp. spores", value=round(values3,2), delta=round((values3-Cs1),2)))
if product == 'Intermediate foods' and ph >4.2 and aw>=0.92 and values2<90: (st.metric(label = "Treatment Time for Clostridium spp. spores", value=round(values3, 2), delta=round((values3-Cs2),2)))


if product == 'Acid or acidified' and ph < 4.00 : st.write(J)
#G22*(10^((H22-L22)/I22))



if hotfill == 'Yes' and product == 'Acid or acidified':	
	st.warning('Values Selected for Hot Fill')

	col1, col2, col3 = st.columns(3)

	with col1:
		st.subheader("pH")
		st.write('Values:', round(phhotfill, 2))

	with col2:
		st.subheader("Temperature")
		st.write('Temperature:', round(hftemp, 2), "C")

	with col3:
		st.subheader("Time")
		st.write('Values:', round(timehotfill,2))

if hotfill == 'Yes' and product == 'Intermediate foods':	
	st.header('Values Selected for Hot Fill')

	col1, col2 = st.columns(2)

	with col1:
		st.subheader("Temperature")
		st.write('Temperature:', round(hftemp, 2), "C")

	with col2:
		st.subheader("Time")
		st.write('Values:', round(timehotfill,2))		


if hotfill == 'Yes':
	IF = 1 * (10**((72 - hftemp)/7.5))
	if product == 'Acid or acidified' and phhotfill <= 4.1 : (st.metric(label = "Treatment Time", value=round(ph7, 2), delta=round((timehotfill-ph7),2)))
	if product == 'Acid or acidified' and 4.11 <= phhotfill < 4.61 : (st.metric(label = "Treatment Time", value=round(ph8, 2), delta=round((timehotfill-ph8),2)))
	if phhotfill <= 4.1 and timehotfill > ph7 : st.success('Process time and temperature will mitigate environmental contamintation (vegetative pathogens and spoilage organisms) ')
	if phhotfill <= 4.1 and timehotfill < ph7 : st.error('Process NOT safe')
	if  4.11 <= phhotfill < 4.61 and timehotfill > ph8 : st.success('Process time and temperature will mitigate environmental contamintation (vegetative pathogens and spoilage organisms) ')
	if  4.11 <= phhotfill < 4.61 and timehotfill < ph8 : st.error('Hot Fill Process NOT safe')
	if product == 'Intermediate foods' : (st.metric(label = "Treatment Time", value=round(IF, 2), delta=round((timehotfill-IF),2)))

	#title = st.markdown('*Title *')
	#G22*(10^((H22-L22)/I22))
	texto = '''Temp = '''
	data= str(J)
	data1 = product
	data2 = ('                                                                                     Temp=\n  \n' + data + 'Product= ' + product+ '\n' + '' + d)
	#data3 = ("This is P1\u\n\n" + "This is P2")

	#logo = open("logo.png", "rb") 
	#text_contents = str(J)
	#st.download_button('Download some text', logo, file_name="flower.png")
	#st.download_button('Download some text', 'Temperature' str(J))

	print(green('hello'))
	print(green('hello', 'bold'))
	print(green('hello', ['bold', 'underlined']))



	html = template.render(
	    ph=ph,
	    values2=values2,
	    project = project,
	    d = d,
	    values3 = values3,
	    #value = value,
	    #values3=f"{values3}/100",
	    J = J,
	    a = round((a),2),
	    result = round((values3-a),2),
	    hftemp = hftemp,
	    timehotfill = timehotfill,
	    date=date.today().strftime("%B %d, %Y")),
	    
	pdf2 = pdfkit.from_string(html, False)


	st.download_button('Download PDF', data=pdf2, file_name="diploma.pdf", mime="application/octet-stream")

	#pdf.output('test.pdf','F')

