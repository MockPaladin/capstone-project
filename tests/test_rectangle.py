import unittest
import sys

sys.path.insert(0, "../src")
from rectangle import Rectangle

rect = Rectangle((200, 50, 10, 90))


class TestRectangle(unittest.TestCase):

    def test_values(self) -> None:

        self.assertEqual(rect.x, 200)
        self.assertEqual(rect.y, 50)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 90)

    def test_new_object(self) -> None:

        rect2 = Rectangle(rect.values)
        self.assertEqual(rect2.values, rect.values)


if __name__ == "__main__":

    unittest.main()
