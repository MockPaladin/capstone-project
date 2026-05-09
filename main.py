import sys
import pygame
import pygame.freetype
import draw
import keys
from player import Player
from rectangle import Rectangle 

pygame.init()
pygame.freetype.init()

font = pygame.font.SysFont('Arial', 120, bold=True)
text_surface = font.render("YOU LOSE", True, (255, 255, 255))

clock = pygame.time.Clock()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # (0, 0) sets native resolution
pygame.display.set_caption("main.py") # NotImplementedError (TechSmart)

running = True
game_over = False
centered_coordinates = draw.center_coordinates(window, (20, 20))
player = Player((centered_coordinates[0], centered_coordinates[1], 20, 20))
player.methods = keys.methods
# window.get_width() // 2 - 10, window.get_height() // 2 - 10 is the center of the screen, accounting for rect size

rect2 = Rectangle((50, 50, 50, 50), (255, 0, 0, 255))

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_r]:
    player.width, player.height = (20, 20)
    player.x, player.y = draw.center_coordinates(window, player)
  
  if keys[pygame.K_ESCAPE]: window = pygame.display.set_mode((1020, 580)) # exit fullscreen
  if keys[pygame.K_f]: window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # enter fullscreen

  window.fill((59, 120, 69))
  draw.rects(window, rect2)
  player.draw(window)

  if player.colliding(rect2): game_over = True
  if game_over:
    break

  pygame.display.flip()
  clock.tick(60)
  
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_ESCAPE]: window = pygame.display.set_mode((1020, 580)) # exit fullscreen
  if keys[pygame.K_f]: window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # enter fullscreen

  window.fill((255, 0, 0))
  window.blit(text_surface, (draw.center_coordinates(window, text_surface)))
  
  pygame.display.flip()

pygame.quit() # -> NotImplementedError (TechSmart)
sys.exit()