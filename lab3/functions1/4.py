def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# Пример использования
numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(filter_prime(numbers))
