import streamlit as st
from utils import load_pdf, split_text
from rag_pipeline import build_vector_store, load_model,create_qa_chain,create_conversational_chain

st.set_page_config(page_title="IPO ADvisor", layout="wide")
st.title("Should you subscribe or not")

if "chat history" not in st.session_state:
    st.session_state.chat_history=[]

file=st.file_uploader('C:/Users/krish/Desktop/RAG/Docs/Vishal_Mega_Mart.pdf',type="pdf")

if file:
    with st.spinner("Reading and indexing pdf"):
        text=load_pdf(file)
        chunks=split_text(text)
        vectors=build_vector_store(chunks)
        llm=load_model()
        # qa_chain=create_qa_chain(llm,vectors)
        qa_chain = create_conversational_chain(llm, vectors)
    st.success("PDF Indexed successfully")
    
    query=st.text_input("Post any queries related to IPO:")
    
    if query and qa_chain:
        with st.spinner("Processing"):
            result = qa_chain({
                "question": query,
                "chat_history": st.session_state.chat_history
            })
            answer = result["answer"]
            # Update history
            st.session_state.chat_history.append((query, answer))
        st.write("### Answer:")
        st.info(answer)

        with st.expander("🕓 Chat History"):
            for i, (q, a) in enumerate(st.session_state.chat_history):
                st.markdown(f"**Q{i+1}:** {q}")
                st.markdown(f"**A{i+1}:** {a}")