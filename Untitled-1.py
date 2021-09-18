from pygame import *
import pygame
import sys
pygame.font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (70, 70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_TAB]: 
            self.rect.y -= self.speed
        if keys[K_DELETE]: 
            self.rect.y += self.speed
        if keys[K_RIGHT]: 
            self.rect.x += self.speed
        if keys[K_BACKSPACE]: 
            self.rect.x -= self.speed

window = display.set_mode((700, 500))
display.set_caption('Dich kakaya eto')
background = transform.scale(image.load('background.jpg'), (700, 500))

player = Player('hero.png', 10, 10, 5)

game = True
finish = False
clock = time.Clock()
fps = 60
IsGame = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if IsGame:
        window.blit(background, (0, 0))
        if finish == False:
            player.update()
            player.reset()

    display.update()
    clock.tick(fps)