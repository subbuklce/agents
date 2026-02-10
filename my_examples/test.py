# %%
from email import message
from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env from parent directory (relative to this script's location)
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path, override=True)
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if gemini_api_key:
    print(f" successfully able to load the key now:{gemini_api_key[:4]}")
else:
    print(f"unable to load the dotenv into environment variables, please cross check once")

from openai import OpenAI

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

python_client = OpenAI(base_url=GEMINI_BASE_URL, api_key=gemini_api_key)

message = [{"role":"user", "content":"what is 2 + 2?"}]
model_name = "gemini-2.5-flash"
response = python_client.chat.completions.create(
    model=model_name,messages=message
)

from IPython.display import Markdown, display

# Display the question using Markdown
question = message[0]["content"]
print("Question:")
display(Markdown(f"**Question:** {question}"))

# Display the response
print("\nAnswer:")
print(response.choices[0].message.content)
display(Markdown(response.choices[0].message.content))

# %%
