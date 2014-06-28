from miniGL import *

e = Engine(800, 600)

t1 = Texture('../data/synqera.png')
t2 = Texture('../data/ifree.png')
m1 = Material('SIMPLE', '../data/shaders/base.vsh', '../data/shaders/simple.fsh')

e.add_object(geometry.plane(40, 40).set_material(m1).translate(0, 0, -60))

cubes = []
for x in range(-1, 2):
    for y in range(-1, 2):
        cube = geometry.cube(.6, .6, .6).set_material(m1).translate(x, y, -5).set_texture([t1,t2])
        if y == 0:
            cube.set_material(m1).set_texture([t2,t1])
        cubes.append(cube)
        e.add_object(cube)


def update(dt):
    for cube in cubes:
        cube.rotate_z(45 * dt).rotate_x(45 * dt)


e.set_update(update)
e.loop()
