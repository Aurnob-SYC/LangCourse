# Activate virtual environment:
    - python -m venv .venv
# Deactivate vm:
    - deactivate
# Start the project:
    - uv run main.py
# How to read env variables:
    - from dotenv import load_dotenv
    - load_dotenv()