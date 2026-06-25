def clean_metadata(metadata, detected_format, detected_media_type, temporal_coverage, spatial_columns, has_file):
    required = {
        "title": "",
        "description": "",
        "keywords": [],
        "format": "",
        "mediaType": "",
        "theme": "",
        "creator": {"@id": ""},
        "license": {"@id": ""},
        "issued": "",
        "modified": "",
        "language": "",
        "spatial": "",
        "temporal": "",
        "accrualPeriodicity": ""
    }

    if not isinstance(metadata, dict):
        metadata = {}

    for key, value in required.items():
        metadata.setdefault(key, value)

    if not isinstance(metadata.get("keywords"), list):
        metadata["keywords"] = []

    metadata["creator"] = {"@id": ""}
    metadata["license"] = {"@id": ""}
    metadata["issued"] = ""
    metadata["modified"] = ""

    if has_file:
        metadata["format"] = detected_format
        metadata["mediaType"] = detected_media_type
        if temporal_coverage:
            metadata["temporal"] = temporal_coverage
        if spatial_columns:
            metadata["spatial"] = ", ".join(spatial_columns)
    else:
        metadata["format"] = ""
        metadata["mediaType"] = ""
        metadata["temporal"] = metadata.get("temporal", "")
        metadata["spatial"] = metadata.get("spatial", "")

    return metadata

def calculate_metadata_score(metadata):
    fields = ["title", "description", "keywords", "format", "mediaType", "theme", "temporal", "spatial"]
    score = 0

    for field in fields:
        value = metadata.get(field)
        if field == "keywords":
            if isinstance(value, list) and len(value) > 0:
                score += 1
        elif value:
            score += 1

    return int((score / len(fields)) * 100)