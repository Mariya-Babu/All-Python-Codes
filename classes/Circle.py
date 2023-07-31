#Python Code to find area and circumference of a circle
class Circle:
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        PI = 3.14
        a = PI * self.radius * self.radius
        print(f'Area of Circle = {a}')
        return a

    def circumference(self):
        PI = 3.14
        c = 2 * PI * self.radius
        print(f'Circumference of Circle = {c}')
        return c


circle_1 = Circle(5) 
circle_1.area()
circle_1.circumference()