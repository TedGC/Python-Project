"""because of the version of some files in the 'reuiqrements txt' 
there is a necessity to install some up-to-date versinos of those requireemtns and libraries
see more details in the error message when running 'pip3 install -r requirement.txt' in the terminal """


from dotenv import load_dotenv
import os 

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

@tool
def add_task(task):
    """add a new task to the user's tak list. use this when the user wants to add or create a new task"""
    print(task)
    print('task added')

tools = [add_task]

todoist_api_key = os.getenv('TODOIST_API_KEY')
gemini_api_key = os.getenv('GEMINI_API_KEY')

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = 'you are a helpful assistant'
user_input = 'add a new task to buy milk and new apple macbook'

prompt = ChatPromptTemplate([
    ("system", system_prompt),
    ("user", user_input),
    MessagesPlaceholder("agent_scratchpad")
])

# chain = prompt | llm | StrOutputParser()

agent = create_openai_tools_agent(llm, tools, prompt)
agent_excecutor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = chain.invoke({"input":user_input})

response = agent_excecutor.invoke({"input": user_input})

print(response)