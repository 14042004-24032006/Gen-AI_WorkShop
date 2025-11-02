from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import os

def load_ncert_data(pdf_paths):
    docs = []
    for path in pdf_paths:
        print(f"📘 Loading {path}...")
        loader = PyPDFLoader(path)
        pdf_docs = loader.load()
        docs.extend(pdf_docs)
        print(f"✅ Loaded {path} — {len(pdf_docs)} pages")
    return docs

def create_vector_store(docs, save_path="ncert_index"):
    # 🔹 Use open-source embeddings (no API key needed)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(save_path)
    print(f"✅ Vector database created and saved at: {save_path}")

if __name__ == "__main__":
    pdf_paths = [
        "data/science class 8.pdf",
    ]
    docs = load_ncert_data(pdf_paths)
    create_vector_store(docs)
