from OpenGL.GL import *
from PIL import Image
class Texture():
    __id = None
    __cache = {}

    def __init__(self, filename):
        if filename in Texture.__cache:
            print 'load texture {0:s} from cache'.format(tag)
            self.__id = Texture.__cache[filename]
        else:
            image = Image.open(filename)
            w = image.size[0]
            h = image.size[1]
            image = image.tostring("raw", "RGBX", 0, -1)
            self.__id = glGenTextures(1)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            glBindTexture(GL_TEXTURE_2D, self.__id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            Texture.__cache[filename] = self.__id
            print 'create texture {0:s}; w: {1:d} h:{2:d}'.format(filename, w, h)

    @property
    def id(self):
        return self.__id