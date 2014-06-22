import miniengine
import objects
import shaders

e = miniengine.Engine(800, 600)

plane = objects.plane(30, 30).set_material(shaders.zebro()).translate(0, 0, -60)
cube1 = objects.cube(2, 2, 2).set_material(shaders.simple()).translate(-1.5, 0, -10)
cube2 = objects.cube(2, 2, 2).set_material(shaders.simple()).translate(1.5, 0, -10)


def update(dt):
    cube1.rotate_z(45 * dt).rotate_x(35 * dt)
    cube2.rotate_z(-45 * dt).rotate_x(-35 * dt)
    plane.rotate_z(25 * dt)

def key(k):
    if k=='z' :
        cube1.set_material(shaders.zebro())
        cube2.set_material(shaders.zebro())
    if k=='s' :
        cube1.set_material(shaders.simple())
        cube2.set_material(shaders.simple())



e.set_keyhandler(key)
e.set_update(update)
e.add_object(plane)
e.add_object(cube1)
e.add_object(cube2)

e.loop()
