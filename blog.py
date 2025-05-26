import streamlit as st

# Set the page title
st.set_page_config(page_title="Harnoor's Blog")

# Start of the blog
st.markdown("""
# Hi! I am Harnoor.
## Welcome to my *First Blog.*
### The Last Passenger

The train to Munich cut through the storm like a blade, the windows rattling with every gust. I wrapped my coat tighter, glancing around the nearly empty carriage.
""")

# Image in between
st.image("img.png", caption="The man in the dark suit", use_container_width=True)

# Continue the blog
st.markdown("""
Only one other passenger sat at the far end—a man in a dark suit, briefcase in hand, eyes locked on me.

I wasn’t supposed to be on this train. My original had been canceled, and this one, they said, was a “special service.” No stops. No questions. Something about the way the conductor said it made my skin crawl.

The man stood. Slowly. Calmly. His gaze never left mine as he walked toward me, step by deliberate step.

> “You switched tickets,” he said. His voice was smooth, almost bored. “That seat wasn’t meant for you.”

...

And in the window, **my reflection was smiling.**

But I wasn’t.
""")
