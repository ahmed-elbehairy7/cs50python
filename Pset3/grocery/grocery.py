grocery = {}

while True:
    try:
        item = input().strip().upper()
        grocery[item] = grocery.get(item, 0) + 1
    except EOFError:
        break
for item in sorted(grocery):
    print(grocery[item], item)
