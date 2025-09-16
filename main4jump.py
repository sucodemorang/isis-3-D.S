import pygame
import os


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Mover Imagem com Setas")


BG_COLOR = (193, 0, 40)


image_file = "GAME\\player.png"
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
else:
   print("Imagem não encontrada")


SPEED = 2
JUMP_STRENGTH = 20
GRAVITY = 0.3
JUMPING = False
VELOCITY_Y = 0


def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)


last_width, last_height = WIDTH, HEIGHT


def limit_movement():
    global img_rect, WIDTH, HEIGHT

    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH    