import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

# print(f"Token loaded: {'HUGGINGFACEHUB_API_TOKEN' in os.environ}")

# 1. Create a client directly from the huggingface_hub library
client = InferenceClient(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)

# 2. Use the .chat_completion() method for chat models
# Note: Chat models expect a list of messages with "role" and "content"
print("Invoking the model directly...")
response = client.chat_completion(
    messages=[
        {"role": "user", "content": "who is sunny leone "}
    ],
    max_tokens=256,
)

# 3. The response is an object, we need to access the content
# response.choices[0].message.content
print("\nResponse from model:")
print(response.choices[0].message.content)