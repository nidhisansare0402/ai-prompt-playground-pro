import json
from pathlib import Path

class TemplateService:
    def __init__(self):
        project_root = Path(__file__).parent.parent
        self.template_file = project_root / "data" / "templates.json"

    def load_templates(self):
        try:
            with open(self.template_file, "r", encoding="utf-8") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_template(self, template):
        required_fields = ["name", "prompt"]

        for field in required_fields:
            if field not in template:
                raise ValueError(f"Missing required field: {field}")

        templates = self.load_templates()

        next_id = (
            max((t["id"] for t in templates), default=0) + 1
        )

        template_record = {
            "id": next_id,
            "name": template["name"],
            "prompt": template["prompt"]
        }

        templates.append(template_record)

        with open(self.template_file, "w", encoding="utf-8") as file:
            json.dump(
                templates,
                file,
                indent=4,
                ensure_ascii=False
            )

    def list_templates(self):
        return self.load_templates()
    
    # search template
    def get_template(self, template_id):
        templates = self.load_templates()

        for template in templates:
            if template["id"] == template_id:
                return template

        return None
    
    def delete_template(self, template_id):
        templates = self.load_templates()

        updated_templates = []
        for template in templates:
            if template["id"] != template_id:
                updated_templates.append(template)

        if len(updated_templates) == len(templates):
            return False

        with open(self.template_file, "w", encoding="utf-8") as file:
            json.dump(
                updated_templates,
                file,
                indent=4,
                ensure_ascii=False
            )