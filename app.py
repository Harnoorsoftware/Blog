import streamlit as st
import base64

# Set page title
st.set_page_config(page_title="My HTML Page")

# Read and encode the image as base64
with open("img.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Load the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace placeholder in HTML with base64 image
html_content = html_content.replace("{{IMAGE_DATA}}", base64_image)

# Display the HTML in Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)
