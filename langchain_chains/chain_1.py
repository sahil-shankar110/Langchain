# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id = "deepseek-ai/DeepSeek-V3.2-Exp",
#     task = "text-generation"
# )
# model = ChatHuggingFace(llm=llm)

# prompt = PromptTemplate(
#     template="Generate 5 interesting factc about {topic}.",
#     input_variables=["topic"]
# )

# parser = StrOutputParser()

# chain = prompt | model | parser
# result = chain.invoke({"topic" : "cricket"})
# print(result)

# print(chain.get_graph().print_ascii())

"""
Docstring for langchain_chains.chain_1
complex chain example with multiple prompts and llm calls
"""

# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id = "deepseek-ai/DeepSeek-V3.2-Exp",
#     task = "text-generation"
# )
# model = ChatHuggingFace(llm=llm)

# prompt1 = PromptTemplate(
#     template="Generate detailed information about {topic}.",
#     input_variables=["topic"]
# )

# prompt2 = PromptTemplate(
#     template="Provide a 5 explanation points about {text}.",
#     input_variables=["text"]
# )
# parser = StrOutputParser()

# chain = prompt1 | model | parser | prompt2 | model | parser
# result = chain.invoke({"topic" : "cricket"})
# print(result)

# print(chain.get_graph().print_ascii())