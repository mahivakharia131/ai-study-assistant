import streamlit as st
import pdfplumber
import io
from google import genai

st.title("📚 AI Study Assistant")
st.caption("Answers from your notes only — nothing else.")

api_key = st.text_input("Enter your Gemini API Key", type="password")

st.header("Step 1 — Upload Your Notes")
uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])

notes_text = ""
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
            notes_text = "\n\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    else:
        notes_text = uploaded_file.read().decode("utf-8", errors="ignore")
    st.success(f"✅ Notes loaded — {len(notes_text.split())} words")

st.header("Step 2 — Ask a Question")
question = st.text_input("Type your question here")
mode = st.radio("Answer style", ["Strict (facts only)", "Simple (plain English)", "Exam (structured)"], horizontal=True)

if st.button("Get Answer", type="primary"):
    if not api_key:
        st.warning("Please enter your Gemini API key above.")
    elif not notes_text:
        st.warning("Please upload your notes first.")
    elif not question.strip():
        st.warning("Please type a question.")
    else:
        mode_key = "strict" if "Strict" in mode else ("simple" if "Simple" in mode else "exam")
        prompts = {
            "strict": f"Answer ONLY using these notes. If not found, say exactly: Not found in notes\n\nNOTES:\n{notes_text}\n\nQuestion: {question}",
            "simple": f"Explain simply using ONLY these notes. If not found, say exactly: Not found in notes\n\nNOTES:\n{notes_text}\n\nQuestion: {question}",
            "exam": f"Write a structured exam answer using ONLY these notes. Format: one key sentence, then 2-3 bullet points. If not found, say exactly: Not found in notes\n\nNOTES:\n{notes_text}\n\nQuestion: {question}",
        }
        with st.spinner("Thinking..."):
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompts[mode_key]
            )
            answer = response.text.strip()
        st.header("Answer")
        if "not found in notes" in answer.lower():
            st.error("⚠️ Not found in notes.")
        else:
            st.success(answer)
