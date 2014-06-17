from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
import Image                    
import sys
import math

class engine :
    __updateFunction = None
    __frame = 0
    def __init__(self, w, h) :
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
        glutInitWindowSize(w,h)
        glutInitWindowPosition ( 0, 0 )
        glutCreateWindow("miniengine")
        glClearColor(0.0,0.0,0.2,0.0)
        glClearDepth(1.0)                
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_DEPTH_TEST)
        gluPerspective(60.0,float(w)/float(h),1.0,60.0)
        glMatrixMode(GL_MODELVIEW )
        glLoadIdentity()
        gluLookAt(0.0,0.0,0.0,1.0,1.0,1.0,0.0,1.0,0.0)
        glutDisplayFunc(self.__draw)
        glutIdleFunc(self.__update)
        glutKeyboardFunc(self.__key)
        frame = 0
      
    def loop(self) :   
        glutMainLoop()

    def __key(self,*args ):
        if(args[0] == '\033'):
            sys.exit ()

    def __draw(self) :
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
        glutSwapBuffers()

    def __update(self) :
        if(self.__updateFunction) :
            self.__updateFunction(self.__frame)
        self.__frame +=1    
        glutPostRedisplay()   

    def setUpdateHandler(self, hdl):
        self.__updateFunction = hdl    

#########################################################################    
  

def myUpdate(i) :
    print(i)


e = engine(400,400)
e.setUpdateHandler(myUpdate)











e.loop()        














