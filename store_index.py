from src.helper import (
    load_pdf_file,
    text_split,
    download_hugging_face_embeddings
)

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

import os


# Load API keys from .env
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set in .env")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


# 1. Load the medical PDF
extracted_data = load_pdf_file(data="Data/")


# 2. Split PDF text into smaller chunks
text_chunks = text_split(extracted_data)


# 3. Create embeddings
embeddings = download_hugging_face_embeddings()


# 4. Connect to Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)


# 5. Name of our Pinecone index
index_name = "medicalbot"


# 6. Create the index
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )


# 7. Store the document embeddings in Pinecone
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

print("Medical documents successfully stored in Pinecone!")