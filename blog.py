import streamlit as st

# Set the page title
st.set_page_config(page_title="My Image App")

# Show the image (make sure img.png is in the same folder)
st.image("img.png", caption="My Image", use_column_width=True)

# Optional text
st.markdown("### Welcome to my simple Streamlit app!")
