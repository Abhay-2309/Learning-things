from langchain_huggingface import HuggingFaceEmbeddings
print("Start..\n")
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
print("converting to emeddings....")
text = "Delhi is the capital of india"
vector = embedding.embed_query(text)
print(f"the type of the vector is {type(vector)}")
print(vector)
print(len(vector))