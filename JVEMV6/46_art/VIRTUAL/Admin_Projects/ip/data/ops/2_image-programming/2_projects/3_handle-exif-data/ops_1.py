# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\2_image-programming\2_projects\3_handle-exif-data\ops_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
at : 2018/08/23 12:33:00

r w && r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\2_image-programming\2_projects\3_handle-exif-data
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
from win32api import GetSystemMetrics
from matplotlib import pylab as plt

#ref https://www.lifewithpython.com/2014/12/python-extract-exif-data-like-data-from-images.html
from PIL import Image
from PIL.ExifTags import TAGS

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

#ref https://www.lifewithpython.com/2014/12/python-extract-exif-data-like-data-from-images.html
def get_exif_of_image(file):
    """Get EXIF of an image if exists.

    指定した画像のEXIFデータを取り出す関数
    @return exif_table Exif データを格納した辞書
    """
    im = Image.open(file)

    # Exif データを取得
    # 存在しなければそのまま終了 空の辞書を返す
    try:
        exif = im._getexif()
    except AttributeError:
        return {}

    # タグIDそのままでは人が読めないのでデコードして
    # テーブルに格納する
    exif_table = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    return exif_table


'''###################
    
    get_GPS_Data(fpath_Image)
    
    @return: tuple
             => (('N', 35, 35, 24.14), ('E', 139, 34, 48.01))
    
    @param fpath_Image: file full path
    
    @example file : C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload\2018-08-22_15-42-10_000.jpg
    
    [ops_1.py:126] dicOf_Exif['GPSInfo'] =>
        {1: 'N', 2: ((35, 1), (35, 1), (2414, 100)), 3: 'E', 4: ((139, 1), (34, 1), (480
        1, 100)), 5: b'\x00', 6: (24268, 387), 7: ((6, 1), (42, 1), (900, 100)), 12: 'K'
        , 13: (0, 1), 16: 'T', 17: (80093, 231), 23: 'T', 24: (80093, 231), 29: '2018:08
        :22', 31: (10, 1)}        
###################'''
def get_GPS_Data(fpath_Image):
    
    dicOf_Exif = get_exif_of_image(fpath_Image)# def get_GPS_Data():
    
    gps_Info = dicOf_Exif['GPSInfo']
    
    '''###################
        lat, longi        
    ###################'''
    txt_Lat = "%s=" % (gps_Info[1])
    txt_Longi = "%s=" % (gps_Info[3])

    '''###################
        values
    ###################'''
    vals_Lat = gps_Info[2]
    
    txt_Lat += "%d-%d-%.02f" % \
            (vals_Lat[0][0], vals_Lat[1][0], vals_Lat[2][0] * 1.0 / vals_Lat[2][1])
#             (vals_Lat[0][0], vals_Lat[1][0])

    vals_Longi = gps_Info[4]
    
    txt_Longi += "%d-%d-%.02f" % \
            (vals_Longi[0][0], vals_Longi[1][0], vals_Longi[2][0] * 1.0 / vals_Longi[2][1])

#     txt_Longi += "%d-%d-" % \
#             (vals_Longi[0][0], vals_Longi[1][0])

    
    '''###################
        tuples
    ###################'''
    data_Lat = (gps_Info[1], vals_Lat[0][0], vals_Lat[1][0], vals_Lat[2][0] * 1.0 / vals_Lat[2][1])
    data_Longi = (gps_Info[3], vals_Longi[0][0], vals_Longi[1][0], vals_Longi[2][0] * 1.0 / vals_Longi[2][1])
    
    data_Final = (data_Lat, data_Longi)
    
    '''###################
        report        
    ###################'''
    print("[%s:%d] txt_Lat = %s, txt_Longi = %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , txt_Lat, txt_Longi
            ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return data_Final
    
#/ def get_GPS_Data(fpath_Image):
    
def test_1():

    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\iphone_to_upload"
#     C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload
    fname_Ops_Image = "2018-08-22_15-32-53_000.jpg"
#     fname_Ops_Image = "2018-08-22_15-42-10_000.jpg"
     
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)

    '''###################
        get : exif data
    ###################'''
#     print(get_exif_of_image(fpath_Ops_Image)) 
# #     print get_exif_of_image(fpath_Ops_Image)
# #     print get_exif_of_image("sample.jpg")
    
    
    #ref https://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python
    
#     for item in dicOf_Exif:
#     
#         print(item)
#         
#     #/for item in dicOf_Exif:

#     for key in sorted(dicOf_Exif.keys()):
#     
#         print(key)
#         
#     #/for key in :

#     print("[%s:%d] dicOf_Exif['SubjectLocation'] => " % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     print(dicOf_Exif['SubjectLocation'])
    
    '''###################
        gps info
    ###################'''
    result = get_GPS_Data(fpath_Ops_Image)
            #(('N', 35, 35, 24.14), ('E', 139, 34, 48.01))
    
    print()
    print("[%s:%d] GPS data =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(result)
    
    
    
    return
    
    dicOf_Exif = get_exif_of_image(fpath_Ops_Image)
    
    print()
    print("[%s:%d] dicOf_Exif['GPSInfo'] => " % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(dicOf_Exif['GPSInfo'])

    '''###################
        gps info
    ###################'''
    gps_Info = dicOf_Exif['GPSInfo']
    
    for item in gps_Info.keys():
#     for item in gps_Info:
    
        print("key => %d" % (item))
        print(gps_Info[item])
        print()
#         print("key => %d" % (item))
#         print(gps_Info[item])
#         print("%s => %s" % (item, gps_Info[item]))
#         print(item, type(item))
#                 #1 <class 'int'>
        
    #/for item in gps_Info:

    
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
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