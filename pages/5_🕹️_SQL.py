import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
import os

st.set_page_config(
    page_title="I see all",
    page_icon="👁️"
)

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

prompt = st.text_area("Input your prompt")

file = st.file_uploader("Input the image")

if file and prompt:
    
        try:
            img = PIL.Image.open(file)
    
            response = model.generate_content([prompt,img])
    
            st.code(response.text)
        except:
            print(NameError)
else:
    st.text("please give input and prompt")