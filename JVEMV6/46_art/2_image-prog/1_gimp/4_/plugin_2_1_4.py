#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	file	: C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\2_image-prog\1_gimp\4_\plugin_2_1_4.py

	at		: 2018/04/06 14:34:49

	plugin at : C:\WORKS_2\Programs\GIMP 2\plugins

'''

from gimpfu import *

from time import time, localtime, strftime

import inspect, os

from fileinput import lineno

# from enum import Enum

import sys, random
# sys.path.append("C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\2_image-prog")
# sys.path.append("C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\2_image-prog\\libs_image_prog")
# sys.path.append('..')
# 
# from libs_image_prog import cons_image

########################################################################
# class CONS(Enum):
# 	
# 	str_Fpath_Debug = "debug!!"


def write_Log(msg):
	
	dpath = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\4_"
# 	dpath = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\4_"
	
	fname = "debug.log"
	
	fpath = "%s\\%s" % (dpath, fname)
	
	f = open(fpath, "a")
	
	f.write("===============================\n")
	
	f.write(msg)
	
	f.write("\n\n")
	
	f.close()
	
#/ def write_Log(msg):

def thisfile(depth=0):
# def _file(depth=0):
#     print "line"

    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    return info.filename                       # __FILE__     -> Test.py
#     print info.filename                       # __FILE__     -> Test.py
#     print info.function                       # __FUNCTION__ -> Main
#     print info.lineno                         # __LINE__     -> 13
    
    '''    
        frame = inspect.currentframe(0)
    #     frame = inspect.currentframe(depth+1)
        
        return os.path.basename(frame.f_code.co_filename)
    #     return frame.f_code.co_filename
    '''
#/def thisfile(depth=0):


def linenum(depth=0):
#     print "line"
    
    #ref https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number 'answered Jul 25 '11 at 1:31'
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                        # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
#     return info.filename                       # __FILE__     -> Test.py
    #     print info.filename                       # __FILE__     -> Test.py
    #     print info.function                       # __FUNCTION__ -> Main
    #     print info.lineno                         # __LINE__     -> 13
    return info.lineno                         # __LINE__     -> 13

    
    '''
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno
    
    '''

'''
    @param string_type
            serial    "20160604_193404"
            basic     "2016/06/04 19:34:04"
'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
#     str = strftime("%Y%m%d_%H%M%S", t)
#     str = strftime("%Y%m%d_%H%M%S", localtime())

    '''###################
        build string        
    ###################'''
    if string_type == "serial" : #if string_type == "serial"
    
        str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    elif string_type == "basic" : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    else : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    #/if string_type == "serial"
    
    
#     str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
    if mili == True :

        if string_type == "serial" : #if string_type == "serial"
            
            str = "%s_%03d" % (str, int(t % 1 * 1000))
        
        else : #if string_type == "serial"
        
            str = "%s.%03d" % (str, int(t % 1 * 1000))

        #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
#         str = "%s_%03d" % (str, int(t % 1 * 1000))
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():


class ImageObject :
	
	image = None
	layer = None
	
	def __init__( self, image ):
		self.image = image
		
		return
		
	def get_Image(self):
		
		return self.image
	
	def add_Layer(self, layer_Name):

		#debug
		msg = "[%s / %s:%d]\nadd_Layer => starting..." \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)
		
		width   = self.image.width
		height  = self.image.height
		type    = RGB_IMAGE
		opacity = 100
		mode    = NORMAL_MODE

		#debug
		msg = "[%s / %s:%d]\ngimp.Layer() ---> calling..." \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)

		self.layer = gimp.Layer(self.image, layer_Name, width, height, type, opacity, mode)
# 		self.layer = gimp.Layer(image, name, width, height, type, opacity, mode)
		
		#debug
		msg = "[%s / %s:%d]\ngimp.Layer() ---> done" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)

		
  		self.layer.fill(1)
  #
		# 画像データの 0 番目の位置にレイヤーを挿入する
		position = 0
		self.image.add_layer(self.layer, position)
# 		self.image.add_layer(layer, position)
		
		# return
		return
	
	#/def add_Layer(self, layer_Name):
		
	def get_Layer(self):
		
		if self.layer == None :
			
			pdb.gimp_message("layer ==> None !!!")
			
			return False
		
		# return layer
		return self.layer

