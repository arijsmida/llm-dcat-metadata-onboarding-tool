import streamlit as st

from services.dataset_analyzer import analyze_dataset


def render_analysis_section(uploaded_file):
    file_context = ""
    detected_format = ""
    detected_media_type = ""
    temporal_coverage = ""
    spatial_columns = []

    if uploaded_file is not None:
        try:
            (
                df,
                dataset_profile,
                file_context,
                detected_format,
                detected_media_type,
                temporal_coverage,
                spatial_columns
            ) = analyze_dataset(uploaded_file)

            st.markdown(
                '<div class="section-title">Dataset Analysis</div>',
                unsafe_allow_html=True
            )

            summary_data = {
                "Dataset Property": [
                    "Rows",
                    "Columns",
                    "Temporal Coverage",
                    "Spatial Information"
                ],
                "Value": [
                    len(df),
                    len(df.columns),
                    temporal_coverage if temporal_coverage else "Not detected",
                    ", ".join(spatial_columns) if spatial_columns else "Not detected"
                ]
            }

            st.table(summary_data)

            st.write("Dataset Preview:")
            st.dataframe(df.head())

        except Exception as e:
            st.error(f"Could not read uploaded file: {e}")
            file_context = ""

    return {
        "file_context": file_context,
        "detected_format": detected_format,
        "detected_media_type": detected_media_type,
        "temporal_coverage": temporal_coverage,
        "spatial_columns": spatial_columns
    }