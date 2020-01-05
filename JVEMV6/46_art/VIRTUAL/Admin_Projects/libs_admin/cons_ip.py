'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\cons_ip.py
    orig    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\lib_ip.py
    at      : 2018/06/08 10:10:11
'''

'''###################
    import : built-in modules        
###################'''
import sys, os

#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum
from time import gmtime, strftime, localtime, time

'''###################
    import : orig modules        
###################'''
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects')
# from libs_admin import libs

'''###################
    @param string_type
            serial    "20160604_193404"
            basic     "2016/06/04 19:34:04"
###################'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
#     t = time.time()
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


class DfltVals(Enum):
    
    #get_4Corners__Corner_Width      = 200
    get_4Corners__Corner_Width      = 100
#     get_4Corners__Corner_Width      = 280
    #get_4Corners__Corner_Padding    = 20
    get_4Corners__Corner_Padding    = 10

    '''###################
        dos attack        
    ###################'''
    numOf_DosAttack = 0

class ColorThresholds(Enum):
    
    '''######################################
        Red
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
#     isRed_Max_Val_R__Lower = 2.2 * 1000
#    isRed_Max_Val_R__Lower = 2.0 * 1000
#    isRed_Max_Val_R__Lower = 1.85 * 1000
    #isRed_Max_Val_R__Lower = 1.70 * 1000
    isRed_Max_Val_R__Lower = 1.60 * 1000
    isRed_Max_Val_R__Upper = 6.0 * 1000
#    isRed_Max_Val_R__Upper = 4.7 * 1000
#     isRed_Max_Val_R__Upper = 3.9 * 1000
    
    
    # G
#     isRed_Max_Val_G__Lower = 2.3 * 1000
#    isRed_Max_Val_G__Lower = 2.0 * 1000
#    isRed_Max_Val_G__Lower = 1.85 * 1000
    isRed_Max_Val_G__Lower = 1.70 * 1000
    isRed_Max_Val_G__Upper = 5.5 * 1000	#=> 20180709_060511
#    isRed_Max_Val_G__Upper = 4.7 * 1000
#     isRed_Max_Val_G__Upper = 3.9 * 1000
    
    # B
#    isRed_Max_Val_B__Lower = 1.6 * 1000
#    isRed_Max_Val_B__Lower = 1.35 * 1000
    isRed_Max_Val_B__Lower = 1.00 * 1000
#     isRed_Max_Val_B__Lower = 1.8 * 1000
#    isRed_Max_Val_B__Upper = 2.5 * 1000
    isRed_Max_Val_B__Upper = 4.25 * 1000
#    isRed_Max_Val_B__Upper = 3.5 * 1000
#     isRed_Max_Val_B__Upper = 3.1 * 1000
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
#    isRed_IdxOf_Max_R__Upper = 50
#     isRed_IdxOf_Max_R__Upper = 70
    isRed_IdxOf_Max_R__Upper = 91
    isRed_IdxOf_Max_R__Lower = 0
     
    # G
    #isRed_IdxOf_Max_G__Upper = 60
    #isRed_IdxOf_Max_G__Upper = 80
    isRed_IdxOf_Max_G__Upper = 105
    isRed_IdxOf_Max_G__Lower = 0
     
    # B
#     isRed_IdxOf_Max_B__Upper = 200
#    isRed_IdxOf_Max_B__Upper = 210
#    isRed_IdxOf_Max_B__Upper = 230
    isRed_IdxOf_Max_B__Upper = 250
    isRed_IdxOf_Max_B__Lower = 150
     

    '''######################################
        Green
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
#     isGreen_Max_Val_R__Lower = 3.0 * 1000
#     isGreen_Max_Val_R__Lower = 2.6 * 1000
    isGreen_Max_Val_R__Lower = 1.8 * 1000
    isGreen_Max_Val_R__Upper = 5.4 * 1000
    #isGreen_Max_Val_R__Upper = 5.3 * 1000
#     isGreen_Max_Val_R__Upper = 4.1 * 1000
    
    # G
    isGreen_Max_Val_G__Lower = 1.4 * 1000
    isGreen_Max_Val_G__Upper = 4.95 * 1000
#    isGreen_Max_Val_G__Upper = 4.5 * 1000
#     isGreen_Max_Val_G__Upper = 3.7 * 1000
#     isGreen_Max_Val_G__Upper = 3.2 * 1000
#     isGreen_Max_Val_G__Upper = 2.8 * 1000
#     isGreen_Max_Val_G__Upper = 2.6 * 1000
    
    # B
    #isGreen_Max_Val_B__Lower = 2.0 * 1000
    isGreen_Max_Val_B__Lower = 1.85 * 1000
    isGreen_Max_Val_B__Upper = 4.85 * 1000
    #isGreen_Max_Val_B__Upper = 4.3 * 1000