def create_image(width, height):
	# 画像データを生成
	return gimp.Image(width, height, RGB)

def display_image(image):
	gimp.Display(image)

def add_layer(image, name):
  # レイヤーの作成に必要なパラメータ
  width   = image.width
  height  = image.height
  type    = RGB_IMAGE
  opacity = 100
  mode    = NORMAL_MODE
  #
  # パラメータをもとにレイヤーを作成
  layer = gimp.Layer(image, name, width, height, type, opacity, mode)
  #
  # レイヤーを背景色で塗りつぶす（GIMP のデフォルトの挙動に合わせています）
  layer.fill(1)
  #
  # 画像データの 0 番目の位置にレイヤーを挿入する
  position = 0
  image.add_layer(layer, position)
  #
  return layer

def draw_pencil_lines(drawable, lines):
  # ペンシルツールで線を描画する
  pdb.gimp_pencil(drawable, len(lines), lines)
  
def draw_rect(drawable, x1, y1, x2, y2):
  lines = [x1, y1, x2, y1, x2, y2, x1, y2, x1, y1]
  draw_pencil_lines(drawable, lines)

def test_8__Multiple_Copies(timg, tdrawable, numOf_NewLayers = 1):	#add layer to the current image ---> multiple layers
	
	layer  = timg.active_layer
	
	name_Orig = layer.name
	
	# conver to int
	numOf_NewLayers = int(numOf_NewLayers)
	
	# undo start
	pdb.gimp_image_undo_group_start(timg)
	
	# copy layer
	for i in range(numOf_NewLayers):

		#ref http://gimpforums.com/thread-python-get-number-of-layers
		new_Layer = layer.copy()
		
		new_Layer.name = "%s.copy-%02d" % (name_Orig, i + 1) 
# 		new_Layer.name = "%s-%02d" % (name_Orig, i) 
		
		timg.add_layer(new_Layer, 0)
	
	# undo end
	pdb.gimp_image_undo_group_end(timg)
	
#/for i in range(numOf_NewLayers):

	
#/ def def test_8__Multiple_Copies(timg, tdrawable, numOf_NewLayers = 1):	#add layer to the current image ---> multiple layers

def test_7__DrawCircle(timg, tdrawable, numOf_NewLayers = 1):
	
	'''###################
		select ellipse		
	###################'''
	#ref https://developer.gimp.org/api/2.0/libgimp/libgimp-gimpimageselect.html#gimp-image-select-ellipse
	#ref CHANNEL_OP_REPLACE https://stackoverflow.com/questions/39641231/gimp-python-fu-how-do-i-select-a-polygon#39654251
	pdb.gimp_image_select_ellipse(timg, CHANNEL_OP_REPLACE, 100, 100, 50, 50)
	
	'''###################
    	border		
    ###################'''
	border_thickness = 5
	
	#ref border https://superuser.com/questions/829495/how-can-i-automate-some-simple-steps-within-the-gimp
	pdb.gimp_selection_border(timg, border_thickness)
	
	'''###################
		fill		
	###################'''
	# fill the selected area
	#refhttps://stackoverflow.com/questions/49888598/gimp-python-fu-create-simple-border
	pdb.gimp_edit_fill(pdb.gimp_image_get_active_drawable(timg), 2)

# 	pdb.gimp_image_select_ellipse(img, gimpfu.CHANNEL_OP_REPLACE, 
# 			x, y, RADIO*2, RADIO*2)

# def test_7__DrawCircle(timg, tdrawable, numOf_NewLayers = 1):

'''###################
	test_6
	copy the active layer
###################'''
def test_6(timg, tdrawable, numOf_NewLayers = 1):	#add layer to the current image ---> multiple layers
	
	layer  = timg.active_layer
	
	name_Orig = layer.name
	
	#ref http://gimpforums.com/thread-python-get-number-of-layers
	new_Layer = layer.copy()
	
	new_Layer.name = "%s-%02d" % (name_Orig, numOf_NewLayers) 
	
	timg.add_layer(new_Layer, 0)
	
# 	image = create_image(640, 400)
	
