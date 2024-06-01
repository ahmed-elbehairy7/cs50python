from cs50 import get_int

own = 50
while own > 0:
    while True:
        print(f"Amount Due: {own}")
        coins = get_int("Insert coin: ")
        if coins / 25 == 1 or coins / 10 == 1 or coins / 5 == 1:
            own -= coins
            break
print("Change Owed:", -own)