#     isGreen_Max_Val_B__Upper = 3.2 * 1000
    
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
#     isGreen_IdxOf_Max_R__Upper = 50
#    isGreen_IdxOf_Max_R__Upper = 65
    #isGreen_IdxOf_Max_R__Upper = 120
    isGreen_IdxOf_Max_R__Upper = 130
    isGreen_IdxOf_Max_R__Lower = 0
     
    # G
#     isGreen_IdxOf_Max_G__Upper = 170
#     isGreen_IdxOf_Max_G__Upper = 210
#     isGreen_IdxOf_Max_G__Upper = 240
    isGreen_IdxOf_Max_G__Upper = 255
    isGreen_IdxOf_Max_G__Lower = 80
     
    # B
#     isGreen_IdxOf_Max_B__Upper = 200
#     isGreen_IdxOf_Max_B__Upper = 120
#     isGreen_IdxOf_Max_B__Upper = 145
    #isGreen_IdxOf_Max_B__Upper = 160
    isGreen_IdxOf_Max_B__Upper = 175
    isGreen_IdxOf_Max_B__Lower = 50
     

    '''######################################
        Yellow
    ######################################'''
    '''###################
        thresholds : max values
    ###################'''
    # max values
    # R
#     ts_Max_Val_R__Lower = 4000
#    isYellow_Max_Val_R__Lower = 2500
#     isYellow_Max_Val_R__Lower = 2.2 * 1000
    isYellow_Max_Val_R__Lower = 1.6 * 1000
    isYellow_Max_Val_R__Upper = 6.4 * 1000
#     isYellow_Max_Val_R__Upper = 5.8 * 1000
#     isYellow_Max_Val_R__Upper = 5000
    
    
    # G
#     isYellow_Max_Val_G__Lower = 3000
#    isYellow_Max_Val_G__Lower = 1.6 * 1000
    isYellow_Max_Val_G__Lower = 1.1 * 1000
    isYellow_Max_Val_G__Upper = 6.3 * 1000
#    isYellow_Max_Val_G__Upper = 4000
#     isYellow_Max_Val_G__Upper = 5.4 * 1000
#     isYellow_Max_Val_G__Upper = 4.8 * 1000
    
    # B
#     isYellow_Max_Val_B__Lower = 3500
#     isYellow_Max_Val_B__Lower = 2000
#    isYellow_Max_Val_B__Lower = 1.6 * 1000
#     isYellow_Max_Val_B__Lower = 1.4 * 1000
    isYellow_Max_Val_B__Lower = 1.2 * 1000
    isYellow_Max_Val_B__Upper = 10.8 * 1000 #=> 20180709_064100
#    isYellow_Max_Val_B__Upper = 6.2 * 1000
#     isYellow_Max_Val_B__Upper = 5.8 * 1000
#     isYellow_Max_Val_B__Upper = 4500
    
#     isYellow_Max_Val_G = 2000
#     isYellow_Max_Val_B = 2000

    '''###################
        thresholds : index of max values
    ###################'''    
    # index of max values
    # R
    isYellow_IdxOf_Max_R__Upper = -1      # -1 ==> not used
#    isYellow_IdxOf_Max_R__Lower = 80
    isYellow_IdxOf_Max_R__Lower = 115
#     isYellow_IdxOf_Max_R__Lower = 95
     
    # G

    isYellow_IdxOf_Max_G__Upper = 250
    isYellow_IdxOf_Max_G__Lower = 115
    #isYellow_IdxOf_Max_G__Lower = 130
#     isYellow_IdxOf_Max_G__Upper = 220
#     isYellow_IdxOf_Max_G__Lower = 145
#     isYellow_IdxOf_Max_G__Lower = 165
#     isYellow_IdxOf_Max_G__Lower = 180
     
    # B
#     isYellow_IdxOf_Max_B__Upper = 200
#     isYellow_IdxOf_Max_B__Upper = 180
#     isYellow_IdxOf_Max_B__Upper = 165
#     isYellow_IdxOf_Max_B__Upper = 240
    isYellow_IdxOf_Max_B__Upper = 255
    isYellow_IdxOf_Max_B__Lower = 140      # -1 ==> not used

    '''######################################
        White
    ######################################'''
    '''###################
        thresholds : index of max values
    ###################'''    
    isWhite_IdxOf_Max = 245
