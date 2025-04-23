import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))

vinyl = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/images/vinyl.jpeg")
vinyl = pygame.transform.scale(vinyl, (300, 300))

# Загружаем песни
playlist = [
    pygame.mixer.Sound("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/music/beabadoobee - the perfect pair.mp3"),
    pygame.mixer.Sound("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/music/Empire Of The Sun - We Are The People.mp3"),
    pygame.mixer.Sound("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/music/Kendrick Lamar - Not Like Us.mp3"),
    pygame.mixer.Sound("c:/Users/Dell/Desktop/labki pp/pp_works/lab7/music/Kiss.mp3")
]

current_song = 0  
playing = False

running = True
while running:
    pygame.mixer_music.set_volume = 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and not playing:  
        playlist[current_song].play()
        playing = True
    
    if keys[pygame.K_e]:  
        playlist[current_song].stop()
        playing = False
    
    if keys[pygame.K_r]:  
        if playing:
            playlist[current_song].stop()
        if current_song < len(playlist) - 1:
            current_song += 1
        else:
            current_song = 0  
        playlist[current_song].play()
        playing = True
    
    if keys[pygame.K_q]:  
        if playing:
            playlist[current_song].stop()
        if current_song > 0:
            current_song -= 1
        else:
            current_song = len(playlist) - 1  
        playlist[current_song].play()
        playing = True
    
    screen.blit(vinyl, (0, 0))
    pygame.display.update()
    
pygame.quit()