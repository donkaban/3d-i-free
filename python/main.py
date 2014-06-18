from objects import *
import shaders

e = Engine(800, 600)

plane = createPlane(2,2).set_material(shaders.zebro())
tri = createTriangle(1).set_material(shaders.simple())
e.add_object(plane)
e.add_object(tri)

e.loop()

