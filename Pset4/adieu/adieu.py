from sys import exit

names = []
while True:
    try:
        text = input()
        names.append(text)
    except EOFError:
        break


print(f"Adieu, adieu, to {names[0]}", end="")

if len(names) == 1:
    print()
    exit()

if len(names) == 2:
    print(" and", names[-1])
    exit()

for name in names[1:-1]:
    print(f", {name}", end="")
print(", and", names[-1])
