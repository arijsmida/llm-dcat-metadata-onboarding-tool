import streamlit as st

from services.llm_generator import generate_metadata_with_llm
from services.metadata_cleaner import clean_metadata


def render_generation_section(dataset_description, uploaded_file, analysis_result):
    st.markdown(
        '<div class="section-title">2. Select Schema & Generate</div>',
        unsafe_allow_html=True
    )

    st.selectbox(
        "Select Schema",
        ["DCAT (W3C Data Catalog Vocabulary)"]
    )

    col1, col2, _ = st.columns([2.2, 1.2, 6.6])

    with col1:
        generate = st.button(
            " Generate Metadata",
            key="generate_btn",
            use_container_width=True
        )

    with col2:
        clear = st.button(
            "↻ Clear",
            key="clear_btn",
            use_container_width=True
        )

    if clear:
        reset_counter = st.session_state["reset_counter"]
        st.session_state.clear()
        st.session_state["reset_counter"] = reset_counter + 1
        st.rerun()

    if generate:
        if not dataset_description.strip() and uploaded_file is None:
            st.warning("Please enter a dataset description or upload a file.")
        else:
            with st.spinner("Generating metadata..."):
                try:
                    metadata = generate_metadata_with_llm(
                        dataset_description=dataset_description,
                        file_context=analysis_result["file_context"]
                    )

                    metadata = clean_metadata(
                        metadata=metadata,
                        detected_format=analysis_result["detected_format"],
                        detected_media_type=analysis_result["detected_media_type"],
                        temporal_coverage=analysis_result["temporal_coverage"],
                        spatial_columns=analysis_result["spatial_columns"],
                        has_file=uploaded_file is not None
                    )

                    metadata["description"] = dataset_description.strip()

                    st.session_state["metadata"] = metadata

                except Exception as e:
                    st.error(f"Error while generating metadata: {e}")