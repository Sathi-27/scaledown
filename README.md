\# Code Documentation Navigator 🔍



A Retrieval-Augmented Generation (RAG) system that helps developers

navigate, search, and understand large Python codebases using semantic search.



---



\## 🚀 What This Project Does



\- Ingests real-world Python repositories

\- Converts source code into vector embeddings

\- Stores embeddings using FAISS

\- Retrieves relevant code based on natural-language queries

\- Explains retrieved code with human-readable summaries



This system demonstrates how RAG can be applied to code intelligence

and documentation navigation.



---



\## 🏗 System Architecture



1\. \*\*Ingestion\*\*  

&nbsp;  Reads all Python files from a target repository



2\. \*\*Embedding\*\*  

&nbsp;  Uses Sentence Transformers to convert code into vector representations



3\. \*\*Retrieval\*\*  

&nbsp;  FAISS performs semantic similarity search over the embeddings



4\. \*\*Explanation\*\*  

&nbsp;  Retrieved code is summarized to help users understand functionality



---



\## 🛠 Tech Stack



\- Python

\- Sentence Transformers

\- FAISS

\- NumPy

\- GitHub (code hosting)



---



\## ▶️ How to Run



```bash

pip install -r requirements.txt

python ingest.py

python embed.py

python search.py



