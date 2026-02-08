import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory="db", embedding_function=embedding)

def ask(query):
    docs = db.similarity_search(query, k=3)
    if not docs:
        return "No relevant code found."
    return "\n\n".join([d.page_content for d in docs])

gr.Interface(
    fn=ask,
    inputs=gr.Textbox(label="Ask about the code"),
    outputs=gr.Textbox(label="Answer"),
    title="Code Documentation Navigator (RAG)",
    description="Ask questions about your codebase using semantic search"
).launch()
