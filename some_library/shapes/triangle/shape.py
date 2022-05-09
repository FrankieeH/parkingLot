class Shape:
    def __init__(self) -> None:
        self.area = None
        self.perimeter = None

    def __str__(self) -> str:
        return f"Shape area: {self.area}, perimeter: {self.perimeter}"

class Triangle(Shape):
    def __init__(self, length, width) -> None:
        self.area = 1/2 * length * width
        self.perimeter = 2 * width + length

    def do_something(triangle_type: str, name: str, other_shape_area: int) -> tuple[Shape, int]:
        """Calculates the angle of the triangle."""
        print(name)
        return_length = other_shape_area * 2
        return Shape(), return_length
