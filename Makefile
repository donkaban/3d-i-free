# HOST - MACOS,LINUX

HOST 	= LINUX
TARGET	= ./test

# -------------------------------------------------------------------------------------------

SOURCES = engineGLX.cpp main.cpp
HEADERS = minimath.h miniengine.h

CXX = g++
CXX_FLAGS = -c -Wall -Wextra -std=c++11 -O3 -DGL_GLEXT_PROTOTYPES -DHOST_$(HOST) 

LINUX_CXX_FLAGS  = 
LINUX_LINK_FLAGS = -lX11 -lGL
MACOS_CXX_FLAGS  = -I/opt/X11/include 
MACOS_LINK_FLAGS = -L/opt/X11/lib -lX11 -lGL


OBJECTS=$(SOURCES:.cpp=.o)

all: $(SOURCES) $(HEADERS) $(TARGET) Makefile
	rm -f $(OBJECTS)

$(TARGET): $(OBJECTS) $(HEADERS)  Makefile
	$(CXX) $(OBJECTS) $($(HOST)_LINK_FLAGS) -o $@
	
.cpp.o: $(SOURCES)  $(HEADERS) 
	$(CXX) $(CXX_FLAGS) $($(HOST)_CXX_FLAGS)  -c -o $@ $<

clean:
	rm -f $(TARGET)
	rm -f $(OBJECTS)

	

	