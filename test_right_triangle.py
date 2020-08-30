import unittest
from typing import Dict

from right_triangle import RightTriangle


class RightTriangleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.expected_attributes: Dict[str, float] = {
            "side_a": 3.00000000,
            "side_b": 4.00000000,
            "side_c": 5.00000000,
            "angle_a": 36.86989765,
            "angle_b": 53.13010235,
        }

    def assert_right_triangle_attributes(
            self,
            right_triangle: RightTriangle,
            expected_attributes: Dict[str, float],
    ):
        actual_attributes = self.right_triangle_to_attributes(right_triangle)
        self.assert_attributes_equal(actual_attributes, expected_attributes)

    @classmethod
    def right_triangle_to_attributes(cls, right_triangle: RightTriangle) -> Dict[str, float]:
        return {
            "side_a": right_triangle.side_a,
            "side_b": right_triangle.side_b,
            "side_c": right_triangle.side_c,
            "angle_a": right_triangle.angle_a,
            "angle_b": right_triangle.angle_b,
        }

    def assert_attributes_equal(self, attributes1: Dict[str, float], attributes2: Dict[str, float]):
        for name, value1 in attributes1.items():
            value2 = attributes2[name]
            self.assertAlmostEqual(
                value1,
                value2,
                places=8,
                msg=f"Attribute '{name}' differs: {value1} != {value2}"
            )

    def test_from_side_a_and_side_b(self):
        rt = RightTriangle.from_side_a_and_side_b(3, 4)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_a_and_side_c(self):
        rt = RightTriangle.from_side_a_and_side_c(3, 5)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_b_and_side_c(self):
        rt = RightTriangle.from_side_b_and_side_c(4, 5)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_a_and_angle_a(self):
        rt = RightTriangle.from_side_a_and_angle_a(3, 36.86989765)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_b_and_angle_a(self):
        rt = RightTriangle.from_side_a_and_angle_a(3, 36.86989765)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_c_and_angle_a(self):
        rt = RightTriangle.from_side_c_and_angle_a(5, 36.86989765)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_a_and_angle_b(self):
        rt = RightTriangle.from_side_a_and_angle_b(3, 53.13010235)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_b_and_angle_b(self):
        rt = RightTriangle.from_side_b_and_angle_b(4, 53.13010235)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_from_side_c_and_angle_b(self):
        rt = RightTriangle.from_side_c_and_angle_b(5, 53.13010235)
        self.assert_right_triangle_attributes(rt, self.expected_attributes)

    def test_make_insufficient(self):
        with self.assertRaises(ValueError):
            RightTriangle.make(side_a=3)
        with self.assertRaises(ValueError):
            RightTriangle.make(side_b=4)
        with self.assertRaises(ValueError):
            RightTriangle.make(side_c=5)
        with self.assertRaises(ValueError):
            RightTriangle.make(angle_a=36.86989765)
        with self.assertRaises(ValueError):
            RightTriangle.make(angle_b=53.13010235)
        with self.assertRaises(ValueError):
            RightTriangle.make(angle_a=36.86989765, angle_b=53.13010235)

    def test_make_inconsistent(self):
        side_c = 6
        rt = RightTriangle.make(side_a=3, side_b=4, side_c=side_c)
        self.assertNotAlmostEqual(side_c, rt.side_c)


if __name__ == '__main__':
    unittest.main()