# 	gimp.message("numOf_NewLayers => %f" % (numOf_NewLayers))
# 	
# 	for i in range(int(numOf_NewLayers)) :
# # 	for i in range(numOf_NewLayers) :
# 	
# 		name_Layer = "L-%02d" % (i + 1)
# # 		name_Layer = "L-1"
# 		
# 		# image instance
# 		imageObj = ImageObject( timg )
# 	# 	imageObj = ImageObject( image )
# 	
# 		im = imageObj.get_Image()
# 		
# 		msg = "[%s / %s:%d]\nimageObj ==> instance made" \
# 					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 	# 					 (str_Time, num_Line, num_Line_EndStack)
# 		write_Log(msg)
# 		
# 		msg = "[%s / %s:%d]\ncalling ---> im.add_Layer()" \
# 					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 	# 					 (str_Time, num_Line, num_Line_EndStack)
# 		write_Log(msg)
# 		
# 		
# 		imageObj.add_Layer(name_Layer)
# 	# 	im.add_Layer(name_Layer)
# 	
# 		msg = "[%s / %s:%d]\nimageObj ==> Layer added" \
# 					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 	# 					 (str_Time, num_Line, num_Line_EndStack)
# 		write_Log(msg)
# 		
# 		'''###################
# 			background		
# 		###################'''
# 		#ref http://coderazzi.net/python/gimp/pythonfu.html
# 		cols_Mix = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# 		
# 		pdb.gimp_context_set_background(cols_Mix)
# 	# 	pdb.gimp_context_set_background((0,0,0))
# 		
# 		# get drawable
# 		drw = pdb.gimp_image_active_drawable(im)
# 		
# 		msg = "[%s / %s:%d]\ndrawable ==> obtained" \
# 					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 	# 					 (str_Time, num_Line, num_Line_EndStack)
# 		write_Log(msg)
# 	
# 		# fill bg
# 		pdb.gimp_drawable_fill(drw, 1)
# 	# 	pdb.gimp_drawable_fill(drw, gimpfu.BACKGROUND_FILL)
# 				# The type of fill { FOREGROUND-FILL (0), BACKGROUND-FILL (1), WHITE-FILL (2), TRANSPARENT-FILL (3), PATTERN-FILL (4), NO-FILL (5) }
# 	
# 		msg = "[%s / %s:%d]\nbg ==> filled" \
# 					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 	# 					 (str_Time, num_Line, num_Line_EndStack)
# 		write_Log(msg)

def test_5(timg, tdrawable, numOf_NewLayers = 1):	#add layer to the current image ---> multiple layers
	
# 	image = create_image(640, 400)
	
	gimp.message("numOf_NewLayers => %f" % (numOf_NewLayers))
	
	for i in range(int(numOf_NewLayers)) :
# 	for i in range(numOf_NewLayers) :
	
		name_Layer = "L-%02d" % (i + 1)
# 		name_Layer = "L-1"
		
		# image instance
		imageObj = ImageObject( timg )
	# 	imageObj = ImageObject( image )
	
		im = imageObj.get_Image()
		
		msg = "[%s / %s:%d]\nimageObj ==> instance made" \
					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
	# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)
		
		msg = "[%s / %s:%d]\ncalling ---> im.add_Layer()" \
					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
	# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)
		
		
		imageObj.add_Layer(name_Layer)
	# 	im.add_Layer(name_Layer)
	
		msg = "[%s / %s:%d]\nimageObj ==> Layer added" \
					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
	# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)
		
		'''###################
			background		
		###################'''
		#ref http://coderazzi.net/python/gimp/pythonfu.html
		cols_Mix = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		
		pdb.gimp_context_set_background(cols_Mix)
	# 	pdb.gimp_context_set_background((0,0,0))
		
		# get drawable
		drw = pdb.gimp_image_active_drawable(im)
		
		msg = "[%s / %s:%d]\ndrawable ==> obtained" \
					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
	# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)
	
		# fill bg
		pdb.gimp_drawable_fill(drw, 1)
	# 	pdb.gimp_drawable_fill(drw, gimpfu.BACKGROUND_FILL)
				# The type of fill { FOREGROUND-FILL (0), BACKGROUND-FILL (1), WHITE-FILL (2), TRANSPARENT-FILL (3), PATTERN-FILL (4), NO-FILL (5) }
	
		msg = "[%s / %s:%d]\nbg ==> filled" \
					% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
	# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
	# 					 (str_Time, num_Line, num_Line_EndStack)
		write_Log(msg)

