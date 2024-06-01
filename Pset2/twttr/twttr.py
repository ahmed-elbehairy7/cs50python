vowels = ["a", "e", "i", "o", "u"]
text = input("Input: ")
for i in text:
    if i.lower() in vowels:
        text = text.replace(i, "")
print("Output:", text)
