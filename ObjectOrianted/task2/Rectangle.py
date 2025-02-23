class Rectangle:
    def __init__(self,length = 1, width = 1):
        if length <= 0 or width <= 0:
            raise ValueError("length and width must be positive")
        self.length = length
        self.width = width

    def area(self)->float:
        return round(self.length * self.width, 2)

    def perimeter(self)->float:
        return round((self.length + self.width) * 2, 2)

    def to_string(self):
        return (str(self.length) + "*" + str(self.width)
                + 'perimeter: '+ str(self.perimeter())
                + 'area: ' + str(self.area()))