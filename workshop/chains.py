from workshop.prompt import prompt_template
from workshop.models import model

# Build the final chain
code_generator_chain = prompt_template | model
