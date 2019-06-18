# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\3_opencv\1_motion-detection\1_\ops_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\2_image-programming\2_projects\3_handle-exif-data\ops_1.py
at : 2018/08/23 12:33:00

pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\3_opencv\1_motion-detection\1_
python ops_1.py



'''
###############################################
import sys

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects') # libs_mm

from libs_admin import libs, lib_ip

'''###################
    import : built-in modules        
###################'''
# import getopt
import os, glob, getopt, math as math, numpy as np
# import inspect

'''###################
    import : built-in modules        
###################'''
import cv2
# from pandas.compat import str_to_bytes
from numpy.distutils.from_template import item_re
#ref https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
# from win32api import GetSystemMetrics
# from matplotlib import pylab as plt

#ref https://www.lifewithpython.com/2014/12/python-extract-exif-data-like-data-from-images.html
# from PIL import Image
# from PIL.ExifTags import TAGS

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

#ref https://www.lifewithpython.com/2014/12/python-extract-exif-data-like-data-from-images.html

'''###################
    at : 2018/08/24 15:38:23
    
    <usage>
        0. C/P video file
            from : anywhere
            to : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\3_opencv\1_motion-detection\data
        1. set
            1. dir path : dpath_Ops_Videos
            2. file name : fname_Ops_Video
        2. console
            exec 
                pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\3_opencv\1_motion-detection\1_
                python ops_1.py
        3. ==> 3 windows show up

###################'''
def test_1():
    
    #debug
    print("[%s:%d] test_1() --> stareting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    '''######################################
        prep
    ######################################'''
    dpath_Ops_Videos = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\3_opencv\\1_motion-detection\\data"
#     C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\3_opencv\1_motion-detection\data
    fname_Ops_Video = "2018-08-24_06-20-53_000.mov.0-10-sec.avi"
#     fname_Ops_Video = "vtest.avi"
     
    fpath_Ops_Video = os.path.join(dpath_Ops_Videos, fname_Ops_Video)

    '''###################
        ops
    ###################'''
    # 定数定義
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # インターバル
    FRAME_RATE = 30  # fps
    
    WINDOW_ORG = "org"
    WINDOW_BACK = "back"
    WINDOW_DIFF = "diff"
    
    FILE_ORG = fpath_Ops_Video
#     FILE_ORG = "org_768x576.avi"
    
    # ウィンドウの準備
    cv2.namedWindow(WINDOW_ORG)
    cv2.namedWindow(WINDOW_BACK)
    cv2.namedWindow(WINDOW_DIFF)
    
    # 元ビデオファイル読み込み
    mov_org = cv2.VideoCapture(FILE_ORG)
    
    # 最初のフレーム読み込み
    has_next, i_frame = mov_org.read()
    
    # 背景フレーム
    back_frame = np.zeros_like(i_frame, np.float32)

    #debug
    print("[%s:%d] prep done. starting while loop..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

    
    # 変換処理ループ
    while has_next == True:
        # 入力画像を浮動小数点型に変換
        f_frame = i_frame.astype(np.float32)
    
        # 差分計算
        diff_frame = cv2.absdiff(f_frame, back_frame)
    
        # 背景の更新
        cv2.accumulateWeighted(f_frame, back_frame, 0.025)
    
        # フレーム表示
        cv2.imshow(WINDOW_ORG, i_frame)
        cv2.imshow(WINDOW_BACK, back_frame.astype(np.uint8))
        cv2.imshow(WINDOW_DIFF, diff_frame.astype(np.uint8))
    
        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break
    
        # 次のフレーム読み込み
        has_next, i_frame = mov_org.read()

    #debug
    print("[%s:%d] while loop done..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    # 終了処理
    cv2.destroyAllWindows()
    mov_org.release()    
    
    '''###################
        message
    ###################'''
    print()
#     print("[%s:%d] test_1 =======================" % \
    print("[%s:%d] test_1 ======================= done" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stderr)
    
    
    
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

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
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())


'''
ApertureValue
BrightnessValue
ColorSpace
ComponentsConfiguration
CustomRendered
DateTime
DateTimeDigitized
DateTimeOriginal
ExifImageHeight
ExifImageWidth
ExifOffset
ExifVersion
ExposureBiasValue
ExposureMode
ExposureProgram
ExposureTime
FNumber
Flash
FlashPixVersion
FocalLength
FocalLengthIn35mmFilm
GPSInfo
ISOSpeedRatings
LensMake
LensModel
LensSpecification
Make
MakerNote
MeteringMode
Model
Orientation
ResolutionUnit
SceneCaptureType
SceneType
SensingMethod
ShutterSpeedValue
Software
SubjectLocation
SubsecTimeDigitized
SubsecTimeOriginal
WhiteBalance
XResolution
YCbCrPositioning
YResolution
'''