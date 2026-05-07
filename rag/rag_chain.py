from langchain_google_genai import ChatGoogleGenerativeAI

def generate_answer(question, docs, api_key):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key
    )

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer ONLY from the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content
