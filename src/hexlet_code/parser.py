import json
import os


def parse_data(file_path):
    _, ext = os.path.splitext(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if ext in ('.json', '.JSON'):
        return json.loads(content)

    raise ValueError(f"Unsupported file format: {ext}")