from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.3 , max_completion_tokens=15)
#temperature is the parameter that controls the randomness of lang model
#lower value (0 - 0.4) -> More Deterministic and predictable Answers
#higher value (0.7 - 1.6) -> More Creative and random Answers

result = model.invoke("Wite a 5 line of Poem on topic of Football")
print(result)
print(result.content)