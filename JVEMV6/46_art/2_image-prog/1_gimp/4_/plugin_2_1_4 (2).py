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

########################################################################
def write_Log(msg):
	
	dpath = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\4_"
	
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


def plugin_main(timg, tdrawable):
	
	test_2(timg, tdrawable)

########################################################################



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
	],	# プロシジャの引数
	[],	# 戻り値の定義

	plugin_main,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)


main() # プラグインを駆動させるための関数


