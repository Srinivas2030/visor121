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


def main():
    # Title and header
    st.set_page_config(page_title="VGS - Your Personalized AI Assistant", layout="wide")
    st.title("VGS: Make the Task Easier with AI")
    st.header("Your AI-Powered Assistant")  # Added a subheader for clarity

    # Text summarization section (expandable)
    with st.expander("Summarize Your Text"):
        text_area = st.text_area("Enter your text to summarize:")
        if st.button("Summarize"):
            summary = get_response(text_area)
            if summary:
                st.success("Here's your summary:")
                st.write(summary)
            else:
                st.error("Error summarizing text. Please try again.")

    # Image generation section (expandable)
    with st.expander("Generate Artwork"):
        prompt_text = st.text_area("Enter your text prompt:")
        art_style = st.selectbox("Choose an Image Style", [
            "Abstract", "Cute", "Fantasy", "Futuristic", "Realistic",
            "Science Fiction", "Surreal", "Techno"
        ])
        if st.button("Generate"):
            artwork_image = generate_image(prompt_text, art_style)
            if artwork_image:
                st.image(artwork_image, width=400)
            else:
                st.error("Error generating image. Please try again.")

    # Text-to-speech section (expandable)
    with st.expander("Listen to Summary"):
        if summary:  # Only display if summary exists
            voice_select = st.selectbox("Select Voice", ["Joanna", "Matthew", "Emma"])
            speech_bytes = convert_text_to_speech(summary, voice_select)
            if speech_bytes:
                st.audio(speech_bytes, format="audio/mpeg")
            else:
                st.error("Error converting text to speech")

if __name__ == "__main__":
    main()
