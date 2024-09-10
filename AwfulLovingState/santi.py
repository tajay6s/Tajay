import streamlit as st
import streamlit.components.v1 as components

# URL where your HTML file is hosted
url = "http://[::]:8000/"  # Change this to the actual URL

# Embedding the HTML page using an iframe
iframe_html = f"<iframe src='{url}' width='100%' height='500' frameborder='0'></iframe>"

components.html(iframe_html, width=400,  height=500)