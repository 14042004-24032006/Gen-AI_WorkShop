from chains import code_generator_chain

def main():
    task = input("Enter what you want to generate code for: ")
    response = code_generator_chain.invoke({"task": task})
    code_output = response.content.replace("```python", "").replace("```", "").strip()
    print("\nGenerated Code:\n")
    print(code_output)

if __name__ == "__main__":
    main()
