from dotenv import load_dotenv
load_dotenv()

import os
import sys
from importlib.metadata import version

from langchain_core import __version__ as core_version
from langchain_openai import ChatOpenAI

#document loader
import tempfile
from pathlib import Path
from langchain_community.document_loaders import (TextLoader)

lg_version = version("langgraph")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


OPENROUTER_BASE_URL = (os.getenv("OPENROUTER_BASE_URL") or "https://openrouter.ai/api/v1").strip()
OPENROUTER_API_KEY = (os.getenv("OPENROUTER_API_KEY") or "").strip()
DEFAULT_MODEL = (os.getenv("DEFAULT_MODEL") or "deepseek/deepseek-v4-flash").strip()


def print_versions():
    print(f"LangChain Core version: {core_version}")
    print(f"LangGraph version: {lg_version}")


def get_llm(model: str, base_url: str, api_key: str, temperature: float = 0.7) -> ChatOpenAI:
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is missing. Set it in .env before running this script.")

    return ChatOpenAI(
        model=model,
        temperature=temperature,
        base_url=base_url,
        api_key=api_key,
    )


def ask_model(llm: ChatOpenAI, prompt: str):
    return llm.invoke(prompt)


def print_response(model: str, response) -> None:
    print(f"Model: {model}")
    print(f"Response from LLM: {response.content}")

def load_text_file():
    #create a temporary text file for testing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp_file:
        tmp_file.write(b"Hello, this is a sample text file for testing.\nIt contains multiple lines of text to demonstrate the TextLoader functionality.")
        tmp_file_path = tmp_file.name
        
    try:
        # Load the text file using TextLoader
        loader = TextLoader(tmp_file_path)
        documents = loader.load()

        # Print the loaded documents once per document
        for i, doc in enumerate(documents, start=1):
            print(f"Document {i} content:\n{doc.page_content}\n")
    finally:
        # Clean up the temporary file
        os.remove(tmp_file_path)

def main(
    model: str = DEFAULT_MODEL,
    base_url: str = OPENROUTER_BASE_URL,
    api_key: str = OPENROUTER_API_KEY,
    prompt: str = "who are you?",
    temperature: float = 0.5,
):
    print_versions()
    #llm = get_llm(model=model, base_url=base_url, api_key=api_key, temperature=temperature)
    #response = ask_model(llm, prompt)
    #print_response(model, response)
    #print("setup complete")
    load_text_file()


if __name__ == "__main__":
    main()
