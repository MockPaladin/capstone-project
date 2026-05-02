import sys
import pygame
import keys
from player import Player

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # (0, 0) sets native resolution
pygame.display.set_caption("main.py") # NotImplementedError (TechSmart)

running = True
player = Player((window.get_width() // 2 - 1, window.get_height() // 2 - 10, 20, 20))
player.methods = keys.methods
# window.get_width() // 2 - 10, window.get_height() // 2 - 10 is the center of the screen, accounting for rect size

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_r]:
    player.width, player.height = (20, 20)
    player.x, player.y = window.get_width() // 2 - 10, window.get_height() // 2 - 10
  
  if keys[pygame.K_ESCAPE]: window = pygame.display.set_mode((1020, 580)) # exit fullscreen
  if keys[pygame.K_f]: window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # enter fullscreen
  

  window.fill((59, 120, 69))
  player.draw(window)

  pygame.display.flip()
  clock.tick(60)
  

pygame.quit() # -> NotImplementedError (TechSmart)
sys.exit()