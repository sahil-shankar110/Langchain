# from langchain_community.tools import DuckDuckGoSearchRun
# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from langchain_core.tools import tool
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# search_tool = DuckDuckGoSearchRun()
# @tool
# def get_weather_data(city: str) -> str:
#   """
#   This function fetches the current weather data for a given city
#   """
#   url = f'https://api.weatherstack.com/current?access_key=d41a8f40bfb79c6d9dac22903a586b08&query={city}'

#   response = requests.get(url)

#   return response.json()

# llm = HuggingFaceEndpoint(
#     repo_id = "deepseek-ai/DeepSeek-V3.2-Exp",
#     task = "text-generation"
# )
# model = ChatHuggingFace(llm=llm)


# system_prompt = "You are an intelligent assistant. Use your tools when needed."
# from langchain.agents import create_agent
# agent = create_agent(
#     model=llm,
#     tools=[search_tool, get_weather_data],
#     system_prompt=system_prompt
# )

# input_data = {"input": "Find the capital of Madhya Pradesh, then find its current weather condition"}

# # Call the agent like a function
# result = agent.invoke(input_data)

# print(result)

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.tools import tool
import requests
from dotenv import load_dotenv

load_dotenv()

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """
    url = f'https://api.weatherstack.com/current?access_key=d41a8f40bfb79c6d9dac22903a586b08&query={city}'
    response = requests.get(url)
    return response.json()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.2-Exp",
    task = "text-generation"
)

# ✔ Wrap into ChatModel
model = ChatHuggingFace(llm=llm)

system_prompt = "You are an intelligent assistant. Use your tools when needed."

from langchain.agents import create_agent
agent = create_agent(
    model=model,             # ✔ FIXED
    tools=[search_tool, get_weather_data],
    system_prompt=system_prompt
)

input_data = {"input": "Find the capital of Madhya Pradesh, then find its current weather condition"}

# ✔ Correct way to run
result = agent.invoke(input_data)

print(result.content)
