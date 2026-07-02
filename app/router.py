def detect_intent(text):

    text = text.lower().strip()

    if text.startswith("bre "):
        text = text[4:]

    if text in ["gpu","vga"]:
        return "gpu"

    if text == "cpu":
        return "cpu"

    if text == "ram":
        return "ram"

    if text in ["kondisi","status","kondisi pc"]:
        return "system"

    return "chat"