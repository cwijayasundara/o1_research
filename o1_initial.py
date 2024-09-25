import warnings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

warnings.filterwarnings('ignore')
_ = load_dotenv()

llm = ChatOpenAI(model='o1-preview', temperature=1)

response = llm.invoke("What is AdS/CFT?")
print(response.content)
