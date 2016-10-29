# coding: utf-8
import ui


class mrRectView(ui.View):
    '''a view that can be moved and resized
    '''

    def touch_moved(self, touch):
        x,y = touch.location
        if x < 0 or y < 0:
            return 
        xp,yp = touch.prev_location
        dx = x-xp
        dy = y-yp
        if x < 30 and y < 30:
            self.width -= dx
            self.height -= dy
            self.x += dx
            self.y += dy
        elif x > self.width - 30 and y < 30:
            self.width += dx
            self.height -= dy
            self.y += dy
        elif x > self.width - 30 and y > self.height - 30:
            self.width += dx
            self.height += dy
        elif x < 30 and y > self.height - 30:
            self.width -= dx
            self.height += dy
            self.x += dx
        else:
            self.x += dx
            self.y += dy
 
