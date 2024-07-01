# point2D.py

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(X: {self.x}, Y: {self.y})"

    def translation(self, dx, dy):
        self.x += dx
        self.y += dy


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def __str__(self):
        return f"(X: {self.x}, Y: {self.y}, Z: {self.z})"

    def translation(self, dx, dy, dz):
        super().translation(dx, dy)
        self.z += dz


if __name__ == "__main__":
    a = Point2D(1, 2)
    print(f"A = {a}")

    a.translation(-1, -2)
    print(f"A = {a}")

    b = Point2D(-3, 0)
    b.translation(5, -1)
    print(f"B = {b}")

    c = Point3D(1, 5, -3)
    c.translation(0, -2, 1)
    print(f"C = {c}")