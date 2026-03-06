from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-genetation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )

)

model = ChatHuggingFace(llm = llm)

result = model.invoke('What is the Capital of United Kingdom')
print(result.content)