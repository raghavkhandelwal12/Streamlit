import streamlit as st #import the streamlit library 

#title
st.title("Streamlit Widgets exampel")

#sliders
age=st.slider("Select your age",1,100,25)
st.write("Your age is",age)

#select box
gender=st.selectbox("Select your gender",["Male","Female","Others"])
st.write("You selected",gender)

#checkbox
if st.checkbox("Show secret message"):
    st.write("Hello, you found the secret message")