#     isWhite_IdxOf_Max = 255
    
    '''###################
        thresholds : max values
    ###################'''
    # R
    isWhite_Max_Val__Lower = 14 * 1000
#     isWhite_Max_Val__Lower = 26 * 1000
#     isYellow_Max_Val_R__Upper = 5000

    '''######################################
        Black
    ######################################'''
    '''###################
        thresholds : index of max values
    ###################'''    
    isBlack_IdxOf_Max = 0
    
    '''###################
        thresholds : max values
    ###################'''
    # R
#     isBlack_Max_Val__Lower = 21 * 1000
    #isBlack_Max_Val__Lower = 16 * 1000
    isBlack_Max_Val__Lower = 15 * 1000
#     isBlack_Max_Val__Lower = 26 * 1000


    '''######################################
        thresholds : HSV
    ######################################'''
    '''###################
        yellow        
    ###################'''
    #isYellow_HSV_Variance__Upper = 0.3
    isYellow_HSV_Variance__Upper = 0.65
    isYellow_HSV_Variance__Lower = 0.0
    #isYellow_HSV_Variance__Lower = 0.002
#     isYellow_HSV_Variance__Lower = 0.01
    
#     isYellow_HSV_Average__Upper = 90.0
    #isYellow_HSV_Average__Upper = 93.0
    #isYellow_HSV_Average__Upper = 97.0
    #isYellow_HSV_Average__Upper = 98.0
    isYellow_HSV_Average__Upper = 99.2
    isYellow_HSV_Average__Lower = 85.500 # 20181217_112606
    #isYellow_HSV_Average__Lower = 88.0
    
    '''###################
        red        
    ###################'''
#     isRed_HSV_Variance__Upper = 0.3
    #isRed_HSV_Variance__Upper = 0.40
    isRed_HSV_Variance__Upper = 0.43
    isRed_HSV_Variance__Lower = 0.0
    #isRed_HSV_Variance__Lower = 0.002
#     isRed_HSV_Variance__Lower = 0.01
    
    #isRed_HSV_Average__Upper = 124.0	# 20190215_070409
    isRed_HSV_Average__Upper = 124.6
    isRed_HSV_Average__Lower = 115.0
    #isRed_HSV_Average__Lower = 116.0
#     isRed_HSV_Average__Lower = 120.0
    
    '''###################
        green        
    ###################'''
#     isGreen_HSV_Variance__Upper = 0.3
    #isGreen_HSV_Variance__Upper = 0.38
    #isGreen_HSV_Variance__Upper = 0.60
    # isGreen_HSV_Variance__Upper = 0.75
    isGreen_HSV_Variance__Upper = 0.76	# 20181103_085711
    isGreen_HSV_Variance__Lower = 0.0
    #isGreen_HSV_Variance__Lower = 0.002
#     isGreen_HSV_Variance__Lower = 0.01
    
#     isGreen_HSV_Average__Upper = 72.0
#     isGreen_HSV_Average__Upper = 75.0
    #isGreen_HSV_Average__Upper = 79.0
    #isGreen_HSV_Average__Upper = 83.0
    isGreen_HSV_Average__Upper = 85.0	# 20190127_075112
    isGreen_HSV_Average__Lower = 58.0
    #isGreen_HSV_Average__Lower = 67.0
