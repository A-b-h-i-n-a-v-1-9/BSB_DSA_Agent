import os
import json

DATA_FILE = os.path.join("data", "user_progress.json")

def init_storage():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        default_data = {"solved": [], "failed": [], "streak": 0, "weak_topics": []}
        save_data(default_data)

def load_data():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return {"solved": [], "failed": [], "streak": 0, "weak_topics": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
