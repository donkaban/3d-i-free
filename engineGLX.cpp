#include "miniengine.h"

#include <X11/Xlib.h>
#include <X11/Xatom.h>
#include <X11/Xutil.h>

#include <GL/glext.h>
#include "GL/glx.h"

#include <cstring> 
#include <stdexcept>

static struct 
{
    Display  * display;
    Window     window;
    Window     root;    
    int        screen;
    Visual   * visual; 
    GLXContext context;
} data;

engine::~engine()
{
    glXDestroyContext(data.display, data.context);
    XDestroyWindow(data.display, data.window);
}

engine::engine(uint w, uint h) :
    width(w),
    height(h),
    curTime(std::chrono::system_clock::now())
{
    // создали нативное X11 окно
    
    XSetWindowAttributes attr; 
    data.display = XOpenDisplay(NULL);
    if(!data.display) 
       throw std::runtime_error("can't open X11 display");
    data.root   = XDefaultRootWindow(data.display);
    data.screen = XDefaultScreen(data.display);
    data.visual = XDefaultVisual(data.display, data.screen);
    data.window = XCreateSimpleWindow(data.display,data.root,0,0,width, height,0,0,0);
    
    // Настраиваем окно, обрабатываемые события, декорация и пр

    std::memset(&attr,0,sizeof(attr));
    attr.event_mask = StructureNotifyMask|ButtonPressMask|ButtonReleaseMask|Button1MotionMask|KeyPressMask;
    attr.background_pixel   = 0xFFFF0000;
    XWithdrawWindow(data.display,data.window, data.screen);  
    XChangeWindowAttributes(data.display,data.window,CWBackPixel|CWOverrideRedirect|CWSaveUnder|CWEventMask|CWBorderPixel, &attr);
    XMapWindow(data.display,data.window);
    XFlush(data.display); // немного паранойи

    // получаем GL контекст с помощью GLX
    
    int glx_attr[] = 
    {
        GLX_DOUBLEBUFFER,
        GLX_USE_GL,      True,
        GLX_RGBA,        True,
        GLX_BUFFER_SIZE, 32,
        GLX_DEPTH_SIZE,  24,
        None
    };
    auto visual = glXChooseVisual(data.display, data.screen, glx_attr);
    if(!visual)
       throw std::runtime_error("[GLX] unable to find visual");
    data.context = glXCreateContext(data.display, visual, NULL, True);
    if(!data.context)
       throw std::runtime_error("[GLX] unable to create window context");
    glXMakeCurrent(data.display, data.window, data.context);

    // задаем GL вьюпорт во все окно

    glViewport(0, 0, static_cast<GLsizei>(width), static_cast<GLsizei>(height));
}

bool engine::update()
{
    std::chrono::duration<float> dt(std::chrono::system_clock::now() - curTime);
   
    // обработаем пользовательский ввод
   
    XEvent evt;
    for (int i = 0; i < XPending(data.display); i++)
    { 
        XNextEvent(data.display, &evt);
        switch (evt.type)
        {
            case KeyPress:
            {
                auto event = reinterpret_cast<XKeyEvent *>(&evt);
                if(event->keycode == 61) return false;
                break;
            }
            default:
                break;
        }
    }

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);   // стерли буффер
    if(onDraw) onDraw(dt.count());                      // позвали что-то, что рисует
    glXSwapBuffers(data.display,data.window);           // показали буффер
    
    curTime = std::chrono::system_clock::now();
    return true;
}

