import pygame
from rectangle import Rectangle, colorType, rectType, rectColorType
from typing import Callable, Final, Tuple

type attributeModifier = Callable[[], Tuple[int, int | colorType]] # TODO: make colors work
type strictAttributeModifier = Callable[[], Tuple[int, int]]

class Player(Rectangle):

  X: Final = 0
  Y: Final = 1
  WIDTH: Final = 2
  HEIGHT: Final = 3
  COLOR: Final = 4

  def __init__(self, rect: rectType | rectColorType) -> None:

    if len(rect) == 2: # rectColorType
      super().__init__(rect[0], rect[1])
    elif len(rect) == 4:
      super().__init__(rect)

    self._methods: dict[int, strictAttributeModifier] = {} # on Pygame.K_*, do attributeModifier

  def draw(self, window: pygame.Surface, can_exit: bool=True) -> None:
    self.update(window, can_exit=can_exit)
    rect = pygame.Rect(self.values)
    rect.normalize() # for negative width | height

    if rect.width == 0:
      rect.width = 5
    if rect.height == 0:
      rect.height = 5

    pygame.draw.rect(window, self.color, rect, border_radius=0)

  def update(self, window: pygame.Surface, can_exit: bool = True) -> None:

    methods = self._methods
    keys = pygame.key.get_pressed()


    for _key, mod in methods.items():
      if keys[_key]:

        attr, delta = mod()

        if attr == Player.X:
          self.x += delta
          if self.colliding(window) and not can_exit:
            self.x -= delta

        if attr == Player.Y:
          self.y += delta
          if self.colliding(window) and not can_exit:
            self.y -= delta

        if attr == Player.WIDTH:
          self.width += delta
          if self.colliding(window) and not can_exit:
            self.width -= delta

        if attr == Player.HEIGHT:
          self.height += delta
          if self.colliding(window) and not can_exit:
            self.height -= delta

  @property
  def methods(self) -> dict[int, strictAttributeModifier]:
    return self._methods
  
  @methods.setter
  def methods(self, args: dict[int, strictAttributeModifier]) -> None:

    _args = {int(key): value for key, value in args.items()}
    self._methods = _args