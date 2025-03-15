import streamlit as st
st.title("Widgets example")

#checkbox
if st.checkbox("Show message"):
    st.write("Hello, welcome to stremlit")
    
#radion button

choice=st.radio("Select an option:",["A","B","C"])
st.write(f"you selected {choice}")

# Select Box (Dropdown)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
st.write(f"Selected Gender: {gender}")