# 📚 Multi-PDF Chatbot

An AI-powered chatbot built with **Streamlit, LangChain, FAISS, and Together AI** that allows users to upload **multiple PDF files** and ask intelligent questions from them in real-time.

---

## 🚀 Features

- ✅ Upload **multiple PDFs at once**
- ✅ Extract text using **PyPDF**
- ✅ Smart text chunking with **LangChain**
- ✅ High-quality embeddings using **MiniLM**
- ✅ Fast vector search with **FAISS**
- ✅ AI answers powered by **Together AI (Mixtral Model)**
- ✅ Clean and simple **Streamlit UI**
- ✅ Real-time question answering

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **FAISS**
- **Together AI**
- **Sentence Transformers**
- **PyPDF**
- **dotenv**

---

## 📂 Project Structure

multi_pdf_chatbot/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DiyaPithva/multi_pdf_chatbot.git
cd multi_pdf_chatbot

2️⃣ Install Required Dependencies
pip install -r requirements.txt

3️⃣ Setup Environment Variables

Create a .env file in the project root and add your Together AI API key:

TOGETHER_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app.py


Then open your browser and go to:

http://localhost:8501
