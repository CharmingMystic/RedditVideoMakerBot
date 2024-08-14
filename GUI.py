import streamlit as st

from utils import settings

st.set_page_config(page_title="RedditVideoMakerBot", page_icon="🤖", layout="wide")

st.title("RedditVideoMakerBot")
st.write("""
    Github: [Original](https://github.com/elebumm/RedditVideoMakerBot) | [Cyteon's Fork](https://github.com/cyteon/RedditVideoMakerBot) \n
    Documentation: https://reddit-video-maker-bot.netlify.app/
""")

with st.sidebar:
    st.page_link("GUI.py", label="Home")
    st.page_link("pages/settings.py", label="Settings")
    st.page_link("pages/examples.py", label="Examples")
    st.page_link("pages/voices.py", label="Voices")
