import unittest

from right_triangle import RightTriangle


class TestRightTriangle(unittest.TestCase):
    def test_creation_from_a_and_c(self):
        triangle = RightTriangle(a=3, c=5)
        self.assertAlmostEqual(triangle.a, 3)
        self.assertAlmostEqual(triangle.a_angle, 36.86989765)
        self.assertAlmostEqual(triangle.b_angle, 53.13010235)

    def test_creation_from_b_and_c(self):
        triangle = RightTriangle(b=4, c=5)
        self.assertAlmostEqual(triangle.a, 3)
        self.assertAlmostEqual(triangle.a_angle, 36.86989765)
        self.assertAlmostEqual(triangle.b_angle, 53.13010235)

    def test_insufficient_creation(self):
        with self.assertRaises(ValueError):
            RightTriangle(a=3)
        with self.assertRaises(ValueError):
            RightTriangle(b=4)
        with self.assertRaises(ValueError):
            RightTriangle(c=5)

    def test_inconsistent_creation(self):
        with self.assertRaises(ValueError):
            RightTriangle(a=4, b=4, c=5)
        with self.assertRaises(ValueError):
            RightTriangle(a=3, b=3, c=5)
        with self.assertRaises(ValueError):
            RightTriangle(a=3, b=4, c=6)


if __name__ == '__main__':
    unittest.main()