#     isGreen_HSV_Average__Lower = 70.0
    
    '''###################
        blue
        ref : https://docs.google.com/spreadsheets/d/1K0hGC_FFcnUhNEgWi2wYSeDBk0F4dDpSh0y5Dg1DOjE/edit#gid=0
    ###################'''
    #isBlue_HSV_Variance__Upper = 0.25
    #isBlue_HSV_Variance__Upper = 0.270	# 20181208_094922
    #isBlue_HSV_Variance__Upper = 0.7000	# 20181209_071939
    isBlue_HSV_Variance__Upper = 0.930	# 20181214_063434
    
    isBlue_HSV_Variance__Lower = 0.01
    
    #isBlue_HSV_Average__Upper = 13.30
    isBlue_HSV_Average__Upper = 17.00	# 20181208_094215    
    isBlue_HSV_Average__Lower = 8.850	# 20181214_063812
    #isBlue_HSV_Average__Lower = 11.00
    #isBlue_HSV_Average__Lower = 9.500	# 20181212_064030
    
    '''###################
        pink
        ref : https://docs.google.com/spreadsheets/d/1K0hGC_FFcnUhNEgWi2wYSeDBk0F4dDpSh0y5Dg1DOjE/edit#gid=0
    ###################'''
    #isPink_HSV_Variance__Upper = 0.40
    isPink_HSV_Variance__Upper = 0.75   # 20190205_153002
    isPink_HSV_Variance__Lower = 0.03	# 20190206_100002
    #isPink_HSV_Variance__Lower = 0.18
    
    #isPink_HSV_Average__Upper = 134.70
    #isPink_HSV_Average__Upper = 136.0   # 20190205_152345
    isPink_HSV_Average__Upper = 141.0   # 20190208_114613
    isPink_HSV_Average__Lower = 127.9   # 20190205_153437
    #isPink_HSV_Average__Lower = 129.5   # 20190205_150749
    #isPink_HSV_Average__Lower = 131.00
    
    '''###################
        black        
    ###################'''
    isBlack_HSV_Variance__Upper = 0.00
    isBlack_HSV_Variance__Lower = 0.00
    
    isBlack_HSV_Average__Upper = 0.0
    isBlack_HSV_Average__Lower = 0.0
    
#/ class ColorThresholds(Enum):    

class FilePaths(Enum):
    
    dpath_LogFile = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\logs"
    
    fname_LogFile = "get_4_corners.%s.log" % get_TimeLabel_Now()
#     fname_LogFile = "get_4_corners.%s.log" % libs.get_TimeLabel_Now()
#     fname_LogFile = "get_4_corners.log"
    
    fname_LogFile__Gradation = "gradation.log"
    
    '''###################
        anims        
    ###################'''
    dpath_Anims_Image_Files = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\data\\data_images"
    
    fname_Anims_Image_Files = "leaf-2.1.png"
    
#/ class ColorThresholds(Enum):
    
