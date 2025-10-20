# Lesson 27

def alpha_cleaner(text):
    cleaned = ""
    for x in text:
        if not x.isalpha() and x != " ":
            cleaned += x
    return cleaned

text = input("Text to clean: ")
print(f"Cleaned text: {alpha_cleaner(text)}")