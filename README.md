# IPO_Subcribtion_Analyzer

An open-source **RAG (Retrieval-Augmented Generation)** application that helps you make informed decisions about **IPO subscriptions**. Upload any IPO's **Red Herring Prospectus (RHP)** in PDF format and ask natural language questions. Powered by **LangChain**, **FAISS**, **FLANT5**, and **Streamlit**.


---

## 🚀 Features

- 🔍 Upload and parse RHP PDF documents
- 🧠 Question answering using Retrieval-Augmented Generation (RAG)
- 📚 Vector search using FAISS and Sentence Transformers
- 🗣️ LLM-powered natural language answers (FLAN-T5)
- 🌐 Simple, no-code UI via Streamlit
- 💬 Support for chat history with memory

---

## 🧱 Tech Stack

| Component      | Technology                     |
|----------------|-------------------------------|
| Frontend       | Streamlit                     |
| Backend        | Python, LangChain             |
| Embeddings     | Sentence Transformers (`MiniLM`) |
| Vector Store   | FAISS                         |
| LLM            |  FLAN-T5                      |
| PDF Parsing    | pdfplumber                    |


## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/krishnaharish9/IPO_Subscription_Analyzer.git
cd ipo-rag

# Create a virtual environment
conda create -n ipo-rag python=3.10
conda activate ipo-rag


# Install dependencies
pip install -r requirements.txt
