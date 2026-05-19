"""
Currently just a small list of methods for the `Player` object, possibly enemy movement later on.
"""

import pygame
from player import Player, strictAttributeModifier

methods: dict[int, strictAttributeModifier] = {
  pygame.K_w: lambda: (Player.Y, -5),
  pygame.K_s: lambda: (Player.Y, 5),
  pygame.K_a: lambda: (Player.X, -5),
  pygame.K_d: lambda: (Player.X, 5)
}