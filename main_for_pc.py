from glitch import *
import random as r
from PIL import Image
from os import listdir

r.seed()
n = Image.open([x for x in listdir('.') if x.endswith('.png') or x.endswith('.jpg')][0])
width = n.size[0]
height = n.size[1]


# fuck_up_colors(n).show()

y0 = int(height * 0.25)
x0 = int(width * 0.255)
gl_widt = int(width * 0.2)
gl_heigth = int(height * 0.4)

# for i in xrange(500):
#     # x=[r.randint(x0, x0+gl_widt), r.randint(x0, x0+gl_widt)]
#     dy = int(0.005 * height)
#     y = [r.randint(y0, y0 + gl_heigth - dy)]
#     if y[0] - y0 < gl_heigth / 2:
#         dx = int(0.5 * (y0 + gl_heigth - y[0]))
#     else:
#         dx = int(0.5 * (y[0] - y0))
#     x = [x0 + dx, r.randint(x0, x0 + gl_widt) + dx]
#     y.append(y[0] + dy)
#     x.sort()
#     if i % 3 == 0:
#         glitch_red(n, r.randint(-5, 5), x[0], y[0], x[1], y[1])
#         glitch_shift_right(n, r.randrange(25), x[0], y[0], x[1], y[1])
#     elif i % 2 == 0:
#         glitch_blue(n, r.randint(-25, 25), x[0], y[0], x[1], y[1])
#         glitch_shift_right(n, r.randrange(15), x[0], y[0], x[1], y[1])
#     else:
#         glitch_green(n, r.randint(-5, 5), x[0], y[0], x[1], y[1])
#         glitch_shift_right(n, r.randrange(5), x[0], y[0], x[1], y[1])

# for i in xrange(20):
#     glitch_shift(n, i * 2, x0, y0 + 2 * i + r.randint(-2, 2), x0 + gl_widt + r.randint(-15, 15),
#                  y0 + 5 + 2 * i + r.randint(-2, 2))

# n.show()
fuck_up_colors3(n, n=256).show()
