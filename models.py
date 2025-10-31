import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAcL9CUkmjPCeWtLoG60sQ4m2Qmd4j2fAU"

# Configure Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
