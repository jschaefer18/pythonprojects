import math

def compute_area_square(side):
    return side **2


def compute_area_rectangle(side1,side2):
    return side1 * side2


def compute_area_circle(rad):
    return 3.14*rad**2


while True:
    shape = input("What shape do you have(sqaure, rectangle, or circle)(Type q to quit) ? ")
    if shape.upper() == "SQUARE":
        side = float(input("What is the length of one side? "))
        area_of_square = compute_area_square(side)
        print(area_of_square)
    if shape.upper() == "RECTANGLE":
        rect_side1 = float(input("What is the length of side one? "))
        rect_side2 = float(input("What is the length of side two? "))
        area_of_rectangle = compute_area_rectangle(rect_side1,rect_side2)
        print(area_of_rectangle)
    if shape.upper() == "CIRCLE":
        radius = float(input("What is the radius of the circle? "))
        area_of_circle = compute_area_circle(radius)
        print(area_of_circle)
    if shape.upper() == "Q":
        print("Goodbye!")
        quit()






