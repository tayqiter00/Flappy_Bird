import pygame
import os

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

def draw_window(red):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(BASE, (0, 700))

    WIN.blit(RED_BIRD, (red.x, red.y))

    pygame.display.update()

def main():
    red = RED_BIRD.get_rect(midleft = (0, HEIGHT / 2))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LALT:
        if (red.bottom < 700):
            red.bottom += 5
        draw_window(red)

if __name__ == "__main__": # ensures this file only runs when run directly
    main()