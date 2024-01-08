import pygame
import os
from start_end import before
import random
pygame.init()

# НЕ ИЗМЕНЯТЬ
clock = pygame.time.Clock()
height = 600
width = 1100
screen = pygame.display.set_mode((width, height))
dog_x = 50
dog_y = 450
dog_image = pygame.image.load(os.path.join('images', "dog.png"))
obsticle = pygame.image.load(os.path.join('images', 'box.png'))


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
running = True
before()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dog_y -= 0.5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dog_y += 0.1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dog_x -= 0.1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dog_x += 0.1
    screen.fill(pygame.Color('white'))
    screen.blit(dog_image, (dog_x, dog_y))
    pygame.draw.rect(screen, pygame.Color('black'), (10, 10, 50, 50))
    #dog_images.draw(screen)
    pygame.display.flip()

pygame.quit()
