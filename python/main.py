from miniengine import *


def my_update(i):
    print(i)

e = engine(400, 400)

e.setUpdateHandler(my_update)

m = material(
    '''
        attribute vec4 position;
        void main()
        {
            gl_Position = position;
        }
    ''',

    '''
        void main()
        {
            gl_FragColor = vec4(1,0,0,1);
        }


    '''
)

e.loop()