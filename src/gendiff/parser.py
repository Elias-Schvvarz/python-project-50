import json
import os

import yaml


def parse_data(file_path):
    _, ext = os.path.splitext(file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if ext in ('.json', '.JSON'):
        return json.loads(content)
    elif ext in ['.yml', '.yaml']:
        return yaml.safe_load(content)

    raise ValueError(f"Unsupported file format: {ext}")