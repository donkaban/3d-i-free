from OpenGL.GL import *
from OpenGL.GLUT import *

class Material:
    __id = None
    __cache = {}

    def __init__(self, tag, vertex, fragment):
        if tag in Material.__cache:
            print 'load material {0:s} from cache'.format(tag)
            self.__id = Material.__cache[tag]
        else:
            v_str = open(vertex).read()
            f_str = open(fragment).read()
            vsh = self.__compile(v_str, GL_VERTEX_SHADER)
            fsh = self.__compile(f_str, GL_FRAGMENT_SHADER)
            self.__id = self.__link(vsh, fsh)
            Material.__cache[tag] = self.__id
            print 'create material {0:s}'.format(tag)

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
        pos_id = glGetAttribLocation(self.__id, 'position')
        tex_id = glGetAttribLocation(self.__id, 'texcoord')
        nor_id = glGetAttribLocation(self.__id, 'normal')
        if pos_id != -1:
            glVertexAttribPointer(pos_id, 3, GL_FLOAT, GL_FALSE, 32, None)
            glEnableVertexAttribArray(pos_id)
        if tex_id != -1:
            glVertexAttribPointer(tex_id, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
            glEnableVertexAttribArray(tex_id)
        if nor_id != -1:
            glVertexAttribPointer(nor_id, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(20))
            glEnableVertexAttribArray(nor_id)

    def set_uniform_matrix(self, k, value):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniformMatrix4fv(uid, 1, GL_FALSE, value)

    def set_uniform_vec4(self, k, x, y, z, w):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniform4f(uid, x, y, z, w)

    def set_uniform_vec3(self, k, x, y, z):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniform3f(uid, x, y, z)

    def set_uniform_float(self, k, value):
        uid = glGetUniformLocation(self.__id, k)
        if uid != -1:
            glUniform1f(uid, value)

    def set_texture(self, num, texture):
        t = [GL_TEXTURE0, GL_TEXTURE1, GL_TEXTURE2, GL_TEXTURE3]
        n = ['texture0', 'texture1', 'texture2', 'texture3']
        uid = glGetUniformLocation(self.__id, n[num])
        if uid != -1:
            glActiveTexture(t[num])
            glBindTexture(GL_TEXTURE_2D, texture.id)
            glUniform1i(uid, num)

    @property
    def id(self):
        return self.__id
