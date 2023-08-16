import os
from langchain.llms import OpenAI
from openai import Completion

try:
    os.environ['OPENAI_API_KEY'] = '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'
    llm=OpenAI(temperature= 0.7)
    a=input()
    print("Give the question:",end="")
    print(llm(a))

except Exception as e:
    print("ERROR:",str(e))
