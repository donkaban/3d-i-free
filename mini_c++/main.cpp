#include "minimath.h"
#include "miniengine.h"
#include <iostream>

int main()
{
    engine e(800,600);

    e.setDrawCallback([](float dt)
    {
        auto color = vec3(rnd_norm(),rnd_norm(),rnd_norm());
        std::cout << color << "  frametime : " << dt << std::endl;
        glClearColor(color.r,color.g,color.b,1);

    });

    while(e.update()) {}
    return 0;
}