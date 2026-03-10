AI Research Assistant (RAG-Powered Chat with PDFs)

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about them.
The system retrieves relevant information from the document and generates accurate AI responses using a Large Language Model.
This project demonstrates practical Generative AI engineering, including document processing, embeddings, vector search, and LLM integration.

--Demo Workflow

User uploads a PDF document 
Text is extracted and split into chunks
Each chunk is converted into vector embeddings
Embeddings are stored in a vector database
User asks a question
Relevant document chunks are retrieved
LLM generates an answer using retrieved context
This approach ensures the AI answers using the document instead of hallucinating.

--Key Features
Upload and analyze PDF documents
Intelligent document chunking
Semantic search using embeddings
Retrieval-Augmented Generation (RAG)
Context-aware answers from documents
Interactive web interface

--Tech Stack

Programming
Python

-AI / LLM
LangChain – orchestration framework
Groq – high-speed LLM inference
Hugging Face – embeddings model

-Vector Database
FAISS – similarity search

-Interface
Streamlit – interactive web UI


--What This Project Demonstrates

-This project showcases practical Generative AI engineering skills:
Retrieval-Augmented Generation (RAG)
LLM integration
Vector databases
Semantic search
Document processing pipelines
API-based AI systems
Building real AI applications with Python
