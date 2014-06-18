from OpenGL.GL import *
from OpenGL.GLUT import *


class Engine:
    __updateFunction = None
    __frame = 0
    __objects = []

    def __init__(self, w, h):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(w, h)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("miniengine")
        glClearColor(0.0, 0.0, 0.2, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        glutDisplayFunc(self.__draw)
        glutIdleFunc(self.__update)
        glutKeyboardFunc(self.__esc)

    @staticmethod
    def __esc(*args):
        if args[0] == '\033':
            sys.exit()

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
        assert isinstance(obj, object)
        self.__objects.append(obj)

    @staticmethod
    def loop():
        glutMainLoop()


class Material:
    __id = None

    def __init__(self, vertex, fragment):
        vsh = self.__compile(vertex, GL_VERTEX_SHADER)
        fsh = self.__compile(fragment, GL_FRAGMENT_SHADER)
        self.__id = self.__link(vsh, fsh)

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
        prog = glCreateProgram()
        glAttachShader(prog, vsh)
        glAttachShader(prog, fsh)
        glLinkProgram(prog)
        glValidateProgram(prog)
        if (glGetProgramiv(prog, GL_VALIDATE_STATUS) == GL_FALSE):
            raise RuntimeError('shader error : %s' % glGetProgramInfoLog(self.__id))
        return prog

    @property
    def id(self):
        return self.__id


# vertex : x,y,z,s,t

class Mesh:
    vertexes = []
    indexes = []
    textures = []
    material = None

    def __init__(self, v, i):
        self.vertexes = v
        self.indexes = i

    def draw(self):
        pass
