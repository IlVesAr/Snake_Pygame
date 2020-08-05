import Pygame_Plus as pg_plus
import pygame
import random

width, height = 920, 920

snake = [pg_plus.Kvadrat(0, 0, 40, 40, 0, 40, pg_plus.color.purple)]
apple = pg_plus.Krag(450, 450, 10, 0, 0, pg_plus.color.red)
posoki = ["right"]

pygame.init()

izqdena = True


def Move():
    global posoki
    global snake

    x = 0
    while x < len(posoki):
        if snake[x].x > width:
            snake[x].x = -40
        if snake[x].y > height:
            snake[x].y = -40
        if snake[x].x < -40:
            snake[x].x = width
        if snake[x].y < -40:
            snake[x].y = height

        if posoki[x] == "left":
            snake[x].x -= snake[x].vel
        if posoki[x] == "right":
            snake[x].x += snake[x].vel
        if posoki[x] == "up":
            snake[x].y -= snake[x].vel
        if posoki[x] == "down":
            snake[x].y += snake[x].vel
        x += 1



def DrAw(win):
    win.fill(pg_plus.color.black)
    apple.draw(win)
    for i in snake:
        i.draw(win)
    pygame.display.flip()


win = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(9)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Move()

    if snake[0].x <= apple.x <= (snake[0].x + snake[0].w) and snake[0].y <= apple.y <= (snake[0].y + snake[0].h):
        apple.x = (random.randrange(40, width) // 40) * 40 - 20
        apple.y = (random.randrange(40, width) // 40) * 40 - 20
        if posoki[len(posoki) - 1] == "left":
            snake.append(pg_plus.Kvadrat((snake[len(snake) - 1].x + snake[0].w), snake[len(snake) - 1].y, snake[0].w, snake[0].h, snake[0].width, snake[0].vel, snake[0].color))
        if posoki[len(posoki) - 1] == "right":
            snake.append(pg_plus.Kvadrat((snake[len(snake) - 1].x - snake[0].w), snake[len(snake) - 1].y, snake[0].w, snake[0].h, snake[0].width, snake[0].vel, snake[0].color))
        if posoki[len(posoki) - 1] == "up":
            snake.append(pg_plus.Kvadrat(snake[len(snake) - 1].x, (snake[len(snake) - 1].y + snake[0].h), snake[0].w, snake[0].h, snake[0].width, snake[0].vel, snake[0].color))
        if posoki[len(posoki) - 1] == "down":
            snake.append(pg_plus.Kvadrat(snake[len(snake) - 1].x, (snake[len(snake) - 1].y - snake[0].h), snake[0].w, snake[0].h, snake[0].width, snake[0].vel, snake[0].color))

        posoki.append(posoki[len(posoki) - 1])

    i = len(posoki) - 1
    while i >= 1:
        posoki[i] = posoki[i - 1]
        i -= 1

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and posoki[0] != "right":
        posoki[0] = "left"
    if key[pygame.K_RIGHT] and posoki[0] != "left":
        posoki[0] = "right"
    if key[pygame.K_UP] and posoki[0] != "down":
        posoki[0] = "up"
    if key[pygame.K_DOWN] and posoki[0] != "up":
        posoki[0] = "down"

    m = 1
    while m < len(snake):
        if snake[0].x == snake[m].x and snake[0].y == snake[m].y:
            run = False
        m += 1

    DrAw(win)

pygame.quit()