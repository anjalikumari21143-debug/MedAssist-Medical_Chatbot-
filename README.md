🩺 MedAssist — AI Medical Chatbot

MedAssist is an AI-powered medical information chatbot built using Python, Flask, LangChain, Pinecone, Hugging Face embeddings, and Groq.
The chatbot uses a Retrieval-Augmented Generation (RAG) approach to retrieve relevant information from a medical knowledge base and generate clear responses to users' medical questions.

⚠️ Disclaimer: MedAssist is intended for educational and informational purposes only. It is not a substitute for professional medical diagnosis, treatment, or advice.

✨ Features

🩺 AI-powered medical information assistant

📚 Answers questions using a medical PDF knowledge base

🔎 Semantic search using Pinecone

🤖 AI-generated responses using Groq

🧠 Hugging Face embeddings

💬 Interactive web-based chat interface

💡 Suggested medical questions

⏳ Response/typing indicator

🧹 Clear chat functionality

📱 Responsive interface for desktop and mobile

🔐 API keys stored securely using environment variables

🚫 .env excluded from Git using .gitignore

🏗️ How It Works

MedAssist follows a Retrieval-Augmented Generation architecture:
User Question
 │
 ▼ Flask Backend 
 │
 ▼ Pinecone Retrieval 
 │
 ▼ Relevant Medical Information 
 │
 ▼ Groq LLM 
 │ 
 ▼ AI Response 
 │
 ▼ Chat Interface 
The medical information is first extracted from the provided PDF, converted into embeddings, and stored in Pinecone.
When a user asks a question, the system searches Pinecone for relevant information and provides that information as context to the language model.

🛠️ Technologies Used

Technology       Purpose
Python           Backend programming
Flask            Web application framework
LangChain        RAG and LLM integration
Pinecone         Vector database
Hugging Face     Text embeddings
Groq             Large Language Model
HTML,CSS,JS      Frontend programming
Git & GitHub     Version control 

📁 Project Structure

MEDICAL_CHATBOT/ 
│
├── Data/ 
│    └── Medical_book.pdf 
│ 
├── src/ 
│    ├── __init__.py 
│    ├── helper.py 
│    └── prompt.py 
├── templates/
│    └── chat.html 
│ 
├── app.py 
├── store_index.py 
├── requirements.txt 
├── .gitignore 
└── README.md 

⚙️ Installation

1. Create a virtual environment

2. Install dependencies

pip install -r requirements.txt 

🔑 Environment Variables

Create a .env file in the main project directory.
Add your API credentials:
PINECONE_API_KEY=your_pinecone_api_key 
GROQ_API_KEY=your_groq_api_key 

📚 Prepare the Medical Knowledge Base

Place your medical PDF inside:
Data/ 
For example:
Data/Medical_book.pdf  

🚀 Run the Application

After the medical documents have been indexed, start the Flask application:
python app.py 
You should see:
Running on http://127.0.0.1:8080 

💬 Example Question
   What are the symptoms of hypertension?

🔐 Security

API keys are stored in environment variables rather than directly inside the source code.
The .env file is excluded using .gitignore.

⚠️ Medical Disclaimer

MedAssist is an educational AI application designed to provide general medical information from its configured knowledge base.
It should not be used to:

Diagnose medical conditions

🔮 Future Improvements

Possible future improvements include:

👤 User authentication

💾 Persistent conversation history

🔊 Voice responses

🌐 Multilingual support

👩‍💻 Project

Project Name: MedAssist
Type: AI-powered Medical Chatbot
Architecture: Retrieval-Augmented Generation (RAG)
Built for learning and educational purposes using modern AI and web-development technologies.