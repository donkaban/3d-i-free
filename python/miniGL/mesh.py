from OpenGL.GL import *
from OpenGL.arrays import ArrayDatatype as adt
import numpy
from material import Material
from engine import Engine
from matrix import mat4

class Mesh:
    __v_hdl = None       # vertex buffer handler
    __i_hdl = None       # index buffer handlwr
    __i_size = None      # index buffer size
    __T = None           # object transform matrix
    __material = None    # object material
    __texture = []       # object textures

    def __init__(self, v, i):
        self.__T = mat4()
        v_buff = numpy.array(v, dtype=numpy.float32)
        i_buff = numpy.array(i, dtype=numpy.int16)
        self.__v_hdl = glGenBuffers(1)
        self.__i_hdl = glGenBuffers(1)
        self.__i_size = adt.arrayByteCount(i_buff) * 2

        glBindBuffer(GL_ARRAY_BUFFER, self.__v_hdl)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__i_hdl)
        glBufferData(GL_ARRAY_BUFFER, adt.arrayByteCount(v_buff), adt.voidDataPointer(v_buff), GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, adt.arrayByteCount(i_buff), adt.voidDataPointer(i_buff), GL_STATIC_DRAW)
        if glGetError() != GL_NO_ERROR:
            raise RuntimeError('mesh create error!')
        Engine.get().add_object(Engine.get(), self)

    def set_material(self, mat):
        assert isinstance(mat, Material)
        self.__material = mat
        return self

    def set_texture(self, textures):
        self.__texture = textures
        return self

    def draw(self):
        if not self.__material:
            return
        glUseProgram(self.__material.id)
        glBindBuffer(GL_ARRAY_BUFFER, self.__v_hdl)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__i_hdl)
        self.__material.set_attributes()
        self.__material.set_uniform_float('time', Engine.get_time())
        self.__material.set_uniform_matrix('modelView', self.__T.ptr)
        self.__material.set_uniform_matrix('prjView', Engine.camera.ptr)

        for tex in self.__texture:
            ndx = self.__texture.index(tex)
            self.__material.set_texture(ndx, tex)
        glDrawElements(GL_TRIANGLES, self.__i_size , GL_UNSIGNED_SHORT, None)

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

