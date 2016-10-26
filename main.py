# coding: utf-8
import glitch
import Image
import photos
import ui
import StringIO
import numpy
from console import hud_alert
from copy import deepcopy
im=None

def saveImage_action(sender):
	photos.save_image(sender.superview['imageview1'].image)
	hud_alert('Saved')


def update_im(v, im_n):
	buff=StringIO.StringIO()
	im_n.save(buff, format='bmp')
	v['imageview1'].image=ui.Image.from_data(buff.getvalue())
	buff.close()
	

@ui.in_background
def takePhoto_action(sender):
	ph=photos.capture_image()
	if ph is None:
		return 
	sender.superview['slider1'].value=0
	global im
	im=ph
	update_im(sender.superview, ph)
	

@ui.in_background
def newImage_action(sender):
	ass = photos.pick_asset(assets=photos.get_assets(),title='Pick image to glitch')
	if ass is None:
		return 
	sender.superview['slider1'].value=0
	sender.superview['imageview1'].image=ass.get_ui_image()
	global im
	im=ass.get_image()


def slider_action(sender):
	v = sender.superview
	n = int(200*numpy.log(1+v['slider1'].value))+1
	global im
	if im is None:
		return 
	im_n = glitch.fuck_up_colors(im, n)
	update_im(v, im_n)

v = ui.load_view('main')
newImage_action(v['imageview1'])

if ui.get_screen_size()[1] >= 768:
	# iPad
	v.present('sheet')
else:
	# iPhone
	v.present()




