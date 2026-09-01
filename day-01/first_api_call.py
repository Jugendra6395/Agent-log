import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("API key loaded:", api_key is not None)
print("Key ends with:", api_key[-4:])

client = OpenAI(api_key=api_key)
question = input("Ask the AI something: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=question
)