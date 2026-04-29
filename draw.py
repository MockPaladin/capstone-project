import pygame
from rectangle import Rectangle, Rectangles

def rects(window: pygame.Surface, rects: Rectangle | Rectangles) -> None:
  
  if isinstance(rects, Rectangle):
    pygame_rect = pygame.Rect(rects.values)
    pygame_rect.normalize() # for negative width | height
    pygame.draw.rect(window, rects.color, pygame_rect, border_radius=0)
    return
  for i in rects:
    pygame.draw.rect(window, i.color, i.values)
  return