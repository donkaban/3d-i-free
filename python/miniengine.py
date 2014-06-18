from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.arrays import ArrayDatatype as ARR
import numpy
import time


class Engine:
    __updateFunction = None
    __frame = 0
    __objects = []
    __time = time.time()

    def __init__(self, w, h):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(w, h)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("miniengine")
        glClearColor(0.0, 0.1, 0.1, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glutDisplayFunc(self.__draw)
        glutReshapeFunc(self.__resize)
        glutIdleFunc(self.__update)
        glutKeyboardFunc(self.__esc)

    @staticmethod
    def __esc(*args):
        if args[0] == '\033':
            sys.exit()

    def __resize(self, w, h):
        print 'resize {0:d}x{1:d}'.format(w, h)
        glViewport(0, 0, w, h)

    def __draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for obj in self.__objects:
            obj.draw()
        glutSwapBuffers()

    def __update(self):
        if self.__updateFunction:
            self.__updateFunction(self.__frame)
        self.__frame += 1
        glutPostRedisplay()

    def set_update(self, hdl):
        self.__updateFunction = hdl

    def add_object(self, obj):
        assert isinstance(obj, Mesh)
        self.__objects.append(obj)

    @staticmethod
    def loop():
        glutMainLoop()

    @staticmethod
    def getTime():
        t = time.time() -Engine.__time
        return t


class Material:
    __id = None
    __pos = None
    __tex = None

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


class Mesh:
    __verts = None
    __ndx = None
    __material = None
    __id = None

    def __init__(self, v, i):
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

        t = glGetUniformLocation(self.__material.id,'time')
        if t != -1 :
            glUniform1f(t,Engine.getTime())

        glVertexAttribPointer(self.__material.pos, 3, GL_FLOAT, GL_FALSE, 20, None)
        glEnableVertexAttribArray(self.__material.pos)
        glVertexAttribPointer(self.__material.tex, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))
        glEnableVertexAttribArray(self.__material.tex)
        glDrawElements(GL_TRIANGLES, ARR.arrayByteCount(self.__ndx) * 2, GL_UNSIGNED_SHORT, None)
        if glGetError() != GL_NO_ERROR:
            raise RuntimeError('draw error!')
