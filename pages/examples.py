import streamlit as st

from utils.settings import check_toml, set_var, set_var2


settings = check_toml("utils/.config.template.toml", "config.toml")

st.set_page_config(page_title="Examples", page_icon="🤖", layout="wide")

st.title("Examples")

st.write("Using capcut, storymode, preset 18")
st.video("https://youtube.com/embed/eKYUeiDmZ88?si=GmddrcWM2KmG2_wL")


with st.sidebar:
    st.page_link("GUI.py", label="Home")
    st.page_link("pages/settings.py", label="Settings")
    st.page_link("pages/examples.py", label="Examples")
    st.page_link("pages/voices.py", label="Voices")
