import unittest

from right_triangle import RightTriangle


class TestRightTriangle(unittest.TestCase):
    def test_creation_from_leg_and_hypotenuse(self):
        triangle = RightTriangle(b=4, c=5)
        self.assertAlmostEqual(triangle.a, 3)
        self.assertAlmostEqual(triangle.a_angle, 36.86989765)
        self.assertAlmostEqual(triangle.b_angle, 53.13010235)


if __name__ == '__main__':
    unittest.main()
