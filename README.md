# Activate virtual environment:
    - python -m venv .venv
    - .venv\Scripts\activate.bat
# Deactivate vm:
    - deactivate
# Start the project:
    - uv run main.py
# How to read env variables:
    - from dotenv import load_dotenv
    - load_dotenv()

# dependencies:
    - langchain
    - chromadb
    - dotenv