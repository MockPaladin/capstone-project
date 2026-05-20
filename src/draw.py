from typing import Tuple
import pygame
from rectangle import Rectangle, Rectangles


def rects(window: pygame.Surface, rect: Rectangle | Rectangles) -> None:

    if isinstance(rect, Rectangle):
        pygame_rect = pygame.Rect(rect.values)
        pygame_rect.normalize()  # for negative width | height
        pygame.draw.rect(window, rect.color, pygame_rect, border_radius=0)
        return
    for i in rect:
        pygame.draw.rect(window, i.color, i.values)
    return


def center_coordinates(
    window: pygame.Surface,
    other: pygame.Surface | Rectangle | Tuple[int, int] | None = None,
) -> Tuple[int, int]:

    if other is None:
        return (window.get_width() // 2, window.get_height() // 2)

    if isinstance(other, Rectangle):

        return (
            window.get_width() // 2 - other.width // 2,
            window.get_height() // 2 - other.height // 2,
        )

    if isinstance(other, tuple):

        return (
            (window.get_width() - other[0]) // 2,
            (window.get_height() - other[1]) // 2,
        )

    return (
        (window.get_width() - other.get_width()) // 2,
        (window.get_height() - other.get_height()) // 2,
    )
