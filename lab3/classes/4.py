import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Пример использования
p1 = Point(3, 4)
p2 = Point(0, 0)

p1.show()  # (3, 4)
p2.show()  # (0, 0)

p1.move(6, 8)
p1.show()  # (6, 8)

print(p1.dist(p2))  # 10.0