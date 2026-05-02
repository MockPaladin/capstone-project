import pygame
from rectangle import Rectangle, Rectangles

def rects(window: pygame.Surface, rect: Rectangle | Rectangles) -> None:
  
  if isinstance(rect, Rectangle):
    pygame_rect = pygame.Rect(rect.values)
    pygame_rect.normalize() # for negative width | height
    pygame.draw.rect(window, rect.color, pygame_rect, border_radius=0)
    return
  for i in rect:
    pygame.draw.rect(window, i.color, i.values)
  return