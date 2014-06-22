from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.arrays import ArrayDatatype as ARR
import time
from matrix import mat4
import numpy


class Engine:
    __updateFunction = None
    __keyboardFunction = None
    __mouseFunction = None
    __objects = []
    __time = time.time()
    __delta = 0
    camera = None

    def __init__(self, w, h, fullscreen=False):
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
        glutKeyboardFunc(self.__key)
        Engine.camera = mat4()


    def __key(self, *args):
        if args[0] == '\033':
            sys.exit()
        elif self.__keyboardFunction:
            self.__keyboardFunction(args[0])

    @staticmethod
    def __resize(w, h):
        print 'resize {0:d}x{1:d}'.format(w, h)
        Engine.camera.perspective(35, w / h, 0.1, 100)
        glViewport(0, 0, w, h)

    def __draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for obj in self.__objects:
            obj.draw()
        glutSwapBuffers()

    def __update(self):
        if self.__updateFunction:
            self.__updateFunction(Engine.get_time() - self.__delta)
        self.__delta = Engine.get_time()
        glutPostRedisplay()

    def set_update(self, hdl):
        self.__updateFunction = hdl

    def set_keyhandler(self, hdl):
        self.__keyboardFunction = hdl

    def add_object(self, obj):
        assert isinstance(obj, Mesh)
        self.__objects.append(obj)

    @staticmethod
    def loop():
        glutMainLoop()

    @staticmethod
    def get_time():
        t = time.time() - Engine.__time
        return t


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

    def rotate_x(self, a):
        self.__T.rotate_x(a)
        return self

    def rotate_y(self, a):
        self.__T.rotate_y(a)
        return self

    def rotate_z(self, a):
        self.__T.rotate_z(a)
        return self

    def hide(self):
        self.__visible = False