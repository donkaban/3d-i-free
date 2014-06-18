from miniengine import *

def createPlane(width,height):
    w = (float)(width)/2.0
    h = (float)(height)/2.0
    return Mesh(
    [
        -w, h, 0.0,  0.0, 0.0,
        -w,-h, 0.0,  0.0, 1.0,
         w,-h, 0.0,  1.0, 1.0,
         w, h, 0.0,  1.0, 0.0
    ],
    [0,1,3,2,3,1])