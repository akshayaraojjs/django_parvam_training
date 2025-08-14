# method overloading: same methods with different parameters
class Area:
    def __init__(self):
        self.sideA = ""
        self.sideB = ""
        self.sideC = ""
    
    # default parameters: paramter assigned as None
    def findArea(self, A=None, B=None, C=None):
        # Initialization
        self.sideA = A
        self.sideB = B
        self.sideC= C
        # Calculation:
        if self.sideA!=None and self.sideB!=None and self.sideC!=None:
            area = self.sideA * self.sideB * self.sideC
            print("Area of Cube: ", area)
        elif self.sideA!=None and self.sideB!=None:
            area = self.sideA * self.sideB
            print("Area of Rectangle: ", area)
        elif self.sideA!=None:
            area = self.sideA * self.sideA
            print("Area of Square: ", area)
        else:
            print("Area cannot be caluculated")
        
NoSide = Area()

NoSide.findArea()

square = Area()

square.findArea(5)

rectangle = Area()

rectangle.findArea(5, 8)

cube = Area()

cube.findArea(5, 8, 9)