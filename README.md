# 📚 AI Study Assistant

> **One-line description:** Upload your notes, ask questions, and get answers strictly from your own content.

---

## 🧩 Problem Statement

Students often have large amounts of notes but waste time searching manually before exams.
This project helps students instantly find answers by asking questions directly from their own notes using AI.

---

## ✨ Features

* Upload notes (`.txt` or `.pdf`)
* Ask questions based on uploaded content
* 3 answer styles: Strict / Simple / Exam
* Returns **"Not found in notes"** if answer is missing
* Minimizes hallucination by restricting answers to provided notes

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API (`gemini-2.5-flash`)
* google-genai SDK
* pdfplumber

---

## ⚙️ How It Works

1. Upload notes file
2. App extracts text
3. User enters question
4. AI receives notes + question + prompt
5. AI generates answer strictly from notes
6. Output displayed

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

## 📸 Screenshots
(Included in the folder)

![alt text](<Screenshot 2026-05-04 003618-1.png>) 
![alt text](<Screenshot 2026-05-04 003709-1.png>) 
![alt text](<Screenshot 2026-05-04 003825-1.png>)

---

## ▶️ Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
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
