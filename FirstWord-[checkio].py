

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """



    for x in text:
        if text.startswith(".") or text[0].isspace():
            text = text.lstrip(".")
            text = text.lstrip()


    var = 0

    while (var < len(text)):
        if text[var] == " ":
            text = text[0:var]
        else:
            var = var + 1

    text = text.rstrip(",")

    return text
