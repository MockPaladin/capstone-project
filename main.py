import sys
import pygame
import draw
from draw import Rectangles

pygame.init()

window: pygame.Surface = pygame.display.set_mode((1018, 573))
pygame.display.set_caption("main.py")

running: bool = True
rectangles = Rectangles((20, 20, 20, 20), ((40, 40, 20, 40), (0, 0, 0)), ((60, 60, 40, 20), (255, 0, 0)))

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False

  window.fill((59, 120, 69))
  draw.rects(window, rectangles)

  pygame.display.flip()

pygame.quit()
sys.exit()