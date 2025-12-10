import json
import os

DATA_PATH = "data"

def load_decade_data(decade):
    file_path = os.path.join(DATA_PATH, f"{decade}.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Decade file not found: {file_path}")

    with open(file_path, "r") as f:
        return json.load(f)
