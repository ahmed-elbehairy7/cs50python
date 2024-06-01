import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
        break
    except ValueError:
        continue

num = random.choice(range(1, level + 1))

while True:
    try:
        guess = int(input("guess: "))
        if guess < 1:
            raise ValueError
        if guess == num:
            print("Just right!")
            break
        if guess < num:
            print("Too small!")
            raise ValueError
        if guess > num:
            print("Too large!")
            raise ValueError
    except ValueError:
        continue
