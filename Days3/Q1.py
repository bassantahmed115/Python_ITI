import math

def calculate_area():
    shape = input("Enter the shape (triangle, rectangle, circle, square): ").lower()
    
    if shape == "triangle":
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height length: "))
        return 0.5 * base * height
    
    elif shape == "rectangle":
        width = float(input("Enter the width length: "))
        height = float(input("Enter the height length: "))
        return width * height
    
    elif shape == "circle":
        radius = float(input("Enter the radius length: "))
        return math.pi * radius ** 2
    
    elif shape == "square":
        side = float(input("Enter the side length: "))
        return side ** 2
    
    else:
        return "Unsupported shape."
area = calculate_area()
print(f"The area is: {area}")

