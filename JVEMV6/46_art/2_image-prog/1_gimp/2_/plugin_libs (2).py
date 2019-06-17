#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# version 1.0.0
#
# GimpPythonFuLayerAction-2-8.py
# Copyright (C) 2012 かんら・から http://www.pixiv.net/member.php?id=3098715
# 
# GimpPythonFuLayerAction-2-8.py is Python-fu plugin for GIMP 2.8
#
# GimpPythonFuLayerAction-2-8.py is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# GimpPythonFuLayerAction-2-8.py is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# GPLv3 ライセンス
# かんら・から http://www.pixiv.net/member.php?id=3098715
# バグレポート・アイデアなどは pixiv メッセージでお願いします。
#
# ダウンロード
# http://www.magic-object.mydns.jp/
#
# このスクリプトを使用して発生した問題に関し、作成者は如何なる保証などを行う事はありません。
# 自己責任でのみの使用を許可します。
########################################################################
from gimpfu import *

# from time import time

########################################################################
########################################################################
# レイヤー操作クラス
#
# レイヤー転写機能群など

'''
    @param string_type
            serial    "20160604_193404"
            basic     "2016/06/04 19:34:04"
'''
# def get_TimeLabel_Now(string_type="serial", mili=False):
# # def get_TimeLabel_Now(string_type="serial"):
#     
#     t = time()
#     
# #     str = strftime("%Y%m%d_%H%M%S", t)
# #     str = strftime("%Y%m%d_%H%M%S", localtime())
# 
#     '''###################
#         build string        
#     ###################'''
#     if string_type == "serial" : #if string_type == "serial"
#     
#         str = strftime("%Y%m%d_%H%M%S", localtime(t))
#     
#     elif string_type == "basic" : #if string_type == "serial"
#     
#         str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
#     
#     else : #if string_type == "serial"
#     
#         str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
#     
#     #/if string_type == "serial"
#     
#     
# #     str = strftime("%Y%m%d_%H%M%S", localtime(t))
#     
#     #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
#     if mili == True :
# 
#         if string_type == "serial" : #if string_type == "serial"
#             
#             str = "%s_%03d" % (str, int(t % 1 * 1000))
#         
#         else : #if string_type == "serial"
#         
#             str = "%s.%03d" % (str, int(t % 1 * 1000))
# 
#         #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
# #         str = "%s_%03d" % (str, int(t % 1 * 1000))
#     
#     return str
#     
#     #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
# #     return strftime("%Y%m%d_%H%M%S", localtime())
# #     return strftime("%Y%m%d_%H%M%S", gmtime())
#     
# #]]get_TimeLabel_Now():

#ref https://jacksonbates.wordpress.com/2015/09/14/python-fu-4-hello-warning/
def hello_warning(image, drawable):
    # function code goes here...
    pdb.gimp_message("Hello, world!")

#ref https://www.ibm.com/developerworks/jp/opensource/library/os-autogimp/
def plugin_main(timg, tdrawable):
    
    dpath = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\2_"
    
    fpath = "%s\\python_fu.txt" % (dpath)
#     fpath = "%s\\python_fu.%s.txt" % (dpath, get_TimeLabel_Now())
#     fpath = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\2_\\python_fu.txt"
    
    f = open(fpath, "a")
    
    f.write("リサイズするスクリプトを作成する")
#     f.write("time is : %s" % get_TimeLabel_Now())
    
    f.write("\n")
    
    f.close()
    
    
#     print "Hello, world!"

register(
        "python_fu_resize",
        "Saves the image at a maximum width and height",
        "Saves the image at a maximum width and height",
        "Nathan A. Good",
        "Nathan A. Good",
        "2010",
        "<Image>/Image/Resize to max...",
        "RGB*, GRAY*",
        [],
        [],
        plugin_main)

register(
		"hello_warning",
		"display message",
		"display message",
		"https://jacksonbates.wordpress.com",
		"https://jacksonbates.wordpress.com",
		"September 14, 2015",
		"<Image>/Image/Hello warning !",
		"RGB*, GRAY*",
		[],
		[],
		hello_warning)
#     hello_warning, menu="/File/Hello warning!")  # second item is menu location

# register(
#     "python-fu-hello-warning",
#     "Hello world warning",
#     "Prints 'Hello, world!' to the error console",
#     "Jackson Bates", "Jackson Bates", "2015",
#     "Hello warning",
#     "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
#     [
#         (PF_IMAGE, "image", "takes current image", None),
#         (PF_DRAWABLE, "drawable", "Input layer", None)
#     ],
#     [],
#     hello_warning, menu="/File")  # second item is menu location
# #     hello_warning, menu="/File/Hello warning!")  # second item is menu location

main() # プラグインを駆動させるための関数

