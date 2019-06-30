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
