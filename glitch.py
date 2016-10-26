# coding: utf-8
def glitch_color(self, delta_x, delta_y, delta_z, min_x, min_y, max_x, max_y):
    if min_x < 0 or min_x > self.size[0]:
        raise ValueError('bad min of x: %f'%min_x)
    if max_x < 0 or max_x > self.size[0]:
        raise ValueError('bad max of x: %f'%max_x)
    if min_y < 0 or min_y > self.size[1]:
        raise ValueError('bad min of y: %f'%min_y)
    if max_y < 0 or max_y > self.size[1]:
        raise ValueError('bad max of y: %f'%max_y)
    pic = self.load()
    for x in xrange(min_x, max_x, 1):
        for y in xrange(min_y, max_y, 1):
            val = pic[x, y]
            pic[x, y] = (val[0] + delta_x, val[1] + delta_y, val[2] + delta_z)


def glitch_red(self, delta_x, min_x, min_y, max_x, max_y):
    glitch_color(self, delta_x, 0, 0, min_x, min_y, max_x, max_y)


def glitch_green(self, delta_x, min_x, min_y, max_x, max_y):
    glitch_color(self, 0, delta_x, 0, min_x, min_y, max_x, max_y)


def glitch_blue(self, delta_x, min_x, min_y, max_x, max_y):
    glitch_color(self, 0, 0, delta_x, min_x, min_y, max_x, max_y)


def glitch_shift_right(self, delta_x, min_x, min_y, max_x, max_y):
    if min_x < 0 or min_x > self.size[0]:
        raise ValueError('bad min of x: %f'%min_x)
    if max_x < 0 or max_x > self.size[0]:
        raise ValueError('bad max of x: %f'%max_x)
    if min_y < 0 or min_y > self.size[1]:
        raise ValueError('bad min of y: %f'%min_y)
    if max_y < 0 or max_y > self.size[1]:
        raise ValueError('bad max of y: %f'%max_y)
    if min_x == max_x:
        return
    buff = self.crop((min_x, min_y, max_x, max_y))
    # print buff.size
    self.paste(buff, (min_x+delta_x, min_y, max_x+delta_x, max_y))
    for y in range(min_y, max_y, 1):
        self.paste(buff.getpixel((0, y - min_y)), (min_x, y, min_x + delta_x, y + 1))


def fuck_up_colors(self, n=128):

    def fun(x):
        x = n * ((x + 1) / n)
        if x == 0:
            return x
        else:
            return x + n - int(n / 16)
    return self.point(fun)


def glitch_one(n=1, ):
    pass

