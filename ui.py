import streamlit as st
from youtube_analyzer import build_agent

st.set_page_config(
    page_title = "youtube analyzer",
    layout="centered"
)

st.title("🎥AI Youtube Video Analyzer")

#cache =. fast access, temp storage => most frequently items
@st.cache_resource 
def get_agent():
    return build_agent()

agent = get_agent()

#input box
video = st.text_input("enter youtube video link")
button = st.button("analyze")