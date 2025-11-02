from langchain.chains import RetrievalQA
from workshop.models import model
from langchain.vectorstores import FAISS

def get_qa_chain():
    db = FAISS.load_local("ncert_index", embeddings=None, allow_dangerous_deserialization=True)
    qa_chain = RetrievalQA.from_chain_type(
        llm=model,
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff"
    )
    return qa_chain
