import Pygame_Plus as pg_plus
import pygame

width, height = 900, 900

snake = [pg_plus.Kvadrat(20, 20, 20, 20, 5, pg_plus.color.pink)]


pygame.init()
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




pygame.quit()