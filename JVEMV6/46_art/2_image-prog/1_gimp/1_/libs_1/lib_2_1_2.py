#!C:\WORKS_2\Programs\GIMP 2\Python\python
# -*- coding: utf-8 -*-
from __future__ import print_function

'''
file : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\2_image-prog\1_gimp\1_\libs_1\libs_2_1_2.py
orig : 
at : 2018/04/04 12:39:39

pushd C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\2_image-prog\1_gimp\1_\libs_1
python libs_2_1_2.py

C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\1_

'''

'''
<python-fu console> ---------------------------------

import os, sys
path = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\1_"
os.chdir(path)
os.getcwd()

sys.path.append('.')

from libs_1 import abc
from libs_1 import lib_2_1_2 as lib
# from libs_1 import lib_2_1_2
# from libs_1 import 2_1_2

lib_2_1_2.test_1()

#ref reload https://atkonn.blogspot.jp/2008/02/python-python37.html
reload(lib)

lib.main()


'''



# from __future__ import print_function

###############################################
import sys

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog')    # libs_VX7GLZ
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\libs_image_prog')    # libs_VX7GLZ

from libs_image_prog import libs

'''###################
    import : built-in modules        
###################'''
import getopt, os, inspect, math as math, random as rnd

###############################################
import wave, struct
# import numpy as np
# from pylab import *

def test_1():

  print(os.getcwd())

  fname = "test.%s.txt" % (libs.get_TimeLabel_Now())

  f = open(fname, "w")
#     f = open("test.txt", "w")

  f.write(libs.get_TimeLabel_Now())

  f.close

  print("file closed")

#/ def test_1():

### height : 画像データの高さ (px)

def create_image(width, height):
  # 画像データを生成
  return gimp.Image(width, height, RGB)
# レイヤーの追加
## 指定した名前のレイヤーを新規に作成し、画像データに挿入する
### image : レイヤーを追加する画像データ
### name : 新規に作成するレイヤーの名前（文字列）
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
# ペンシルツールで線を描く
## 配列に格納した座標列を結ぶ線を描画領域にペンシルツールで描く
### drawable : 描画領域（レイヤーなど）
### lines : 描画される線の座標列を格納した配列
def draw_pencil_lines(drawable, lines):
  # ペンシルツールで線を描画する
  pdb.gimp_pencil(drawable, len(lines), lines)
# ペンシルツールで矩形を描く
## 左上、右下座標をもとに描画領域に矩形を描く
### drawable : 描画領域（レイヤーなど）
### x1 : 左上の X 座標
### y1 : 左上の Y 座標
### x2 : 右下の X 座標
### y2 : 右下の Y 座標
def draw_rect(drawable, x1, y1, x2, y2):
  lines = [x1, y1, x2, y1, x2, y2, x1, y2, x1, y1]
  draw_pencil_lines(drawable, lines)
# エアブラシで線を描く
## 配列に格納した座標列を結ぶ線を描画領域にエアブラシで描く
### drawable : 描画領域（レイヤーなど）
### pressure : 筆圧 (0-100)
### lines : 描画される線の座標列を格納した配列
def draw_airbrush_lines(drawable, pressure, lines):
  # エアブラシで線を描画する
  pdb.gimp_airbrush(drawable, pressure, len(lines), lines)
# 文字列を描画する
## 指定した描画領域に文字列を描画します
### drawable : 描画領域（レイヤーなど）
### x : 文字列を描画する位置の X 座標
### y : 文字列を描画する位置の Y 座標
### size : フォントサイズ
### str : 描画する文字列
def draw_text(drawable, x, y, size, str):
  image = drawable.image
  border = -1
  antialias = True
  size_type = PIXELS
  fontname = '*'
  floating_sel = pdb.gimp_text_fontname(image, drawable, x, y, str, border,
                 antialias, size, size_type, fontname)
  pdb.gimp_floating_sel_anchor(floating_sel)
# 描画する色を変更する
## パレットの前景色を変更して描画色を設定する
### r : 赤要素 (0-255)
### g : 緑要素 (0-255)
### b : 青要素 (0-255)
### a : 透明度 (0-1.0)
def set_color(r, g, b, a):
  color = (r, g, b, a)
  pdb.gimp_context_set_foreground(color)
# 描画する線の太さを変える
## ブラシのサイズを変更して線の太さを設定する
### width : 線の太さ
def set_line_width(width):
  pdb.gimp_context_set_brush_size(width)
# 画像の表示
## 新しいウィンドウを作成し、画像データを表示する
### image : 表示する画像データ
def display_image(image):
  gimp.Display(image)
def main():
#   image = create_image(640, 800)
  image = create_image(640, 400)
  layer = add_layer(image, "背景")
  draw_rect(layer, 390, 210, 490, 310)
  draw_text(layer, 200, 180, 20, "こんにちは")
  lines = [110,90, 120,180, 130,110, 140,150]
  draw_airbrush_lines(layer, 75, lines)
  set_color(255,0,0,1.0)  # Red
  set_line_width(1)
  draw_rect(layer, 420, 240, 520, 340)
  display_image(image)
def exec_prog():

  '''###################
        ops        
  ###################'''
  test_1()

  print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()

            ), file=sys.stderr)

'''
<usage>
test_1.py [-fXXX]  #=> frequency
test_1.py -f402
'''
if __name__ == "__main__" :

  '''###################
    	validate : help option		
  ###################'''

  '''###################
    	get options		
  ###################'''

  '''###################
    	evecute		
  ###################'''
  exec_prog()

  print()

  print("[%s:%d] all done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()

            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
