# Semantic Search Engine

A semantic search engine built for Pokemon card descriptions using [Sentence Transformers](https://www.sbert.net/) (`sentence-transformers/all-MiniLM-L6-v2`), [ChromaDB](https://www.trychroma.com/), and [Streamlit](https://streamlit.io/).

## Repository Structure
```
.
├── chromadb/
│   └── chroma.sqlite3
├── app.py
├── requirements.txt
└── README.md
```

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/colbyrobbins/Semantic-Search-Engine.git
   cd Semantic-Search-Engine
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Deploying to Streamlit Community Cloud

1. Push your repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Click **New app** and select your repository (`colbyrobbins/Semantic-Search-Engine`).
4. Set the Main file path to `app.py`.
5. Click **Deploy!**
