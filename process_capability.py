### PROCESS CAPABILITY ANALYSIS ###

# Import required libraries
import streamlit as st
import numpy as np
import statsmodels.api as sm

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])
x = sm.add_constant(x)

#model = sm.Logit(y, x)
model = sm.Logit(-44.22, 34)

result = model.fit(method='newton')

result.params

#st.write(result.predict(x))

#st.write(result.summary())
