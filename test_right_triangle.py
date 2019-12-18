import unittest

from right_triangle import RightTriangle


class RightTriangleTest(unittest.TestCase):
    def test_valid_creation(self):
        creation_cases = [
            {
                "a": 3.00000000,
                "b": 4.00000000,
            },
            {
                "a": 3.00000000,
                "c": 5.00000000,
            },
            {
                "b": 4.00000000,
                "c": 5.00000000,
            },
            {
                "a": 3.00000000,
                "a_angle": 36.86989765,
            },
            {
                "b": 4.00000000,
                "a_angle": 36.86989765,
            },
            {
                "c": 5.00000000,
                "a_angle": 36.86989765,
            },
            {
                "a": 3.00000000,
                "b_angle": 53.13010235,
            },
            {
                "b": 4.00000000,
                "b_angle": 53.13010235,
            },
            {
                "c": 5.00000000,
                "b_angle": 53.13010235,
            },
        ]
        expected = {
            "a": 3.00000000,
            "b": 4.00000000,
            "c": 5.00000000,
            "a_angle": 36.86989765,
            "b_angle": 53.13010235,
        }

        for creation_case in creation_cases:
            try:
                right_triangle = RightTriangle(**creation_case)

                result = {
                    "a": right_triangle.a,
                    "b": right_triangle.b,
                    "c": right_triangle.c,
                    "a_angle": right_triangle.a_angle,
                    "b_angle": right_triangle.b_angle,
                }
                for attribute in expected:
                    with self.subTest(
                            creation_case=creation_case,
                            attribute=attribute,
                    ):
                        self.assertAlmostEqual(
                            expected[attribute],
                            result[attribute],
                            places=8,
                        )
            except ValueError:
                with self.subTest():
                    raise AssertionError(
                        "Could not create RightTriangle with parameters: "
                        + str(creation_case)
                    )

    def test_insufficient_creation(self):
        with self.assertRaises(ValueError):
            RightTriangle(a=3)
        with self.assertRaises(ValueError):
            RightTriangle(b=4)
        with self.assertRaises(ValueError):
            RightTriangle(c=5)
        with self.assertRaises(ValueError):
            RightTriangle(a_angle=36.86989765)
        with self.assertRaises(ValueError):
            RightTriangle(b_angle=53.13010235)
        with self.assertRaises(ValueError):
            RightTriangle(a_angle=36.86989765, b_angle=53.13010235)

    def test_inconsistent_creation(self):
        with self.assertRaises(ValueError):
            RightTriangle(a=4, b=4, c=5)
        with self.assertRaises(ValueError):
            RightTriangle(a=3, b=3, c=5)
        with self.assertRaises(ValueError):
            RightTriangle(a=3, b=4, c=6)


if __name__ == '__main__':
    unittest.main()
