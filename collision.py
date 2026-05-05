import pygame
from rectangle import Rectangle

def check_collision(rect1: Rectangle, rect2: Rectangle | pygame.Surface) -> None:

  if isinstance(rect2, pygame.Surface):

    rect2_rect = rect2.get_bounding_rect()
    values = tuple(rect2_rect)

    rect2_rect = Rectangle(values) if len(values) == 4 else 0 # Pylance being annoying
    if rect2_rect == 0: return # removing the annoying


