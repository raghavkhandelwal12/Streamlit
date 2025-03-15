import streamlit as st
import pandas as pd
import numpy as np

st.title("Data and charts in streamlit")

# Generate a random DataFrame
df=pd.DataFrame(np.random.randn(10,3), columns=['A','B','C'])

#display DataFrame

st.write("### Data Table")
st.dataframe(df)

#line chart
st.write(" ### Line Chart")
st.line_chart(df)