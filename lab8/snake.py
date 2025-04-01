import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20  # Размер ячейки сетки
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Скорость игры
speed = 10

# Класс Змеи
class Snake:
    def __init__(self):
        self.body = [[100, 100], [90, 100], [80, 100]]  # Начальное тело змеи
        self.direction = "RIGHT"  # Начальное направление
        self.change_to = self.direction  

    def move(self):
        """Обновляет положение змеи в зависимости от направления."""
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

        # Определяем новую голову
        head = self.body[0].copy()
        if self.direction == "UP":
            head[1] -= GRID_SIZE
        elif self.direction == "DOWN":
            head[1] += GRID_SIZE
        elif self.direction == "LEFT":
            head[0] -= GRID_SIZE
        elif self.direction == "RIGHT":
            head[0] += GRID_SIZE

        self.body.insert(0, head)  # Добавляем новую голову

        # Если не съела еду, удаляем хвост (иначе змейка растёт)
        if head == food.position:
            global SCORE, LEVEL, speed
            SCORE += 1
            food.new_position(self.body)  # Генерируем новую еду
            if SCORE % 3 == 0:  # Каждые 3 еды новый уровень
                LEVEL += 1
                speed += 2  # Увеличиваем скорость
        else:
            self.body.pop()  

    def check_collision(self):
        """Проверяет столкновение со стенами или самой собой."""
        head = self.body[0]
        if head in self.body[1:]:  # Столкновение с собой
            return True
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:  
            return True  # Столкновение со стеной
        return False

    def draw(self):
        """Рисует змею на экране."""
        for segment in self.body:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Класс Еды
class Food:
    def __init__(self):
        self.position = [random.randrange(0, SCREEN_WIDTH, GRID_SIZE), random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)]

    def new_position(self, snake_body):
        """Генерирует новую позицию для еды, избегая змеи."""
        while True:
            new_pos = [random.randrange(0, SCREEN_WIDTH, GRID_SIZE), random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)]
            if new_pos not in snake_body:  # Убедимся, что еда не появляется на змее
                self.position = new_pos
                break

    def draw(self):
        """Рисует еду на экране."""
        pygame.draw.rect(SCREEN, RED, pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Инициализация игры
snake = Snake()
food = Food()
SCORE = 0
LEVEL = 1
clock = pygame.time.Clock()

# Главный игровой цикл
running = True
while running:
    SCREEN.fill(BLACK)  # Заполняем экран цветом
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Закрытие игры
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_to = "UP"
            elif event.key == pygame.K_DOWN:
                snake.change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                snake.change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                snake.change_to = "RIGHT"

    snake.move()  # Двигаем змею

    if snake.check_collision():  # Проверка на столкновение
        running = False  # Завершаем игру

    snake.draw()
    food.draw()

    # Отображение счета и уровня
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))
    SCREEN.blit(level_text, (320, 10))

    pygame.display.flip()
    clock.tick(speed)  # Обновляем FPS

pygame.quit()