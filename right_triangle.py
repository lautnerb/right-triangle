import math


class RightTriangle:
    def __init__(
            self,
            a: float = None,
            b: float = None,
            c: float = None,
            a_angle: float = None,
            b_angle: float = None):
        self._a = a
        self._b = b
        self._c = c
        self._a_angle = a_angle
        self._b_angle = b_angle

        if self._has_leg_and_hypotenuse:
            try:
                self._init_from_leg_and_hypotenuse()
            except ValueError:
                raise ValueError(f"Inconsistent RightTriangle(\n"
                                 + f"\ta = {a}"
                                 + f"\tb = {b}"
                                 + f"\tc = {c}"
                                 + "a or b should not be given")

    @property
    def a(self) -> float:
        return self._a

    @property
    def b(self) -> float:
        return self._b

    @property
    def c(self) -> float:
        return self._c

    @property
    def a_angle(self) -> float:
        return self._a_angle

    @property
    def b_angle(self) -> float:
        return self._b_angle

    def _has_leg_and_hypotenuse(self):
        return (self._has_leg()
                and self._has_hypotenuse())

    def _has_leg(self):
        return (self._a is not None
                or self._b is not None)

    def _has_hypotenuse(self):
        return self._c is not None

    def _init_from_leg_and_hypotenuse(self):
        leg = self._a if self._a is not None else self._b
        hypotenuse = self._c
        other_leg = math.sqrt(hypotenuse ** 2 - leg ** 2)
        self._set_other_leg(other_leg)
        self._calculate_angles()

    def _set_other_leg(self, other_leg):
        if self._a is None:
            self._a = other_leg
        elif self._b is None:
            self._b = other_leg
        else:
            self._raise_error_if_attribute_inconsistent(self._b, other_leg)

    def _calculate_angles(self):
        self._a_angle = math.degrees(math.asin(self.a / self.c))
        self._b_angle = 90 - self.a_angle

    @staticmethod
    def _raise_error_if_attribute_inconsistent(attribute_value, expected_value):
        if attribute_value != expected_value:
            raise ValueError()

    def __str__(self):
        return (f"RightTriangle"
                + f"\n\ta = {self.a}"
                + f"\n\tb = {self.b}"
                + f"\n\tc = {self.c}"
                + f"\n\tA = {self.a_angle: .2f}°"
                + f"\n\tB = {self.b_angle: .2f}°")
