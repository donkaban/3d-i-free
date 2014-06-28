#ifndef _MINIENGINE_H_
#define _MINIENGINE_H_

#include <functional>
#include <chrono>

#include <GL/gl.h>

using uint = unsigned int;

class engine
{
    using draw_t = std::function<void(float)>;
    using tpoint = std::chrono::time_point<std::chrono::system_clock>;
public:
    engine(uint,uint);
    ~engine();
    bool update();
    void setDrawCallback(const draw_t &&cb) {onDraw = std::move(cb);}
    
private:
    uint   width;
    uint   height; 
    tpoint curTime;
    draw_t onDraw {};
};




#endif