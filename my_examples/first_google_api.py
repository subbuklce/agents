import os
from google import genai
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env
api_key = os.getenv("GEMINI_API_KEY")


# The client automatically picks up the API key from the environment variable
client = genai.Client(api_key=api_key)
# Use the key to configure the SDK
# genai.configure(api_key=api_key)
# Select a model (e.g., "gemini-2.5-flash" is versatile and fast)
model_name = "gemini-2.5-flash"

# Send a prompt to the model
response = client.models.generate_content(
    model=model_name,
    contents="Explain how AI works in a few words"
)

# Print the model's response
print(response.text)
