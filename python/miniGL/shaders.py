from material import Material

def simple() :
    return Material('SIMPLE',
        '''
            attribute vec3 position;
            attribute vec2 texcoord;
            uniform   mat4 modelView;
            uniform   mat4 prjView;
            varying   vec2 v_tex;

            void main()
            {
                v_tex=texcoord;
                gl_Position = vec4(position,1) * modelView * prjView;
            }
        ''',
        '''
            uniform sampler2D texture0;

            varying vec2  v_tex;

            void main()
            {
                gl_FragColor = texture2D(texture0, v_tex);
            }
        '''
    )


def cells() :
    return Material('GREEN CELLS',
        '''
            attribute vec3  position;
            attribute vec2  texcoord;
            uniform mat4 modelView;
            uniform mat4 prjView;

            varying   vec2  v_tex;
            void main()
            {
                v_tex=texcoord;
                gl_Position = vec4(position,1) * modelView * prjView;
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
    return Material('WATER',
        '''
            attribute vec3  position;
            attribute vec2  texcoord;
            uniform mat4 modelView;
            uniform mat4 prjView;

            varying   vec2  v_tex;
            void main()
            {
                v_tex=texcoord;
                gl_Position = vec4(position,1) * modelView * prjView;
            }
        ''',
        '''
            uniform sampler2D texture0;
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
	            vec4 col = texture2D(texture0, v_tex);
	            gl_FragColor = col + vec4(pow(c, 7.0)) + vec4(0.0, 0.15, 0.2, 1.0);
}
        '''
    )


