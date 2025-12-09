import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- NEW IMPORTS FOR EMBEDDINGS AND TOGETHER AI LLM ---
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_together.llms import Together
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

from dotenv import load_dotenv
import os

# --- Load API Key ---
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Choose Together AI model
TOGETHER_MODEL_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# --- Error Handling for Missing API Key ---
if not TOGETHER_API_KEY:
    st.error("Error: Together AI API key not found.")
    st.info("Create a .env file with TOGETHER_API_KEY=sk-tg-XXXXXXXX")
    st.stop()

st.header("📚 Multi-PDF Chatbot")

with st.sidebar:
    st.title("Your Documents")
    files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)

# --- Process Uploaded PDFs ---
if files:
    text = ""
    for file in files:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Embeddings & Vector Store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(chunks, embeddings)

    # User question
    user_question = st.text_input("❓ Ask a question about your PDFs")

    if user_question:
        # Search relevant chunks
        match = vector_store.similarity_search(user_question)

        # Define LLM
        llm = Together(
            model=TOGETHER_MODEL_ID,
            together_api_key=TOGETHER_API_KEY,
            temperature=0.1,
            max_tokens=1000
        )

        # Chain
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.invoke({"input_documents": match, "question": user_question})

        st.write(response["output_text"])
