class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pi=3.14159265359
        return pi**self.radius

    def perimeter(self):
        pi=3.14159265359
        return 2*pi*self.radius

a=circle(10)

print(a.area())
print(a.perimeter())