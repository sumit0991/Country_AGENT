import os
import requests
from dotenv import load_dotenv

from tools import get_country_info
from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-oss-20b:free"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def call_llm(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    return response.json()


def extract_country(user_input):
    """
    Extract country name from user input.
    Examples:
    Nepal
    Tell me about India
    Capital of Japan
    Population of Brazil
    """

    words = user_input.split()

    ignore = {
        "capital",
        "currency",
        "population",
        "language",
        "languages",
        "continent",
        "country",
        "about",
        "tell",
        "me",
        "of",
        "what",
        "is",
        "the"
    }

    country = []

    for word in words:
        if word.lower() not in ignore:
            country.append(word)

    return " ".join(country)


def is_country_query(user_input):
    keywords = [
        "capital",
        "currency",
        "population",
        "language",
        "continent",
        "country",
        "about"
    ]

    text = user_input.lower()

    if any(word in text for word in keywords):
        return True

    # single word like "Nepal"
    if len(user_input.split()) == 1:
        return True

    return False


def agent_loop(user_input):
    memory = load_memory()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(memory)

    if is_country_query(user_input):

        country = extract_country(user_input)

        tool_data = get_country_info(country)

        prompt = f"""
Country Information:

{tool_data}

Answer the user's question professionally.

Question:
{user_input}
"""

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

    else:

        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

    result = call_llm(messages)

    answer = result["choices"][0]["message"]["content"]

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    save_memory(messages[1:])

    return answer


if __name__ == "__main__":

    print("🌍 Country Info AI Agent")
    print("Using OpenRouter")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        try:
            response = agent_loop(user_input)
            print("\nAgent:", response)
            print()

        except Exception as e:
            print("Error:", e)