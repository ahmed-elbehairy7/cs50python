answer = (
    input(
        "What is the Answer to the Great Question Of Life, the Universe and Everything? "
    )
    .strip()
    .lower()
    .replace("-", " ")
)
match answer:
    case "42" | "forty two":
        print("Yes")
    case _:
        print("No")
