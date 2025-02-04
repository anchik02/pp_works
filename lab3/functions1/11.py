def is_palindrome(s):
    # Убираем пробелы и приводим строку к нижнему регистру
    s = s.replace(" ", "").lower()
    # Сравниваем строку с её обратной версией
    return s == s[::-1]

# Пример использования
word_or_phrase = input("Введите слово или фразу: ")
if is_palindrome(word_or_phrase):
    print("Это палиндром!")
else:
    print("Это не палиндром.")