# coding: utf-8
import glitch
import Image
import photos
import ui
import StringIO
import numpy
from console import hud_alert
from copy import deepcopy
import overlay
from mrView import mrRectView
import random as rn

rn.seed()
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


def fuckUp_load(sender):
    global v, vMain, im, buff
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('fuckupcolors')
    im_n = vMain['imageview1'].image
    v['imageview1'].image = im_n
    im, buff = from_ui_to_norm(im_n)
    v.present('full_screen', animated=False, hide_title_bar=True)


def shift_load(sender):
    global v, vMain, im, buff
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('shift')
    im_n = vMain['imageview1'].image
    v['view1']['imageview1'].image = im_n
    im, buff = from_ui_to_norm(im_n)
    v.present('full_screen', animated=False, hide_title_bar=True)
    
    
def coloring_load(sender):
    global v, vMain, im, buff
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('coloring')
    im_n = vMain['imageview1'].image
    v['imageview1'].image = im_n
    im, buff = from_ui_to_norm(im_n)
    v.present('full_screen', animated=False, hide_title_bar=True)


def save_action(sender):
    v_im = sender.superview['imageview1'].image
    global vMain, v, im, buff
    vMain['imageview1'].image = v_im
    del im
    im = None
    buff.close()
    sender.superview.close()


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


def fuckUpSlider_action(sender):
    global im
    v = sender.superview
    n = int(200 * numpy.log(1 + v['fuckUpSlider'].value)) + 1
    im_n = glitch.fuck_up_colors(im, n)
    v['imageview1'].image, buff = from_norm_to_ui(im_n)
    buff.close()


def shiftSlider_action(sender):
    global im
    v = sender.superview
    dx = v['shiftSlider1'].value
    intens = v['shiftSlider1'].value
    regFrame=v['view1']['region'].frame
    xMin = int(regFrame)
    if v['dirControl'].selected_index==0:
        glitch.glitch_shift_right(12)
    else:
        for i in range(int(intens*100)):
            glitch.glitch_shift_right(im, int(100*dx),regFrame[0]+15, regFrame[1]+15, regFrame[0]+regFrame[2]-15, regFrame[1]+regFrame[3]-15)
    v['view1']['imageview1'].image, buff = from_norm_to_ui(im)
    buff.close()


vMain = ui.load_view('main')
vMain.present('full_screen', animated=False, hide_title_bar=True)
#vMain['imageview1'].image,buff2=from_norm_to_ui(Image.new('RGB',(100,100),'red'))


