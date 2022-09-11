import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import io
import numpy as np


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
# Load the data
@st.experimental_memo
def load_data():
    return pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

# Create and cache a Plotly figure
@st.experimental_memo
def create_figure(df):
    fig = st.line_chart(chart_data)
    return fig

df = load_data()
fig = create_figure(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

#st.line_chart(chart_data)
#fig = create_figure(chart_data)


# Create an in-memory buffer
buffer = io.BytesIO()

# Save the figure as a pdf to the buffer
#fig.write_image(file=buffer, format="pdf")
fig.write_image(file=buffer, format="png")

# Download the pdf from the buffer
st.download_button(
    label="Download PDF",
    data=buffer,
    file_name="figure.png",
    mime="application/png",
)

#st.plotly_chart(fig)
