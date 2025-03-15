import streamlit as st #import the library
#title
st.title("User input Example")

#text input
name=st.text_input("enter your name")

#button
if st.button("Submit"):
    st.write("Hello",name,"Wecome to streamlit")