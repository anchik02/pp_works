import re


def get(text):
    matches = re.sub(r"([a-z])([A-Z])", r"\1_\2" , text)
    print(matches.lower())


get("iAmYourKing!")  