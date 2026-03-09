from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the Capital of United Kingdom")
print(result.content)
