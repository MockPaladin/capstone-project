import pygame
from player import Player, strictAttributeModifier

methods: dict[int, strictAttributeModifier] = {
  pygame.K_w: lambda: (Player.Y, -5),
  pygame.K_s: lambda: (Player.Y, 5),
  pygame.K_a: lambda: (Player.X, -5),
  pygame.K_d: lambda: (Player.X, 5),
  pygame.K_LEFT: lambda: (Player.WIDTH, -5),
  pygame.K_RIGHT: lambda: (Player.WIDTH, 5),
  pygame.K_UP: lambda: (Player.HEIGHT, -5),
  pygame.K_DOWN: lambda: (Player.HEIGHT, 5)

}