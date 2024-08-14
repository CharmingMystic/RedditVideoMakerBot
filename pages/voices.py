import streamlit as st

from utils.settings import check_toml, set_var, set_var2


settings = check_toml("utils/.config.template.toml", "config.toml")

st.set_page_config(page_title="Voices", page_icon="🤖", layout="wide")

st.title("Voices")

st.write("todo")


with st.sidebar:
    st.page_link("GUI.py", label="Home")
    st.page_link("pages/settings.py", label="Settings")
    st.page_link("pages/examples.py", label="Examples")
    st.page_link("pages/voices.py", label="Voices")
