import streamlit as st

from components.layout import render_layout
from components.input_section import render_input_section
from components.analysis_section import render_analysis_section
from components.generation_section import render_generation_section
from components.review_section import render_review_section
from components.output_section import render_output_section


st.set_page_config(
    page_title="LLM-Assisted DCAT Tool",
    layout="wide"
)


if "reset_counter" not in st.session_state:
    st.session_state["reset_counter"] = 0


render_layout()

dataset_description, uploaded_file = render_input_section()

analysis_result = render_analysis_section(uploaded_file)

render_generation_section(
    dataset_description=dataset_description,
    uploaded_file=uploaded_file,
    analysis_result=analysis_result
)

render_review_section(analysis_result)

render_output_section()