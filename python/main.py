import miniengine
import objects
import shaders

e = miniengine.Engine(800, 600)

e.add_object(objects.plane(40, 40).set_material(shaders.cells()).translate(0, 0, -60))

cubes = []
for x in range (-1,2):
    for y in range (-1,2):
        cube = objects.cube(.6, .6, .6).set_material(shaders.water()).translate(x, y, -4)
        cubes.append(cube)
        e.add_object(cube)



def update(dt):
    for cube in cubes :
        cube.rotate_z(45 * dt).rotate_x(45 * dt)

def key(k):
    pass
    if k=='z' :
        for cube in cubes :
            cube.set_material(shaders.zebro())
    if k=='s' :
        for cube in cubes :
            cube.set_material(shaders.simple())

e.set_keyhandler(key)
e.set_update(update)

e.loop()
