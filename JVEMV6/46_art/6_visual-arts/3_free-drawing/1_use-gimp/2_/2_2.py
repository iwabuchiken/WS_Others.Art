# -*- coding: utf-8 -*-
'''
C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\3_free-drawing\1_use-gimp\2_
python 2_2.py

pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\3_free-drawing\1_use-gimp\2_
python 2_2.py


'''

'''
    Regex
print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^ +(print )(".+" %.+\(.+\).*)$
^( +)(print )(".+" %.+\(.+\).*)$
$1$2($3)

print "[%s:%d] result => %s" % \
        (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^( +)(print )(".+" %) \\\r\n(.+)$
$1$2($3)$4$5
$1$2($3 \\\r\n$4)

print ("[%s:%d] all done" % (libs.thisfile(), libs.linenum()))
^( +)(print )(.+)(libs.+file\(\))(.+)
$1$2$3os.path.basename($4)$5
'''


import sys
from sympy.solvers.tests.test_constantsimp import C2

import os

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
from libs_46_art import cons_art
# from libs_31 import libmt

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
from libs_mm import libs
# from libs import libs

import getopt
import os
import inspect

import math as math, struct, numpy as np

from shutil import copyfile

import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont

from random import randint

###############################################
def test_3():
    
    '''###################
        params        
    ###################'''
    w = 640
    h = 640
    
    center_X = w / 2
    center_Y = h / 2
    
    r = 200
#     r = 50
    
    col_R = randint(0, 255)
    col_G = randint(0, 255)
    col_B = randint(0, 255)
    
    colsOf_ImageNew = (col_R, col_G, col_B)
    
    sizeOf_Canvas = (w, h)
    
    dataOf_Ellipse = (center_X - r, center_Y - r,
                      center_X + r, center_X + r)
    
    im = Image.new("RGB", sizeOf_Canvas, colsOf_ImageNew)
#     im = Image.new("RGB", sizeOf_Canvas, (128, 128, 128))
#     im = Image.new("RGB", (512, 512), (128, 128, 128))
    
    '''###################
        ellipse        
    ###################'''
    draw = ImageDraw.Draw(im)
    
    #ref https://stackoverflow.com/questions/4789894/python-pil-how-to-draw-an-ellipse-in-the-middle-of-an-image#4790962
    #ref outline https://endoyuta.com/2015/09/27/python3-pillowの使い方/
    draw.ellipse(dataOf_Ellipse, outline=(0,0,0))
#     draw.ellipse(dataOf_Ellipse, fill=(0, 0, 255))
#     draw.ellipse((250, 300, 450, 400), fill=(0, 0, 255))
    
    '''###################
        lines
    ###################'''
    coords_L1 = (w/2 - r, h/2, w/2 + r, h/2)
    draw.line(coords_L1, fill=(255, 0, 0), width=2)
#     draw.line(coords_L1, fill=(255, 0, 0), width=8)
#     draw.line((0, im.height, im.width, 0), fill=(255, 0, 0), width=8)

    coords_L2 = (w/2, h/2 - r, w/2, h/2 + r)
    draw.line(coords_L2, fill=(255, 0, 0), width=2)
    
#     # 45 degrees
#     th = np.pi / 4
#     
#     dx = r * np.cos(th)
#     dy = r * np.sin(th)
#     
#     coords_L3 = (w/2 + dx, h/2 - dy, w/2 - dx, h/2 + dy)
#     draw.line(coords_L3, fill=(255, 0, 0), width=2)
    
    for i in (1,2, 4, 5) :
#     for i in (1,2) :

        th = np.pi * i / 6
        
        dx = r * np.cos(th)
        dy = r * np.sin(th)
        
        coords_L4 = (w/2 + dx, h/2 - dy, w/2 - dx, h/2 + dy)
        draw.line(coords_L4, fill=(255, 0, 0), width=2)
        
    '''###################
        file        
    ###################'''

    dpath_Out = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/6_visual-arts/3_free-drawing/1_use-gimp/2_/data2"
    
    fname = "image_%s.jpg" % libs.get_TimeLabel_Now()
    
    fpath_Out = "%s/%s" % (dpath_Out, fname)
    
    #ref https://endoyuta.com/2015/09/27/python3-pillowの使い方/
    res = im.save(fpath_Out)
    
    print()
    print("[%s:%d] save image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , res
            ), file=sys.stderr)
    
    
    print()
    print ("[%s:%d] test_3 => done")

    
#/def test_2():

def test_2():
    
    w = 640
    h = 640
    
    center_X = w / 2
    center_Y = h / 2
    
    radius = 200
#     radius = 50
    
    col_R = randint(0, 255)
    col_G = randint(0, 255)
    col_B = randint(0, 255)
    
    colsOf_ImageNew = (col_R, col_G, col_B)
    
    sizeOf_Canvas = (w, h)
    
    dataOf_Ellipse = (center_X - radius, center_Y - radius,
                      center_X + radius, center_X + radius)
    
    im = Image.new("RGB", sizeOf_Canvas, colsOf_ImageNew)
#     im = Image.new("RGB", sizeOf_Canvas, (128, 128, 128))
#     im = Image.new("RGB", (512, 512), (128, 128, 128))
    
    draw = ImageDraw.Draw(im)
    
    #ref https://stackoverflow.com/questions/4789894/python-pil-how-to-draw-an-ellipse-in-the-middle-of-an-image#4790962
    #ref outline https://endoyuta.com/2015/09/27/python3-pillowの使い方/
    draw.ellipse(dataOf_Ellipse, outline=(0,0,0))
#     draw.ellipse(dataOf_Ellipse, fill=(0, 0, 255))
#     draw.ellipse((250, 300, 450, 400), fill=(0, 0, 255))
    
    '''###################
        file        
    ###################'''

    dpath_Out = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/6_visual-arts/3_free-drawing/1_use-gimp/2_/data2"
    
    fname = "image_%s.jpg" % libs.get_TimeLabel_Now()
    
    fpath_Out = "%s/%s" % (dpath_Out, fname)
    
    #ref https://endoyuta.com/2015/09/27/python3-pillowの使い方/
    res = im.save(fpath_Out)
    
    print()
    print("[%s:%d] save image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , res
            ), file=sys.stderr)
    
    
    print()
    print ("[%s:%d] test_1 => done")

    
#/def test_2():

def test_1():
    
    im = Image.new("RGB", (512, 512), (128, 128, 128))
    
    dpath_Out = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/6_visual-arts/3_free-drawing/1_use-gimp/2_/data2"
    
    fname = "image_%s.jpg" % libs.get_TimeLabel_Now()
    
    fpath_Out = "%s/%s" % (dpath_Out, fname)
    
    #ref https://endoyuta.com/2015/09/27/python3-pillowの使い方/
    res = im.save(fpath_Out)
    
    print()
    print("[%s:%d] save image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , res
            ), file=sys.stderr)
    
    
    print()
    print ("[%s:%d] test_1 => done")

    
#/def test_2():

def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_3()
#     test_2()
#     test_1()
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog(): # from : 20180116_103908

'''
<usage>
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
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))

