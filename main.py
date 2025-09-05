import pygame

# Isso inicia o modulo do Pygame
pygame.init()

WIDHT, HEIGHT = 800,600

screen = pygame.displayset_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Meu jogo")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
    pygame.display.flip()

pygame.quit()
