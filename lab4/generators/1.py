#1
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2


N = 10
for square in square_generator(N):
    print(square)

#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(map(str, even_generator(n))))

#3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
print(list(divisible_by_3_and_4(n)))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Тестирование генератора
for num in squares(1, 5):
    print(num)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Тестирование генератора
for num in countdown(5):
    print(num)