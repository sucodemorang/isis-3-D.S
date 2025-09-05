import pygame
import os


pygame.init()


WIDHT, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Janela com Imagem")


BG_COLOR = (30, 30, 40)


image_file = "player.png"
if os.path.exist(image_file):
    img = pygame.image.load(image_file).convert_alpha()
    img_rect = img.get_rect(center=(WIDHT // 2, HEIGHT // 2))
else:
   print("Imagem não encontrada!")


SPEED = 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


keys = pygame.key.get_pressed()

#paramos por aq