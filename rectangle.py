from __future__ import annotations
from typing import  Self, Tuple
import pygame

type rectType = Tuple[int, int, int, int] # x, y, width, height
type colorType = Tuple[int, int, int] | Tuple[int, int, int, int]# RGB | RGBA
type rectColorType = Tuple[rectType, colorType]

class Rectangle:

  color: pygame.Color # RGBA, A=255

  def __init__(self, rect: rectType | pygame.Rect, color: colorType = (255, 255, 255, 255)) -> None:

    self.color = pygame.Color(*color)

    if isinstance(rect, pygame.Rect):
      self.values = tuple(rect)


    self.values = rect
    return
  
  def colliding(self, rect2: Rectangle | pygame.Surface) -> bool:
  
    _rect1 = pygame.Rect(self.values,)

    if isinstance(rect2, pygame.Surface):
      _rect2 = rect2.get_bounding_rect()
      if _rect1.union(_rect2) != _rect2: # if part of _rect1 is outside of _rect2
        return True
      return False

    _rect2 = pygame.Rect(rect2.values,)
    if _rect1.colliderect(_rect2):
      return True
    return False
  
  def __iter__(self) -> Self:
    self._idx = 0
    return self
  
  def __next__(self) -> int:
    try:
      value = self.values[self._idx]
    except IndexError:
      raise StopIteration()
    
    self._idx += 1
    return value
    
  
  @property
  def x(self) -> int:
    return self.values[0]
  
  @x.setter
  def x(self, value: int) -> None:
    self.values = (value, self.y, self.width, self.height)

  @property
  def y(self) -> int:
    return self.values[1]
  
  @y.setter
  def y(self, value: int) -> None:
    self.values = (self.x, value, self.width, self.height)

  @property
  def width(self) -> int:
    return self.values[2]
  
  @width.setter
  def width(self, value: int) -> None:
    self.values = (self.x, self.y, value, self.height)

  @property
  def height(self) -> int:
    return self.values[3]
  
  @height.setter
  def height(self, value: int) -> None:
    self.values = (self.x, self.y, self.width, value)

  
  
class Rectangles:

  rects: Tuple[Rectangle, ...]
  _idx: int
  _size: int

  def __init__(self, *rects: rectType | rectColorType) -> None:

    self.rects = ()
    for rect in rects: # rect is rectType | rectColorType

      if isinstance(rect[0], tuple) and len(rect) == 2: # rectColorType
        self.rects = self.rects + (Rectangle(rect[0], rect[1]),)
      elif len(rect) == 4: # rectType
        self.rects = self.rects + (Rectangle(rect),)

    self._size = len(rects)
    self._idx = 0
    return

  
  def __iter__(self) -> Self:
    self._idx = 0
    return self
  
  def __next__(self) -> Rectangle:

    try:
      rect = self.rects[self._idx]
    except IndexError:
      raise StopIteration()
    
    self._idx += 1
    return rect