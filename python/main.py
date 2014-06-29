from miniGL import *

e = Engine(800, 600)

t1 = Texture('../data/synqera.png')
t2 = Texture('../data/earth.png')
m1 = Material('SIMPLE', '../data/shaders/base.vsh', '../data/shaders/simple.fsh')

back = geometry.plane(80, 60).set_material(m1).set_texture([t1]).translate(0, 0, -80)
earth = geometry.sphere(4,32).set_material(m1).set_texture([t2]).translate(0, 0, -10)

def update(dt):
    earth.rotate_z(-15 * dt).rotate_y(10 * dt)


e.set_update(update)
e.loop()
