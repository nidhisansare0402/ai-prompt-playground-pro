import json
# Locate files reliably
from pathlib import Path

class HistoryService:
    # HistoryService learns where history.json is located and provides methods to read and write to it.
    # I don't want to hardcode the path to history.json because it may change in the future, and I want to be able to run this code from any directory.
    def __init__(self):
        project_root = Path(__file__).parent.parent
        self.history_file = project_root / "data" / "history.json"