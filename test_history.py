from services.history_service import HistoryService

history_service = HistoryService()

record = {
    "user_prompt": "Explain Python Lists",
    "enhanced_prompt": "Explain Python Lists. Return only JSON.",
    "output_format": "json",
    "model": "gemini-2.5-pro",
    "response": {
        "title": "Python Lists",
        "difficulty": "Easy"
    }
}

history_service.save_history(record)

history = history_service.load_history()

print(history)