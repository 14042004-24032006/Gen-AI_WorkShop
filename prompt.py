from langchain_core.prompts import ChatPromptTemplate

system_msg = """
You are an expert Python code generator.
Generate ONLY raw Python code — no markdown, no explanations, no comments.
Respond strictly with runnable Python code.
If the user asks something non-coding-related, reply with:
"I am a code generator assistant. Please ask me a coding-related query."
"""

user_msg = "Write a Python program to {task}"

# Create prompt template
prompt_template = ChatPromptTemplate([
    ("system", system_msg),
    ("user", user_msg)
])
