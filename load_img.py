import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprytes = pygame.sprite.Group()
cur_im = load_image('dog.png')
cur = pygame.sprite.Sprite(all_sprytes)
cur.image = cur_im
cur.rect = cur.image.get_rect()
pygame.mouse.set_visible(False)
running = True
while running:
    screen.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cur.rect.topleft = event.pos
    if pygame.mouse.get_focused():
        all_sprytes.draw(screen)

    pygame.display.flip()
    clock.tick(100)
pygame.quit()