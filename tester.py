# import the streamlit library
[theme]
base = "dark"

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
# =(Time+(10^((Temp-Tref)/Zref)+(10^((Tref-Tref)/Zref)))/2*(Time)) 
# give a title to our app
df1 = pd.DataFrame(
...    np.random.randn(50, 20),
...    columns=('col %d' % i for i in range(20)))
...
>>> my_table = st.table(df1)
>>>
>>> df2 = pd.DataFrame(
...    np.random.randn(50, 20),
...    columns=('col %d' % i for i in range(20)))
...
>>> my_table.add_rows(df2)
