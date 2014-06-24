from miniGL import *

e = Engine(800, 600)

t1 = Texture('data/synqera.png')
t2 = Texture('data/ifree.png')

e.add_object(objects.plane(40, 40).set_material(shaders.cells()).translate(0, 0, -60))

cubes = []
for x in range(-1, 2):
    for y in range(-1, 2):
        cube = objects.cube(.6, .6, .6).set_material(shaders.water()).translate(x, y, -5).set_texture(t1)
        if y == 0:
            cube.set_material(shaders.simple()).set_texture(t2)
        cubes.append(cube)
        e.add_object(cube)


def update(dt):
    for cube in cubes:
        cube.rotate_z(45 * dt).rotate_x(45 * dt)


e.set_update(update)
e.loop()
