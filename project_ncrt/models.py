import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set Google API Key
os.environ["GOOGLE_API_KEY"]="AIzaSyDTfCxG7H2mMnvJ7Gvnr0ljf-UB-JGXJGk"

# Gemini model with multilingual understanding
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
)
