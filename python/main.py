import miniengine
import objects
import shaders

e = miniengine.Engine(800, 600)

plane = objects.plane(30, 30).set_material(shaders.zebro()).translate(0,0,-60)
cube  = objects.cube(2,2,2).set_material(shaders.simple()).translate(0,0,-10)

def update(dt):
    cube.rotate_z(45 * dt)
    cube.rotate_x(35 * dt)
    cube.scale(1.001,1.001,1.001)

e.set_update(update)
e.add_object(plane)
e.add_object(cube)

e.loop()
