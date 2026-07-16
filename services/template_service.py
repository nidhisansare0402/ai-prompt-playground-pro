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

    def _save_templates(self, templates):
        """
        Save all templates to templates.json
        """
        with open(self.template_file, "w", encoding="utf-8") as file:
            json.dump(
                templates,
                file,
                indent=4,
                ensure_ascii=False
            )

    def list_templates(self):
        return self.load_templates()

    def save_template(self, template):
        """
        Save a new template.
        """
        required_fields = ["name", "prompt"]

        for field in required_fields:
            if field not in template:
                raise ValueError(f"Missing required field: {field}")

        templates = self.load_templates()

        # Duplicate name validation
        for existing in templates:
            if existing["name"].strip().lower() == template["name"].strip().lower():
                raise ValueError("A template with this name already exists.")

        next_id = max(
            (t["id"] for t in templates),
            default=0
        ) + 1

        template_record = {
            "id": next_id,
            "name": template["name"].strip(),
            "prompt": template["prompt"].strip()
        }

        templates.append(template_record)

        self._save_templates(templates)

    def get_template(self, template_id):
        """
        Get template by ID.
        """
        templates = self.load_templates()

        for template in templates:
            if template["id"] == template_id:
                return template
        return None

    def update_template(self, template_id, updated_prompt):
        """
        Update an existing template.
        """
        templates = self.load_templates()

        for template in templates:
            if template["id"] == template_id:
                template["prompt"] = updated_prompt.strip()
                self._save_templates(templates)
                return True

        return False

    def delete_template(self, template_id):
        """
        Delete template by ID.
        """
        templates = self.load_templates()

        updated_templates = [
            template
            for template in templates
            if template["id"] != template_id
        ]

        if len(updated_templates) == len(templates):
            return False

        self._save_templates(updated_templates)

        return True