import pygame
from typing import Tuple

type rectType = Tuple[int, int, int, int] # x, y, width, height
type colorType = Tuple[int, int, int] | Tuple[int, int, int, int] # RGB | RGBA
type rectColorType = Tuple[rectType, colorType]

class Rectangle:

  color: pygame.Color # RGBA, A=255
  x: int
  y: int
  width: int
  height: int

  def __init__(self, rect: rectType, color: colorType = (255, 255, 255, 255)) -> None:

    self.color = pygame.Color(*color)
    self.x, self.y, self.width, self.height = rect
    return

  @property
  def values(self) -> rectType:
    return self.x, self.y, self.width, self.height
  
class Rectangles:

  rects: Tuple[Rectangle, ...]
  _idx: int
  _size: int

  def __init__(self, *rects: rectType | rectColorType) -> None:

    self.rects = ()
    for rect in rects: # rect is rectType | rectColorType
      if isinstance(rect[0], tuple) and len(rect) == 2: # rect == rectColorType
        self.rects = self.rects + (Rectangle(rect[0], rect[1]),)
      elif len(rect) == 4: # rect == rectType (rect is always a Tuple[Unknown, ...] so we don't need to check for it)
        self.rects = self.rects + (Rectangle(rect),)

    self._size = len(rects)
    self._idx = 0
    return

  
  def __iter__(self):
    self._idx = 0
    return self
  
  def __next__(self) -> Rectangle:

    try:
      rect = self.rects[self._idx]
    except IndexError:
      raise StopIteration()
    
    self._idx += 1
    return rect


def rects(window: pygame.Surface, rects: Rectangle | Rectangles) -> None:
  
  if isinstance(rects, Rectangle):
    pygame.draw.rect(window, rects.color, rects.values)
    return
  for i in rects:
    pygame.draw.rect(window, i.color, i.values)
  return