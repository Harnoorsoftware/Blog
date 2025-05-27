import streamlit as st
import os

# Page configuration
st.set_page_config(page_title="Harnoor's Blog")

st.markdown("""
# Hi! I am Harnoor.
## Welcome to my *First Blog.*
### **The Last Passenger**
""")

# Blog Content Part 1
st.markdown("""
The train to Munich cut through the storm like a blade, the windows rattling with every gust.  
I wrapped my coat tighter, glancing around the nearly empty carriage.  
Only one other passenger sat at the far end—a man in a dark suit, briefcase in hand, eyes locked on me.

I wasn’t supposed to be on this train. My original had been canceled, and this one, they said, was a “special service.”  
No stops. No questions. Something about the way the conductor said it made my skin crawl.

The man stood. Slowly. Calmly. His gaze never left mine as he walked toward me, step by deliberate step.  
I stood too, instincts screaming.

**“You switched tickets,”** he said. His voice was smooth, almost bored.  
**“That seat wasn’t meant for you.”**

My throat went dry.  
**“What do you mean?”**

He opened his coat and flashed a badge. *Interpol*.
""")

# --- Robust image path handling ---
img_path = os.path.join(os.path.dirname(__file__), "img.png")
if os.path.exists(img_path):
    st.image(img_path, caption="The mysterious man in the suit", use_container_width=True)
else:
    st.warning("Image 'img.png' not found in the app directory.")

# Blog Content Part 2
st.markdown("""
**“There’s a kill order on the person meant to be sitting here,”** he said.  
**“You're in danger.”**

A chill shot down my spine.  
**“Why me?”**

He didn’t answer. He just scanned the carriage like he was expecting something. Or someone.

Then the intercom crackled: *“Next stop, midnight.”*

I frowned. **“Trains don’t stop at midnight.”**

When I turned back, the man was gone. Just… gone.

The windows showed only black. No trees. No lights. Nothing.

That’s when I heard the whisper behind me:  
**“You shouldn’t be here.”**

I turned slowly.

A woman stood there, wearing red.  
Her face—**my face**—was an exact mirror of mine.

**“I’m the real passenger,”** she said with a smile.  
**“And this train… this is where they erase mistakes.”**

The lights went out.

**Total darkness.** I couldn’t move. I couldn’t scream.

When the lights came back on, I was sitting again.

**Alone.**

The train still moving.

And in the window, **my reflection was smiling.**

But I wasn’t.
""")
