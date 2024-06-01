file = input("File name: ").strip().lower()

match file:
    case s if s.endswith(".jpg") | s.endswith(".jpeg"):
        print("image/jpeg")
    case s if s.endswith(".gif"):
        print("image/gif")
    case s if s.endswith(".png"):
        print("image/png")
    case s if s.endswith(".pdf"):
        print("application/pdf")
    case s if s.endswith(".txt"):
        print("text/plain")
    case s if s.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")
