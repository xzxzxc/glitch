# coding: utf-8
import glitch
import Image
import photos
import ui
import StringIO
import numpy
from console import hud_alert
from copy import deepcopy
v=None
vMain=None


def cancel_action(sender):
	sender.superview.close()


def update_im(v, im_n):
	buff=StringIO.StringIO()
	im_n.save(buff, format='bmp')
	v['imageview1'].image=ui.Image.from_data(buff.getvalue())
	buff.close()


def fuckUp_load(sender):
	global v, vMain
	if im is None:
		hud_alert('No image loaded')
	v=ui.load_view('fuckupcolors')
	v['imageview1'].image=vMain['imageview1'].image
	v.present('full_screen', animated=False, hide_title_bar=True)


def save_action(sender):
	v_im=sender.superview['imageview1'].image
	global im, vMain
	buff=StringIO.StringIO(v_im.to_png())
	im=Image.open(buff)
	buff.close()
	vMain['imageview1'].image=v_im
	sender.superview.close()


def saveLibrary_action(sender):
	global im
	if im is None:
		return 
	photos.save_image(sender.superview['imageview1'].image)
	hud_alert('Saved')

	

@ui.in_background
def takePhoto_action(sender):
	ph=photos.capture_image()
	if ph is None:
		return 
	if sender.superview.name=='fuckupcolors':
		sender.superview['fuckUpSlider'].value=0
	global im
	im=ph
	update_im(sender.superview, ph)
	

@ui.in_background
def fromLibrary_action(sender):
	ass = photos.pick_asset(assets=photos.get_assets(),title='Pick image to glitch')
	if ass is None:
		return 
	if sender.superview.name=='fuckupcolors':
		sender.superview['fuckUpSlider'].value=0
	sender.superview['imageview1'].image=ass.get_ui_image()
	global im
	im=ass.get_image()


def fuckUpSlider_action(sender):
	v = sender.superview
	n = int(200*numpy.log(1+v['fuckUpSlider'].value))+1
	global im
	if im is None:
		return 
	im_n = glitch.fuck_up_colors(im, n)
	update_im(v, im_n)

vMain = ui.load_view('main')
vMain.present('full_screen', animated=False, hide_title_bar=True)

