import pygame
import os

WIDTH, HEIGHT = 432, 768

ZERO = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '0.png')), (WIDTH / 10, HEIGHT / 20))
ZERO_RECT = ZERO.get_rect(midtop=(WIDTH / 2, 20))

ONE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '1.png')), (WIDTH / 10, HEIGHT / 20))
ONE_RECT = ONE.get_rect(midtop=(WIDTH / 2, 20))

TWO = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '2.png')), (WIDTH / 10, HEIGHT / 20))
TWO_RECT = TWO.get_rect(midtop=(WIDTH / 2, 20))

THREE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '3.png')), (WIDTH / 10, HEIGHT / 20))
THREE_RECT = THREE.get_rect(midtop=(WIDTH / 2, 20))

FOUR = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '4.png')), (WIDTH / 10, HEIGHT / 20))
FOUR_RECT = FOUR.get_rect(midtop=(WIDTH / 2, 20))

FIVE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '5.png')), (WIDTH / 10, HEIGHT / 20))
FIVE_RECT = FIVE.get_rect(midtop=(WIDTH / 2, 20))

SIX = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '6.png')), (WIDTH / 10, HEIGHT / 20))
SIX_RECT = SIX.get_rect(midtop=(WIDTH / 2, 20))

SEVEN = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '7.png')), (WIDTH / 10, HEIGHT / 20))
SEVEN_RECT = SEVEN.get_rect(midtop=(WIDTH / 2, 20))

EIGHT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '8.png')), (WIDTH / 10, HEIGHT / 20))
EIGHT_RECT = EIGHT.get_rect(midtop=(WIDTH / 2, 20))

NINE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'sprites', '9.png')), (WIDTH / 10, HEIGHT / 20))
NINE_RECT = NINE.get_rect(midtop=(WIDTH / 2, 20))