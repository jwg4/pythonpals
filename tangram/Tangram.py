# coding: utf-8
import numpy as np
import math


# Define square, corners, string method
class Square(object):

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return "%s %s %s %s" % (self.points[0], self.points[1], self.points[2], self.points[3])


# Define triangle, corners, string method
class Triangle(object):

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return "%s %s %s" % (self.points[0], self.points[1], self.points[2])


# Define parallelogram, corners, string method
class Parallel(object):

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return "%s %s %s %s" % (self.points[0], self.points[1], self.points[2], self.points[3])

# Function 'trans'
# Translates shape by adding translation vector to coordinate vectors in turn
# Usage: 'shape' = shape to be translated, 'x' = units to move in x direction, 'y' = units to move in y direction
def trans(shape, x, y):

    trans_vec = np.array([x, y])

    for i in range(len(shape.points)):
        shape.points[i] = shape.points[i] + trans_vec


# Function 'reflect'
# Reflects shape across x or y axis
# Usage: 'shape' = shape to be reflected
# Usage: set 'x' = -1 to reflect across x-axis, else set as 1, same applies to 'y'
def reflect(shape, x, y):

    # As reflecting about origin, determine whether point1 is at origin
    # If not, save temp coordinates and move point1 to origin
    at_origin = np.array_equal(shape.points[0], np.array([0, 0]))

    if at_origin == False:
        temp_point = shape.points[0]

        trans(shape, -temp_point[0], -temp_point[1])

    # Reflect across x-axis then y-axis as appropriate
    for i in range(len(shape.points)):
        shape.points[i][0] = shape.points[i][0] * y
        shape.points[i][1] = shape.points[i][1] * x

    # If translated back to origin, return to original coordinates
    if at_origin == False:
        trans(shape, temp_point[0], temp_point[1])


# Function 'rotate'
# Rotates shape by using rotation matrix on coordinate vectors in turn
# Usage: 'shape' = shape to be rotated clockwise, 'angle' = angle to be rotated in degrees
def rotate(shape, angle):

    angle = math.radians(angle)
    rot_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])

    # Round to avoid errors
    rot_matrix = np.around(rot_matrix)

    # As reflecting about origin, determine whether point1 is at origin
    # If not, save temp coordinates and move point1 to origin
    at_origin = np.array_equal(shape.points[0], np.array([0, 0]))

    if (at_origin == False):
        temp_point = shape.points[0]

        trans(shape, -temp_point[0], -temp_point[1])

    # Rotate
    for i in range(len(shape.points)):
        shape.points[i] = np.round(np.dot(shape.points[i], rot_matrix), 0)

    # If translated back to origin, return to original coordinates
    if at_origin == False:
        trans(shape, temp_point[0], temp_point[1])


if __name__ == "__main__":

    # Declare shape coordinates
    square_test_points = [np.array([0, 0]), np.array([1, 0]), np.array([1, 1]), np.array([0, 1])]
    triangle_test_points = [np.array([0, 0]), np.array([1, 0]), np.array([0, 1])]
    parallel_test_points = [np.array([0, 0]), np.array([2, 0]), np.array([3, 1]), np.array([1, 1])]
    square_1 = Square(square_test_points)
    triangle_1 = Triangle(triangle_test_points)
    parallel_1 = Parallel(parallel_test_points)

    # test by translating shape and rotating
    print(square_1)
    trans(square_1, 2, 0)
    rotate(square_1, 90)
    print("Square translated 2 in x-direction and rotated 90 deg clockwise")
    print(square_1)
    print('************************')

    print(triangle_1)
    rotate(triangle_1, 90)
    reflect(triangle_1, 1, -1)
    print("Triangle rotated 90 deg clockwise and reflected across y-axis")
    print(triangle_1)
    print('************************')

    print(parallel_1)
    reflect(parallel_1, -1, 1)
    rotate(parallel_1, 180)
    print("Parallelogram reflected across x-axis and rotated 180 deg clockwise")
    print(parallel_1)
    print('************************')