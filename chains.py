from prompt import prompt_template
from models import model

# Build the final chain
code_generator_chain = prompt_template | model
