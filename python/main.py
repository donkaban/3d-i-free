from miniGL import *

e = Engine(800, 600)

t1 = Texture('../data/normal_map1.png')
t2 = Texture('../data/normal_map3.png')

m1 = Material('SIMPLE', '../data/shaders/base.vsh', '../data/shaders/simple.fsh')
m2 = Material('PLAZMA', '../data/shaders/base.vsh', '../data/shaders/plasma.fsh')

back = shapes.plane(80, 60).set_material(m2).set_texture([t1]).translate(0, 0, -80)
sph = shapes.sphere(4, 32).set_material(m1).set_texture([t2]).translate(0, 0, -10)


def update(dt):
  sph.rotate_y(-10 * dt).rotate_z(-15 * dt)

e.set_update(update)
e.loop()

