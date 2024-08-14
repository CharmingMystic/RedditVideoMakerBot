import streamlit as st

from utils.settings import check_toml, set_var, set_var2


settings = check_toml("utils/.config.template.toml", "config.toml")

st.set_page_config(page_title="Settings", page_icon="🤖", layout="wide")

st.title("Settings")

st.write("### General")

def update_value(cat, var):
    value = st.session_state[var]

    set_var(cat, var, value)

def update_value_two_cats(cat, cat2, var):
    value = st.session_state[var]

    set_var2(cat, cat2, var, value)

st.slider("Times to run", 1, 100, settings["settings"]["times_to_run"], on_change=update_value, args=("settings","times_to_run",), key="times_to_run")

st.toggle("Use Capcut", settings["settings"]["use_capcut"], key="use_capcut", on_change=update_value, args=("settings","use_capcut",))
st.toggle("Mememode", settings["settings"]["mememode"], key="mememode", on_change=update_value, args=("settings","mememode",))
st.toggle("Storymode", settings["settings"]["storymode"], key="storymode", on_change=update_value, args=("settings","storymode",))

st.selectbox("Storymode method", [0, 1], index=settings["settings"]["storymodemethod"], on_change=update_value, args=("settings","storymodemethod",), key="storymodemethod")

st.slider("Storymode max length", 1, 20000, settings["settings"]["storymode_max_length"], step=100, on_change=update_value, args=("settings","storymode_max_length",), key="storymode_max_length")

res = [720, 1080, 1440, 1920, 2560, 3840, 4320, 7680]
st.select_slider("Width", res, settings["settings"]["resolution_w"], on_change=update_value, args=("settings","resolution_w",), key="resolution_w")
st.select_slider("Height", res, settings["settings"]["resolution_h"], on_change=update_value, args=("settings","resolution_h",), key="resolution_h")

st.slider("Zoom", 0.0, 2.0, settings["settings"]["zoom"], on_change=update_value, args=("settings","zoom",), key="zoom")
st.text_input("Channel name", settings["settings"]["channel_name"], on_change=update_value, args=("settings","channel_name",), key="channel_name")

st.write("### Background")
st.text_input(
    "Background video",
    settings["settings"]["background"]["background_video"],
    on_change=update_value_two_cats,
    args=("settings","background","background_video"),
    key="background_video")
st.text_input(
    "Background audio",
    settings["settings"]["background"]["background_audio"],
    on_change=update_value_two_cats,
    args=("settings","background","background_audio"),
    key="background_audio"
)

st.write("### Text-to-speech")

st.text_input(
    "Voice choice",
    settings["settings"]["tts"]["voice_choice"],
    on_change=update_value_two_cats,
    args=("settings","tts","voice_choice"),
    key="voice_choice"
)
st.toggle(
    "Random voice",
    settings["settings"]["tts"]["random_voice"],
    on_change=update_value_two_cats,
    args=("settings","tts","random_voice"),
    key="random_voice"
)
st.text_input(
    "Streamlabs polly voice",
    settings["settings"]["tts"]["streamlabs_polly_voice"],
    on_change=update_value_two_cats,
    args=("settings","tts","streamlabs_polly_voice"),
    key="streamlabs_polly_voice"
)

st.write("### Reddit")
st.text_input(
    "Subreddit",
    settings["reddit"]["thread"]["subreddit"],
    on_change=update_value_two_cats,
    args=("reddit","thread","subreddit"),
    key="subreddit"
)
st.text_input(
    "Post Id (optional)",
    settings["reddit"]["thread"]["post_id"],
    on_change=update_value_two_cats,
    args=("reddit","thread","post_id"),
    key="post_id"
)
st.slider(
    "Max comment length",
    10, 10000,
    settings["reddit"]["thread"]["max_comment_length"],
    on_change=update_value_two_cats,
    args=("reddit","thread","max_comment_length"),
    key="max_comment_length"
)
st.slider(
    "Min comment length",
    0, 10000,
    settings["reddit"]["thread"]["min_comment_length"],
    on_change=update_value_two_cats,
    args=("reddit","thread","min_comment_length"),
    key="min_comment_length"
)



with st.sidebar:
    st.page_link("GUI.py", label="Home")
    st.page_link("pages/settings.py", label="Settings")
