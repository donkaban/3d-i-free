env = Environment()

env.Append(CPPFLAGS  = [
	'-Wall', 
	'-Wextra',
	'-std=c++11',
	'-DGL_GLEXT_PROTOTYPES',
	'-I/opt/X11/include'
])

env.Append(LINKFLAGS = ['-L/opt/X11/lib'])
env.Append(LIBS =['X11', 'GL'])


env.Program('test',['engineGLX.cpp','main.cpp'])