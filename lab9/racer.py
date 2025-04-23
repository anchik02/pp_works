import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # New variable for collected coins
COIN_THRESHOLD = 5  # Increase enemy speed every 5 coins collected

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
you_win = font.render("You Win", True, BLACK)

background = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab8/images/AnimatedStreet.png")
coin_image = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab8/images/Coin.png")  # Load coin image
coin_image = pygame.transform.scale(coin_image, (100,100))
pygame.mixer.Sound('c:/Users/Dell/Desktop/labki pp/pp_works/lab8/images/lab8_racer_images_background.wav').play()
 

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy Class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("c:/Users/Dell/Desktop/labki pp/pp_works/lab8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_image, (25, 25))  # Resize coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 300))

    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # Move coin down slower than enemy
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 300))

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_display = font_small.render(f"Coins: {COINS}", True, BLACK)  # Show collected coins
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins_display, (300, 10))  # Display coins in top right

    if SCORE >=10:
        DISPLAYSURF.fill(GREEN)
        DISPLAYSURF.blit(you_win, (30,250))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision check between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('c:/Users/Dell/Desktop/labki pp/pp_works/lab8/images/crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()     

    # Collision check between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += random.randint(1, 3)  # Increase collected coins
        if COINS % COIN_THRESHOLD == 0:  # Increase speed when reaching threshold
            SPEED += 1
        C1.rect.top = 0  # Move coin back to the top
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(50, 300))

    pygame.display.update()
    FramePerSec.tick(FPS)