def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

# Пример использования
s = input("Введите строку: ")
print(reverse_words(s))