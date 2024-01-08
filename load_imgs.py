import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprytes = pygame.sprite.Group()
dog_img = load_image('dog.png')
cur = pygame.sprite.Sprite(all_sprytes)
cur.image = dog_img
cur.dog = cur.image.get_rect()


running = True
while running:
    screen.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    else:
        all_sprytes.draw(screen)

    pygame.display.flip()
    clock.tick(100)
pygame.quit()