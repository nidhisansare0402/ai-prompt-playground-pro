import json
# Locate files reliably
from pathlib import Path
from datetime import datetime

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
        # Save a new history record.
        # Validate required fields
        required_fields = [
            "user_prompt",
            "enhanced_prompt",
            "output_format",
            "model",
            "response"
        ]

        for field in required_fields:
            if field not in record:
                raise ValueError(f"Missing required field: {field}")
            
        # Load existing history
        history = self.load_history()

        # Generate next ID
        if history:
            next_id = len(history) + 1
        else:
            next_id = 1
        
        # Create a new history record
        history_record = {
            "id": next_id,
            "timestamp": datetime.now().isoformat(),
            "user_prompt": record["user_prompt"],
            "enhanced_prompt": record["enhanced_prompt"],
            "output_format": record["output_format"],
            "model": record["model"],
            "response": record["response"]
    }
        # Add the new record
        history.append(history_record)

        # Save the updated history
        with self.history_file.open("w", encoding= "utf-8") as file:
            json.dump(history, file, indent= 4, ensure_ascii=False)