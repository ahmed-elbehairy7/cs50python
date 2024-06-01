from sys import argv, exit

if len(argv) != 2 or not argv[1].endswith(".py"):
    exit("usage: python lines.py file.py")
line_count = 0
try:
    with open(argv[1]) as file:
        reader = file.readlines()
        for line in reader:
            if not line.strip().startswith("#") and not line.isspace():
                line_count += 1
except FileNotFoundError:
    exit("File not found")
print(line_count)
