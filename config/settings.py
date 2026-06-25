PAGE_TITLE = "LLM-Assisted DCAT Tool"
PAGE_LAYOUT = "wide"

APP_TITLE = "LLM-Assisted DCAT Metadata Onboarding Tool"
APP_SUBTITLE = "Generate DCAT-compatible metadata from dataset files and descriptions"

LOGO_PATH = "assets/uni_logo.png"

SCHEMA_OPTIONS = [
    "DCAT (W3C Data Catalog Vocabulary)"
]

ALLOWED_FILE_TYPES = ["csv", "json", "xlsx"]

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"
OLLAMA_TIMEOUT = 300

PRIMARY_COLOR = "#84bd00"