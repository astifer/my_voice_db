import streamlit as st
import io

import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder


backend = "http://fastapi:8000/upload"

def process(j, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", j, "application/json")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r


input_json = st.file_uploader("insert image") 

if st.button("Get map"):

    if input_json:
        embs = process(input_json, backend)

        
    else:
        # handle case with no image
        st.write("Insert a file!")