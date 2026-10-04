from flask import Flask, render_template, request, jsonify

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_pinecone import PineconeVectorStore

from src.helper import download_hugging_face_embeddings
from src.prompt import prompt

import os


# Load environment variables from .env
load_dotenv()


# Create Flask application
app = Flask(__name__)


# Pinecone index
index_name = "medicalbot"


# Create embedding model
embeddings = download_hugging_face_embeddings()


# Connect to the existing Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)


# Create retriever
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# Create Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form.get("msg")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Search Pinecone for relevant medical information
    documents = retriever.invoke(user_message)

    # Combine retrieved documents into context
    context = "\n\n".join(
        document.page_content for document in documents
    )

    # Create the prompt
    formatted_prompt = prompt.invoke(
        {
            "context": context,
            "input": user_message
        }
    )

    # Ask Groq to generate the answer
    response = llm.invoke(formatted_prompt)

    return response.content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)