class ColorNameSet(Enum):

    lo_Color_Sets = [
        
            "oooo"  # other
            
#             '''######################################
#                 r,g,y ==> each only        # 3 types
#             ######################################'''
#             '''###################
#                 r : red
#             ###################'''
            , "ooor"    # kb
            #, "oorr"	# 朝永
            , "oorr"	# シュッツ	20200105_100303
            
#             '''###################
#                 b : blue
#             ###################'''
            #, "booo"    # :m X-X*X RES / 245 / 『相対性理論』　メラー　永田恒夫、伊藤大介、訳 / p.XX
            , "booo"    # :m X-X*X RES / 245 / 『古典場から量子場への道』　高橋康 / p.XX #20190806_084436
            #, "bboo"    # :m X-X*X RES / 245 / 『不完全性定理』　ゲーデル　林晋、八杉満利子 / p.XX
            #, "bboo"    # :m X-X*X RES / 245 / 『四元数』　今野紀雄 / p.XX #20190510_080306
            , "bboo"    # :m RES 1-2*2 / free# VX7GLZ 27#8 / 27. math / 8. miscs / id=68OZ / マクローリン級数、テイラー級数 #20190611_105855

#             '''###################
#                 g : green
#             ###################'''
            #, "gooo"    # ":m 食べた物　間食 / 砂糖菓子"
            , "gooo"    # ":m 食べた物　間食 / 味噌スープ"	# 20191209_091533
            , "ggoo"    # :m 食べた物　間食 / ヨーグルト / +=
            
#             '''###################
#                 y : yellow
#             ###################'''
            , "oooy"    # :m 食べた物
            , "ooyy"    # delete

#             '''###################
#                 p : pink
#             ###################'''
            , "ooop"    # :m 記録 / お酒
            , "oopp"    # : ":m to-write / diary"            
            , "ooyy"    # delete

    
#             '''###################
#                 a : black
#             ###################'''
            , "aaaa"    # 読みたい本
            , "aaao"    # 読みたい本
            , "aaoo"    # 読みたい本
            
#             '''###################
#                 w : white
#             ###################'''
            , "wwww"    # 読みたい本
            , "owww"    # 読みたい本
    
#             '''######################################
#                 r,g,y ==> each, 2        
#             ######################################'''
#             '''###################
#                 blue red
#             ###################'''
            , "boor"    # :diary / diary / 20181206 / (K,C,P,R,)

#             '''###################
#                 blue green
#             ###################'''
            , "bgoo"    # :m RES 1-3*3 / free# JVEMV6 44#5.1_2X / 44. currency / 5. ea tools / 1. first / memo


#             '''###################
#                 blue yellow
#             ###################'''
            , "booy"    # :m art / dessin / D-17 8# / des.竹林、巻雲

#             '''###################
#                 yellow white
#             ###################'''
            , "oowy"    # :m 食べた物
#             '''###################
#                 yellow black
#             ###################'''
            , "aooy"    # :m 食べた物
            , "aaoy"    # :m 食べた物

#             '''###################
#                 green red
#             ###################'''
            , "goor"    # :m XXX
#             '''###################
#                 green yellow
#             ###################'''
            , "gooy"

#             '''###################
#                 green black
#             ###################'''
            , "aggo"	# :m 食べた物　間食 / ヨーグルト / +=

#             '''###################
#                 red yellow
#             ###################'''
            , "oory"    # 読んだ本

#             '''###################
#                 red black
#             ###################'''
            , "aoor"    # kb

#             '''######################################
#                 pink
#             ######################################'''
#             '''###################
#                 pink : yellow
#             ###################'''
            , "oopy"    # :m X-X*X RES / 245 / 『カオスとフラクタル』　山口昌哉 / p.XX

#             '''###################
#                 r,g,y ==> each, 3        # 3 types
#             ###################'''
            
#             '''###################
#                 r,g,y ==> each, 4        # 3 types
#             ###################'''
    
            
#             '''###################
#                 r,g,y ==> 1 or 2 each, 2 kinds        # 3 types
#             ###################'''
#             '''###################
#                 white black
#             ###################'''
            # 1 a / 2 w / 
            , "aoww"    # 読みたい本
            
            # 2 a / 2 1 / 
            , "aaow"    # 読みたい本
            
            
        ]#lo_Color_Sets = [
    
    do_Color_Sets_Memo = {
        
            "oooo" : ""

#             '''#########################################################
#                 r,g,y ==> each only        # 3 types
#             #########################################################'''
#             '''######################################
#                 1 letter
#             ######################################'''
#             '''###################
#                 red
#             ###################'''
#           #, "ooor" : "UNDEFINED"
            #, "ooor" : u':m music / log / XXX / '
            #, "ooor" : u':m music / log / kb / XXX'	# 20181231_072022
            #, "ooor" : u':m music / log / kb / s.1:XXX s.2:XXX s.3:XXX s.4:XXX s.5:XXX'	# 20190505_075300
            #, "ooor" : u':m music / log / kb / s.1:XXX s.2:XXX s.3:XXX s.4:XXX s.5:XXX s.6:XXX s.7:XXX'	# 20190529_105137
            , "ooor" : u':m music / log / gt / || s.1:XXX || s.2:XXX || s.3:XXX || s.4:XXX || s.5:XXX || s.6:XXX || s.7:XXX'	# 20190816_085002
            #, "oorr" : ":m X-X*X RES / 245 / 『量子力学　I』　朝永 / p.XX"	# 朝永	# 20190113_063411
            , "oorr" : ":m X-X*X RES / 245 / 『相対論』　シュッツ / p.XX"	# シュッツ	# 2020年1月5日10:01:28

#             '''###################
#                 green
#             ###################'''
            #, "gooo" : ":m 食べた物　間食 / 砂糖菓子or乾物菓子"
            #, "gooo" : ":m 食べた物　間食 / 砂糖菓子" # 20190204_095122
            #, "ggoo" : u':m 食べた物　間食 / 味噌スープ' # 20191209_091705
            , "gooo" : u':m 食べた物　間食 / 味噌スープ' # 20191209_091705

#             '''###################
#                 yeloow
#             ###################'''
            , "oooy" : u':m 食べた物'

#             '''###################
#                 b : blue
#             ###################'''
            #, "booo" : ":m X-X*X RES / 245 / 『相対性理論』　メラー　永田恒夫、伊藤大介、訳 / p.XX"
            , "booo" : ":m X-X*X RES / 245 / 『古典場から量子場への道』　高橋康 / p.XX" #20190806_084536

#             '''###################
#                 p : pink
#             ###################'''
            , "ooop" : ":m 記録 / お酒"
            , "oopp" : ":m to-write / diary"

#             '''######################################
#                 2 letters
#             ######################################'''
            #, "bboo" : ":m X-X*X RES / 245 / 『不完全性定理』　ゲーデル　林晋、八杉満利子 / p.XX"
            #, "bboo" : ":m X-X*X RES / 245 / 『四元数』　今野紀雄 / p.XX" #20190510_080306
            #, "bboo" : ":m RES 1-2*2 / free# VX7GLZ 27#15_1 / 27. math / 15. quaternion / XXX" #20190611_105855
            #, "bboo" : ":m 1-X*X RES / free# VX7GLZ 28#3CVF XX / 28. physics / 3CVF spinors / XXX" #20190624_150437
            , "bboo" : ":m 1*1 res VX7GLZ / 28#12_1.XX / 28. physics / 12. twistor / 1. lie groups" #20190707_110442
            #, "ggoo" : u':m 食べた物　間食 / ヨーグルト / += '
            #, "ggoo" : u':m 食べた物　間食 / 味噌スープ'	# 20190219_085106
            , "ooyy" : u'\'-*'
            #, "oorr" : u'MEMO'
            
            , "oowy" : u':m 食べた物'
            , "aooy" : u':m 食べた物'
            , "aaoy" : u':m 食べた物'
            , "aaoo" : u':m 読みたい本 / 『XXX』 / 著者=XXX'    # 読みたい本            

#             '''###################
#                 red : black
#             ###################'''
            , "aoor" : u':m music / log / kb / '	# 20190329_101815

#             '''######################################
#                 pink
#             ######################################'''
#             '''###################
#                 pink : yellow
#             ###################'''
            , "oopy" : ":m X-X*X RES / 245 / 『カオスとフラクタル』　山口昌哉 / p.XX"
            
#             '''###################
#                 r,g,y ==> each, 2        # 3 types
#             ###################'''
#             , "oorr"

            #, "oorr" : uMEMO'UNDEFINED'

#             '''######################################
#                 3 letters
#             ######################################'''
            , "owww" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本
            , "aaao" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本

#             '''###################
#                 r,g,y ==> each, 3        # 3 types
#             ###################'''
            
#             '''###################
#                 r,g,y ==> each, 4        # 3 types
#             ###################'''
            , "aaaa" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本
            , "wwww" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本

#             '''###################
#                 r,g,y ==> 1 each, 2 kinds        # 3 types
#             ###################'''
            #, "goor" : u'UNDEFINED'
            , "goor" : u':m XXX'
            
            , "gooy" : u'\'-*'
            
            , "aggo" : u':m 食べた物　間食 / ヨーグルト / +='	# 20181215_070822
            
            , "oory" : u':bookmemo / 読んだ本 / 『XXX』 / 著者=XXX'

#             '''###################
#                 r,g,y ==> 1 or 2 each, 2 kinds        # 3 types
#             ###################'''
            , "aoww" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本
            , "aaow" : u':m 読みたい本 / 『』 / 著者=XXX'    # 読みたい本

#             '''#########################################################
#                 2 kinds
#             #########################################################'''
#             '''######################################
#                 blue, red
#             ######################################'''
            #, "boor" : ":diary / diary / 20181206 / (K,C,P,R,)"
            #, "boor" : ":diary / diary / 20181206 / (K;C;P;R;)"
            #, "boor" : ":diary / diary / 20181206 / (K*C*P*R*)"	# 20181229_085109
            #, "boor" : ":diary / diary / 20190211 / (K*C*P*R*)"	# 20190128_062550
            #, "boor" : ":diary / diary / 20190314 / (K*C*P*R*)"	# 20190314_082519
            #, "boor" : ":diary / diary / 20190403 / (K*C*P*R*)"	# 20190403_073227
            , "boor" : ":diary / memo;diary / 201905XX / (K*C*P*R*J*)"	# 20190530_090842

#             '''###################
#                 blue green
#             ###################'''
            , "bgoo" : ":m RES 1-3*3 / free# JVEMV6 44#5.1_2X / 44. currency / 5. ea tools / 1. first / memo"


#             '''######################################
#                 blue, yellow
#             ######################################'''
            , "booy" : ":m art / dessin / D-17 8# / des.XXX"

        }#do_Color_Sets_Memo = {

    memo_Unknown = "UNKNOWN"
    
    colName_Red = "red"
    colName_Yellow = "yellow"
    colName_Green = "green"
    colName_White = "white"
    colName_Black = "black"
    
    colName_Blue = "blue"   # symbol : "b"
    colName_Pink = "pink"   # symbol : "p"
    
#/ class ColorNameSet(Enum):
    
class Anims_Params(Enum):
    
    '''###################
        main        
    ###################'''
    PARAM__1_MOVE_LEAVES = "1"
    
    PARAM__2_MOVE_LEAVES__V2    = "2"
    PARAM__3_CLUSTERS           ="3"
    
#/ class Anims_Params(Enum):