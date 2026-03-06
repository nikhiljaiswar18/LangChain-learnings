# LangChain Learning Projects

This repository contains my practice implementations while learning **LangChain and LLM application development**.
The projects in this repository cover the fundamentals of working with **Large Language Models (LLMs), Chat Models, Embedding Models, and Document Similarity** using Python.

## 📚 What I Learned

* How to use **LLMs with LangChain**
* Working with **Chat Models**
* Understanding **Embedding Models**
* Measuring **document similarity using vector embeddings**
* Building small practical projects with LangChain

## 📂 Project Included

### Document Similarity using Embeddings

This project demonstrates how to use **embedding models** to measure similarity between a user query and a set of documents.

The program:

1. Converts documents into **vector embeddings**
2. Converts the user query into an embedding
3. Computes **similarity scores**
4. Returns the document that is most similar to the query.

Example:

Query:

```
tell me about virat kohli
```

Output:

```
Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.
similarity score: 0.6631
```

## ⚙️ Technologies Used

* Python
* LangChain
* HuggingFace Embeddings
* NumPy

## ▶️ How to Run

1. Clone the repository
2. Install dependencies

```
pip install langchain huggingface-hub python-dotenv
```

3. Create a `.env` file and add your API keys

4. Run the program

```
python small_embed_docSimilarity_proj/document_similarity.py
```

## 🔐 Note

The `.env` file is not included in the repository to keep API keys secure.

---

This repository is part of my learning journey toward becoming an **AI/ML Engineer and building real-world LLM applications using LangChain**.