# 	
# 	#debug
# 	pdb.gimp_message("layer => added")
# 	
# 	layer = im.get_Layer()
# 
# 	draw_rect(layer, 190, 210, 490, 310)
# # 	draw_rect(layer, 390, 210, 490, 310)
	
# 	display_image(im)
# 	display_image(image)

def test_4(timg, tdrawable):	#add layer to the current image ]] 20180504_122012
	
# 	image = create_image(640, 400)
	
	name_Layer = "L-1"
	
	# image instance
	imageObj = ImageObject( timg )
# 	imageObj = ImageObject( image )

	im = imageObj.get_Image()
	
	msg = "[%s / %s:%d]\nimageObj ==> instance made" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	msg = "[%s / %s:%d]\ncalling ---> im.add_Layer()" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	
	imageObj.add_Layer(name_Layer)
# 	im.add_Layer(name_Layer)

	msg = "[%s / %s:%d]\nimageObj ==> Layer added" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	'''###################
		background		
	###################'''
	#ref http://coderazzi.net/python/gimp/pythonfu.html
	cols_Mix = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	
	pdb.gimp_context_set_background(cols_Mix)
# 	pdb.gimp_context_set_background((0,0,0))
	
	# get drawable
	drw = pdb.gimp_image_active_drawable(im)
	
	msg = "[%s / %s:%d]\ndrawable ==> obtained" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)

	# fill bg
	pdb.gimp_drawable_fill(drw, 1)
# 	pdb.gimp_drawable_fill(drw, gimpfu.BACKGROUND_FILL)
			# The type of fill { FOREGROUND-FILL (0), BACKGROUND-FILL (1), WHITE-FILL (2), TRANSPARENT-FILL (3), PATTERN-FILL (4), NO-FILL (5) }

	msg = "[%s / %s:%d]\nbg ==> filled" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)

# 	
# 	#debug
# 	pdb.gimp_message("layer => added")
# 	
# 	layer = im.get_Layer()
# 
# 	draw_rect(layer, 190, 210, 490, 310)
# # 	draw_rect(layer, 390, 210, 490, 310)
	
# 	display_image(im)
# 	display_image(image)

def test_3(timg, tdrawable):
	
	image = create_image(640, 400)
	
	name_Layer = "L-1"
	
	# image instance
	imageObj = ImageObject( image )

	im = imageObj.get_Image()
	
	msg = "[%s / %s:%d]\nimageObj ==> instance made" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	msg = "[%s / %s:%d]\ncalling ---> im.add_Layer()" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	
	imageObj.add_Layer(name_Layer)
# 	im.add_Layer(name_Layer)

	msg = "[%s / %s:%d]\nimageObj ==> Layer added" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	'''###################
		background		
	###################'''
	#ref http://coderazzi.net/python/gimp/pythonfu.html
	pdb.gimp_context_set_background((0,0,0))
	
	# get drawable
	drw = pdb.gimp_image_active_drawable(im)
	
	msg = "[%s / %s:%d]\ndrawable ==> obtained" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)

	# fill bg
	pdb.gimp_drawable_fill(drw, 1)
# 	pdb.gimp_drawable_fill(drw, gimpfu.BACKGROUND_FILL)
			# The type of fill { FOREGROUND-FILL (0), BACKGROUND-FILL (1), WHITE-FILL (2), TRANSPARENT-FILL (3), PATTERN-FILL (4), NO-FILL (5) }

	msg = "[%s / %s:%d]\nbg ==> filled" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)

# 	
# 	#debug
# 	pdb.gimp_message("layer => added")
# 	
# 	layer = im.get_Layer()
# 
# 	draw_rect(layer, 190, 210, 490, 310)
# # 	draw_rect(layer, 390, 210, 490, 310)
	
	display_image(im)
# 	display_image(image)

def test_2(timg, tdrawable):
	
	image = create_image(640, 400)
	
	name_Layer = "L-1"
	
	# image instance
	imageObj = ImageObject( image )

	im = imageObj.get_Image()
	
