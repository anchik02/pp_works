#1
import re

# with open("input.txt", "r", encoding="utf-8") as file:
#     for i in range(len(file.readlines())):
#         if re.search(r"аб*", file.readline()):
#             print("FOUND!")
#         else:
#             print("NOT FOUND")

text = "abbbb ak ab erg"
matches = re.findall(r"ab+", text)
print(matches)
# if re.search(r"ab*", text):
#     print("FOUND")
# else:
#     print("NOT FOUND")

#2
import re

text = "abbbb ak abbb ab abb erg asd asd"
matches = re.findall(r"\bab{2,3}\b", text)
print(matches)

#3
import re

def get(text):
    matches = re.findall(r"[a-z]+_[a-z]+$", text)
    if len(matches) > 0:
        print(matches)
    else:
        print("not matches")

get("avada_kedavra")
get("bratan")
get("bro_SAMTYBRO")
get("ok_ko")

#4
import re

def get(text):
    matches = re.findall(r"[A-Z]+[a-z]+$", text)
    if len(matches) > 0:
        print(matches)
    else:
        print("not matches")

get("aVadakedavra")
get("Bratan")
get("Bro_SAMTYBRO")

#5
import re

def get(text):
    matches = re.findall(r"a.*?b$", text)
    if len(matches) > 0:
        print(matches)
    else:
        print("not matches")

get("aVadakedavra")
get("Brotanb")
get("Brao_SAMTYBROb")

#6
import re

def get(text):
    matches = re.sub(r"[ ,.]", ":", text)
    print(matches)

get("Hello world!,Bratan.")

#7
import re


def get(text):
    matches = re.sub(r"_([a-z])", lambda l:l.group(1).upper(), text)
    print(matches)


get("i_am_your_king!") 
#8
import re


def get(text):
    print(re.split(r"(?=[A-Z])", text))


get("iAmYourKing") 

#9
import re


def get(text):
    print(re.sub(r"([a-z])([A-Z])", r"\1 \2", text))


get("iAmYourKing")  

#10
import re


def get(text):
    matches = re.sub(r"([a-z])([A-Z])", r"\1_\2" , text)
    print(matches.lower())


get("iAmYourKing!")  