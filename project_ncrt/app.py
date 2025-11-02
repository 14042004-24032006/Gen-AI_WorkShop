import streamlit as st
from chain import get_qa_chain

st.set_page_config(page_title="NCERT Chatbot", page_icon="📚", layout="wide")

st.title("📚 Multilingual NCERT Chatbot")
st.write("Ask your questions about NCERT syllabus in **any language** — English, தமிழ், हिंदी, etc.")

qa_chain = get_qa_chain()

# Chat memory (simple)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.text_input("Ask your question:")

if st.button("Ask"):
    if user_query:
        response = qa_chain.run(user_query)
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, text in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"🧑 **{speaker}:** {text}")
    else:
        st.markdown(f"🤖 **{speaker}:** {text}")
