# coding: utf-8
import glitch
import Image
import photos
import ui
import StringIO
import numpy
from console import hud_alert
from mrView import mrRectView
import random as rn


v = None
vMain = None
im = None
buff = None


@ui.in_background
def clear(buff1=None):
    global im, buff
    del im
    im=None
    buff.close()
    if buff1:
        buff1.close()


def cancel_action(sender):
    sender.superview.close()


def from_norm_to_ui(norm_im):
    buff = StringIO.StringIO()
    norm_im.save(buff, format='bmp')
    ui_im = ui.Image.from_data(buff.getvalue())
    return ui_im, buff


def from_ui_to_norm(ui_im):
    buff=StringIO.StringIO(ui_im.to_png())
    norm_im= Image.open(buff)
    return norm_im, buff
    

def fuckUpSlider_action(sender):
    global im
    v = sender.superview
    if v['control'].selected_index==0:
        n = int(200 * numpy.log(1 + v['fuckUpSlider'].value)) + 1
        im_n = glitch.fuck_up_colors1(im, n)
    elif v['control'].selected_index==1:
        n = int(254*v['fuckUpSlider'].value) + 1
        im_n = glitch.fuck_up_colors2(im, n)
    else:
        n = int(254*v['fuckUpSlider'].value) + 1
        im_n = glitch.fuck_up_colors3(im, n)
    v['imageview1'].image, buff = from_norm_to_ui(im_n)
    buff.close()


def shiftSlider_action(sender):
    global im
    v = sender.superview
    xShift = int(0.2*im.size[0]*v['shiftSlider2'].value) + 1
    intens = v['shiftSlider1'].value
    if intens==0.:
        return 
    region=v['view1']['region']
    x0 = int((region.x + 15)*im.size[0]/v['view1'].width)
    gl_widt = int((region.width - 30)*im.size[0]/v['view1'].width)
    y0 = int((region.y + 15)*im.size[1]/v['view1'].height)
    gl_heigth = int((region.height - 30) *im.size[1]/v['view1'].height)
    dy = int(0.0025 * im.size[1])
    im_n=im.copy()
    if v['control'].selected_index==0:
        for i in xrange(int(intens*300)):
            y = [rn.randint(y0, y0 + gl_heigth - dy)]
            if y[0] - y0 < gl_heigth / 2:
                dx = int(numpy.sqrt(gl_heigth*xShift*(y[0] - y0)/im.size[1]))
            else:
                dx = int(numpy.sqrt(gl_heigth*xShift*(y0 + gl_heigth - y[0])/im.size[1]))
            x = [max(0, rn.randint(x0, x0 + gl_widt) - dx), max(0, x0 + gl_widt - dx)]
            y.append(y[0] + dy)
            x.sort()
            glitch.glitch_shift_left(im_n, rn.randint(int(0.75*xShift), xShift), x[0], y[0], x[1], y[1])
    else:
        for i in xrange(int(intens*300)):
            y = [rn.randint(y0, y0 + gl_heigth - dy)]
            if y[0] - y0 < gl_heigth / 2:
                dx = int(numpy.sqrt(gl_heigth*xShift*(y[0] - y0)/im.size[1]))
            else:
                dx = int(numpy.sqrt(gl_heigth*xShift*(y0 + gl_heigth - y[0])/im.size[1]))
            x = [min(im.size[0], x0 + dx), min(im.size[0], rn.randint(x0, x0 + gl_widt) + dx)]
            y.append(y[0] + dy)
            x.sort()
            glitch.glitch_shift_right(im_n, rn.randint(int(0.75*xShift), xShift), x[0], y[0], x[1], y[1])
    v['view1']['imageview1'].image, buff = from_norm_to_ui(im_n)
    buff.close()
    
    
def rSlider_action(sender):
    global im
    v = sender.superview
    r = int(255 * v['rSlider'].value)
    region=v['view1']['region']
    x0 = int((region.x + 15)*im.size[0]/v['view1'].width)
    gl_widt = int((region.width - 30)*im.size[0]/v['view1'].width)
    y0 = int((region.y + 15)*im.size[1]/v['view1'].height)
    gl_heigth = int((region.height - 30) *im.size[1]/v['view1'].height)
    rn.seed()
    dy = int(0.0025 * im.size[1])
    im_n=im.copy()
    for i in xrange(r):
        y = [rn.randint(y0, y0 + gl_heigth - dy)]
        x=[rn.randint(x0, x0+gl_widt), rn.randint(x0, x0+gl_widt)]
        y.append(y[0]+dy)
        x.sort()
        glitch.glitch_red(im_n, rn.randint(-50,100), x[0], y[0], x[1], y[1]) 
    v['view1']['imageview1'].image, buff = from_norm_to_ui(im_n)
    buff.close()


