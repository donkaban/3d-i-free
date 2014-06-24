from OpenGL.GL import *
from OpenGL.GLUT import *

class Material:
    __id = None
    __pos = None
    __tex = None
    __mv = None
    __pv = None

    def __init__(self, vertex, fragment):
        vsh = self.__compile(vertex, GL_VERTEX_SHADER)
        fsh = self.__compile(fragment, GL_FRAGMENT_SHADER)
        self.__id = self.__link(vsh, fsh)
        print 'create material:{0:d}. pos: {1:d} uv: {2:d}'.format(self.__id, self.__pos, self.__tex)

    @staticmethod
    def __compile(source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        result = glGetShaderiv(shader, GL_COMPILE_STATUS)
        if not result:
            raise RuntimeError('compile error : %s' % (glGetShaderInfoLog(shader),))
        return shader

    def __link(self, vsh, fsh):
        prg = glCreateProgram()
        glAttachShader(prg, vsh)
        glAttachShader(prg, fsh)
        glLinkProgram(prg)
        glValidateProgram(prg)
        if glGetProgramiv(prg, GL_VALIDATE_STATUS) == GL_FALSE:
            raise RuntimeError('shader error : %s' % glGetProgramInfoLog(self.__id))
        self.__pos = glGetAttribLocation(prg, 'pos')
        self.__tex = glGetAttribLocation(prg, 'tex')
        self.__pv = glGetUniformLocation(prg, 'prjView')
        self.__mv = glGetUniformLocation(prg, 'modelView')
        return prg

    @property
    def id(self):
        return self.__id

    @property
    def pos(self):
        return self.__pos

    @property
    def tex(self):
        return self.__tex

    @property
    def mv(self):
        return self.__mv

    @property
    def pv(self):
        return self.__pv



