from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model1 = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.2-Exp",
    task = "conversational"
)
model1 = ChatHuggingFace(llm=model1)

model2 = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task = "conversational"
)
model2 = ChatHuggingFace(llm=model2)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 question and answers from the following text \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provides notes and queston answers into a single document \n Notes: {notes} \n Q&A: {qa}",
    input_variables=["notes", "qa"]
)
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "qa": prompt2 | model2 | parser
    }
)
Merge_chain = prompt3 | model1 | parser 
final_chain = parallel_chain | Merge_chain 
text = """LangChain is a framework for developing applications powered by language models. It enables developers to build robust and scalable applications by providing modular components and tools that facilitate the integration of language models into various workflows. With LangChain, developers can create applications that leverage the capabilities of large language models for tasks such as natural language understanding, generation, and interaction."""

result = final_chain.invoke({"text": text})

print(result)
print(final_chain.get_graph().print_ascii())