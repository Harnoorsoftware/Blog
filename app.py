import streamlit as st

# Set page title
st.set_page_config(page_title="My HTML Page")

# Load the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display it in the Streamlit app
st.components.v1.html(html_content, height=600, scrolling=True)
