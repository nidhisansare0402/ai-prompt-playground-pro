import json
# Locate files reliably
from pathlib import Path

class HistoryService:
    # HistoryService learns where history.json is located and provides methods to read and write to it.
    # I don't want to hardcode the path to history.json because it may change in the future, and I want to be able to run this code from any directory.
    def __init__(self):
        project_root = Path(__file__).parent.parent
        self.history_file = project_root / "data" / "history.json"

    def load_history(self):
        # Load history from the JSON file
        try:
            with self.history_file.open("r",encoding="utf-8") as file:
                history = json.load(file)
            return history

        except FileNotFoundError:
            print("History file not found.")
            return []

        except json.JSONDecodeError:
            print("History file is corrupted.")
            return []
    
    def save_history(self, record):
        # Load history from json file append new record and overwrite the file back to json file
        history = self.load_history()
        history.append(record)

        with self.history_file.open("w", encoding= "utf-8") as file:
            json.dump(history, file, indent= 4, ensure_ascii=False)