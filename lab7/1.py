import pygame
from datetime import datetime  

pygame.init()
screen = pygame.display.set_mode((700, 525))

# Загружаем изображения
clock_img = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/images/clock.png")
clock_img = pygame.transform.scale(clock_img, (700, 525))

sec_img = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/images/leftarm.png")
sec_img = pygame.transform.scale(sec_img, (31, 525))

min_img = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/images/rightarm.png")
min_img = pygame.transform.scale(min_img, (700, 525))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.now()
    seconds = now.second
    minutes = now.minute
    sec_angle = -seconds * 6
    min_angle = -minutes * 6

    screen.fill((100, 100, 100))  
    screen.blit(clock_img, (0, 0))  
    

    # Вращаем стрелки и центрируем их
    rotated_sec = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = rotated_sec.get_rect(center=(350, 260))  
    screen.blit(rotated_sec, sec_rect.topleft)

    rotated_min = pygame.transform.rotate(min_img, min_angle)
    min_rect = rotated_min.get_rect(center=(350, 260))
    screen.blit(rotated_min, min_rect.topleft)
    
    pygame.display.update() 

pygame.quit()