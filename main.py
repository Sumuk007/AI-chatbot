from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="AI Project1/.venv/.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

question = input("Ask a question: ")

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
        system_instruction=[
            types.Part.from_text(text="""Your name is \"my ai\" and you are an ai assistant who helps the user in daily tasks and answer any question he asks, also you should be able to converse with the user like a human being."""),
        ],
    ),
)
print(response.text)


