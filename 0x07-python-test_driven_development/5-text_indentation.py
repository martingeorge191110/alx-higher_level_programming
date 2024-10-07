#!/usr/bin/python3

def text_indentation(text):
    """Function that prints text

    Args:
       text (str): text to be printed

    Raises:
       TypeError: if the text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    length = len(text)
    i = 0
    while i < length:
        if text[i] != ' ':
            print(text[i], end="")
            if text[i] in ['.', '?', ':']:
                print("\n\n", end="")
                i += 1
                while i < length and text[i] == "":
                    i += 1
                continue
        else:
            if i > 0 and text[i - 1] not in (".", "?", ":"):
                print(text[i], end="")
        i += 1
