import pandas as pd

import pandas_profiling

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport

import pandas as pd
df = pd.read_csv("crops data.csv")
df.describe(include='all')

df = pd.read_csv("crops data.csv", na_values=['='])

from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile


profile = ProfileReport(df,

                        title="Agriculture Data",

        dataset={

        "description": "This profiling report was generated for Analytics Vidhya Blog",

        "copyright_holder": "Analytics Vidhya",

        "copyright_year": "2021",

        "url": "https://www.analyticsvidhya.com/blog/",

    },

    variables={

        "descriptions": {

            "State_Name": "Name of the state",

            "District_Name": "Name of district",

            "Crop_Year": "Year when it was seeded",

            "Season": "Crop year",

            "Crop": "Which crop was seeded?",

            "Area": "How much area was allocated to the crop?",

            "Production": "How much production?",




        }

    }

)




st.title("Pandas Profiling in Streamlit!")

st.write(df)

st_profile_report(profile)
