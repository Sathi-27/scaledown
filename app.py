import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load vector database
db = Chroma(persist_directory="db", embedding_function=embedding)

def ask(query):
    docs = db.similarity_search(query, k=5)

    seen = set()
    unique_chunks = []

    for d in docs:
        text = d.page_content.strip()
        if text and text not in seen:
            seen.add(text)
            unique_chunks.append(text)

    if not unique_chunks:
        return "❌ No relevant code found."

    return "\n\n".join(unique_chunks)

# Gradio Interface
gr.Interface(
    fn=ask,
    inputs=gr.Textbox(placeholder="Ask about the code..."),
    outputs=gr.Textbox(label="Relevant Code"),
    title="🔍 Code Documentation Navigator (RAG)",
    description="Ask natural language questions to understand large codebases using semantic search."
).launch()