def gSlider_action(sender):
    global im
    v = sender.superview
    g = int(255 * v['rSlider'].value)
    region=v['view1']['region']
    x0 = int((region.x + 15)*im.size[0]/v['view1'].width)
    gl_widt = int((region.width - 30)*im.size[0]/v['view1'].width)
    y0 = int((region.y + 15)*im.size[1]/v['view1'].height)
    gl_heigth = int((region.height - 30) *im.size[1]/v['view1'].height)
    rn.seed()
    dy = int(0.0025 * im.size[1])
    im_n=im.copy()
    for i in xrange(g):
        y = [rn.randint(y0, y0 + gl_heigth - dy)]
        x=[rn.randint(x0, x0+gl_widt), rn.randint(x0, x0+gl_widt)]
        y.append(y[0]+dy)
        x.sort()
        glitch.glitch_green(im_n, rn.randint(-50, 100), x[0], y[0], x[1], y[1]) 
    v['view1']['imageview1'].image, buff = from_norm_to_ui(im_n)
    buff.close()
    
    
def bSlider_action(sender):
    global im
    v = sender.superview
    b = int(255 * v['rSlider'].value)
    region=v['view1']['region']
    x0 = int((region.x + 15)*im.size[0]/v['view1'].width)
    gl_widt = int((region.width - 30)*im.size[0]/v['view1'].width)
    y0 = int((region.y + 15)*im.size[1]/v['view1'].height)
    gl_heigth = int((region.height - 30) *im.size[1]/v['view1'].height)
    rn.seed()
    dy = int(0.0025 * im.size[1])
    im_n=im.copy()
    for i in xrange(b):
        y = [rn.randint(y0, y0 + gl_heigth - dy)]
        x=[rn.randint(x0, x0+gl_widt), rn.randint(x0, x0+gl_widt)]
        x.sort()
        y.append(y[0]+dy)
        glitch.glitch_blue(im_n, rn.randint(-50, 100), x[0], y[0], x[1], y[1]) 
    v['view1']['imageview1'].image, buff = from_norm_to_ui(im_n)
    buff.close()
    

def fuckUp_load(sender):
    global v, vMain, im, buff
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('fuckupcolors')
    im_n = vMain['imageview1'].image
    v['imageview1'].image = im_n
    im, buff = from_ui_to_norm(im_n)
    v['control'].action=fuckUpSlider_action
    v.present('full_screen', animated=False, hide_title_bar=True, orientations=['portrait'])


def shift_load(sender):
    global v, vMain, im, buff
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('shift')
    im_n = vMain['imageview1'].image
    v['view1']['imageview1'].image = im_n
    im, buff = from_ui_to_norm(im_n)
    rn.seed()
    v['control'].action=shiftSlider_action
    v.present('full_screen', animated=False, hide_title_bar=True, orientations=['portrait'])
    
    
def coloring_load(sender):
    global v, vMain, im, buff
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('coloring')
    im_n = vMain['imageview1'].image
    v['view1']['imageview1'].image = im_n
    im, buff = from_ui_to_norm(im_n)
    rn.seed()
    v.present('full_screen', animated=False, hide_title_bar=True, orientations=['portrait'])


def save_and_exit_action(sender):
    if sender.superview.name == 'shift' or sender.superview.name == 'coloring':
        v_im = sender.superview['view1']['imageview1'].image
    else:
        v_im = sender.superview['imageview1'].image
    global vMain, v, im, buff
    vMain['imageview1'].image = v_im
    del im
    im = None
    buff.close()
    sender.superview.close()


def save_action(sender):
    if sender.superview.name == 'shift' or sender.superview.name == 'coloring':
        v_im = sender.superview['view1']['imageview1'].image
    else:
        v_im = sender.superview['imageview1'].image
    global im, buff
    buff.close()
    im, buff = from_ui_to_norm(v_im)


def saveLibrary_action(sender):
    if sender.superview['imageview1'].image is None:
        hud_alert('No image to save', icon='error')
        return 
    photos.save_image(sender.superview['imageview1'].image)
    hud_alert('Saved')


@ui.in_background
def takePhoto_action(sender):
    ph = photos.capture_image()
    if ph is None:
        return
    if sender.superview.name == 'fuckupcolors':
        sender.superview['fuckUpSlider'].value = 0
    if sender.superview.name == 'shift':
        sender.superview['shiftSlider1'].value = 0
        sender.superview['shiftSlider2'].value = 0
    if sender.superview.name == 'color':
        sender.superview['rSlider'].value = 0
        sender.superview['gSlider'].value = 0
        sender.superview['bSlider'].value = 0
    sender.superview['imageview1'].image, buff = from_norm_to_ui(ph)
    buff.close()


@ui.in_background
def fromLibrary_action(sender):
    ass = photos.pick_asset(assets=photos.get_assets(), title='Pick image to glitch')
    if ass is None:
        return
    if sender.superview.name == 'fuckupcolors':
        sender.superview['fuckUpSlider'].value = 0
    sender.superview['imageview1'].image = ass.get_ui_image()



vMain = ui.load_view('main')
vMain.present('full_screen', animated=False, hide_title_bar=True, orientations=['portrait'])
#vMain['imageview1'].image,buff2=from_norm_to_ui(Image.new('RGB',(100,100),'red'))


