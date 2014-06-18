from miniengine import *
from math import *


def plane(width, height):
    w = float(width) / 2.0
    h = float(height) / 2.0
    return Mesh(
        [
            -w,  h, 0.0,    0.0, 0.0,
            -w, -h, 0.0,    0.0, 1.0,
             w, -h, 0.0,    1.0, 1.0,
             w,  h, 0.0,    1.0, 0.0
        ],
        [0, 1, 3, 2, 3, 1])


def triangle(radius):
    y = float(radius) * -sin(degrees(30))
    x = float(radius) * cos(degrees(30))
    return Mesh(
        [
            -x,   -y,   0.0,  0.0, 0.0,
             x,   -y,   0.0,  0.0, 1.0,
            .0, radius, 0.0,  0.5, 1.0
        ],
        [0, 1, 2])
