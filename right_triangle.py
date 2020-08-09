import math


class RightTriangle:
    def __init__(
            self,
            side_a: float,
            side_b: float,
            side_c: float,
            angle_a: float,
            angle_b: float,
    ):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
        self._angle_a = angle_a
        self._angle_b = angle_b

    @property
    def side_a(self) -> float:
        return self._side_a

    @property
    def side_b(self) -> float:
        return self._side_b

    @property
    def side_c(self) -> float:
        return self._side_c

    @property
    def angle_a(self) -> float:
        return self._angle_a

    @property
    def angle_b(self) -> float:
        return self._angle_b

    @property
    def angle_c(self) -> float:
        return 90

    @classmethod
    def make(
            cls,
            side_a: float = None,
            side_b: float = None,
            side_c: float = None,
            angle_a: float = None,
            angle_b: float = None,
    ) -> "RightTriangle":
        if side_a and side_b:
            return cls.from_side_a_and_side_b(side_a, side_b)
        elif side_a and side_c:
            return cls.from_side_a_and_side_c(side_a, side_c)
        elif side_b and side_c:
            return cls.from_side_b_and_side_c(side_b, side_c)
        elif side_a and angle_a:
            return cls.from_side_a_and_angle_a(side_a, angle_a)
        elif side_b and angle_a:
            return cls.from_side_b_and_angle_a(side_b, angle_a)
        elif side_c and angle_a:
            return cls.from_side_c_and_angle_a(side_c, angle_a)
        elif side_a and angle_b:
            return cls.from_side_a_and_angle_b(side_a, angle_b)
        elif side_b and angle_b:
            return cls.from_side_b_and_angle_b(side_b, angle_b)
        elif side_c and angle_b:
            return cls.from_side_c_and_angle_b(side_c, angle_b)
        else:
            raise ValueError(
                f"Insufficient parameters for a RightTriangle: "
                f"{side_a=}, {side_b=}, {side_c=}, {angle_a=}, {angle_b=}"
            )

    @classmethod
    def from_side_a_and_side_b(cls, side_a: float, side_b: float) -> "RightTriangle":
        side_c = calculate_hypotenuse_from_legs(side_a, side_b)
        angle_a, angle_b = calculate_acute_angles_from_legs(side_a, side_b)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_a_and_side_c(cls, side_a: float, side_c: float) -> "RightTriangle":
        side_b = calculate_leg_from_other_leg_and_hypotenuse(side_a, side_c)
        angle_a, angle_b = calculate_acute_angles_from_legs(side_a, side_b)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_b_and_side_c(cls, side_b: float, side_c: float) -> "RightTriangle":
        side_a = calculate_leg_from_other_leg_and_hypotenuse(side_b, side_c)
        angle_a, angle_b = calculate_acute_angles_from_legs(side_a, side_b)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_a_and_angle_a(cls, side_a: float, angle_a: float) -> "RightTriangle":
        side_b = calculate_leg_from_other_leg_and_adjacent_angle(side_a, angle_a)
        side_c = calculate_hypotenuse_from_legs(side_a, side_b)
        angle_b = calculate_acute_angle_from_other_acute_angle(angle_a)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_b_and_angle_a(cls, side_b: float, angle_a: float) -> "RightTriangle":
        side_a = calculate_leg_from_other_leg_and_opposed_angle(side_b, angle_a)
        side_c = calculate_hypotenuse_from_legs(side_a, side_b)
        angle_b = calculate_acute_angle_from_other_acute_angle(angle_a)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_c_and_angle_a(cls, side_c: float, angle_a: float) -> "RightTriangle":
        side_a = calculate_leg_from_hypotenuse_and_opposed_angle(side_c, angle_a)
        side_b = calculate_leg_from_other_leg_and_hypotenuse(side_a, side_c)
        angle_b = calculate_acute_angle_from_other_acute_angle(angle_a)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_a_and_angle_b(cls, side_a: float, angle_b: float) -> "RightTriangle":
        angle_a = calculate_acute_angle_from_other_acute_angle(angle_b)
        side_b = calculate_leg_from_other_leg_and_adjacent_angle(side_a, angle_a)
        side_c = calculate_hypotenuse_from_legs(side_a, side_b)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_b_and_angle_b(cls, side_b: float, angle_b: float) -> "RightTriangle":
        angle_a = calculate_acute_angle_from_other_acute_angle(angle_b)
        side_a = calculate_leg_from_other_leg_and_opposed_angle(side_b, angle_a)
        side_c = calculate_hypotenuse_from_legs(side_a, side_b)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    @classmethod
    def from_side_c_and_angle_b(cls, side_c: float, angle_b: float) -> "RightTriangle":
        angle_a = calculate_acute_angle_from_other_acute_angle(angle_b)
        side_a = calculate_leg_from_hypotenuse_and_opposed_angle(side_c, angle_a)
        side_b = calculate_leg_from_other_leg_and_hypotenuse(side_a, side_c)
        return cls(side_a, side_b, side_c, angle_a, angle_b)

    def __str__(self):
        return (
            "RightTriangle" + "\n"
            "\t" + f"{self.side_a=}" + "\n"
            "\t" + f"{self.side_b=}" + "\n"
            "\t" + f"{self.side_c=}" + "\n"
            "\t" + f"{self.angle_a=}" + "\n"
            "\t" + f"{self.angle_b=}"
        )


def calculate_acute_angles_from_legs(side_a: float, side_b: float):
    side_c = calculate_hypotenuse_from_legs(side_a, side_b)
    angle_a = math.degrees(math.asin(side_a / side_c))
    angle_b = calculate_acute_angle_from_other_acute_angle(angle_a)
    return angle_a, angle_b


def calculate_leg_from_hypotenuse_and_opposed_angle(
        hypotenuse, opposed_angle):
    leg = hypotenuse * math.sin(math.radians(opposed_angle))
    return leg


def calculate_leg_from_other_leg_and_opposed_angle(
        other_leg, opposed_angle):
    leg = other_leg * math.tan(math.radians(opposed_angle))
    return leg


def calculate_acute_angle_from_other_acute_angle(other_acute_angle):
    angle = 90 - other_acute_angle
    return angle


def calculate_leg_from_other_leg_and_adjacent_angle(
        other_leg, adjacent_angle):
    leg = other_leg / math.tan(math.radians(adjacent_angle))
    return leg


def calculate_hypotenuse_from_legs(leg_a, leg_b):
    hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
    return hypotenuse


def calculate_leg_from_other_leg_and_hypotenuse(other_leg, hypotenuse):
    leg = math.sqrt(hypotenuse ** 2 - other_leg ** 2)
    return leg
