while True:
    text = input("> ")
    if text.startswith("EXIT"):
        break
    elif text.startswith("LOG: "):
        print(text[4:])