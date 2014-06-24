from OpenGL.GL   import *
import Image

class Texture():
    __id = None

    def __init__(self,fileName):
        image  = Image.open(fileName)
        w = image.size[0]
        h = image.size[1]
        image  = image.tostring("raw","RGBX",0,-1)
        self.__id = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glBindTexture(GL_TEXTURE_2D,self.__id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
        print 'create texture {0:s}; w: {1:d} h:{2:d}'.format(fileName,w,h)

    @property
    def id(self):
        return self.__id