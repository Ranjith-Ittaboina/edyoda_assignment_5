class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def square_sum(self):
        return (self.x*self.x) + (self.y*self.y) + (self.z*self.z)

square_object = point(1,3,5)
print(square_object.square_sum())