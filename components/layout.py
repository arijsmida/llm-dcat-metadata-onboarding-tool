import streamlit as st

from utils.image_utils import image_to_base64
from styles.css import CSS


def render_layout():
    logo_base64 = image_to_base64("assets/uni_logo.png")

    st.markdown(CSS, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="fixed-sidebar">
        <div class="sidebar-logo">
            <img src="data:image/png;base64,{logo_base64}">
        </div>
    </div>

    <div class="topbar">
        <div class="topbar-title">LLM-Assisted DCAT Metadata Onboarding Tool</div>
        <div class="topbar-subtitle">
            Generate DCAT-compatible metadata from dataset files and descriptions
        </div>
    </div>
    """, unsafe_allow_html=True)