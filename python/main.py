import miniengine
import objects
import shaders

e = miniengine.Engine(800, 600)

e.add_object(objects.plane(2, 2).set_material(shaders.zebro()))
e.add_object(objects.triangle(1).set_material(shaders.simple()))

e.loop()
