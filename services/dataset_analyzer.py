import json
import pandas as pd

def detect_temporal_coverage(df):
    for col in df.columns:
        if any(w in col.lower() for w in ["date", "time", "timestamp", "year"]):
            dates = pd.to_datetime(df[col], errors="coerce")
            if dates.notna().sum() > 0:
                return f"{dates.min().date()} to {dates.max().date()}"
    return ""

def detect_spatial_columns(df):
    keywords = ["city", "country", "location", "region", "address", "latitude", "longitude", "lat", "lon", "room"]
    return [col for col in df.columns if any(w in col.lower() for w in keywords)]

def analyze_dataset(uploaded_file):
    file_name = uploaded_file.name
    file_extension = file_name.split(".")[-1].lower()

    if file_extension == "csv":
        detected_format = "CSV"
        detected_media_type = "text/csv"
        df = pd.read_csv(uploaded_file)

    elif file_extension == "xlsx":
        detected_format = "XLSX"
        detected_media_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        df = pd.read_excel(uploaded_file)

    elif file_extension == "json":
        detected_format = "JSON"
        detected_media_type = "application/json"
        df = pd.read_json(uploaded_file)

    else:
        raise ValueError("Unsupported file format")

    temporal_coverage = detect_temporal_coverage(df)
    spatial_columns = detect_spatial_columns(df)

    dataset_profile = {
        "file_name": file_name,
        "format": detected_format,
        "media_type": detected_media_type,
        "number_of_rows": len(df),
        "number_of_columns": len(df.columns),
        "columns": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "unique_values_per_column": df.nunique().to_dict(),
        "statistics": df.describe(include="all").fillna("").to_dict(),
        "detected_temporal_coverage": temporal_coverage,
        "detected_spatial_columns": spatial_columns,
        "sample_rows": df.head(5).to_dict(orient="records")
    }

    file_context = json.dumps(dataset_profile, indent=2, default=str)

    return df, dataset_profile, file_context, detected_format, detected_media_type, temporal_coverage, spatial_columns