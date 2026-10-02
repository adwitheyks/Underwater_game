import pygame

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class submarine:
    def __init__(self):
        self.submarine_img = pygame.transform.scale(pygame.image.load("Submarine.png"), (200,200))
        self.submarine = self.submarine_img.get_rect()
        self.speed = 5


    def move_down(self):
        self.submarine.y += self.speed

    def move_up(self):
        self.submarine.y -= self.speed

    def draw(self):
        screen.blit(self.submarine_img, (400,400))

class fish:
    def __init__(self):
        self.dolphin_img = pygame.transform.scale(pygame.image.load("Dolphin.png"), (150,150))
        self.dolphin = self.dolphin_img.get_rect()

    def draw(self):
        screen.blit(self.dolphin_img, (100,500))
            

class game:
    def __init__(self):
        self.font = pygame.font.Font(None, 50)
        self.player = submarine()
        self.fish = fish()

    def draw(self):
        self.bg = pygame.transform.scale(pygame.image.load("Water_img1.webp"), (800,800))
        screen.blit(self.bg, (0,0))
        self.player.draw()
        self.fish.draw()
        

        pygame.display.flip()


Game = game()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Game.draw()



    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        Game.player.submarine.y += Game.player.speed
        