# 	#debug
# 	t = time()
# 	str_Time = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
	
# 	num_Line = linenum(0)
# 
# 	lenOf_Stacks = len(inspect.stack())
# 	
# 	num_Line_EndStack = linenum(lenOf_Stacks - 1)
# 	
# # 	ref https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number 'answered Jul 25 '11 at 1:31'
# 	callerframerecord = inspect.stack()[1]	# 0 represents this line
# # 										 1 represents line at caller
# 	
#  	lenOf_Stacks = len(inspect.stack())
# 	
# 	frame = inspect.currentframe(1)
# 	num_Line_Current = frame.f_lineno
	
# 	msg = "[%s / %d] imageObj ==> instance made (lenOf_Stacks = %d)" % \
# 	msg = "[%s / %d] imageObj ==> instance made (num_Line_EndStack = %d / num_Line_Current = %d)" \
	msg = "[%s / %s:%d]\nimageObj ==> instance made" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	msg = "[%s / %s:%d]\ncalling ---> im.add_Layer()" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)
	
	
	imageObj.add_Layer(name_Layer)
# 	im.add_Layer(name_Layer)

	msg = "[%s / %s:%d]\nimageObj ==> Layer added" \
				% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 				% (str_Time, num_Line, num_Line_EndStack, num_Line_Current)
# 					 (str_Time, num_Line, num_Line_EndStack)
	write_Log(msg)


# 	
# 	#debug
# 	pdb.gimp_message("layer => added")
# 	
# 	layer = im.get_Layer()
# 
# 	draw_rect(layer, 190, 210, 490, 310)
# # 	draw_rect(layer, 390, 210, 490, 310)
	
	display_image(im)
# 	display_image(image)

def test_1(timg, tdrawable):
	
	image = create_image(640, 400)
	
	name_Layer = "L-1"
	
	layer = add_layer(image, name_Layer)
# 	layer = add_layer(image, "背景")

	draw_rect(layer, 390, 210, 490, 310)
	
	display_image(image)

# def show_Message(image, layer, message):

#ref https://jacksonbates.wordpress.com/2015/09/14/python-fu-5-automating-workflows-coding-a-complete-plug-in/
def extreme_unsharp_desaturation(image, drawable):
    pdb.gimp_image_undo_group_start(image)
    radius = 5.0
    amount = 5.0
    threshold = 0
    pdb.plug_in_unsharp_mask(image, drawable, radius, amount, threshold)
    pdb.gimp_desaturate_full(drawable, DESATURATE_LIGHTNESS)
    pdb.gimp_image_undo_group_end(image)

def extreme_unsharp_desaturation_options(image, drawable, radius, amount, mode):
    pdb.gimp_image_undo_group_start(image)
    threshold = 0
    pdb.plug_in_unsharp_mask(image, drawable, radius, amount, threshold) 
    pdb.gimp_desaturate_full(drawable, mode)
    pdb.gimp_image_undo_group_end(image)

def circles(image, drawable):
	
	tlabel = get_TimeLabel_Now()
	
	gimp.message("circles() : %s" % (tlabel))
	
	img=pdb.gimp_image_new(SIZE, SIZE, gimpfu.RGB)

	#add layer with 100% of opacity
	layer=pdb.gimp_layer_new(img, SIZE, SIZE, gimpfu.RGB_IMAGE, "base", 100, gimpfu.NORMAL_MODE)
	pdb.gimp_image_add_layer(img, layer, 0)
	
	#we need it with alpha channel
	pdb.gimp_layer_add_alpha(layer)
	
	#access its drawable
	drw = pdb.gimp_image_active_drawable(img)
	
	#set background to black, and foreground to white
	pdb.gimp_context_set_background((0,0,0))
	pdb.gimp_context_set_foreground((255, 255, 255))
	
	#fill the background - black
	pdb.gimp_drawable_fill(drw, gimpfu.BACKGROUND_FILL)
	
	#to set the brush, check first for available brushes using  pdb.gimp_brushes_get_list("")
	#Exanples of brush with width 3 is '1. Pixel', and with width 1, 'Pixel (1x1 square)'
	
	#set brush to simple pixel (width: 1)
	pdb.gimp_context_set_brush('Circle (01)')
	
	#draw a square around the image
	ctrlPoints = [RADIO, RADIO, SIZE-RADIO, RADIO, SIZE-RADIO, 
	              SIZE-RADIO, RADIO, SIZE-RADIO, RADIO, RADIO]
	pdb.gimp_paintbrush_default(drw,len(ctrlPoints),ctrlPoints)
	
	#now we draw 9 transparent circles (3 rows x 3 columns)
	#a transparent circle means -with an alpha layer-, to select the area and cut it
	for x in (0, SIZE/2-RADIO, SIZE-2*RADIO):
		for y in (0, SIZE/2-RADIO, SIZE-2*RADIO):
			#next call was available on 2.6, not on 2.8
			#pdb.gimp_image_select_ellipse(img, gimpfu.CHANNEL_OP_REPLACE, 
			#                              x, y, RADIO*2, RADIO*2)
			pdb.gimp_ellipse_select(img, x, y, RADIO*2, RADIO*2, 
			                        gimpfu.CHANNEL_OP_REPLACE, True, False, 0)
			pdb.gimp_edit_cut(drw)
	
	#remove any selection
	pdb.gimp_selection_none(img)
	
	#and display the image
	display=pdb.gimp_display_new(img)
	
