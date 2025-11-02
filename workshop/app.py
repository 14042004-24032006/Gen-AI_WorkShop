
from chains import code_generator_chain
# import streamlit as st


# def main():
#     task = input("Enter what you want to generate code for: ")
#     response = code_generator_chain.invoke({"task": task})
#     code_output = response.content.replace("```python", "").replace("```", "").strip()
#     print("\nGenerated Code:\n")
#     print(code_output)

# def poem_generator_app():
#     st.sidebar.title("Poem Generator")

#     section = st.sidebar.radio(
#         "Select Mode",
#         ["Generate with RAG", "Generate with Default Model"]
#     )

#     if section == "Generate with RAG":
#         st.title("Let's Generate a Poem with RAG!")
#         with st.form("PoemGenerator"):
#             topic = st.text_input("Enter a topic for the poem:")
#             submitted = st.form_submit_button("Generate Poem")

#             if submitted and topic:
#                 response = code_generator_chain.invoke({"task": f"write a short poem about {topic}"})
#                 poem = response.content.strip()
#                 st.write(f"### Generated Poem about '{topic}':")
#                 st.write(poem)

#     elif section == "Generate with Default Model":
#         st.title("Generate Poem (Default Model)")
#         with st.form("PoemGeneratorDefault"):
#             topic = st.text_input("Enter a topic for the poem:")
#             submitted = st.form_submit_button("Generate Poem")

#             if submitted and topic:
#                 st.write(f"### Generated Poem about '{topic}':")
#                 st.write(
#                     f"The winds whisper softly,\nOf tales untold,\nA poem of {topic},\nIn verses bold. ✨"
#                 )

# if __name__ == "__main__":
#     poem_generator_app()

from workshop.chains import code_generator_chain
import streamlit as st
import re

def split_questions(user_input):
    """
    Splits the user's input into multiple questions based on conjunctions or punctuation.
    """
    # Split by 'and', '?', or '.' while keeping meaningful parts
    parts = re.split(r'\band\b|[?.]', user_input, flags=re.IGNORECASE)
    # Clean and remove empty strings
    questions = [p.strip() for p in parts if p.strip()]
    return questions


def multi_question_app():
    st.title("🤖 Smart Code/Question Handler")

    user_input = st.text_area("Enter your question(s):", placeholder="e.g. write code for factorial and explain recursion")
    submit = st.button("Generate Answer")

    if submit and user_input:
        questions = split_questions(user_input)

        if len(questions) > 1:
            st.info(f"🔍 Detected {len(questions)} separate questions.")
        else:
            st.info("💡 Single question detected.")

        for i, q in enumerate(questions, start=1):
            st.markdown(f"### 🧩 Question {i}: {q}")
            response = code_generator_chain.invoke({"task": q})
            answer = response.content.strip()
            st.markdown(f"**Answer {i}:**")
            st.write(answer)


if __name__ == "__main__":
    multi_question_app()

