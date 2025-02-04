def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [10, 15, 3, 7, 20, 17, 19, 22, 5]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)  # [3, 7, 17, 19, 5]