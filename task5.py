# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 5 Object-Oriented Programming
# done by Sora
# Create a Python class called Rectangle that represents a rectangle. Include methods to calculate the area and perimeter of the rectangle.

class Rectangle:
    # initialize the Rectangle object with length and width
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # calculate the area of the rectangle
    def calculateArea(self):
        return self.width * self.height

    # calculate the perimeter of the rectangle
    def calculatePerimeter(self):
        return 2 * (self.width + self.height)    

# Example usage:
rectangle = Rectangle(5,10)
area = rectangle.calculateArea()
perimeter = rectangle.calculatePerimeter()
print("Area:", area)
print("Perimeter:", perimeter)