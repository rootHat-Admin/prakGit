# Example 5: check length of each word

text = input("Enter some words: ")  # str
words = text.split()  # list of str

for word in words:
    length = len(word)  # int
    is_long = length > 5  # bool

    if is_long:
        print(word, "- long word (", length, "letters )")
    else:
        print(word, "- short word (", length, "letters )")
