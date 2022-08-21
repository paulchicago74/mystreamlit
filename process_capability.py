### PROCESS CAPABILITY ANALYSIS ###

# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

st.set_option('deprecation.showPyplotGlobalUse', False)

# Set specification limits
target = st.sidebar.number_input('Insert a number', key=None)
LSL = st.sidebar.number_input('Insert a number', key=1)
USL = st.sidebar.number_input('Insert a number', key=2)

# Generate normally distributed data points
data = np.random.normal(loc=target,scale=1,size=100)

# Generate probability density function 
x = np.linspace(min(data), max(data), 1000)
y = norm.pdf(x, loc=5, scale=1)

# Plot histogram for data along with probability density functions and specification limits
plt.figure(figsize=(15,10))
plt.hist(data, color="lightgrey", edgecolor="black", density=True)
sns.kdeplot(data, color="blue", label="Density ST")
plt.plot(x, y, linestyle="--", color="black", label="Theorethical Density ST")
plt.axvline(LSL, linestyle="--", color="red", label="LSL")
plt.axvline(USL, linestyle="--", color="orange", label="USL")
plt.axvline(target, linestyle="--", color="green", label="Target")
plt.title('Process Capability Analysis')
plt.xlabel("Measure")
plt.ylabel("")
plt.yticks([])
plt.legend()
plt.show()

st.pyplot()

# Calculate Cp
Cp = (USL-LSL)/(6*np.std(data))
st.write (Cp)
# Calculate Cpk
Cpk = min((USL-data.mean())/(3*data.std()), (data.mean()-LSL)/(3*data.std()))

# Calculate z-value
z = min((USL-data.mean())/(data.std()), (data.mean()-LSL)/(data.std()))

# Get data summary statistics
num_samples = len(data)
sample_mean = data.mean()
sample_std = data.std()
sample_max = data.max()
sample_min = data.min()
sample_median = np.median(data)

# Get percentage of data points outside of specification limits
pct_below_LSL = len(data[data < LSL])/len(data)*100
pct_above_USL = len(data[data > USL])/len(data)*100

# Write .txt file with results

st.write ('PROCESS CAPABILITY ANALYSIS')
    
st.write("-----------------------------------\n")
st.write(f"Specifications\n")
st.write(f"\nTaget: {target}\n")
st.write(f"LSL: {LSL}\n")
st.write(f"USL: {USL}\n")    
    
st.write("-----------------------------------\n")
st.write(f"Indices\n")
st.write(f"\nCp: {round(Cp,2)}\n")
st.write(f"Cpk: {round(Cpk,2)}\n")
st.write(f"z: {round(z,2)}\n")
    
st.write("-----------------------------------\n")
st.write(f"Summary Statistics\n")
st.write(f"\nNumber of samples: {round(num_samples,2)}\n")
st.write(f"Sample mean: {round(sample_mean,2)}\n")
st.write(f"Sample std: {round(sample_std,2)}\n")
st.write(f"Sample max: {round(sample_max,2)}\n")
st.write(f"Sample min: {round(sample_min,2)}\n")
st.write(f"Sample median: {round(sample_median,2)}\n")
    
st.write(f"Percentage of data points below LSL: {round(pct_below_LSL,2)}%\n")
st.write(f"Percentage of data points above USL: {round(pct_above_USL,2)}%\n")
