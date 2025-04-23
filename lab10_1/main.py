import pygame
import sys
import random
from db import get_or_create_user, save_score

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS_BASE = 10

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

username = input("Enter your username: ")
user_id = get_or_create_user(username)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with DB")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

snake = [(100, 100), (80, 100), (60, 100)]
direction = (BLOCK_SIZE, 0)
food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
score = 0
level = 1

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

def show_text(text, x, y):
    surface = font.render(text, True, BLACK)
    screen.blit(surface, (x, y))

def pause_game():
    save_score(user_id, score, level)
    paused = True
    show_text("Game Paused. Press R to resume.", 100, HEIGHT // 2)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                paused = False

running = True
while running:
    clock.tick(FPS_BASE + level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, score, level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)
            elif event.key == pygame.K_p:
                pause_game()

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake = [new_head] + snake[:-1]

    if new_head == food:
        snake.append(snake[-1])
        score += 10
        if score % 30 == 0:
            level += 1
        food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    if (new_head in snake[1:] or
        not (0 <= new_head[0] < WIDTH) or
        not (0 <= new_head[1] < HEIGHT)):
        save_score(user_id, score, level)
        running = False

    screen.fill(WHITE)
    draw_snake()
    draw_food()
    show_text(f"Score: {score}", 10, 10)
    show_text(f"Level: {level}", 10, 40)
    pygame.display.update()

pygame.quit()