import json
import streamlit as st


def render_output_section():
    if "edited_metadata" not in st.session_state or "rdf_output" not in st.session_state:
        return

    edited_metadata = st.session_state["edited_metadata"]
    rdf_output = st.session_state["rdf_output"]

    st.markdown(
        '<div class="section-title">4. Final Output</div>',
        unsafe_allow_html=True
    )

    tab_json, tab_rdf = st.tabs(["JSON", "RDF / Turtle"])

    with tab_json:
        json_output = json.dumps(edited_metadata, indent=4)

        st.code(json_output, language="json")

        st.download_button(
            "Download JSON",
            data=json_output,
            file_name="dcat_metadata.json",
            mime="application/json"
        )

    with tab_rdf:
        st.code(rdf_output, language="turtle")

        st.download_button(
            "Download RDF / Turtle",
            data=rdf_output,
            file_name="dcat_metadata.ttl",
            mime="text/turtle"
        )