# coding: utf-8
import ui


class mrRectView(ui.View):
    '''a view that can be moved and resized
    '''
    def __init__(self):
        region1=ui.View(flex='WH',frame=(15,15,self.width-30,self.height-30), background_color='#d2d2d2', name='region')
        region1.border_width=1
        region1.border_color='black'
        region1.alpha=0.3
        self.add_subview(region1)
        region2=ui.View(flex='WH',frame=(16,16,self.width-32,self.height-32), background_color='#d2d2d2', name='region')
        region2.border_width=1
        region2.border_color='white'
        region2.alpha=0.3
        self.add_subview(region2)

        
    def touch_moved(self, touch):
        x,y = touch.location
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
        if self.x<-self.subviews[0].x:
            self.x=-self.subviews[0].x
        if self.y<-self.subviews[0].y:
            self.y=-self.subviews[0].y
        if self.x + self.width - self.subviews[0].x>self.superview.width:
            self.x=self.superview.width-self.width+self.subviews[0].x
        if self.y + self.height - self.subviews[0].y>self.superview.height:
            self.y=self.superview.height-self.height+self.subviews[0].y
 
