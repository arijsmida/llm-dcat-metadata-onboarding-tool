import streamlit as st


def render_input_section():
    st.markdown(
        '<div class="section-title">1. Input Dataset</div>',
        unsafe_allow_html=True
    )

    reset_counter = st.session_state["reset_counter"]

    dataset_description = st.text_area(
        "Describe your dataset in natural language :",
        height=160,
        placeholder="Describe your dataset here...",
        key=f"dataset_description_{reset_counter}"
    )

    uploaded_file = st.file_uploader(
        "Upload dataset file",
        type=["csv", "json", "xlsx"],
        key=f"dataset_file_{reset_counter}"
    )

    return dataset_description, uploaded_file