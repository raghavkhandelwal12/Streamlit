import streamlit as st
st.title("Image and Video Example")

#display image
st.image("Example.jpg",caption="Example Image",use_column_width=True)

# Display Video
st.video("example.mp4")