#/ def circles(image, drawable):

def lazy_Resize(timg, tdrawable, max_width, max_height):	
	
# 	print ("max width: %s\nmax height: %s" % (max_width, max_height))
	gimp.message("max width: %s\nmax height: %s" % (max_width, max_height))
	
	width = tdrawable.width
	height = tdrawable.height

	if max_width <= 0:
		# Assume width is okay as it is
		max_width = width
	if max_height <= 0:
		# Assume height is okay
		max_height= height

	if width <= max_width and height <= max_height:
		
		gimp.message("Nothing to do, returning")
# 		print ("Nothing to do, returning")
		return

	image_aspect	= float(width) / float(height)
	boundary_aspect = float(max_width) / float(max_height)
	
	if image_aspect > boundary_aspect:
		# Width is the limiting factor:
		new_width = max_width
		new_height= int(round(  new_width/image_aspect ))
	else:
		# Height is the limiting factor:
		new_height = max_height
		new_width = int(round(  image_aspect*new_height  ))

	gimp.message("Resizing %s:%s to %s:%s" % (width, height, new_width, new_height))
# 	print ("Resizing %s:%s to %s:%s" % (width, height, new_width, new_height))

	# At present, documnatation does not specify the interpolation--
	# another tutorial claimed it was cubic:
	pdb.gimp_image_scale(timg, new_width, new_height)	
	
#/ def lazy_Resize(timg, tdrawable, max_width, max_height):	

def show_Message(timg, tdrawable):
	
	tlabel = get_TimeLabel_Now()
# 	
	msg = "[%s / %s:%d]\nshow_Message()" \
			% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))

	write_Log(msg)

	'''###################
		ops		
	###################'''
	width  = tdrawable.width

	msg = "[%s / %s:%d]\nwidth => %d" \
			% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0)
			, width
			
			)

	write_Log(msg)
	
	'''###################
		message		
	###################'''
	gimp.message("Hello, World!: %s" % (tlabel))
# # 	gimp.message("Hello, World!: %s (%s)" % (tlabel, CONS.str_Fpath_Debug.value))
# # 	gimp.message("Hello, World!: %s (%s)" % (tlabel, cons_image.FPath.str_Test.value))
# # 	gimp.message("Hello, World!: %s (%s)" % (tlabel, cons_image.FPath.dpath_Gimp_Debug.value))
# #     gimp.message("Hello, World: " + message)
# 	
# 	'''###################
# 		write to file		
# 	###################'''
# 	dpath = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\4_"
# # 	dpath = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\4_"
# 	
# 	fname = "debug.%s.log" % tlabel
# 	
# 	fpath = "%s\\%s" % (dpath, fname)
# 	
# 	f = open(fpath, "a")
# 	
# 	f.write("===============================\n")
# 	
# 	msg = "[%s / %s:%d]\ntest show_Message" \
# 		% (get_TimeLabel_Now(), os.path.basename(thisfile()), linenum(0))
# 
# 	f.write(msg)
# # 	f.write(msg)
# 	
# 	f.write("\n\n")
# 	
# 	f.close()

