import pygame
import os
from random import randint

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 432, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption("My Flappy Bird")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'background-day.png')), (WIDTH, HEIGHT))
BASE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'base.png')), (WIDTH, HEIGHT / 10))

RED_BIRD = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'redbird-midflap.png')), (WIDTH / 7, HEIGHT / 15))
PIPE_BTM = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'pipe-red.png')), (WIDTH / 6, HEIGHT / 1.5))
PIPE_TOP = pygame.transform.rotate(PIPE_BTM, 180)

pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 2000)

# PIPES = []
def pipe_move(pipes):
    if pipes:
        for pipe_rect in pipes:
            pipe_rect.x -= 5
        pipes = [pipe for pipe in pipes if pipe.x > -100]
    return pipes

def draw_window(red, pipes):
    WIN.blit(BACKGROUND, (0, 0))

    for pipe_rect in pipes:
        WIN.blit(PIPE_BTM, pipe_rect)
        WIN.blit(PIPE_TOP, (pipe_rect.x, pipe_rect.y - 700))

    WIN.blit(RED_BIRD, (red.x, red.y))
    WIN.blit(BASE, (0, 700))

    pygame.display.update()

def main():

    red = RED_BIRD.get_rect(midleft = (0, HEIGHT / 2))
    clock = pygame.time.Clock()
    run = True

    velocity = 0
    gravity = 0.5
    jump = -10
    pipes = []

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    velocity = jump
            
            if event.type == pipe_timer:
                pipes.append(PIPE_BTM.get_rect(topleft = (432, randint(350, 450))))

        velocity += gravity
        red.y += velocity
        if (red.bottom > 700):
            red.bottom = 700
        elif (red.y < 0):
            red.y = 0

        pipes = pipe_move(pipes)
        draw_window(red, pipes)

if __name__ == "__main__": # ensures this file only runs when run directly
    main()





