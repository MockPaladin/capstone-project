import unittest
import sys
import pygame

sys.path.insert(0, "../src")
from rectangle import Rectangle

rect = Rectangle((200, 50, 10, 90), (0, 0, 255, 255))


class TestRectangle(unittest.TestCase):

    def test_color(self) -> None:

        self.assertEqual(rect.color, pygame.Color(0, 0, 255, 255))

    def test_values(self) -> None:

        self.assertEqual(rect.x, 200)
        self.assertEqual(rect.y, 50)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 90)
        self.assertEqual(rect.values, (200, 50, 10, 90))

    def test_colliding(self) -> None:

        window = pygame.display.set_mode((100, 100))
        self.assertTrue(rect.colliding(window))

        rect2 = Rectangle((150, 100, 100, 100))
        self.assertTrue(rect.colliding(rect2))

        rect3 = Rectangle((100, 50, 10, 10))
        self.assertTrue(rect.colliding((rect2, rect3)))

    def test_new_object(self) -> None:

        rect2 = Rectangle(rect.values)
        self.assertEqual(rect2.values, rect.values)

    def test_iter(self) -> None:

        values = []
        for i in rect:

            values.append(i)

        self.assertEqual(tuple(values), rect.values)

    def test_vec_to(self) -> None:

        rect2 = Rectangle((200, 51, 10, 90))

        self.assertEqual(rect.vec_to(rect2), (0.0, 1.0))
        # see if the vector from rect -> rect2
        # is equal to the unit vector going down


if __name__ == "__main__":

    unittest.main()
