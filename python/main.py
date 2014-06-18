from miniengine import *


def my_update(i):
    print(i)

e = Engine(400, 400)

e.set_update(my_update)

m = Material(
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