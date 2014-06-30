from miniGL import *

e = Engine(800, 600)

t1 = Texture('../data/synqera.png')
t2 = Texture('../data/earth.png')

m1 = Material('SIMPLE', '../data/shaders/base.vsh', '../data/shaders/simple.fsh')
m2 = Material('STARS',  '../data/shaders/base.vsh', '../data/shaders/stars.fsh')

back = geometry.plane(80, 60).set_material(m2).set_texture([t1]).translate(0, 0, -80)
sph = geometry.sphere(4, 32).set_material(m1).set_texture([t2,t1]).translate(0, 0, -10)


def update(dt):
  sph.rotate_y(-10 * dt).rotate_z(-15 * dt)

e.set_update(update)
e.loop()
