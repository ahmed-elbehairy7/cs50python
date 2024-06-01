import random

levelquide = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]

def main():
    # Get level and generate problems
    level = get_level()
    problems = generate_integer(level)

    # Initiate score
    score = 0
    for problem in problems:
        right_answer = int(problem[0]) + int(problem[1])

        wrongs = 0
        while True:
            try:
                user_answer = int(input(f"{problem[0]} + {problem[1]} = "))
                if not user_answer == right_answer:
                    if wrongs < 3:
                        raise ValueError
                    else:
                        print(f"{problem[0]} + {problem[1]} = {right_answer}")
                score += 1
                break
            except ValueError:
                print("EEE")
                wrongs += 1
                continue

    print(f"Score: {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if not level in levels:
                raise ValueError
            return level
        except ValueError:
            continue
        

def generate_integer(level):
    probs = []
    while len(probs) < 10:
        # x = [
        #     random.choice(range(10 ** (level - 1), 10**level)),
        #     random.choice(range(10 ** (level - 1), 10**level)),
        # ]
        # x = [
        #     random.choice(range((level - 1) * 10, 10*level)),
        #     random.choice(range((level - 1) * 10, 10*level)),
        # ]
        # x = [
        #     round(random.uniform(10 ** (level - 1), 10 ** level)),
        #     round(random.uniform(10 ** (level - 1), 10 ** level)),
        # ]
        # x = [
        #     random.randrange(10 ** (level - 1), 10**level),
        #     random.randrange(10 ** (level - 1), 10**level),
        # ]
        x = [
            random.randint(10 ** (level - 1), 10**level),
            random.randint(10 ** (level - 1), 10**level),
        ]
        if not x in probs:
            probs.append(x)
    return probs


if __name__ == "__main__":
    main()
