import streamlit as st #import the library 
import pandas as pd

st.title("File uploaded Example")

#file uploader
uploaded_file=st.file_uploader("Upload a csv file",type=["csv"])

if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.dataframe(data)