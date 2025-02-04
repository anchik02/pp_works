from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

# Пример использования
s = input("Введите строку: ")
print_permutations(s)