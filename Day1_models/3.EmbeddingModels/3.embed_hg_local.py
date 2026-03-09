from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "Suryakumar Yadav is the Caption of Indian Team"

vector = embedding.embed_query(text)

print(str(vector))

#for Documests

documents = [
    "Suryakumar Yadav is the Caption of Indian Team"
    "Rashid Khan is the Caption of Afghanistan Team"
    "Harry Brook is the Caption of England Team"
    "Mitchell Santner is the Caption of New Zealand Team"
]

vector2 = embedding.embed_documents(documents)
print(str(vector2))