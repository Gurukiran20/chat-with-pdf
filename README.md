#  Chat with PDF — FastAPI + Gemini + Vanilla JS

A production-style **Chat with PDF** application that lets you upload any PDF and ask natural language questions.  
Built using **FastAPI**, **Gemini 2.5 Flash**, and a clean **HTML/CSS/JavaScript** frontend.  

This project follows a modern, startup-grade folder structure with separation of API routes, services, and components.

---

## 🚀 Features

- 📤 Upload any PDF directly from the frontend  
- 🔍 Extract & chunk PDF text  
- 🧠 Convert chunks into embeddings using **Gemini embeddings**  
- 🔎 Perform semantic similarity search (RAG)  
- 💬 Ask questions grounded in the uploaded PDF  
- ⚡ Lightweight frontend (no React, no frameworks)  
- 🗂️ Clean, industry-level folder structure  

---

## 📌 App Screenshot

> <img width="1869" height="961" alt="Screenshot 2025-12-01 231914" src="https://github.com/user-attachments/assets/90ca462d-458b-4782-811c-7ca4412256c7" />


---
## Project structure 


<img width="850" height="557" alt="image" src="https://github.com/user-attachments/assets/75a84a90-e459-4c3d-9a2f-d98d647c874e" />

---

###Start backend: uvicorn app.main:app --reload,  it will runs at (http://127.0.0.1:8000) 

###Frontend: cd frontend/public, http://127.0.0.1:5500 (through live server) 

---

## 🧰 Tech Stack

| Backend:  used FastAPI 
| Frontend | HTML, CSS, JS (no frameworks used because Fast, minimal) 
| LLM:  Gemini 2.5 Flash API key is used
| Embeddings: Gemini Embeddings API 
| PDF Parsing: PyPDF2 
| Vector Store: NumPy cosine similarity 

<img width="938" height="286" alt="image" src="https://github.com/user-attachments/assets/e51ab484-1c50-42f7-8327-ea99bf6f3e77" />

---
## Install & Run


1. Backend (FastAPI)

cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload


