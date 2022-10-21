class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"X: {self.x} Y: {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __call__(self, *args, **kwds):
        print('Vector was called!')

v1 = Vector(10,30)
v2 = Vector(20,40)
v3 = v1 + v2
print(v3)
v3()