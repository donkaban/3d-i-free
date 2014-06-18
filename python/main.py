from objects import *
import shaders

e = Engine(800, 600)

e.add_object(createPlane(2,2).set_material(shaders.zebro()))
e.add_object(createTriangle(1).set_material(shaders.simple()))

e.loop()

