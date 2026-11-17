import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

st.set_page_config(
    page_title="Pokemon Semantic Search Engine",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Semantic Search Engine")
st.markdown("Search over Pokemon cards using semantic similarity with **Sentence Transformers** and **ChromaDB**.")

@st.cache_resource
def load_resources():
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path="./chromadb")
    collection = client.get_collection("my_collection")
    return model, collection

model, collection = load_resources()

query = st.text_input("Enter your search query:", placeholder="e.g., fiery flying dragon or powerful psychic")
top_k = st.slider("Number of results", min_value=1, max_value=10, value=3)

if query:
    with st.spinner("Searching..."):
        query_embedding = model.encode([query]).tolist()
        results = collection.query(query_embeddings=query_embedding, n_results=top_k)

    st.subheader("Top Matches")
    if results and results.get('documents') and len(results['documents'][0]) > 0:
        for i, doc in enumerate(results['documents'][0]):
            with st.container(border=True):
                st.markdown(f"**Result {i + 1}**")
                st.write(doc)
    else:
        st.info("No matches found.")
