import json
import requests

from config.settings import (
    OLLAMA_URL,
    OLLAMA_MODEL,
    OLLAMA_TIMEOUT
)


def generate_metadata_with_llm(dataset_description, file_context):
    prompt = f"""
You are a DCAT-compatible metadata generator.

Your task is to generate metadata ABOUT the dataset.
You must not simply rewrite or summarize the user description.

Available evidence:
1. User description
2. Uploaded file name
3. File type
4. Media type
5. Column names
6. Data types
7. Missing values
8. Unique values
9. Statistics
10. Sample rows
11. Detected temporal coverage
12. Detected spatial columns

Return ONLY valid JSON.
Do not write explanations.
Do not use markdown.
Do not wrap the answer in ```json.

Use exactly this JSON structure:

{{
  "title": "",
  "description": "",
  "keywords": [],
  "format": "",
  "mediaType": "",
  "theme": "",
  "creator": {{
    "@id": ""
  }},
  "license": {{
    "@id": ""
  }},
  "issued": "",
  "modified": "",
  "language": "",
  "spatial": "",
  "temporal": "",
  "accrualPeriodicity": ""
}}

Rules:
- Generate metadata from dataset evidence.
- If a file is uploaded, prioritize file structure over the description.
- If description and file are both available, combine both sources.
- If the dataset profile and the description conflict, trust the dataset profile.
- Dataset structure, column names, and sample values are stronger evidence than user-written descriptions.
- Do NOT simply copy the description.
- Generate a catalog-quality dataset title.
- Titles should be specific, descriptive, and suitable for publication in a data catalog.
- Avoid generic titles such as "Dataset", "Measurements", or "Observations".
- The title should describe the dataset as it would appear in a public data catalog.
- Infer title from dataset content.
- Generate keywords that improve dataset discoverability.
- Include important variables, entities, measurements, and domain concepts.
- Prefer specific keywords over generic ones.
- Metadata should be derived from evidence, not copied from evidence.
- Synthesize information from multiple signals to produce catalog-ready metadata.
- Analyze the meaning of the dataset rather than individual keywords.
- Infer temporal coverage only when dates, timestamps, or explicit time periods are present.
- Infer spatial coverage only when geographic locations are present.
- Infer dataset purpose and potential use cases from the available evidence.
- Generate metadata that would help users discover and understand the dataset in a public data catalog.
- Prefer semantic understanding over keyword matching.
- Generate a metadata description, not a summary of the user's text.
- The description should explain what data is contained, what variables are present, and what the dataset can be used for.
- Infer theme from the dataset domain.
- Fill format and mediaType only from uploaded file information.
- If no file is uploaded, format and mediaType must be empty.
- Fill temporal only if explicit date/time evidence exists.
- Fill spatial only if explicit location evidence exists.
- Temporal coverage may be inferred from explicit dates, years, or time ranges present in the description.
- Spatial coverage may be inferred from explicit geographic locations present in the description.
- Do not leave temporal or spatial empty when explicit evidence exists.
- Prefer human-readable values for temporal and spatial coverage.
- Do not return Python lists or JSON objects as strings inside metadata fields.
- Do not infer temporal coverage or frequency from assumptions.
- Never use values such as Daily, Monthly, Yearly unless clearly stated in the evidence.
- Do NOT invent creator.
- Do NOT invent license.
- Do NOT invent issued date.
- Do NOT invent modified date.
- Do NOT invent accrualPeriodicity.
- If evidence is missing, use an empty string.
- keywords must be an array of strings.
- creator must be an object with @id.
- license must be an object with @id.
- Do not add extra fields.

Description Rules:
- Do not rewrite or paraphrase the user description sentence by sentence.
- Summarize variables into higher-level concepts when appropriate.
- Describe the dataset from a catalog perspective rather than repeating the source text.
- Mention potential analytical or research uses when supported by the evidence.
- Prefer abstraction and synthesis over repetition.

Good title examples:
- Weather Monitoring and Climate Observation Dataset
- Indoor Environmental Sensor Measurements Dataset
- Retail Sales Transactions Dataset
- Urban Traffic Flow Monitoring Dataset

User description:
{dataset_description}

Dataset profile:
{file_context}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=OLLAMA_TIMEOUT
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    result = response.json().get("response", "")
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    if not result:
        raise ValueError(
            f"The model returned an empty response. "
            f"Check that Ollama is running and {OLLAMA_MODEL} is installed."
        )

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        raise ValueError(
            f"The model did not return valid JSON.\n\nModel response:\n{result}"
        )