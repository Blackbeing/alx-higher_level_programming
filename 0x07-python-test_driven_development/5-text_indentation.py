#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints 2 newlines after . ? and :

    Args:
        text: str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = ""

    for idx, char in enumerate(text):
        if char in [".", "?", ":"]:
            sentence += char
            sentence += "\n"
            sentence.strip("")
            print(sentence.strip(" "))
            sentence = ""
        else:
            sentence += char

    if sentence:
        print(sentence.strip(), end="")
