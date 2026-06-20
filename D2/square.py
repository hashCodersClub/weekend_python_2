from .shape import Shape
class Square(Shape):
    def area(self,side):
        return side*side
    
    def circumference(self,side):
        return 4*side
