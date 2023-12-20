import pygame
import sys

pygame.init()

screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Interactive Game")

font = pygame.font.Font(None, 50)

text_surface = font.render("Interactive Game menu", True, (255, 255, 255))

text_rect = text_surface.get_rect()

text_rect.center = (screen_width / 2, screen_height / 2)

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

  screen.fill((0, 0, 0))
  screen.blit(text_surface, text_rect)

	
   pygame.display.flip()

pygame.quit()
sys.exit()