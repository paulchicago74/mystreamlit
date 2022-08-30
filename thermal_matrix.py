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
st.sidebar.title('Thermal Matrix Calculation')


def check_password():e
	"""Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.sidebar.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
   

        text =  str(Image.open('figure2.jpg'))
        image = 'shot.png'
        #pdf = PDF(orientation='P', unit='mm', format='A4')

        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")

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
        #st.write('Values:', ph)

        values2 = st.sidebar.slider(
             'Select the temperaeture in celsius',
             0, 200)
        #st.write('Values:', values2)

        values3 = st.sidebar.slider(
             'Select the time in minutes',
             0, 240)
        #st.write('Values:', values3)
        col1, col2 = st.columns(2)

        with col1:
            title = st.text_input('Project')
            
        with col2:
            d = str(st.date_input(
            "Date"))
       
        number = st.sidebar.number_input('Fahrenheit to Celsius conversion')
        celsius = (number-32)*5/9
        if number > 0: st.sidebar.write('Temp in C:')
        if number > 0: st.sidebar.subheader(celsius)
        round (celsius, 2)
	
		J = 8.5 * (10**((60 - values2)/4.9))
		R = 10 * (10**((90 - values2)/9))
		#IF = 1	  * (10**((72 - hftemp)/7.5))
		ph1 = 0.1 * (10**((93.3 - values2)/8.9))
		ph2 = 1 * (10**((93.3 - values2)/8.9))
		ph3 = 2.5 * (10**((93.3 - values2)/8.9))
		ph4 = 5 * (10**((93.3 - values2)/8.9))
		ph5 = 10 * (10**((93.3 - values2)/8.9))
		ph6 = 20 * (10**((93.3 - values2)/8.9))
		Cs1 = 10 * (10**((90 - values2)/10))
		Cs2 = 37 * (10**((86 - values2)/7))

			#ph8 = 2.5 * (10**((74.44 - hftemp)/9.5))

		round(ph1, 2)

	if product == 'Acid or acidified' and ph < 3.9 : (st.metric(label = "Treatment Time", value=round(ph1, 2), delta=round((values3-ph1),2)))
	if product == 'Acid or acidified' and 3.9 <= ph < 4.1 : (st.metric(label = "Treatment Time", value=round(ph2, 2), delta=round((values3-ph2),2)))
	if product == 'Acid or acidified' and 4.1 <= ph < 4.2 : (st.metric(label = "Treatment Time", value=round(ph3, 2), delta=round((values3-ph3),2)))
	if product == 'Acid or acidified' and 4.2 <= ph < 4.3 : (st.metric(label = "Treatment Time", value=round(ph4, 2), delta=round((values3-ph4),2)))
	if product == 'Acid or acidified' and 4.3 <= ph < 4.4 : (st.metric(label = "Treatment Time", value=round(ph5, 2), delta=round((values3-ph5),2)))
	if product == 'Acid or acidified' and 4.4 <= ph <= 4.6 : (st.metric(label = "Treatment Time", value=round(ph6, 2), delta=round((values3-ph6),2)))

     
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
		st.header('Values Selected for Hot Fill')

		col1, col2, col3 = st.columns(3)

		with col1:
			st.header("pH")
			st.write('Values:', round(phhotfill, 2))

		with col2:
			st.header("Temperature")
			st.write('Temperature:', round(hftemp, 2), "C")

		with col3:
			st.header("Time")
			st.write('Values:', round(timehotfill,2))

	if hotfill == 'Yes' and product == 'Intermediate foods':	
		st.header('Values Selected for Hot Fill')

		col1, col2 = st.columns(2)

		with col1:
			st.header("Temperature")
			st.write('Temperature:', round(hftemp, 2), "C")

		with col2:
			st.header("Time")
			st.write('Values:', round(timehotfill,2))		


	if hotfill == 'Yes':
		IF = 1 * (10**((72 - hftemp)/7.5))
		if product == 'Acid or acidified' and phhotfill <= 4.1 : (st.metric(label = "Treatment Time", value=round(ph7, 2), delta=round((timehotfill-ph7),2)))
		if product == 'Acid or acidified' and 4.11 <= phhotfill < 4.61 : (st.metric(label = "Treatment Time", value=round(ph78, 2), delta=round((timehotfill-ph8),2)))
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
		    values3=f"{values3}/100",
		    J = J,
		    date=date.today().strftime("%B %d, %Y"))
		pdf2 = pdfkit.from_string(html, False)
                                
            
		st.download_button('Download PDF', data=pdf2, file_name="diploma.pdf", mime="application/octet-stream")

		#pdf.output('test.pdf','F')

