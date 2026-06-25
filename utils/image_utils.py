import base64
from pathlib import Path

def image_to_base64(path):
    if Path(path).exists():
        return base64.b64encode(Path(path).read_bytes()).decode()
    return ""
