
import io
import streamlit as st
import time
import requests
from PIL import Image
from io import BytesIO
import boto3
import json
import base64
import io
from gtts import gTTS
import autoplay

from txt_image import generate_image
from txt_speech import convert_text_to_speech
from txt_summarizer import get_response


# this part is for text summarizer
st.set_page_config(page_title="Personalized Artwork Creator", layout="wide")
st.header("VGS  Make the Task easier")

text = st.text_area("Write text to summarize")
sett=get_response(text)
if st.button("Summarize It"):
   st.write(sett)



# this part is for image generatoin it also take gets prompt in beign only like prompt for tet summarixation and image genratio both are same
st.title("Genrated Image")
prompt_column, result_column = st.columns(2)
st.subheader("Customize your artwork")
prompt_text = text
art_style = st.selectbox("Choose a Image style you want", ["Abstract", "Cute", "Fantasy", "Futuristic", "Realistic", "Science Fiction", "Surreal", "Techno"])
st.subheader("Your Generated Image will take little bit time please have some patience")
artwork_image = generate_image(text, art_style)
st.image(artwork_image, width=400)    





# we are doing join the lsit of words the its easy to convert text to audio

summarized_text=sett
text_list = list(summarized_text)  # Convert the generator to a list
summarized_text = " ".join(text_list)  # Join elements with spaces
voice_select = st.selectbox("Select Voice", ["Joanna", "Matthew", "Emma"])




#here this is last work that calling functin for converting text to audio
speech_bytes = convert_text_to_speech(summarized_text, voice_select)
if speech_bytes:

    st.audio(speech_bytes, format="audio/mpeg")
else:
     
    st.error("Error converting text to speech")