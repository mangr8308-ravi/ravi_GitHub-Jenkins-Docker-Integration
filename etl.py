import pandas as pd
import streamlit as st

st.write('Welcome to AVD')

data = {
    "Name": ["Suresh", "Uma", "Ravi", "Shashi", "Akansha"],
    "Status": ["Father", "Mother", "Self","Brother","Sister"],
    "Income":[90000,70000,50000,40000,20000]
}

df = pd.DataFrame(data)
st.write("ETL Processing Status : ", df)
