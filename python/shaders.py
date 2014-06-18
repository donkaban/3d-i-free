from miniengine import *


def zebro() :
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            varying   vec2  v_tex;
            void main()
            {
                v_tex=tex;
                gl_Position = vec4(pos,1);
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;
            void main()
            {
                float x = 0.5 - v_tex.x;
                float y = 0.5 - v_tex.y;
                float r = (x * x + y * y);
                float z = cos((r +  time * 0.2)/0.01);
                gl_FragColor = vec4(z,z,z,1);
           }
        '''
    )



