import os
from dotenv import load_dotenv

# This line is the same, it loads all variables from your .env file
load_dotenv() 
print("Done")
print("..")

# --- CHANGE 1: Import the Gemini embedding class instead of OpenAI's ---
# from langchain_openai import OpenAIEmbeddings  <-- We don't need this anymore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- CHANGE 2: Instantiate the GoogleGenerativeAIEmbeddings class ---
# We must specify the model we want to use for embeddings.
# "models/embedding-001" is Google's standard, high-quality embedding model.
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


# --- NO OTHER CHANGES NEEDED! ---
# The rest of your code works exactly the same because both classes
# have the same .embed_query() method. This is the power of LangChain.
result = embedding.embed_query("Delhi is the capital of india")

# The result is a long list of numbers (the embedding vector), which is correct.
# We'll print the first 10 numbers to confirm it worked.
print("Successfully got embedding from Google Gemini!")
print(str(result))
print(f"Vector dimension: {len(result)}")