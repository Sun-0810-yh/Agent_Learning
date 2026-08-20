from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
name = os.getenv("TEST_NAME")
age = os.getenv("TEST_AGE")

print(api_key)
print(name)
print(age)


