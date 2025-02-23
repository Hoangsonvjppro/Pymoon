class Rectangle:
    def __init__(self,length = 1, width = 1):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def to_string(self):
        return (str(self.length) + "*" + str(self.width)
                + 'perimeter: '+ str(self.perimeter())
                + 'area: ' + str(self.area()))