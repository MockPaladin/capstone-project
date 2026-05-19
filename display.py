"""
General module for displaying static screens, such as `GAME OVER` or other such things.
"""

import pygame
import pygame.freetype
import draw

def GAME_OVER() -> None:

  pygame.init()
  pygame.freetype.init()

  running = True

  window = pygame.display.set_mode((800, 600), pygame.SCALED)
  pygame.display.set_caption("GAME OVER")

  font = pygame.font.SysFont('Arial', 120, bold=True)
  text_surface = font.render("YOU LOSE", True, (255, 255, 255))

  while running:

    for event in pygame.event.get():
      if event.type == pygame.QUIT: running = False

    window.fill((255, 0, 0))
    window.blit(text_surface, (draw.center_coordinates(window, text_surface))) # add text surface to window

    pygame.display.flip()

  pygame.quit()