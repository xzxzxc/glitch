# coding: utf-8
import glitch
import Image
import photos
import ui
import StringIO
import numpy
from console import hud_alert
from copy import deepcopy

v = None
vMain = None


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
    global v, vMain
    if vMain['imageview1'].image is None:
        hud_alert('No image loaded', icon='error')
        return 
    v = ui.load_view('fuckupcolors')
    v['imageview1'].image = vMain['imageview1'].image
    v.present('full_screen', animated=False, hide_title_bar=True)


def save_action(sender):
    v_im = sender.superview['imageview1'].image
    global vMain
    vMain['imageview1'].image = v_im
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
    sender.superview['imageview1'].image = from_norm_to_ui(ph)


@ui.in_background
def fromLibrary_action(sender):
    ass = photos.pick_asset(assets=photos.get_assets(), title='Pick image to glitch')
    if ass is None:
        return
    if sender.superview.name == 'fuckupcolors':
        sender.superview['fuckUpSlider'].value = 0
    sender.superview['imageview1'].image = ass.get_ui_image()


def fuckUpSlider_action(sender):
    v = sender.superview
    n = int(200 * numpy.log(1 + v['fuckUpSlider'].value)) + 1
    im = v['imageview1'].image
    if im is None:
        return
    im_n = glitch.fuck_up_colors(from_ui_to_norm(im), n)
    v['imageview1'].image=from_norm_to_ui(im_n)


vMain = ui.load_view('main')
vMain.present('full_screen', animated=False, hide_title_bar=True)
