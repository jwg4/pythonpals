
# coding: utf-8

# In[12]:

import numpy as py
import math

# Define square, corners, print method
class Square(object):
    
    corners = 4
    
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
    
    def print(self):
        print(self.point1)
        print(self.point2)
        print(self.point3)
        print(self.point4)

# Define triangle, corners, print method
class Triangle(object):
    
    corners = 3
    
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        
    def print(self):
        print(self.point1)
        print(self.point2)
        print(self.point3)


# Function 'trans'
# Translates shape by adding translation vector to coordinate vectors in turn
# Usage: 'shape' = shape to be translated, 'x' = units to move in x direction, 'y' = units to move in y direction
def trans(shape, x, y):
    
    trans_vec = py.array([x, y])
    
    shape.point1 = shape.point1 + trans_vec
    shape.point2 = shape.point2 + trans_vec
    shape.point3 = shape.point3 + trans_vec
    
    if shape.corners == 4:
        shape.point4 = shape.point4 + trans_vec
    

# Function 'reflect'
# Reflects shape across x or y axis
# Usage: 'shape' = shape to be reflected
# Usage: set 'x' = -1 to reflect across x-axis, else set as 1, same applies to 'y'
def reflect(shape, x, y):
    
    # As rotating about origin, save temp coordinates and move point1 to origin
    if (shape.point1[0] and shape.point1[1]) == 0:
        temp_point = shape.point1
        
        trans(shape, -temp_point[0], -temp_point[1])
        flag = 'moved'
    
    # Reflect across x-axis then y-axis as appropriate
    shape.point1[0] = shape.point1[0] * x
    shape.point2[0] = shape.point2[0] * x
    shape.point3[0] = shape.point3[0] * x
    shape.point1[1] = shape.point1[1] * y
    shape.point2[1] = shape.point2[1] * y
    shape.point3[1] = shape.point3[1] * y
        
    
    if shape.corners == 4:
        shape.point4[0] = shape.point1[0] * x
        shape.point4[1] = shape.point1[1] * y
    
    # If translated back to origin, return to original coordinates
    if flag == 'moved':
        trans(shape, temp_point[0], temp_point[1])
        

# Function 'rotate'
# Rotates shape by using rotation matrix on coordinate vectors in turn
# Usage: 'shape' = shape to be rotated clockwise, 'angle' = angle to be rotated in degrees
def rotate(shape, angle):
    
    angle = math.radians(angle)
    rot_matrix = py.array([[math.cos(angle), -math.sin(angle)],[math.sin(angle), math.cos(angle)]])
    
    # As rotating about origin, save temp coordinates and move point1 to origin
    if (shape.point1[0] and shape.point1[1]) == 0:
        temp_point = shape.point1
        
        trans(shape, -temp_point[0], -temp_point[1])
        flag = 'moved'
    
    # Rotate
    shape.point1 = py.round(py.dot(shape.point1, rot_matrix), 2)
    shape.point2 = py.round(py.dot(shape.point2, rot_matrix), 2)
    shape.point3 = py.round(py.dot(shape.point3, rot_matrix), 2)
    
    if shape.corners == 4:
        shape.point4 = py.round(py.dot(shape.point4, rot_matrix), 2)
    
    # If translated back to origin, return to original coordinates
    if flag == 'moved':
        trans(shape, temp_point[0], temp_point[1])

        
# Declare square and triangle, vectors used for coordinates        
square_1 = Square(py.array([0, 0]), py.array([1, 0]), py.array([1, 1]), py.array([0, 1]))
triangle_1 = Triangle(py.array([0, 0]), py.array([1, 0]), py.array([0, 1]))        
        

# test by translating shape and rotating
square_1.print()
trans(square_1, 2, 0)
rotate(square_1, 90)
print("Square translated 2 in x-direction and rotated 90 deg clockwise")
square_1.print()
print('************************')

triangle_1.print()
rotate(triangle_1, 90)
reflect(triangle_1, -1, 1)
print("Triangle rotated 90 deg clockwise and reflected across x-axis")
triangle_1.print()
print('************************')



# In[ ]:



