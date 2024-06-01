camel = input("camelCase: ")
snake = ""
for letter in camel:
    if letter.isupper():
        snake += f"_{letter.lower()}"
        continue
    snake += letter
print("snake_case: ", snake)
