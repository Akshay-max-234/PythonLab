class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Rectangle(Shape):
    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rect = Rectangle(length, breadth)
print("\n--- Rectangle Details ---")
print("Length:", rect.length)
print("Breadth:", rect.breadth)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
