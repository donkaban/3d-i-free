from math import *
from numpy import *
import ctypes

class mat4:
    __M = None

    def __init__(self):
        self.__M = identity(4, dtype=float32)

    @property
    def ptr(self):
        return self.__M.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    def translate(self, x, y, z):
        self.__M = self.__M * matrix([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]],dtype=float32)
    def scale(self, x, y, z):
        self.__M = self.__M * matrix([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]],dtype=float32)

    def rotate_x(self, a):
        s = sin(radians(a))
        c = cos(radians(a))
        self.__M = self.__M * matrix([[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]],dtype=float32)

    def rotate_y(self, a):
        s = sin(radians(a))
        c = cos(radians(a))
        self.__M = self.__M * matrix([[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]],dtype=float32)

    def rotate_z(self, a):
        s = sin(radians(a))
        c = cos(radians(a))
        self.__M = self.__M * matrix([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],dtype=float32);

    def perspective(self,fov, aspect, n, f):
        h = tan(radians(fov) * .5)
        w = h * aspect
        dz = f - n
        self.__M =  matrix([[1./w,0,0,0],[0,1./h,0,0],[0,0,-(f+n)/dz,-2. * f * n / dz],[0,0,-1,0]],dtype = float32)
