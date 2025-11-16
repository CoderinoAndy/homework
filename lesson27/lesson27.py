# Lesson 27

def alpha_cleaner(text):
    cleaned = "" # initialized empty string
    for x in text:
        if x.isalpha():
            cleaned += x.lower()
    return cleaned

text = input("Text to clean: ")
print(f"Cleaned text: {alpha_cleaner(text)}")