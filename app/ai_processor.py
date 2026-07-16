import json
from app.prompt_builder import build_prompt
from app.response_parser import parse_response
from services.gemini_service import generate_response
from services.history_service import HistoryService
from config.settings import MODEL_NAME

history_service = HistoryService()

def process_prompt(
    user_prompt,
    response_format
):

    final_prompt = build_prompt(
        user_prompt,
        response_format
    )

    raw_response = generate_response(
        final_prompt
    )

    parsed_response = parse_response(
        raw_response,
        response_format
    )

    record = {
        "user_prompt": user_prompt,
        "enhanced_prompt": final_prompt,
        "output_format": response_format,
        "model": MODEL_NAME,
        "response": parsed_response
    }

    history_service.save_history(
        record
    )
    return parsed_response

