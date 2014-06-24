from mesh import Mesh

def plane(width, height):
    w = float(width) / 2.0
    h = float(height) / 2.0
    return Mesh([
        -w,  h, 0.0,    0.0, 0.0,
        -w, -h, 0.0,    0.0, 1.0,
         w, -h, 0.0,    1.0, 1.0,
         w,  h, 0.0,    1.0, 0.0],
        [0, 1, 3, 2, 3, 1])

def cube(width,height, tin):
    w = float(width)  / 2.
    h = float(height) / 2.
    z = float(tin)    / 2.
    return Mesh([
         -w, -h,  z, 0, 0,
          w, -h,  z, 1, 0,
         -w, -h, -z, 0, 1,
          w, -h, -z, 1, 1,
         -w, -h, -z, 1, 0,
         -w,  h, -z, 0, 0,
          w,  h, -z, 1, 0,
          w, -h, -z, 0, 0,
         -w, -h,  z, 1, 1,
         -w,  h,  z, 0, 1,
          w,  h,  z, 1, 1,
          w, -h,  z, 0, 1,
         -w, -h,  z, 0, 0,
          w, -h,  z, 1, 0,],
        [0,3,1,0,2,3,2,6,3,2,5,6,4,8,9,4,9,5,5,9,10,5,10,6,6,10,11,6,11,7,9,12,13,9,13,10])
