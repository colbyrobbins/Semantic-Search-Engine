# Semantic Search Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://semantic-search-enginegit-gkos3wfqg7ibztjwxsa9f2.streamlit.app/)

🔗 **Live Demo**: [https://semantic-search-enginegit-gkos3wfqg7ibztjwxsa9f2.streamlit.app/](https://semantic-search-enginegit-gkos3wfqg7ibztjwxsa9f2.streamlit.app/)

A semantic search engine built for Pokémon card descriptions using [Sentence Transformers](https://www.sbert.net/) (`sentence-transformers/all-MiniLM-L6-v2`), [ChromaDB](https://www.trychroma.com/), and [Streamlit](https://streamlit.io/).

## Features
- **Semantic Similarity Search**: Find cards by concepts, moves, or descriptions (e.g., "fiery flying dragon" or "psychic trickster") rather than just exact keyword matches.
- **Pre-computed Vector Database**: Over 13,000 Pokémon cards embedded and indexed in ChromaDB for instant sub-second retrieval.
- **Interactive Streamlit Interface**: Clean UI with adjustable result count (top-K).

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
