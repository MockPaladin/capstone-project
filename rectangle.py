from typing import Tuple
import pygame

type rectType = Tuple[int, int, int, int] # x, y, width, height
type colorType = Tuple[int, int, int] | Tuple[int, int, int, int] # RGB | RGBA
type rectColorType = Tuple[rectType, colorType]

class Rectangle:

  color: pygame.Color # RGBA, A=255

  def __init__(self, rect: rectType, color: colorType = (255, 255, 255, 255)) -> None:

    self.color = pygame.Color(*color)
    self.values = rect
    return
  
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