import streamlit as st

from services.rdf_exporter import generate_rdf


def render_review_section(analysis_result):
    if "metadata" not in st.session_state:
        return

    metadata = st.session_state["metadata"]

    st.markdown(
        '<div class="section-title">3. Review and Edit Metadata</div>',
        unsafe_allow_html=True
    )

    with st.form("edit_metadata_form"):
        edited_title = st.text_input("Title", value=metadata.get("title", ""))

        edited_description = st.text_area(
            "Description",
            value=metadata.get("description", ""),
            height=120
        )

        edited_keywords = st.text_input(
            "Keywords (comma separated)",
            value=", ".join(metadata.get("keywords", []))
        )

        edited_format = st.text_input(
            "Format",
            value=metadata.get("format", analysis_result["detected_format"])
        )

        edited_media_type = st.text_input(
            "Media Type",
            value=metadata.get("mediaType", analysis_result["detected_media_type"])
        )

        edited_theme = st.text_input(
            "Theme",
            value=metadata.get("theme", "")
        )

        edited_creator = st.text_input(
            "Creator URI",
            value=metadata.get("creator", {}).get("@id", "")
        )

        edited_license = st.text_input(
            "License URI",
            value=metadata.get("license", {}).get("@id", "")
        )

        edited_issued = st.text_input(
            "Issued Date",
            value=metadata.get("issued", "")
        )

        edited_modified = st.text_input(
            "Modified Date",
            value=metadata.get("modified", "")
        )

        edited_language = st.text_input(
            "Language",
            value=metadata.get("language", "")
        )

        edited_spatial = st.text_input(
            "Spatial Coverage",
            value=metadata.get("spatial", "")
        )

        edited_temporal = st.text_input(
            "Temporal Coverage",
            value=metadata.get("temporal", "")
        )

        edited_frequency = st.text_input(
            "Accrual Periodicity",
            value=metadata.get("accrualPeriodicity", "")
        )

        confirm_metadata = st.form_submit_button("Confirm Metadata")

    if confirm_metadata:
        edited_metadata = {
            "title": edited_title,
            "description": edited_description,
            "keywords": [k.strip() for k in edited_keywords.split(",") if k.strip()],
            "format": edited_format,
            "mediaType": edited_media_type,
            "theme": edited_theme,
            "creator": {"@id": edited_creator},
            "license": {"@id": edited_license},
            "issued": edited_issued,
            "modified": edited_modified,
            "language": edited_language,
            "spatial": edited_spatial,
            "temporal": edited_temporal,
            "accrualPeriodicity": edited_frequency
        }

        st.session_state["edited_metadata"] = edited_metadata
        st.session_state["rdf_output"] = generate_rdf(edited_metadata)