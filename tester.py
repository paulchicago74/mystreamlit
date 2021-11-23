# import the streamlit library


import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# give a title to our app

D= 150
Time = 50
Tref = 120
Zref = 10
Temp = 100
F = (10 ** ((Temp - Tref)/Zref))/1 * Time

T2 = Time / 10

# Create the pandas DataFrame
data = [[0, 0, 0]]
df = pd.DataFrame(data, columns = ['Time', 'Fvalue', 'Dvalue'])
my_table = st.table(df)
# df2 = ('Time' df + T2, df + 2, df + 3)
df2 = ({'Time': [df + T2, 3, 4],
                   'Fvalue': [360, 180, 360]},
my_table.add_rows(df2)
# print dataframe.
df


df1 = pd.DataFrame(
np(50, 20),
columns=('col %d' % i for i in range(20)))

my_table = st.table(df1)

df2 = pd.DataFrame(
np.random.randn(50, 20),
columns=('col %d' % i for i in range(20)))

my_table.add_rows(df2)
