from dotenv import load_dotenv
import os
import streamlit as st
from rag_pipeline import create_rag_chain
import tempfile

load_dotenv()
st.title("AI Research Assistant")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    retriever, llm = create_rag_chain(pdf_path)

    question = st.text_input("Ask a question")

    if question:
        docs = retriever.invoke(question)

        context = " ".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {question}
        """

        response = llm.invoke(prompt)

        st.write(response.content)