from miniengine import *

def simple() :
    return Material(
        '''
            attribute vec3 pos;
            attribute vec2 tex;
            uniform   mat4 modelView;
            uniform   mat4 prjView;
            varying   vec3 v_pos;
            varying   vec2 v_tex;

            void main()
            {
                v_tex=tex;
                v_pos=(pos + 1.)/2.0;
                gl_Position = vec4(pos,1) * modelView * prjView;
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;
            varying vec3 v_pos;

            void main()
            {
                gl_FragColor = vec4(v_pos,1);
            }
        '''
    )


def zebro() :
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            uniform mat4 modelView;
            uniform mat4 prjView;

            varying   vec2  v_tex;
            void main()
            {
                v_tex=tex;
                gl_Position = vec4(pos,1) * modelView * prjView;
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
                gl_FragColor = vec4(z,sin(time),cos(time),1);
           }
        '''
    )



