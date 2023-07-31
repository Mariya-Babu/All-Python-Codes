#Python Code to find area and parimeter of a Rectangle
class RectAngle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def parimeter(self):
        return 2 * (self.length + self.width)
    

rectangle_1 = RectAngle(4,5)
print(rectangle_1.area())
print(rectangle_1.parimeter())


