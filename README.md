


# 📚 RAG-Based AI Study Assistant

One-line description: Upload your notes, ask questions, and get AI-generated answers strictly from your own content using Retrieval Augmented Generation (RAG).

---

# 🧩 Problem Statement

Students often have large amounts of notes but waste time searching manually before exams. This project helps students instantly find answers directly from their own notes using AI-powered Retrieval Augmented Generation (RAG).

The system retrieves only the most relevant sections from uploaded notes before generating answers, improving accuracy and reducing hallucinations.

---

# ✨ Features

- Upload notes (`.txt` or `.pdf`)
- Ask questions based on uploaded content
- 3 answer styles:
  - Strict
  - Simple
  - Exam
- Uses ChromaDB vector database for retrieval
- Retrieves only relevant note sections before answering
- Returns `"Not found in notes"` if answer is missing
- Minimizes hallucination by restricting answers to uploaded notes
- Clean and simple Streamlit interface

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API (`gemini-2.5-flash`)
- google-genai SDK
- LangChain
- ChromaDB
- HuggingFace Embeddings
- pdfplumber
- sentence-transformers

---

# ⚙️ How The RAG System Works

## Step 1 — Upload Notes

User uploads PDF or TXT notes.

---

## Step 2 — Text Extraction

The application extracts text from uploaded files.

---

## Step 3 — Chunking

Large notes are split into smaller chunks using LangChain text splitters.

---

## Step 4 — Embedding Generation

Embeddings are generated using HuggingFace sentence transformer models.

---

## Step 5 — Vector Storage

Embeddings are stored in ChromaDB vector database.

---

## Step 6 — Retrieval

When user asks a question, the system retrieves the most relevant note chunks.

---

## Step 7 — AI Generation

Gemini AI generates answers using ONLY the retrieved context.

---

## Step 8 — Output

The answer is displayed in the Streamlit interface.

---

# 🧠 RAG Architecture

```text
User Uploads Notes
        ↓
Text Extraction
        ↓
Chunking
        ↓
Embeddings Generation
        ↓
ChromaDB Vector Storage
        ↓
Relevant Chunk Retrieval
        ↓
Gemini AI Generation
        ↓
Final Answer



---

## ⚡ Quick Demo
1. Upload notes file
2. Ask: **"What is photosynthesis?"**
3. Get answer OR **"Not found in notes"**

---

## 🤖 Prompts Used

### 1. Strict Prompt

Ensures answers come only from notes.

```
Answer ONLY using these notes.
If not found, say exactly: Not found in notes
```

---

### 2. Simple Prompt

Explains in easy language.

```
Explain simply using ONLY these notes.
If not found, say exactly: Not found in notes
```

---

### 3. Exam Prompt

Structured answer format.

```
Write a structured exam answer using ONLY these notes.
Format: one sentence + bullet points.
If not found, say exactly: Not found in notes
```

---
## ▶️ Quick Start

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 📊 Sample Input / Output

**Input:** What is photosynthesis?
**Output:** Photosynthesis is the process by which plants convert sunlight into energy

**Input:** What is chlorophyll?
**Output:** Chlorophyll is the pigment that absorbs light

**Input:** What is hashing?
**Output:** Not found in notes

---

## 🔮 Future Improvements

* Multiple file upload
* Chat history
* Highlight answers in notes
* Quiz generation

---

## 💡 Lessons Learned

* Prompt design is critical for accuracy
* Simpler projects are more reliable
* Avoid overengineering in hackathons
* Retrieval improves relevance and reduces hallucination

---

## 🧠 Why This Project Stands Out

* Solves a real student problem
* Focuses on accuracy over complexity
* Uses prompt engineering effectively
* Fast and easy to use

---

## 👤 Author

Mahi Vakharia
ALTA AI Builders Fellowship
