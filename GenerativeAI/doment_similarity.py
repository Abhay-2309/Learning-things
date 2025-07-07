from langchain_google_genai import  GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001',dimensions = 300)
documents = [
"Amitabh Bachchan - Known as the 'Shahenshah of Bollywood', with a career spanning over five decades. Notable films include Sholay, Piku, and Zanjeer.",
"Shah Rukh Khan - The 'King of Bollywood', famous for romantic and dramatic roles in films like DDLJ, My Name is Khan, and Pathaan.",
"Rajinikanth - Superstar of Tamil cinema, admired for his unique style and iconic films like Baashha, Enthiran, and Jailer.",
"Ranbir Kapoor - A versatile actor from the Kapoor dynasty, known for acclaimed performances in Rockstar, Barfi!, and Sanju.",
"N. T. Rama Rao Jr. (Jr. NTR) - Telugu cinema's powerhouse performer, known for his energy, dance skills, and roles in RRR and Janatha Garage."
]
query = 'tell me about Rajnikanth'

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)
scores = cosine_similarity([query_embeddings],doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]
print("Query is -",query)
print("search output is : ")
print(documents[index])
print(f"similarity score is {int(score*100)}%")