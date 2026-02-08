from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

def load_code(path):
    texts = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), encoding="utf-8", errors="ignore") as f:
                    texts.append(f.read())
    return texts

print("Loading code...")
docs = load_code("sample_repo")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = splitter.create_documents(docs)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = Chroma.from_documents(chunks, embedding, persist_directory="db")
db.persist()

print("✅ DONE: Code indexed successfully")
