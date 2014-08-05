from mesh import Mesh
from math import *

def plane(width, height):
    w = float(width) / 2.0
    h = float(height) / 2.0
    return Mesh([
                -w, h, 0,   0, 1,    0, 0, 1,
                -w,-h, 0,   0, 0,    0, 0, 1,
                 w,-h, 0,   1, 0,    0, 0, 1,
                 w, h, 0,   1, 1,    0, 0, 1],
                [0, 1, 3, 2, 3, 1])


def cube(width, height, tin):
    w = float(width) / 2.
    h = float(height) / 2.
    z = float(tin) / 2.
    return Mesh([
                   -w, -h,  z,  0, 0, 0, 0, 1,
                    w, -h,  z,  1, 0, 0, 0, 1,
                   -w, -h, -z,  0, 1, 0, 0, 1,
                    w, -h, -z,  1, 1, 0, 0, 1,
                   -w, -h, -z,  1, 0, 0, 0, 1,
                   -w,  h, -z,  0, 0, 0, 0, 1,
                    w,  h, -z,  1, 0, 0, 0, 1,
                    w, -h, -z,  0, 0, 0, 0, 1,
                   -w, -h,  z,  1, 1, 0, 0, 1,
                   -w,  h,  z,  0, 1, 0, 0, 1,
                    w,  h,  z,  1, 1, 0, 0, 1,
                    w, -h,  z,  0, 1, 0, 0, 1,
                   -w, -h,  z,  0, 0, 0, 0, 1,
                    w, -h,  z,  1, 0, 0, 0, 1,],
    [0, 3, 1, 0, 2, 3, 2, 6, 3, 2, 5, 6, 4, 8, 9, 4, 9, 5, 5, 9, 10, 5, 10, 6, 6, 10, 11, 6, 11, 7, 9, 12,13, 9, 13, 10])


def sphere(radius, slices):
    step = (pi * 2) / float(slices)
    parallels = slices / 2
    r = radius / 1.5
    v = []
    n = []
    for i in range(0, parallels + 1, 1):
        for j in range(0, slices + 1, 1):
            x = r * sin(step * i) * sin(step * j)
            y = r * cos(step * i)
            z = r * sin(step * i) * cos(step * j)
            v.append([x, y, z, j / float(slices), i / float(parallels), x / r, y / r, z / r])
    for i in range(0,slices/2, 1):
        for j in range(0, slices,1):
            n.append((i * (slices + 1) + j))
            n.append(((i + 1) * (slices + 1) + j))
            n.append(((i + 1) * (slices + 1) + (j + 1)))
            n.append((i * (slices + 1) + j))
            n.append(((i + 1) * (slices + 1) + (j + 1)))
            n.append((i * (slices + 1) + (j + 1)))
    return Mesh(v, n)


