import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document


def load_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text="\n".join([page.extract_text() or "" for page in pdf.pages])

    return text

def split_text(text):
    splitter=RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=200)
    chunks=splitter.split_text(text)
    return [Document(page_content=chunk) for chunk in chunks]

