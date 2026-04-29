import sys
import pygame
import draw
from rectangle import Rectangle

pygame.init()
clock = pygame.time.Clock()

window: pygame.Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # (0, 0) sets native resolution
pygame.display.set_caption("main.py") # NotImplementedError (TechSmart)

running: bool = True
rectangle = Rectangle((window.get_width() // 2 - 1, window.get_height() // 2 - 10, 20, 20))
# window.get_width() // 2 - 10, window.get_height() // 2 - 10 is the center of the screen, accounting for rect size

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
  
  keys = pygame.key.get_pressed()
    
  if keys[pygame.K_s]:
    rectangle.y += 5
  if keys[pygame.K_w]:
    rectangle.y -= 5
  if keys[pygame.K_a]:
    rectangle.x -= 5
  if keys[pygame.K_d]:
    rectangle.x += 5
  
  if keys[pygame.K_LEFT]:
    rectangle.width -= 5
  if keys[pygame.K_RIGHT]:
    rectangle.width += 5
  if keys[pygame.K_UP]:
    rectangle.height -= 5
  if keys[pygame.K_DOWN]:
    rectangle.height += 5
  
  if keys[pygame.K_r]:
    rectangle.width, rectangle.height = (20, 20)
    rectangle.x, rectangle.y = window.get_width() // 2 - 10, window.get_height() // 2 - 10
  
  if keys[pygame.K_ESCAPE]: window = pygame.display.set_mode((1020, 580)) # exit fullscreen
  if keys[pygame.K_f]: window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # enter fullscreen
  

  window.fill((59, 120, 69))
  draw.rects(window, rectangle)

  pygame.display.flip()
  clock.tick(60)
  

pygame.quit() # -> NotImplementedError (TechSmart)
sys.exit()