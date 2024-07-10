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

RED_BIRD_DOWNFLAP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'redbird-downflap.png')), (WIDTH / 7, HEIGHT / 15))
RED_BIRD_MIDFLAP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'redbird-midflap.png')), (WIDTH / 7, HEIGHT / 15))
RED_BIRD_UPFLAP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'redbird-upflap.png')), (WIDTH / 7, HEIGHT / 15))
RED_BIRD_FLAPS = [RED_BIRD_DOWNFLAP, RED_BIRD_MIDFLAP, RED_BIRD_UPFLAP]
RED_BIRD_INDEX = 0
RED_BIRD_SURF = RED_BIRD_FLAPS[RED_BIRD_INDEX]
RED_BIRD_RECT = RED_BIRD_SURF.get_rect(midleft=(32, HEIGHT / 2))

PIPE_BTM = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', 'pipe-red.png')), (WIDTH / 6, HEIGHT / 1.5))
PIPE_TOP = pygame.transform.rotate(PIPE_BTM, 180)

pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 2000)

def collisions(red_bird, pipes_btm, pipes_top):
    for pipe_rect in pipes_btm:
        if red_bird.colliderect(pipe_rect):
            return False
    for pipe_rect in pipes_top:
        if red_bird.colliderect(pipe_rect):
            return False
    return True

def bird_animation():
    global RED_BIRD_SURF, RED_BIRD_INDEX

    RED_BIRD_INDEX += 0.1
    if RED_BIRD_INDEX >= len(RED_BIRD_FLAPS): RED_BIRD_INDEX = 0
    RED_BIRD_SURF = RED_BIRD_FLAPS[int(RED_BIRD_INDEX)]

def pipe_move(pipes_btm, pipes_top):
    if pipes_btm:
        for pipe_rect in pipes_btm:
            pipe_rect.x -= 5
        pipes_btm = [pipe for pipe in pipes_btm if pipe.x > -100]
    if pipes_top:
        for pipe_rect in pipes_top:
            pipe_rect.x -= 5
        pipes_top = [pipe for pipe in pipes_top if pipe.x > -100]
    return pipes_btm, pipes_top

def draw_window(red, pipes_btm, pipes_top):
    WIN.blit(BACKGROUND, (0, 0))

    for pipe_rect in pipes_btm:
        WIN.blit(PIPE_BTM, pipe_rect)
    for pipe_rect in pipes_top:
        WIN.blit(PIPE_TOP, pipe_rect)

    WIN.blit(RED_BIRD_SURF, (red.x, red.y))
    WIN.blit(BASE, (0, 700))

    pygame.display.update()

def shifted_pipes(pipes_btm):
    pipes_top = []
    for pipe_rect in pipes_btm:
        shifted_rect = pipe_rect.copy()
        shifted_rect.y -= 700
        pipes_top.append(shifted_rect)
    return pipes_top

def main():
    clock = pygame.time.Clock()
    run = True

    velocity = 0
    gravity = 0.5
    jump = -10
    pipes_btm = []
    pipes_top = []

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
                pipes_btm.append(PIPE_BTM.get_rect(topleft=(432, randint(350, 450))))
                pipes_top = shifted_pipes(pipes_btm)
    
        velocity += gravity
        RED_BIRD_RECT.y += velocity
        if RED_BIRD_RECT.bottom > 700:
            RED_BIRD_RECT.bottom = 700
        elif RED_BIRD_RECT.y < 0:
            RED_BIRD_RECT.y = 0

        pipes_btm, pipes_top = pipe_move(pipes_btm, pipes_top)
        bird_animation()
        draw_window(RED_BIRD_RECT, pipes_btm, pipes_top)
        run = collisions(RED_BIRD_RECT, pipes_btm, pipes_top)

if __name__ == "__main__":
    main()





