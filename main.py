def clean_prompt(text):
    text = " ".join(text.split())

    return f"""
Role: Professional Assistant

Task:
{text}

Requirements:
- Clear structure
- Professional tone
- Practical examples
"""

if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    result = clean_prompt(prompt)
    print(result)
