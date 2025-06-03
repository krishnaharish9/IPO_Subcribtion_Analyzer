from transformers import AutoTokenizer,AutoModelForSeq2SeqLM,pipeline
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA 
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFacePipeline

def build_vector_store(documents):
    embedding=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectors=FAISS.from_documents(documents,embedding)
    return vectors

def load_model():
    model_id = "google/flan-t5-large"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)
    return HuggingFacePipeline(pipeline=pipe)

#Just for Retrieval QA
def create_qa_chain(llm,vector_store):
    retriever=vector_store.as_retriever(search_kwags={"k":5})
    return RetrievalQA.from_chain_type(llm=llm,retriever=retriever)

#For historical conversations
def create_conversational_chain(llm, vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)


