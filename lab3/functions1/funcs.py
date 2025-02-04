# functions.py

import random
import math

# Функция для проверки палиндрома
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Функция для вывода гистограммы
def histogram(lst):
    for value in lst:
        print('*' * value)

# Функция для вычисления объёма сферы
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Функция для поиска уникальных элементов в списке
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Функция для игры "Guess the number"
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break