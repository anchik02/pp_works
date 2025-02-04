import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Пример использования
radius = float(input("Введите радиус сферы: "))
print(f"Объём сферы: {sphere_volume(radius)}")