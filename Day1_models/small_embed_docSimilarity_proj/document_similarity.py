from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is known for his aggressive batting style and is one of the most consistent run scorers in international cricket.",
    "MS Dhoni is famous for his calm leadership and led India to victory in the 2011 Cricket World Cup.",
    "Sachin Tendulkar, called the God of Cricket, holds many records including the most runs in international cricket.",
    "Hardik Pandya is a powerful all-rounder known for his explosive batting and fast bowling.",
    "Virender Sehwag was a fearless opening batsman famous for his aggressive and attacking style of play."
]

query = "Tell me about Virat Kohli"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

result = cosine_similarity([query_embedding],doc_embedding)[0]

index, score = sorted(list(enumerate(result)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is: ",score)
