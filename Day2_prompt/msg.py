from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b"
)

msgs = [
    SystemMessage(content='You are a Helpful Assistents'),
    HumanMessage(content="Tell me about langchain")
]

result = model.invoke(msgs)

msgs.append(AIMessage(content = result.content))

print(msgs)