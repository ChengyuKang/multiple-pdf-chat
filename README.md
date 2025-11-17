# multiple-pdf-chat

<img width="2546" height="1348" alt="image" src="https://github.com/user-attachments/assets/372c2403-0c40-40f3-9f52-8e92972a624f" />

## 📄 Multiple PDF Chat (Local Only)

A local PDF chat application built with Streamlit + LangChain + OpenAI APIs (or compatible providers).
It allows you to upload multiple PDF files and chat with their content using retrieval-based question answering.

✔ Runs fully locally  
✔ .env is used for secrets and not uploaded to GitHub  
✔ Simple, lightweight, and easy to extend  

## ✨ Features

Upload and process multiple PDF files

Extract text and split into chunks automatically

Build embeddings + vector store (FAISS / Chroma)

Chat with your PDFs using LangChain retrieval chains

OpenAI or drop-in compatible models supported

Fully local execution (no deployment required)

## 🧰 Installation
1. Clone the repository
git clone https://github.com/your-username/multiple-pdf-chat.git
cd multiple-pdf-chat

2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

## 🔑 Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


⚠️ .env is already added to .gitignore, so it will not be pushed to GitHub.

## ▶️ Run the App
streamlit run app.py


Then open:

http://localhost:8501

## 📦 Dependencies

Key libraries used:

streamlit

PyPDF2

langchain

langchain-openai

python-dotenv

faiss-cpu (or Chroma)

tiktoken

All dependencies are included in requirements.txt.

🗂 Project Structure
multiple-pdf-chat/  
│── app.py  
│── requirements.txt  
│── .env              # local only, not committed  
│── .gitignore  
└── README.md
