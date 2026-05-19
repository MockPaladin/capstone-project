import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) # ignore runtime warnings, like when the window gets forcibly resized by the OS
import sys
import pygame
import pygame.freetype
import display
import draw
import method
from player import Player
from rectangle import Rectangles

pygame.init()
pygame.freetype.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # (0, 0) sets native resolution
pygame.display.set_caption("main.py") # -> NotImplementedError (TechSmart)

background = pygame.image.load("./assets/background.png")
background = pygame.transform.scale(background, (window.width, window.height))

running = True
game_over = False

centered_coordinates = draw.center_coordinates(window, (20, 20))
player = Player((centered_coordinates[0], centered_coordinates[1], 20, 20))
del centered_coordinates
player.methods = method.methods

lazers = Rectangles(((200, 0, 10, 150), (255, 0, 0)),
                    ((400, 0, 10, 150), (255, 0, 0)),
                    ((600, 0, 10, 150), (255, 0, 0)))

while running:

  ## -- EVENTS -- ##

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_r]:
    player.width, player.height = (20, 20)
    player.x, player.y = draw.center_coordinates(window, player) 
  if keys[pygame.K_ESCAPE]:
    window = pygame.display.set_mode((1020, 580)) # exit fullscreen
    background = pygame.transform.scale(background, (window.width, window.height))
  if keys[pygame.K_f]:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # enter fullscreen
    background = pygame.transform.scale(background, (window.width, window.height))

  ## -- LOGIC -- ##

  for lazer in lazers:

    lazer.y += 25
    if lazer.y > window.height:
      lazer.y = 0 - lazer.height

  ## -- DRAWING -- ##

  window.blit(background, (0, 0))

  draw.rects(window, lazers)
  player.draw(window, can_exit=False)
  
  if player.colliding(tuple(lazers)):
    game_over = True
    print("Player was struck by a lazer and died.")
  if game_over:
    break

  pygame.display.flip()
  clock.tick(60)
  
pygame.quit() # -> NotImplementedError (TechSmart)

if game_over: 
  display.GAME_OVER()

sys.exit()