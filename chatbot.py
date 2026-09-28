import streamlit as st
from langchain_ollama import ChatOllama

#pip install -qU langchain-ollama
#pip install langchain

st.title("simple chatbot made with ollama and langchain!!!!")
st.write("get more info at https://www.youtube.com/watch?v=vJOGC8QJZJQ")
with st.form("llm-form"):
    text=st.text_area("Enter your question")
    submit=st.form_submit_button("submit")


def generate_response(input_text):

    model=ChatOllama(model="llama3.2:3b")

    response=model.invoke(input_text)

    return response.content
if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

if submit and text:
    with st.spinner("generating response..."):
        response=generate_response(text)
        st.session_state["chat_history"].append({"user":text,"ollama":response})
        st.write(response)

st.write("## chat history")
for chat in reversed(st.session_state["chat_history"]):
    st.write(f"**user**:{chat['user']}")
    st.write(f"**Assistant**:{chat['ollama']}")
    st.write("---")

