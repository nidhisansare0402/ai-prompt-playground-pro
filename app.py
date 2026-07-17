import json
import streamlit as st
from app.ai_processor import process_prompt
from services.template_service import TemplateService
from services.history_service import HistoryService

# Initialize services
template_service = TemplateService()
history_service = HistoryService()

# Page Configuration
st.set_page_config(
    page_title="AI Prompt Playground Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Content
def render_generate():
    st.title("⚡AI Prompt Playground Pro")
    st.write("Create AI responses using your own prompt or a saved template.")
    st.divider()

    # Load Templates
    templates = template_service.list_templates()

    template_names = ["None"]
    template_map = {}

    for template in templates:

        template_names.append(template["name"])
        template_map[template["name"]] = template["prompt"]


    # Choose Template
    selected_template = st.selectbox(
        "Choose Template (Optional)",
        template_names
    )

    prompt = ""

    if selected_template != "None":
        prompt = template_map[selected_template]

    # Prompt
    user_prompt = st.text_area(
        "Prompt",
        value=prompt,
        height=180,
        placeholder="Enter your prompt..."
    )

    # Response Format
    response_format = st.selectbox(
        "Response Format",
        [
            "text",
            "markdown",
            "json"
        ]
    )

    # Generate
    if st.button(
        "Generate Response"
    ):

        if not user_prompt.strip():
            st.warning("Please enter a prompt.")
            return

        try:
            with st.spinner("Generating response..."):

                response = process_prompt(
                    user_prompt,
                    response_format
                )

            st.success("Response generated successfully!")
            st.divider()

            st.subheader("Generated Response")

            if response_format == "json":
                st.json(response)

            elif response_format == "markdown":
                st.markdown(response)

            else:
                st.write(response)

        except RuntimeError as e:
            st.error(f"Gemini API Error\n\n{e}")

        except ValueError as e:
            st.error(f"Response Parsing Error\n\n{e}")

        except Exception as e:
            st.error(f"Unexpected Error\n\n{e}")


def render_templates():
    st.title("Prompt Templates")

    st.write("Create, edit and manage reusable prompts.")
    st.divider()

    templates = template_service.list_templates()

    # Existing Templates
    st.subheader("Existing Templates")

    if templates:
        selected = st.selectbox(
            "Select Template",
            templates,
            format_func=lambda t: t["name"]
        )

        updated_prompt = st.text_area(
            "Template Prompt",
            value=selected["prompt"],
            height=180
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "Update Template"
            ):

                template_service.update_template(
                    selected["id"],
                    updated_prompt
                )

                st.success("Template updated successfully!")
                st.rerun()

        with col2:
            if st.button(
                "Delete Template"
            ):

                template_service.delete_template(
                    selected["id"]
                )

                st.success("Template deleted successfully!")
                st.rerun()

    else:
        st.info("No templates available.")

    st.divider()

    # Create New Template
    st.subheader("Create New Template")
    with st.form("create_template"):

        template_name = st.text_input(
            "Template Name"
        )

        template_prompt = st.text_area(
            "Template Prompt",
            height=180
        )

        submitted = st.form_submit_button(
            "Save Template"
        )

        if submitted:
            if not template_name.strip():
                st.warning("Template name cannot be empty.")

            elif not template_prompt.strip():
                st.warning("Template prompt cannot be empty.")

            else:

                try:

                    template_service.save_template(
                        {
                            "name": template_name,
                            "prompt": template_prompt
                        }
                    )

                    st.success("Template created successfully!")
                    st.rerun()

                except ValueError as e:
                    st.warning(str(e))


def render_history():

    st.title("Prompt History")
    st.write("View all previously generated prompts and responses.")
    st.divider()

    history = history_service.load_history()

    if not history:
        st.info("No prompt history available.")
        return

    st.metric("Total Records", len(history))
    st.divider()

    for record in reversed(history):
        with st.expander(record["user_prompt"]):

            st.markdown("### Prompt")
            st.write(record["user_prompt"])

            st.markdown("### Enhanced Prompt")
            st.write(record["enhanced_prompt"])

            st.markdown("### Response Format")
            st.write(record["output_format"])

            st.markdown("### Model")
            st.write(record["model"])

            st.markdown("### Response")
            if record["output_format"] == "json":
                st.json(record["response"])

            elif record["output_format"] == "markdown":
                st.markdown(record["response"])

            else:
                st.write(record["response"])

def render_about():
    st.title("About AI Prompt Playground Pro")
    st.write(
        """
AI Prompt Playground Pro is a Prompt Engineering application that helps developers create, test, organize and reuse AI prompts using Google's Gemini API.
"""
    )

    st.divider()

    st.subheader("Features")

    st.markdown("""
- AI Prompt Generation
- Prompt Template Management
- Prompt History
- Multiple Response Formats
- Gemini Integration
- JSON Storage
- Modular Architecture
""")

    st.divider()

    st.subheader("Tech Stack")

    st.markdown("""
- Python
- Streamlit
- Gemini API
- JSON
- Modular Services
""")

    st.divider()

    st.subheader("Architecture")

    st.code(
"""
User
   │
   ▼
Streamlit UI
   │
   ▼
AI Processor
   │
   ├── Prompt Builder
   ├── Gemini Service
   ├── Response Parser
   ├── Template Service
   └── History Service
""",
        language="text"
    )

    st.divider()

    st.success("Built as part of an Agentic AI learning journey.")

# Sidebar Configuration
st.sidebar.image(
    "assets/logo.png",
    width=450
)
menu = st.sidebar.radio(
    "Navigation",
    [
        "Generate",
        "Templates",
        "History",
        "About"
    ]
)

if menu == "Generate":
    render_generate()
elif menu == "Templates":
    render_templates()
elif menu == "History":
    render_history()
else:
    render_about()