def plugin_main(timg, tdrawable, numOf_NewLayers):
# def plugin_main(timg, tdrawable):
	
	test_6(timg, tdrawable, numOf_NewLayers)
# 	test_5(timg, tdrawable, numOf_NewLayers)
# 	test_4(timg, tdrawable)
# 	test_3(timg, tdrawable)
# 	test_2(timg, tdrawable)

########################################################################

def test_group_2(timg, tdrawable, numOf_NewLayers):
# def plugin_main(timg, tdrawable):
	
	test_8__Multiple_Copies(timg, tdrawable, numOf_NewLayers)
# 	test_7__DrawCircle(timg, tdrawable)

#/ def test_group_2(timg, tdrawable, numOf_NewLayers):

########################################################################



register(
	'test_group_2',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'test_group_2',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
		, (PF_SPINNER, 'numOf_NewLayers', 'num of new layers (max 15)', 1, (1, 15, 1))
	],	# プロシジャの引数
	[],	# 戻り値の定義

	test_group_2,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)

register(
	'plugin_main',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'new image',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
		, (PF_SPINNER, 'numOf_NewLayers', 'num of new layers', 1, (1, 3, 1))
	],	# プロシジャの引数
	[],	# 戻り値の定義

	plugin_main,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)

register(
	'show_Message',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'show_Message',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
	],	# プロシジャの引数
	[],	# 戻り値の定義

	show_Message,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)

register(
	'extreme_unsharp_desaturation',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'extreme_unsharp_desaturation',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
	],	# プロシジャの引数
	[],	# 戻り値の定義

	extreme_unsharp_desaturation,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)

register(
#     "python-fu-extreme-unsharp-desaturation-options",
#     "Unsharp mask and desaurate image, with options",
#     "Run an unsharp mask with variables set by user",
#     "Jackson Bates", "Jackson Bates", "2015",
#     "Extreme unsharp and desaturate options...",
#     "RGB",
	'extreme_unsharp_desaturation_options',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'extreme_unsharp_desaturation_options',				# メニューアイテム
	'*',						# 対応する画像タイプ


	[
	    (PF_IMAGE, "image", "takes current image", None),
	    (PF_DRAWABLE, "drawable", "Input layer", None),
	    (PF_SLIDER, "radius", "Radius", 5, (0, 500, 0.5)),
	    # note extra tuple (min, max, step)
	    (PF_SLIDER, "amount", "Amount", 5.0, (0, 10, 0.1)),
	    (PF_RADIO, "mode", "Set Desauration mode: ", DESATURATE_LIGHTNESS,
	        (
	             ("Lightness", DESATURATE_LIGHTNESS),
	             ( "Luminosity", DESATURATE_LUMINOSITY),
	             ("Average", DESATURATE_AVERAGE)
	        )
	     )
	],
	[],
	extreme_unsharp_desaturation_options, menu="<Image>/Layer/user_libs")

register(
	'circles',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'circles',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
	],	# プロシジャの引数
	[],	# 戻り値の定義

	circles,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)

register(
	'lazy_Resize',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'lazy_Resize',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		# 引数  (type, name, description, default [, extra])
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None),
		(PF_INT, "max_width", "Maximum new width", 200),
        (PF_INT, "max_height", "Maximum new height", 200)
# 		(PF_INT, "max_width", "Maximum new width", 1280),
#         (PF_INT, "max_height", "Maximum new height", 900)
	],	# プロシジャの引数
	[],	# 戻り値の定義

	lazy_Resize,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)


# register(
#         "python_fu_FUNCTION_NAME",
#         "blurb: 推薦文",
#         "help: もう少し詳しい説明",
#         "author",
#         "copyright",
#         "2014/9/20",
#         "<Image>/Image/ABC", # メニュー項目
#         "*", # imagetypes: "RGB*, GRAY*" など
#         [ # 引数  (type, name, description, default [, extra])
#            (PF_STRING, "string", "Text string", 'Hello, world!')
#         ],
#         [], # 戻り値
#         show_Message) # 関数名
# #         plugin_main) # 関数名


main() # プラグインを駆動させるための関数


