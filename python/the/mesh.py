from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.arrays import ArrayDatatype as ARR
import numpy

from material import  Material
from texture import Texture
from engine import Engine
from matrix import mat4

class Mesh:
    __id = None
    __verts = None
    __ndx = None
    __T = None
    __material = None
    __texture = None

    def __init__(self, v, i):
        self.__T = mat4()
        self.__verts = numpy.array(v, dtype=numpy.float32)
        self.__ndx = numpy.array(i, dtype=numpy.int16)
        self.__id = glGenBuffers(2)
        glBindBuffer(GL_ARRAY_BUFFER, self.__id[0])
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__id[1])
        glBufferData(GL_ARRAY_BUFFER,
                     ARR.arrayByteCount(self.__verts),
                     ARR.voidDataPointer(self.__verts),
                     GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                     ARR.arrayByteCount(self.__ndx),
                     ARR.voidDataPointer(self.__ndx),
                     GL_STATIC_DRAW)
        if glGetError() != GL_NO_ERROR:
            raise RuntimeError('mesh vbo error!')

    def set_material(self, mat):
        assert isinstance(mat, Material)
        self.__material = mat
        return self

    def set_texture(self,texture):
        assert isinstance(texture, Texture)
        self.__texture = texture
        return self

    def draw(self):
        if not self.__material :
            return
        glUseProgram(self.__material.id)
        glBindBuffer(GL_ARRAY_BUFFER, self.__id[0])
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__id[1])
        self.__material.set_attributes()
        self.__material.set_uniform_float('time',Engine.get_time())
        self.__material.set_uniform_matrix('modelView',self.__T.ptr)
        self.__material.set_uniform_matrix('prjView',Engine.camera.ptr)
        if self.__texture:
            self.__material.set_texture('texture0',self.__texture)

        glDrawElements(GL_TRIANGLES, ARR.arrayByteCount(self.__ndx) * 2, GL_UNSIGNED_SHORT, None)

    def translate(self, x, y, z):
        self.__T.translate(x, y, z)
        return self

    def scale(self, x, y, z):
        self.__T.scale(x, y, z)
        return self

    def rotate_x(self, a):
        self.__T.rotate_x(a)
        return self

    def rotate_y(self, a):
        self.__T.rotate_y(a)
        return self

    def rotate_z(self, a):
        self.__T.rotate_z(a)
        return self

