from OpenGL.GL import *
from OpenGL.GLUT import *

class Material:
    __id = None
    __attributes = {}
    __cache = {}

    def __init__(self, tag, vertex, fragment):
        if tag in Material.__cache:
            print 'load material {0:s}'.format(tag)
            self.__id = Material.__cache[tag]
        else:
            vsh = self.__compile(vertex, GL_VERTEX_SHADER)
            fsh = self.__compile(fragment, GL_FRAGMENT_SHADER)
            self.__id = self.__link(vsh, fsh)
            self.__add_attribute('position')
            self.__add_attribute('texcoord')
            Material.__cache[tag] = self.__id
            print 'create material {0:s}'.format(tag)

    def __add_attribute(self, tag):
        self.__attributes[tag] = glGetAttribLocation(self.__id, tag)

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
        pos_id = self.__attributes['position']
        tex_id = self.__attributes['texcoord']
        if pos_id != -1:
            glVertexAttribPointer(pos_id, 3, GL_FLOAT, GL_FALSE, 20, None)
            glEnableVertexAttribArray(pos_id)
        if tex_id != -1:
            glVertexAttribPointer(tex_id, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))
            glEnableVertexAttribArray(tex_id)

    def set_uniform_matrix(self, k, value):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniformMatrix4fv(uid, 1, GL_FALSE, value)

    def set_uniform_vec4(self, k, x, y, z, w):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniform4f(uid, x, y, z, w)

    def set_uniform_vec3(self, k, x,y,z):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniform3f(uid, x, y, z)

    def set_uniform_float(self, k, value):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniform1f(uid, value)

    def set_texture(self, k, texture):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, texture.id)
            glUniform1i(uid, 0)

    @property
    def id(self):
        return self.__id
