from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.arrays import ArrayDatatype as ARR
import numpy

from material import  Material
from engine import Engine
from matrix import mat4

class Mesh:
    __verts = None
    __ndx = None
    __material = None
    __id = None
    __T = None

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

    def draw(self):
        glUseProgram(self.__material.id)
        glBindBuffer(GL_ARRAY_BUFFER, self.__id[0])
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__id[1])
        t = glGetUniformLocation(self.__material.id, 'time')

        if t != -1:
            glUniform1f(t, Engine.get_time())
        if self.__material.mv != -1:
            glUniformMatrix4fv(self.__material.mv, 1, GL_FALSE, self.__T.ptr)
        if self.__material.pv != -1:
            glUniformMatrix4fv(self.__material.pv, 1, GL_FALSE, Engine.camera.ptr)

        glVertexAttribPointer(self.__material.pos, 3, GL_FLOAT, GL_FALSE, 20, None)
        glEnableVertexAttribArray(self.__material.pos)
        glVertexAttribPointer(self.__material.tex, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))
        glEnableVertexAttribArray(self.__material.tex)
        glDrawElements(GL_TRIANGLES, ARR.arrayByteCount(self.__ndx) * 2, GL_UNSIGNED_SHORT, None)
        if glGetError() != GL_NO_ERROR:
            raise RuntimeError('draw error!')

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

