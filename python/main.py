from miniengine import *
from objects import *
import shaders

e = Engine(400, 400)

plane = createPlane(1,1).set_material(shaders.zebro())

e.add_object(plane)
e.loop()

