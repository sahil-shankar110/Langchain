from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Assistant")
user = st.text_input("Enter your prompt")
llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.2-Exp",
    task = "text-generation"
)
model = ChatHuggingFace(llm=llm)
if st.button("Get Response"):
    response = model.invoke(user)
    st.write(response.content)
