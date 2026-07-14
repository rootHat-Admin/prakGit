# Python: Lists & Strings

text = " Python - is great!"

print(text.upper())
clear_text = text.strip()

print(clear_text)

new_text = text.replace("cool", "convenient")
print(new_text)

words = text.split()
print(words)

words_list = ["python", "Java", "C++"]
joined_text = ", ".join(words_list)
print(words_list)
print(joined_text)
index = text.find("This")
print(index)
is_python = text.strip().startswith("Python")
print(is_python)