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


def cells() :
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
                float c = .1/cos((v_tex.x*32.+(time/50.)*100.));
                c += .1/cos((v_tex.y*32.+(time/50.)*100.));
                c += sin(v_tex.x*30.);

	            gl_FragColor = vec4(0,c,0,1.0 );
            }

        '''
    )

def water() :
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

            #define MAX_ITER 8

            void main()
            {
	            vec2 p = v_tex * 8.0- vec2(30.0);
	            vec2 i = p;
	            float c = 1.0;
	            float inten = .05;
	            for (int n = 0; n < MAX_ITER; n++)
	            {
		            float t = time * (1.0 - (3.0 / float(n+1)));
		            i = p + vec2(cos(t - i.x) + sin(t + i.y), sin(t - i.y) + cos(t + i.x));
		            c += 1.0/length(vec2(p.x / (sin(i.x+t)/inten),p.y / (cos(i.y+t)/inten)));
	            }
	            c /= float(MAX_ITER);
	            c = 1.5-sqrt(c);
	            gl_FragColor = vec4(pow(c, 7.0)) + vec4(0.0, 0.15, 0.25, 1.0);
}
        '''
    )


