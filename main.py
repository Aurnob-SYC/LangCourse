from dotenv import load_dotenv
load_dotenv()

import os
import sys
from importlib.metadata import version

from langchain_core import __version__ as core_version
from langchain_openai import ChatOpenAI

lg_version = version("langgraph")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

print(f"LangChain Core version: {core_version}")
print(f"LangGraph version: {lg_version}")


OPENROUTER_BASE_URL = (os.getenv("OPENROUTER_BASE_URL") or "https://openrouter.ai/api/v1").strip()
OPENROUTER_API_KEY = (os.getenv("OPENROUTER_API_KEY") or "").strip()
DEFAULT_MODEL = (os.getenv("DEFAULT_MODEL") or "deepseek/deepseek-v4-flash").strip()


def main():
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is missing. Set it in .env before running this script.")

    llm = ChatOpenAI(
        model=DEFAULT_MODEL,
        temperature=0.7,
        base_url=OPENROUTER_BASE_URL,
        api_key=OPENROUTER_API_KEY,
    )
    response = llm.invoke("who are you?")
    print(f"Model: {DEFAULT_MODEL}")
    print(f"Response from LLM: {response.content}")

    print("setup complete")


if __name__ == "__main__":
    main()
