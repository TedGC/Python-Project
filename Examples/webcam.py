import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    #open the camera
    camera_image = st.camera_input('camera') 


if camera_image:
    #create a pilow image instance
    image = Image.open(camera_image)

    #convert the pilow image to grayscale
    gray_img = image.convert("L")

    #render the grayscale image on the webpage
    st.image(gray_img)