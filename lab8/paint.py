import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Переменные состояния
drawing = False
tool = "pencil"  # pencil, rect, circle, eraser
color = BLACK
start_pos = None

# Добавлена поверхность canvas
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas.fill(WHITE)

# Основной цикл
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Определяем инструмент
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                tool = "pencil"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            
            # Выбор цвета
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

        # Начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos  # Запоминаем начальную позицию

        # Окончание рисования
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "rect":
                pygame.draw.rect(canvas, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
            
            elif tool == "circle":
                radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(canvas, color, center, radius, 2)

        # Непрерывное рисование (кисть и ластик)
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "pencil":
                pygame.draw.line(canvas, color, start_pos, event.pos, 2)
                start_pos = event.pos  # Обновляем позицию для плавности
            
            elif tool == "eraser":
                pygame.draw.circle(canvas, WHITE, event.pos, 10)  # Ластик рисует белым

    screen.blit(canvas, (0, 0))
    pygame.display.flip()

pygame.quit()