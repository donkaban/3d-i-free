from OpenGL.GL import *
from OpenGL.GLUT import *

class Material:
    __id = None
    __attributes = {}

    def __init__(self, name, vertex, fragment):
        vsh = self.__compile(vertex, GL_VERTEX_SHADER)
        fsh = self.__compile(fragment, GL_FRAGMENT_SHADER)
        self.__id= self.__link(vsh, fsh)
        self.__add_attribute('position')
        self.__add_attribute('texcoord')
        print 'create material {0:s}'.format(name)

    def __add_attribute(self, name):
        self.__attributes[name] = glGetAttribLocation(self.__id, name)

    @staticmethod
    def __compile(source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        result = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if not result:
            raise RuntimeError('shader compile error : {0:s}'.format(glGetShaderInfoLog(shader)))
        return shader

    @staticmethod
    def __link(vsh, fsh):
        prg = glCreateProgram()
        glAttachShader(prg, vsh)
        glAttachShader(prg, fsh)
        glLinkProgram(prg)
        glValidateProgram(prg)
        if glGetProgramiv(prg, GL_VALIDATE_STATUS) == GL_FALSE:
            raise RuntimeError('shader link error : {0:s}'.format(glGetProgramInfoLog(prg)))
        return prg

    def set_attributes(self):
        p = self.__attributes['position']
        t = self.__attributes['texcoord']
        if (p != -1):
            glVertexAttribPointer(p, 3, GL_FLOAT, GL_FALSE, 20, None)
            glEnableVertexAttribArray(p)
        if (t != -1):
            glVertexAttribPointer(t, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))
            glEnableVertexAttribArray(t)

    def set_uniform_matrix(self, k, value):
       id = glGetUniformLocation(self.__id,k)
       if id != -1:
            glUniformMatrix4fv(id, 1, GL_FALSE, value)

    def set_uniform_float(self, k, value):
       id = glGetUniformLocation(self.__id,k)
       if id != -1:
            glUniform1f(id, value)

    def set_texture(self,k,texture):
        id = glGetUniformLocation(self.__id,k)
        if id != -1:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, texture.id)
            glUniform1i(id,0)


    @property
    def id(self):
        return self.__id


