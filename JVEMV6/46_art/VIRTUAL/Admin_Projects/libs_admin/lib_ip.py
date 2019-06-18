'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\lib_ip.py
    orig    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\libs.py
    at      : 2018/05/26 13:29:43
'''
# from sympy.matrices.densetools import row
'''###################
    import : built-in modules        
###################'''
import inspect, os, sys
# import inspect, os, sys, cv2

from enum import Enum
#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time

'''###################
    import : user-installed modules        
###################'''
# from sympy.physics.vector.printing import params
from scipy.stats import skew
from sympy.matrices.densetools import row

import cv2, numpy as np, matplotlib.pyplot as plt
# import numpy as np, matplotlib.pyplot as plt

from PIL import Image
from PIL.ExifTags import TAGS

'''###################
    import : orig modules        
###################'''
# sys.path.append('.')

#C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\libs.py
from libs_admin import libs, cons_ip
# from libs_admin import libs #=> working
# import libs

'''#########################################################
    enums        
#########################################################'''

'''#########################################################
    functions        
#########################################################'''
'''###################
    get_Std_Dev(lo_Data)
    
    at : 
    
    @return: dictionary of skew values        
    
        {'R' : 1.1002928031008152, 
            'G' : 4.955577672343114,
            'B' : 6.775475308994965 }
    
###################'''
def get_Std_Dev(lo_Data):
    
    '''###################
        get : mean value        
    ###################'''
    # values of each color composite
#     valsOf_R = [x * 0.001 for x in lo_Data]
#     valsOf_R = [x * np.power(10, -3) for x in lo_Data]
    valsOf_R = lo_Data
#     valsOf_R = do_Image_MetaData['valsOf_R']
    
#     #debug
#     print()
#     print("[%s:%d] valsOf_R[0:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(valsOf_R[0:10])
    
    # sum
    sumOf_ValsOf_R = sum(valsOf_R)

    # mean
    meanOf_R = sumOf_ValsOf_R / len(valsOf_R)
    
#     #debug
#     print()
#     print("[%s:%d] meanOf_R = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , meanOf_R
#         ), file=sys.stderr)
    
    # vals squared
    valsSquared_R = [np.power(x, 2) for x in valsOf_R]
    
#     #debug
#     print()
#     print("[%s:%d] valsSquared_R[0:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(valsSquared_R[0:10])


    # summation of vals squared
    summationOf_ValsSquared_R = sum(valsSquared_R)
#     summationOf_ValsSquared_R = sum[valsSquared_R]

#     #debug
#     print()
#     print("[%s:%d] summationOf_ValsSquared_R = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , summationOf_ValsSquared_R
#         ), file=sys.stderr)
    
    # length
    lenOf_R = len(valsOf_R)
    
    # standard dev
    variance_R = 1.0 * summationOf_ValsSquared_R / lenOf_R - np.power(meanOf_R, 2)
    
#     #debug
#     print()
#     print("[%s:%d] variance_R = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , variance_R
#         ), file=sys.stderr)
    
    # standard dev
    stdDev_R = np.sqrt(variance_R)

    '''###################
        return        
    ###################'''
    return stdDev_R
    
#/ def get_Std_Dev(lo__Data):
    
'''###################
    get_Moment(valsOf_ColorComposite, moment_Num)
    
    @return: Nnd moment        
                e.g. 4.955577672343114,
    
###################'''
def get_Moment(valsOf_ColorComposite, moment_Num):
    
    # length
    lenOf_Vals = len(valsOf_ColorComposite)
    
#     # stddev
#     stddev = get_Std_Dev(valsOf_ColorComposite)
    
    # average
    avg = sum(valsOf_ColorComposite) / lenOf_Vals
    
    lo_Power = [np.power(x - avg, moment_Num) for x in valsOf_ColorComposite]
    
    moment = sum(lo_Power) / lenOf_Vals
#     moment = sum(lo_Power) / lenOf_Vals / np.power(stddev, moment_Num)
    
    '''###################
        return        
    ###################'''
    return moment

#/ def get_Moment(valsOf_ColorComposite, 3):

'''###################
    get_Skew_Value(valsOf_ColorComposite)
    
    @return: skew value (float)        
                e.g. 4.955577672343114,
    
###################'''
# def get_Skew_Value(lo_Image_Data):
def get_Skew_Value(valsOf_ColorComposite):
    
    '''###################
        prep        
    ###################'''

    '''###################
        get : std dev
    ###################'''
    # values of each color composite
#     valsOf_R = valsOf_ColorComposite
    
    # std dev
    stdDev = get_Std_Dev(valsOf_ColorComposite)
#     stdDev_R = get_Std_Dev(valsOf_R)
    
#     #debug
#     print()
#     print("[%s:%d] stdDev_R = %.05f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , stdDev_R
#             ), file=sys.stderr)
    
    '''###################
        get : moment : 3
    ###################'''
    moment_Number = 3
    
    moment_3 = get_Moment(valsOf_ColorComposite, moment_Number)
    
    '''###################
        skew
    ###################'''
    skew = 1.0 * moment_3 / stdDev
    
    '''###################
        return        
    ###################'''
    return skew
#     return -999
    
#     pass
    
#/ def get_Skew_Value(list):

'''###################
    get_Skews(img_Data)
    
    @return: dictionary of skew values        
    
        {'R' : 1.1002928031008152, 
            'G' : 4.955577672343114,
            'B' : 6.775475308994965 }
    
###################'''
def get_Skews(img_Data):
    
    '''###################
        vars
    ###################'''
    do_Skews = {"skew_R" : -1, "skew_G" : -1, "skew_B" : -1}
    
    '''###################
        skew : prep
    ###################'''
    # meta data
    do_Image_MetaData = get_Image_MetaData_Basic(img_Data)
    
    # tuple of vals
    valsOf_R = do_Image_MetaData['valsOf_R']
    valsOf_G = do_Image_MetaData['valsOf_G']
    valsOf_B = do_Image_MetaData['valsOf_B']
    
#     to_Vals = (valsOf_R, valsOf_G, valsOf_B)
    
    '''###################
        skew
        
        ref : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\2_\2_1.py
    ###################'''
    # adjust values
    valOf_Adjust = 0.01
    
    valsOf_R__ = [x * valOf_Adjust for x in valsOf_R]
    valsOf_G__ = [x * valOf_Adjust for x in valsOf_G]
    valsOf_B__ = [x * valOf_Adjust for x in valsOf_B]
    
    do_Skews['skew_R'] = get_Skew_Value(valsOf_R__)
    do_Skews['skew_G'] = get_Skew_Value(valsOf_G__)
    do_Skews['skew_B'] = get_Skew_Value(valsOf_B__)
#     do_Skews['skew_R'] = get_Skew_Value(valsOf_R)
#     do_Skews['skew_G'] = get_Skew_Value(valsOf_G)
#     do_Skews['skew_B'] = get_Skew_Value(valsOf_B)
#     do_Skews['skew_R'] = skew(valsOf_R)
#     do_Skews['skew_G'] = skew(valsOf_G)
#     do_Skews['skew_B'] = skew(valsOf_B)
    
#     # sum
#     sumOf_ValsOf_R = sum(valsOf_R)
#     sumOf_ValsOf_G = sum(valsOf_G)
#     sumOf_ValsOf_B = sum(valsOf_B)
#     
# #     print()
# #     print("[%s:%d] sumOf_ValsOf_R = %d, sumOf_ValsOf_G = %d, sumOf_ValsOf_B = %d" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , sumOf_ValsOf_R, sumOf_ValsOf_G, sumOf_ValsOf_B
# #             ), file=sys.stderr)
# #     print("[%s:%d] sumOf_ValsOf_R => %d" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , sumOf_ValsOf_R
# #             ), file=sys.stderr)
# 
#     # means
#     meanOf_R = sumOf_ValsOf_R / len(valsOf_R)
#     meanOf_G = sumOf_ValsOf_G / len(valsOf_G)
#     meanOf_B = sumOf_ValsOf_B / len(valsOf_B)
#     
# #     #debug
# #     print()
# #     print("[%s:%d] meanOf_R = %.03f, meanOf_G = %.03f, meanOf_B = %.03f" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , meanOf_R, meanOf_G, meanOf_B
# #             ), file=sys.stderr)
#     
#     # summation
#     lo_PowerOf_R_3 = [np.power((x - meanOf_R), 3) for x in valsOf_R]
# #     lo_PowerOf_3_R = [x * 3 for x in valsOf_R]
# #     summationOf_R = [x * 3 for x in valsOf_R]
# #     summationOf_R = sum[np.power((x - meanOf_R), 3) for x in valsOf_R]
#     
#     summationOf_R_3 = sum[lo_PowerOf_R_3]
#     
#     # squares of Rs
#     
    
    '''###################
        return        
    ###################'''
    return do_Skews
#     return -1
    
#/ def get_Skew(img_Data):

'''###################
    get_Image_MetaData_Basic(img_Data)
    
    at : 2018/05/28 07:59:22
    
    @return:     
        do_MetaData['max_R'] = max_R
        do_MetaData['max_G'] = max_G
        do_MetaData['max_B'] = max_B
        
        do_MetaData['min_R'] = min_R
        do_MetaData['min_G'] = min_G
        do_MetaData['min_B'] = min_B
        
        do_MetaData['valsOf_R'] = valsOf_R
        do_MetaData['valsOf_G'] = valsOf_G
        do_MetaData['valsOf_B'] = valsOf_B        
###################'''
def get_Image_MetaData_Basic(img_Data):
    
    '''###################
        vars        
    ###################'''
    do_MetaData = {}
    
    max_R = -1; max_G = -1; max_B = -1
    min_R = 256; min_G = 256; min_B = 256
#     min_R = 255; min_G = 255; min_B = 255

    # counter
    cntOf_Row = 0
    cntOf_Cell = 0
    
    # values
    valsOf_R = [0] * 256
    valsOf_G = [0] * 256
    valsOf_B = [0] * 256

    for row in img_Data:
#     for row in item:
    
        for cell in row:
            
            # get value
            R = cell[0]; G = cell[1]; B = cell[2]
            
            # histogram
            valsOf_R[R] += 1
            valsOf_G[G] += 1
            valsOf_B[B] += 1
            
            # max value
            if R > max_R : max_R = R
            if G > max_G : max_G = G
            if B > max_B : max_B = B
            
            # min value
            if R < min_R : min_R = R
            if G < min_G : min_G = G
            if B < min_B : min_B = B
            
            # count
            cntOf_Cell += 1
        
        # reset count of cells
        cntOf_Cell = 0
        
        # count
        cntOf_Row += 1
        
    #/for row in item:
    
    # set : data
    
    do_MetaData['max_R'] = max_R
    do_MetaData['max_G'] = max_G
    do_MetaData['max_B'] = max_B
    
    do_MetaData['min_R'] = min_R
    do_MetaData['min_G'] = min_G
    do_MetaData['min_B'] = min_B
    
    do_MetaData['valsOf_R'] = valsOf_R
    do_MetaData['valsOf_G'] = valsOf_G
    do_MetaData['valsOf_B'] = valsOf_B
    
#     lo_Image_MetaData.append(
#         [
# #                 valsOf_R
# #                 , valsOf_G
# #                 , valsOf_B
#             
# #                 , max_R
#             max_R
#             , max_G
#             , max_B
#             
#             , min_R
#             , min_G
#             , min_B
#             
#             , valsOf_R
#             , valsOf_G
#             , valsOf_B
#             ]
#     )
        
    '''###################
        return        
    ###################'''
    return do_MetaData
    
#/ def get_Image_MetaData_Basic(img_Data):

'''###################
    get_IdxOf_Maxes(img_Data)
    
    @param img_Data: [
                        [ 
                            [103 101  93], [100  98  90],..., [ 72  80  10] 
                        ],
                        [ 
                            [103 101  93], [100  98  90],..., [ 72  80  10] 
                        ],
                        ...
                    ]
    
###################'''
def get_IdxOf_Maxes(img_Data):

    '''###################
        metadata        
    ###################'''
    # meta data
    do_Image_MetaData = get_Image_MetaData_Basic(img_Data)
    
    # tuple of vals
    valsOf_R = do_Image_MetaData['valsOf_R']
    valsOf_G = do_Image_MetaData['valsOf_G']
    valsOf_B = do_Image_MetaData['valsOf_B']

    
    '''###################
        vars        
    ###################'''
    # index
    idxOf_Max_R = -1
    idxOf_Max_G = -1
    idxOf_Max_B = -1

    # vals
    maxVal_R = -1
    maxVal_G = -1
    maxVal_B = -1
    
    # counter
    cntOf_R = 0
    cntOf_G = 0
    cntOf_B = 0
    
    '''###################
        iteration        
    ###################'''
    '''###################
        red
    ###################'''
    for val in valsOf_R:
        
        # judge
        if val > maxVal_R : 
            maxVal_R = val; idxOf_Max_R = cntOf_R
        
        # count
        cntOf_R += 1
        
    #/for val in valsOf_R:
    
    '''###################
        G
    ###################'''
    for val in valsOf_G:
        
        # judge
        if val > maxVal_G : 
            maxVal_G = val; idxOf_Max_G = cntOf_G
        
        # count
        cntOf_G += 1
        
    #/for val in valsOf_G:
    
    '''###################
        B
    ###################'''
    for val in valsOf_B:
        
        # judge
        if val > maxVal_B : 
            maxVal_B = val; idxOf_Max_B = cntOf_B
        
        # count
        cntOf_B += 1
        
    #/for val in valsOf_B:
    
#     print()
#     print("[%s:%d] idxOf_Max_R = %d, len(valsOf_R) = %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , idxOf_Max_R, len(valsOf_R)
#             ), file=sys.stderr)
#     
    
#     iteration
#     for xs in img_Data:
#         
#         for ys in xs:
#         
# #             #debug
# #             print()
# #             print("[%s:%d] vals =>" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     
# #                     ), file=sys.stderr)
# #             print(vals)
# 
#             # get : elem vals
#             R = ys[0]
#             G = ys[1]
#             B = ys[2]
#             
#             # update max val, idx of max
#             if R > maxVal_R : 
#                 maxVal_R = R
#                 idxOf_Max_R = cntOf_R
#                 
#             if G > maxVal_G : maxVal_G = G; idxOf_Max_G = cntOf_G
#             if B > maxVal_B : maxVal_B = B; idxOf_Max_B = cntOf_B
#             
#             # counter
#             cnt
# 
#         
#     #/for vals in img_Data:
    
    '''###################
        return        
    ###################'''
    return idxOf_Max_R, idxOf_Max_G, idxOf_Max_B, \
            maxVal_R, maxVal_G, maxVal_B

#/ def get_IdxOf_Maxes(img_Data):

'''###################
    is_CornerOf_Green__PhotoOf_Sweets
    
    @return: res, msg
        res    boolean
        msg    string ==> if res is 'False', gives info
    
###################'''
def is_CornerOf_Green__PhotoOf_Sweets(image_StatsData):
    
    '''###################
        vars        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
#     print()
#     print("[%s:%d] idxOf_Maxes =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(idxOf_Maxes)
    
    max_Vals = image_StatsData['max_Vals']

#     print()
#     print("[%s:%d] max_Vals =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(max_Vals)
    
    '''###################
        judge        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    # thresholds
    ts_Max_Val_R = 5500
    ts_Max_Val_G = 5500
    ts_Max_Val_B = 500

    # judge : index of max val
    # 'B' ===> color element of R (data is obtained in BGR format)
    if idxOf_Maxes_B > 20 : 
        
        msg = "False : idxOf_Max_B > 20 (%d)" % idxOf_Maxes_B
        
#        print()
#         print("[%s:%d] False : idxOf_Max_B > 20 (%d)" % \
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    if idxOf_Maxes_G < 30 or idxOf_Maxes_G > 80 : 

#         print()
#         print("[%s:%d] False : idxOf_Max_G < 30 or idxOf_Maxes_G > 80" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False
        
        msg = "False : idxOf_Max_G < 30 or idxOf_Maxes_G > 80 (%d)" % idxOf_Maxes_G
        
#        print()
#         print("[%s:%d] False : idxOf_Max_B > 20 (%d)" % \
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg

    if idxOf_Maxes_R < 30 or idxOf_Maxes_R > 80 : 
        
#         print()
#         print("[%s:%d] False : idxOf_Max_R < 30 or idxOf_Maxes_R > 80" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False

        msg = "False : idxOf_Max_R < 30 or idxOf_Maxes_R > 80 (%d)" % idxOf_Maxes_R
        
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg

    # judge : max vals
#     if max_Val_R < 5000 : 
#     if max_Val_R > 5000 : 
    if max_Val_R > ts_Max_Val_R : 
        
        
        
#         print()
# #         print("[%s:%d] False : max_Val_R < 5000" % \
#         print("[%s:%d] False : max_Val_R > 5000 (%d)" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , max_Val_R
#             ), file=sys.stderr)
#         
#         return False

        msg = "False : max_Val_R > 5000 (%d)" % max_Val_R
        
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg

#     if max_Val_G < 5000 : 
#     if max_Val_G > 5000 : 
    if max_Val_G > ts_Max_Val_G : 

#         print()
#         print("[%s:%d] False : max_Val_G > 5000" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False

        msg = "False : max_Val_G > 5000 (%d)" % max_Val_G
        
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg


    if max_Val_B < 5000 or max_Val_B > 7500 : 

#         print()
#         print("[%s:%d] False : max_Val_B < 5000 or max_Val_B > 7500" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
#         
#         return False
        
        '''###################
            judge : index of max val ==> 0?        
        ###################'''
        if max_Val_B > 7500 and not idxOf_Maxes_B == 0 : #if max_Val_B > 7500 and not idxOf_Maxes_B == 0
        
            msg = "False : max_Val_B < 5000 or max_Val_B > 7500 (%d, idxOf_Max = %d)" \
                    % (max_Val_B, idxOf_Maxes_B)
            
#            print()
#            print("[%s:%d] %s" % \
#                (os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg
#                ), file=sys.stderr)
            
            return False, msg
            
        #/if max_Val_B > 7500 and not idxOf_Maxes_B == 0
        
        
#         msg = "False : max_Val_B < 5000 or max_Val_B > 7500 (%d)" % max_Val_B
        msg = "False : max_Val_B < 5000 or max_Val_B > 7500 (%d, idxOf_Max = %d)" \
                % (max_Val_B, idxOf_Maxes_B)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
#         
#         return False, msg

    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_CornerOf_Green(image_StatsData):

'''###################
    is_ColorName_Green
     
    description :
        1. copy of is_CornerOf_Green__PhotoOf_Sweets
        2. using RGB values for judgement
     
    at : 2018/06/05 07:39:31
     
    @return: res, msg
        res    boolean
        msg    string ==> if res is 'False', gives info
     
###################'''
def is_ColorName_Green(image_StatsData):
    
    '''###################
        get vars : indices, max vals        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
    max_Vals = image_StatsData['max_Vals']
    
    '''###################
        get vars : each color element
        
        R
            ==> in the sheet graph and genreted data --> 'r'
            ==> in reality --> 'b'
        G
            ==> in the sheet graph and genreted data --> 'g'
            ==> in reality --> 'g'
        B
            ==> in the sheet graph and genreted data --> 'b'
            ==> in reality --> 'r'
        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    '''###################
        judge : order of idxOf_Maxes
    ###################'''
    condition_IdxOf_Maxes_1 = \
            (idxOf_Maxes_G > idxOf_Maxes_B \
             and idxOf_Maxes_B > idxOf_Maxes_R)
    
#     if not (idxOf_Maxes_G > idxOf_Maxes_R and idxOf_Maxes_R > idxOf_Maxes_B): 
    if not (condition_IdxOf_Maxes_1): 

#         msg = "False : order of idxOf_Maxes ==> incomplicit (idxOf_Maxes_G = %d, idxOf_Maxes_R = %d, idxOf_Maxes_B = %d)" \
        msg = "False : order of idxOf_Maxes ==> incomplicit (should be : G > R > B | idxOf_Maxes_R = %d, idxOf_Maxes_G = %d, idxOf_Maxes_B = %d)" \
                % (idxOf_Maxes_R, idxOf_Maxes_G, idxOf_Maxes_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        prep vars : thresholds
    ###################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
    ts_Max_Val_R__Lower = cons_ip.ColorThresholds.isGreen_Max_Val_R__Lower.value
    ts_Max_Val_R__Upper = cons_ip.ColorThresholds.isGreen_Max_Val_R__Upper.value
#     ts_Max_Val_R__Lower = 2.2 * 1000
#     ts_Max_Val_R__Upper = 3.9 * 1000
    
    # G
    ts_Max_Val_G__Lower = cons_ip.ColorThresholds.isGreen_Max_Val_G__Lower.value
    ts_Max_Val_G__Upper = cons_ip.ColorThresholds.isGreen_Max_Val_G__Upper.value

#     ts_Max_Val_G__Lower = 2.3 * 1000
#     ts_Max_Val_G__Upper = 3.9 * 1000
    
    # B
    ts_Max_Val_B__Lower = cons_ip.ColorThresholds.isGreen_Max_Val_B__Lower.value
    ts_Max_Val_B__Upper = cons_ip.ColorThresholds.isGreen_Max_Val_B__Upper.value
    
#     ts_Max_Val_B__Lower = 1.8 * 1000
#     ts_Max_Val_B__Upper = 2.5 * 1000
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
    ts_IdxOf_Max_R__Upper = cons_ip.ColorThresholds.isGreen_IdxOf_Max_R__Upper.value
    ts_IdxOf_Max_R__Lower = cons_ip.ColorThresholds.isGreen_IdxOf_Max_R__Lower.value
#     ts_IdxOf_Max_R__Upper = 50
#     ts_IdxOf_Max_R__Lower = 0
     
    # G
#     ts_IdxOf_Max_G__Upper = 60
#     ts_IdxOf_Max_G__Lower = 0
    ts_IdxOf_Max_G__Upper = cons_ip.ColorThresholds.isGreen_IdxOf_Max_G__Upper.value
    ts_IdxOf_Max_G__Lower = cons_ip.ColorThresholds.isGreen_IdxOf_Max_G__Lower.value
     
    # B
#     ts_IdxOf_Max_B__Upper = 200
#     ts_IdxOf_Max_B__Lower = 150
    ts_IdxOf_Max_B__Upper = cons_ip.ColorThresholds.isGreen_IdxOf_Max_B__Upper.value
    ts_IdxOf_Max_B__Lower = cons_ip.ColorThresholds.isGreen_IdxOf_Max_B__Lower.value
     
    '''###################
        judge : max value : blue
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_R > ts_Max_Val_R__Upper \
        or max_Val_R < ts_Max_Val_R__Lower : 
        
        msg = "False : max_Val_R ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_R__Upper, ts_Max_Val_R__Lower, max_Val_R)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : max value : green
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_G > ts_Max_Val_G__Upper \
        or max_Val_G < ts_Max_Val_G__Lower : 
        
        msg = "False : max_Val_G ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_G__Upper, ts_Max_Val_G__Lower, max_Val_G)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : max value : red
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_B > ts_Max_Val_B__Upper \
        or max_Val_B < ts_Max_Val_B__Lower : 
        
        msg = "False : max_Val_B ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_B__Upper, ts_Max_Val_B__Lower, max_Val_B)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg

    '''###################
        judge : index of max value : blue
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
    if not (idxOf_Maxes_R > ts_IdxOf_Max_R__Lower \
            and idxOf_Maxes_R < ts_IdxOf_Max_R__Upper) : 
        
        msg = "False : idxOf_Max_R ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_IdxOf_Max_R__Upper, ts_IdxOf_Max_R__Lower, idxOf_Maxes_R)        
#                 
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        judge : index of max value : green
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 

    if not (idxOf_Maxes_G > ts_IdxOf_Max_G__Lower \
            and idxOf_Maxes_G < ts_IdxOf_Max_G__Upper) : 
        
        msg = "False : idxOf_Maxe_G ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_IdxOf_Max_G__Upper, ts_IdxOf_Max_G__Lower, idxOf_Maxes_G)        
#                 
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        judge : index of max value : red
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
#     if not (idxOf_Maxes_R > ts_IdxOf_Max_R__Upper) : 

    if not (idxOf_Maxes_B > ts_IdxOf_Max_B__Lower \
            and idxOf_Maxes_B < ts_IdxOf_Max_B__Upper) : 
        
        msg = "False : idxOf_Max_B ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_IdxOf_Max_B__Upper, ts_IdxOf_Max_B__Lower, idxOf_Maxes_B)        
#                 
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_ColorName_Red(image_StatsData):

'''###################
    is_ColorName_Yellow
    
    description :
        
    
    at : 2018/06/08 09:42:37    
    @return: res, msg
        res    boolean
        msg    string ==> if res is 'False', gives info
    
###################'''
def is_ColorName_Yellow(image_StatsData):
    
    '''###################
        get vars : indices, max vals        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
#     print()
#     print("[%s:%d] idxOf_Maxes =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(idxOf_Maxes)
    
    max_Vals = image_StatsData['max_Vals']

#     print()
#     print("[%s:%d] max_Vals =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(max_Vals)
    
    '''###################
        get vars : each color element
        
        R
            ==> in the sheet graph and genreted data --> 'r'
            ==> in reality --> 'b'
        G
            ==> in the sheet graph and genreted data --> 'g'
            ==> in reality --> 'g'
        B
            ==> in the sheet graph and genreted data --> 'b'
            ==> in reality --> 'r'
        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    '''###################
        judge : order of idxOf_Maxes
    ###################'''
    condition_IdxOf_Maxes_1 = \
            (idxOf_Maxes_B > idxOf_Maxes_R \
             and idxOf_Maxes_G > idxOf_Maxes_R)
    
    condition_IdxOf_Maxes_2 = \
            (idxOf_Maxes_B >= idxOf_Maxes_G \
             or np.abs(idxOf_Maxes_B - idxOf_Maxes_G) < 20)
        
        
#     if not (idxOf_Maxes_R > idxOf_Maxes_G and idxOf_Maxes_G > idxOf_Maxes_B): 
    if not (condition_IdxOf_Maxes_1): 
        
        msg = "False : order of idxOf_Maxes ==> incomplicit (should be : R,G > B | idxOf_Maxes_R = %d, idxOf_Maxes_G = %d, idxOf_Maxes_B = %d)" \
                % (idxOf_Maxes_R, idxOf_Maxes_G, idxOf_Maxes_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    if not (condition_IdxOf_Maxes_2): 
        
        msg = "False : order of idxOf_Maxes ==> incomplicit (should be : R >= G or abs(R - G) < 20 | idxOf_Maxes_R = %d, idxOf_Maxes_G = %d, idxOf_Maxes_B = %d)" \
                % (idxOf_Maxes_R, idxOf_Maxes_G, idxOf_Maxes_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    

    '''###################
        prep vars : thresholds
    ###################'''
    # max values
    # R
#     ts_Max_Val_R__Lower = 4000
    ts_Max_Val_R__Lower = cons_ip.ColorThresholds.isYellow_Max_Val_R__Lower.value
    ts_Max_Val_R__Upper = cons_ip.ColorThresholds.isYellow_Max_Val_R__Upper.value
#     ts_Max_Val_R__Lower = 2500
#     ts_Max_Val_R__Upper = 5000
    
    # G
#     ts_Max_Val_G__Lower = 3000
#     ts_Max_Val_G__Lower = 2000
#     ts_Max_Val_G__Upper = 4000
    ts_Max_Val_G__Lower = cons_ip.ColorThresholds.isYellow_Max_Val_G__Lower.value
    ts_Max_Val_G__Upper = cons_ip.ColorThresholds.isYellow_Max_Val_G__Upper.value
    
    # B
#     ts_Max_Val_B__Lower = 3500
#     ts_Max_Val_B__Lower = 2000
#     ts_Max_Val_B__Upper = 4500
    ts_Max_Val_B__Lower = cons_ip.ColorThresholds.isYellow_Max_Val_B__Lower.value
    ts_Max_Val_B__Upper = cons_ip.ColorThresholds.isYellow_Max_Val_B__Upper.value
    
#     ts_Max_Val_G = 2000
#     ts_Max_Val_B = 2000
    
    # index of max values
    # R
    ts_IdxOf_Max_R__Upper = cons_ip.ColorThresholds.isYellow_IdxOf_Max_R__Upper.value
    ts_IdxOf_Max_R__Lower = cons_ip.ColorThresholds.isYellow_IdxOf_Max_R__Lower.value
#     ts_IdxOf_Max_R__Upper = -1      # -1 ==> not used
#     ts_IdxOf_Max_R__Lower = 80

    # G
#     ts_IdxOf_Max_G__Upper = 220
#     ts_IdxOf_Max_G__Lower = 165
    ts_IdxOf_Max_G__Upper = cons_ip.ColorThresholds.isYellow_IdxOf_Max_G__Upper.value
    ts_IdxOf_Max_G__Lower = cons_ip.ColorThresholds.isYellow_IdxOf_Max_G__Lower.value
     
    # B
#     ts_IdxOf_Max_B__Upper = 200
#     ts_IdxOf_Max_B__Upper = 180
#     ts_IdxOf_Max_B__Lower = -1      # -1 ==> not used
    ts_IdxOf_Max_B__Upper = cons_ip.ColorThresholds.isYellow_IdxOf_Max_B__Upper.value
    ts_IdxOf_Max_B__Lower = cons_ip.ColorThresholds.isYellow_IdxOf_Max_B__Lower.value
     
#     #debug
#     print() 
#     print("[%s:%d] ts_IdxOf_Max_B__Upper = %d, ts_IdxOf_Max_B__Lower = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , ts_IdxOf_Max_B__Upper, ts_IdxOf_Max_B__Lower
#         ), file=sys.stderr)
    
#     ts_IdxOf_Max_G = 110 
#     ts_IdxOf_Max_B = 120 

    '''###################
        judge : max value : blue
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_R > ts_Max_Val_R__Upper \
        or max_Val_R < ts_Max_Val_R__Lower : 
        
        msg = "False : max_Val_R ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_R__Upper, ts_Max_Val_R__Lower, max_Val_R)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : max value : green
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_G > ts_Max_Val_G__Upper \
        or max_Val_G < ts_Max_Val_G__Lower : 
        
        msg = "False : max_Val_G ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_G__Upper, ts_Max_Val_G__Lower, max_Val_G)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : max value : red
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_B > ts_Max_Val_B__Upper \
        or max_Val_B < ts_Max_Val_B__Lower : 
        
        msg = "False : max_Val_B ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_B__Upper, ts_Max_Val_B__Lower, max_Val_B)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg

    '''###################
        judge : index of max value : blue
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
    if not (idxOf_Maxes_R < ts_IdxOf_Max_R__Lower) : 
        
        
        msg = "False : idxOf_Max_R ==> out of range (idxOf_Maxes_R = %d, ts_IdxOf_Max_R__Lower = %d)" \
                % (idxOf_Maxes_R, ts_IdxOf_Max_R__Lower)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        judge : index of max value : green
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
    if not (idxOf_Maxes_G < ts_IdxOf_Max_G__Upper \
            and idxOf_Maxes_G > ts_IdxOf_Max_G__Lower) : 
        
        msg = "False : idxOf_Maxe_G ==> out of range (max = %d, min = %d, value = %d)" \
                % (ts_IdxOf_Max_G__Upper, ts_IdxOf_Max_G__Lower, idxOf_Maxes_G)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        judge : index of max value : red
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
#     if not (idxOf_Maxes_R > ts_IdxOf_Max_R__Upper) : 
    if not (idxOf_Maxes_B > ts_IdxOf_Max_B__Lower \
            and idxOf_Maxes_B < ts_IdxOf_Max_B__Upper) : 
#     if not (idxOf_Maxes_B > ts_IdxOf_Max_B__Upper) : 
        
        msg = "False : idxOf_Max_B ==> out of range (max = %d, min = %d, value = %d)" \
                % (ts_IdxOf_Max_B__Upper, ts_IdxOf_Max_B__Lower, idxOf_Maxes_B)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : span between indices of max valuea : B - G
    ###################'''
    # condition
    spanOf_IdxOf_Maxes_BG = 50
    
    condition_Span__BG = (idxOf_Maxes_B - idxOf_Maxes_G) < spanOf_IdxOf_Maxes_BG
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
#     if not (idxOf_Maxes_R > ts_IdxOf_Max_R__Upper) : 
    if not (condition_Span__BG) : 
#     if not (idxOf_Maxes_B > ts_IdxOf_Max_B__Upper) : 
        
        msg = "False : span between idxOf_Max B and G ==> out of range (idxOf_Maxes_B = %d, idxOf_Maxes_G = %d, spanOf_IdxOf_Maxes_BG = %d)" \
                % (idxOf_Maxes_B, idxOf_Maxes_G, spanOf_IdxOf_Maxes_BG)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_ColorName_Yellow(image_StatsData):

'''###################
    is_ColorName_White
    
    description :
        
    
    at : 2018/06/21 07:41:17    
    @return: res, msg
        res    boolean
        msg    string ==> if res is 'False', gives info
    
###################'''
def is_ColorName_White(image_StatsData):
    
    '''###################
        get vars : indices, max vals        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
#     print()
#     print("[%s:%d] idxOf_Maxes =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(idxOf_Maxes)
    
    max_Vals = image_StatsData['max_Vals']

#     print()
#     print("[%s:%d] max_Vals =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(max_Vals)
    
    '''###################
        get vars : each color element
        
        R
            ==> in the sheet graph and genreted data --> 'r'
            ==> in reality --> 'b'
        G
            ==> in the sheet graph and genreted data --> 'g'
            ==> in reality --> 'g'
        B
            ==> in the sheet graph and genreted data --> 'b'
            ==> in reality --> 'r'
        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    '''###################
        judge : order of idxOf_Maxes
    ###################'''
    condition_IdxOf_Maxes_1 = \
            (idxOf_Maxes_B > cons_ip.ColorThresholds.isWhite_IdxOf_Max.value \
             and idxOf_Maxes_R > cons_ip.ColorThresholds.isWhite_IdxOf_Max.value \
             and idxOf_Maxes_G > cons_ip.ColorThresholds.isWhite_IdxOf_Max.value)
#             (idxOf_Maxes_B == cons_ip.ColorThresholds.isWhite_IdxOf_Max.value \
#              and idxOf_Maxes_R == cons_ip.ColorThresholds.isWhite_IdxOf_Max.value \
#              and idxOf_Maxes_G == cons_ip.ColorThresholds.isWhite_IdxOf_Max.value)
    
    condition_Max_Val_1 = \
            (max_Val_B > cons_ip.ColorThresholds.isWhite_Max_Val__Lower.value \
             and max_Val_G > cons_ip.ColorThresholds.isWhite_Max_Val__Lower.value \
             and max_Val_R > cons_ip.ColorThresholds.isWhite_Max_Val__Lower.value
             )
        
        
#     if not (idxOf_Maxes_R > idxOf_Maxes_G and idxOf_Maxes_G > idxOf_Maxes_B): 
    if not (condition_IdxOf_Maxes_1): 
        
        msg = "False : order of idxOf_Maxes ==> incomplicit (should be : R,G,B == %d | idxOf_Maxes_R = %d, idxOf_Maxes_G = %d, idxOf_Maxes_B = %d)" \
                % (cons_ip.ColorThresholds.isWhite_IdxOf_Max.value \
                   , idxOf_Maxes_R, idxOf_Maxes_G, idxOf_Maxes_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    if not (condition_Max_Val_1): 
        
        msg = "False : max vals ==> incomplicit (should be : R,G,B > %d | max_Val_R = %d, max_Val_G = %d, max_Val_B = %d)" \
                % (cons_ip.ColorThresholds.isWhite_Max_Val__Lower.value \
                   , max_Val_R, max_Val_G, max_Val_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_ColorName_Yellow(image_StatsData):

'''###################
    is_ColorName_Black(image_StatsData)
    
    description :
        
    
    at : 2018/06/21 17:04:48
    
    @return: res, msg
        res    boolean
        msg    string ==> if res is 'False', gives info
    
###################'''
def is_ColorName_Black(image_StatsData):
    
    '''###################
        get vars : indices, max vals        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
#     print()
#     print("[%s:%d] idxOf_Maxes =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(idxOf_Maxes)
    
    max_Vals = image_StatsData['max_Vals']

#     print()
#     print("[%s:%d] max_Vals =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(max_Vals)
    
    '''###################
        get vars : each color element
        
        R
            ==> in the sheet graph and genreted data --> 'r'
            ==> in reality --> 'b'
        G
            ==> in the sheet graph and genreted data --> 'g'
            ==> in reality --> 'g'
        B
            ==> in the sheet graph and genreted data --> 'b'
            ==> in reality --> 'r'
        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    '''###################
        judge : order of idxOf_Maxes
    ###################'''
    condition_IdxOf_Maxes_1 = \
            (idxOf_Maxes_B == cons_ip.ColorThresholds.isBlack_IdxOf_Max.value \
             and idxOf_Maxes_R == cons_ip.ColorThresholds.isBlack_IdxOf_Max.value \
             and idxOf_Maxes_G == cons_ip.ColorThresholds.isBlack_IdxOf_Max.value)
    
    condition_Max_Val_1 = \
            (max_Val_B > cons_ip.ColorThresholds.isBlack_Max_Val__Lower.value \
             and max_Val_G > cons_ip.ColorThresholds.isBlack_Max_Val__Lower.value \
             and max_Val_R > cons_ip.ColorThresholds.isBlack_Max_Val__Lower.value
             )
        
        
#     if not (idxOf_Maxes_R > idxOf_Maxes_G and idxOf_Maxes_G > idxOf_Maxes_B): 
    if not (condition_IdxOf_Maxes_1): 
        
        msg = "False : order of idxOf_Maxes ==> incomplicit (should be : R,G,B == %d | idxOf_Maxes_R = %d, idxOf_Maxes_G = %d, idxOf_Maxes_B = %d)" \
                % (cons_ip.ColorThresholds.isWhite_IdxOf_Max.value \
                   , idxOf_Maxes_R, idxOf_Maxes_G, idxOf_Maxes_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    if not (condition_Max_Val_1): 
        
        msg = "False : max vals ==> incomplicit (should be : R,G,B > %d | max_Val_R = %d, max_Val_G = %d, max_Val_B = %d)" \
                % (cons_ip.ColorThresholds.isWhite_Max_Val__Lower.value \
                   , max_Val_R, max_Val_G, max_Val_B)
         
#        print()
#        print("[%s:%d] %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , msg
#            ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_ColorName_Yellow(image_StatsData):

'''###################
    is_ColorName_Red
    
    description :
        
    
    at : 2018/06/10 12:24:45    
    @return: res, msg
        res    boolean
        msg    string ==> if res is 'False', gives info
    
###################'''
def is_ColorName_Red(image_StatsData):
    
    '''###################
        get vars : indices, max vals        
    ###################'''
    idxOf_Maxes = image_StatsData['idxOf_Maxes']
    
#     print()
#     print("[%s:%d] idxOf_Maxes =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(idxOf_Maxes)
    
    max_Vals = image_StatsData['max_Vals']

#     print()
#     print("[%s:%d] max_Vals =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(max_Vals)
    
    '''###################
        get vars : each color element
        
        R
            ==> in the sheet graph and genreted data --> 'r'
            ==> in reality --> 'b'
        G
            ==> in the sheet graph and genreted data --> 'g'
            ==> in reality --> 'g'
        B
            ==> in the sheet graph and genreted data --> 'b'
            ==> in reality --> 'r'
        
    ###################'''
    # prep vars
    idxOf_Maxes_R = idxOf_Maxes[0]
    idxOf_Maxes_G = idxOf_Maxes[1]
    idxOf_Maxes_B = idxOf_Maxes[2]

    max_Val_R = max_Vals[0]
    max_Val_G = max_Vals[1]
    max_Val_B = max_Vals[2]

    '''###################
        prep vars : thresholds
    ###################'''
    '''###################
        thresholds : max values
    ###################'''
    # R
    ts_Max_Val_R__Lower = cons_ip.ColorThresholds.isRed_Max_Val_R__Lower.value
    ts_Max_Val_R__Upper = cons_ip.ColorThresholds.isRed_Max_Val_R__Upper.value
#     ts_Max_Val_R__Lower = 2.2 * 1000
#     ts_Max_Val_R__Upper = 3.9 * 1000
    
    # G
    ts_Max_Val_G__Lower = cons_ip.ColorThresholds.isRed_Max_Val_G__Lower.value
    ts_Max_Val_G__Upper = cons_ip.ColorThresholds.isRed_Max_Val_G__Upper.value

#     ts_Max_Val_G__Lower = 2.3 * 1000
#     ts_Max_Val_G__Upper = 3.9 * 1000
    
    # B
    ts_Max_Val_B__Lower = cons_ip.ColorThresholds.isRed_Max_Val_B__Lower.value
    ts_Max_Val_B__Upper = cons_ip.ColorThresholds.isRed_Max_Val_B__Upper.value
    
#     ts_Max_Val_B__Lower = 1.8 * 1000
#     ts_Max_Val_B__Upper = 2.5 * 1000
    
    '''###################
        thresholds : index of max values
    ###################'''    
    # R
    ts_IdxOf_Max_R__Upper = cons_ip.ColorThresholds.isRed_IdxOf_Max_R__Upper.value
    ts_IdxOf_Max_R__Lower = cons_ip.ColorThresholds.isRed_IdxOf_Max_R__Lower.value
#     ts_IdxOf_Max_R__Upper = 50
#     ts_IdxOf_Max_R__Lower = 0
     
    # G
#     ts_IdxOf_Max_G__Upper = 60
#     ts_IdxOf_Max_G__Lower = 0
    ts_IdxOf_Max_G__Upper = cons_ip.ColorThresholds.isRed_IdxOf_Max_G__Upper.value
    ts_IdxOf_Max_G__Lower = cons_ip.ColorThresholds.isRed_IdxOf_Max_G__Lower.value
     
    # B
#     ts_IdxOf_Max_B__Upper = 200
#     ts_IdxOf_Max_B__Lower = 150
    ts_IdxOf_Max_B__Upper = cons_ip.ColorThresholds.isRed_IdxOf_Max_B__Upper.value
    ts_IdxOf_Max_B__Lower = cons_ip.ColorThresholds.isRed_IdxOf_Max_B__Lower.value
     
    '''###################
        judge : max value : blue
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_R > ts_Max_Val_R__Upper \
        or max_Val_R < ts_Max_Val_R__Lower : 
        
        msg = "False : max_Val_R ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_R__Upper, ts_Max_Val_R__Lower, max_Val_R)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : max value : green
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_G > ts_Max_Val_G__Upper \
        or max_Val_G < ts_Max_Val_G__Lower : 
        
        msg = "False : max_Val_G ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_G__Upper, ts_Max_Val_G__Lower, max_Val_G)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    '''###################
        judge : max value : red
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
    if max_Val_B > ts_Max_Val_B__Upper \
        or max_Val_B < ts_Max_Val_B__Lower : 
        
        msg = "False : max_Val_B ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_Max_Val_B__Upper, ts_Max_Val_B__Lower, max_Val_B)
#         
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg

    '''###################
        judge : index of max value : blue
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
    if not (idxOf_Maxes_R > ts_IdxOf_Max_R__Lower \
            and idxOf_Maxes_R < ts_IdxOf_Max_R__Upper) : 
        
        msg = "False : idxOf_Max_R ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_IdxOf_Max_R__Upper, ts_IdxOf_Max_R__Lower, idxOf_Maxes_R)        
#                 
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        judge : index of max value : green
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 

    if not (idxOf_Maxes_G > ts_IdxOf_Max_G__Lower \
            and idxOf_Maxes_G < ts_IdxOf_Max_G__Upper) : 
        
        msg = "False : idxOf_Maxe_G ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_IdxOf_Max_G__Upper, ts_IdxOf_Max_G__Lower, idxOf_Maxes_G)        
#                 
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        judge : index of max value : red
    ###################'''
    # judge : index of max val
    # 'R' ===> color element of R (data is obtained in BGR format)
#     if idxOf_Maxes_R > ts_IdxOf_Max_R__Lower : 
#     if not (idxOf_Maxes_R > ts_IdxOf_Max_R__Upper) : 

    if not (idxOf_Maxes_B > ts_IdxOf_Max_B__Lower \
            and idxOf_Maxes_B < ts_IdxOf_Max_B__Upper) : 
        
        msg = "False : idxOf_Max_B ==> out of range (max = %d, min = %d, actual = %d)" \
                % (ts_IdxOf_Max_B__Upper, ts_IdxOf_Max_B__Lower, idxOf_Maxes_B)        
#                 
#         print()
#         print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg
#             ), file=sys.stderr)
        
        return False, msg
    
    
    '''###################
        return        
    ###################'''
    return True, "True"

#/ def is_ColorName_Red(image_StatsData):

'''###################
    get_Corner_Images(img_Src, corner_Length)        
    
    @return: [left bottom, right bottom, left up, right up]

    |------------------------|
    |(2)                  (3)|
    |                        |
    |                        |
    |                        |
    |(0)                  (1)|
    |------------------------|
    
###################'''
# def get_Corner_Images(img_Src, corner_Length) :
def get_Corner_Images(img_Src, corner_Length, padding = 0) :
    
    height, width, channels = img_Src.shape
    
    clips = [
    
        img_Src[(height - corner_Length) : height - padding, \
                    0 + padding : corner_Length], # clp_LB
        
        img_Src[(height - corner_Length) : height - padding, \
                    width - corner_Length : width - padding], # clp_RB
        
        img_Src[0 + padding : corner_Length, \
                0 + padding : corner_Length], # clp_LU
        
        img_Src[0 + padding : corner_Length, \
                width - corner_Length : width - padding], # clp_RU
#         img_Src[(height - corner_Length) : height, 0 : corner_Length], # clp_LB
#         img_Src[(height - corner_Length) : height, width - corner_Length : width], # clp_RB
#         img_Src[0 : corner_Length, 0 : corner_Length], # clp_LU
#         img_Src[0 : corner_Length, width - corner_Length : width], # clp_RU
    ]
    
    # return
    return clips
    
#/ def get_Corner_Images(img_RGB, corner_Length) :

# def _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images, lo_Image_MetaData):

# def is_PhotoOf__Sweets(dpath_Images, fname_Image) :

'''###################
    is_PhotoOf__Sweets        
###################'''
def is_PhotoOf__Sweets \
(dpath_Images, fname_Image, flg_SaveImage = False, \
    corner_Width = 280, param_Corner_Padding = 0) :
    
    '''###################
                
    ###################'''
    '''###################
        get : cv instance        
    ###################'''
    fpath_Image = "%s\\%s" % (dpath_Images, fname_Image)
    
    # validate
    res = os.path.isfile(fpath_Image)
    
    if res == False : #if res == True

        print("[%s:%d] file NOT exist! => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image
        ), file=sys.stderr)
        
        # set dic
        msg = "file NOT exist : %s" % fpath_Image
        
        # return
        return False, msg
    
        # cv instance
    img_Orig = cv2.imread(fpath_Image)
    
    print()
    print("[%s:%d] cv2 image ==> loaded" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    # convert to RGB
    img_RGB = img_Orig
    
#     #TEST
#     get_ColorName_From_CornerImage(img_RGB, dpath_Images, fname_Image)
#     return

    '''###################
        get : meta data
    ###################'''
    # data
    height, width, channels = img_RGB.shape
    
#     print()
#     print("[%s:%d] height = %d, width = %d, channels = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , height, width, channels
#         ), file=sys.stderr)

    '''###################
        get : 4 corners        
    ###################'''
    corner_Length = corner_Width
#     corner_Length = 280
    
    padding = param_Corner_Padding
#     padding = 0
    
    img_Corners = get_Corner_Images(img_RGB, corner_Length, padding)
    
    '''###################
        save : images of 4 corners        
    ###################'''
    save_Image = flg_SaveImage
#     save_Image = True
#     save_Image = False
    
    lo_Names_Of_Corner_Images = \
            get_4_corners__SaveImage_4Corners(img_Corners, fname_Image, save_Image)

    '''###################
        get : basic data
    ###################'''
    lo_Image_MetaData = get_4_corners__Get_MetaData(img_Corners)

    '''###################
        get : stat data
    ###################'''
    lo_Image_StatsData = get_4_corners__Get_StatsData(img_Corners)

    '''###################
        filtering : a corner of green ?
    ###################'''
    res, comment = is_CornerOf_Green__PhotoOf_Sweets(lo_Image_StatsData[0])

    '''###################
        get : color name of the corner
    ###################'''
    lo_Color_Names = []
    
    lenOf_Lo_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
    for i in range(lenOf_Lo_Names_Of_Corner_Images) :
    
        nameOf_CornerImage = lo_Names_Of_Corner_Images[i]
        
        #debug
        print()
        
        msg = "[%s / %s:%d] inspecting ===> %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile())
                , libs.linenum()
                , nameOf_CornerImage
                )
        
        print(msg, file=sys.stderr)
        
        #debug
#        libs.write_Log(msg, True)
        
        stats_Data = lo_Image_StatsData[i]
        
        color_Name = get_Color_Name_From_StatsData(stats_Data)
        
        # append
        lo_Color_Names.append([nameOf_CornerImage, color_Name])
        
    #/for i in lenOf_Lo_Names_Of_Corner_Images:
    
    msg = "[%s / %s:%d] lo_Color_Names =>" % \
        (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
        
        )
    
    #debug
    libs.write_Log(msg, True)
    
    for item in lo_Color_Names:

#         print(item)

        #debug
        msg = "%s => %s" % (item[0], item[1])
        
        libs.write_Log(msg, True)
        
    #/for item in lo_Color_Names:

    '''###################
        write log : file names
    ###################'''
#     _exec_get_4_corners__Write_Log(
    get_4_corners__Write_Log(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    , comment
                    )

    '''###################
        get color names : HSV
    ###################'''
    lo_Color_Names_2 = []
    
    for i in range(lenOf_Lo_Names_Of_Corner_Images) :
        
        # name of the image
        nameOf_CornerImage = lo_Names_Of_Corner_Images[i]
        
        # corner image
        img = img_Corners[i]
        
        # inspect
        msg = get_ColorName_From_CornerImage(img, dpath_Images, fname_Image, i)
        
        # append
        lo_Color_Names_2.append([nameOf_CornerImage, msg])
#         lo_Color_Names_2.append([nameOf_CornerImage, color_Name])
    
    '''###################
        report
    ###################'''
    msg = "lo_Color_Names_2 =>"
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)

    for item in lo_Color_Names_2:

        msg = "file = %s / color name = %s" % (item[0], item[1])
                        
        msg_Log = "%s" % \
                (
                    msg)
        
        libs.write_Log(msg_Log, True)
        
    #/for item in lo_Color_Names_2:


    '''###################
        return        
    ###################'''
    return res, comment, (height, width, channels)
#     return res, comment
#     return False, msg
    
#/ def is_PhotoOf__Sweets(dir_path, file_name) :

'''###################
    get_ColorName_Set_From_Image
    
    @return: color name
            e.g. "others", "yellow"
    
###################'''
def get_ColorName_Set_From_Image(\
    dpath_Images, fpath, flg_SaveImage, \
#     dpath_Images, fname, flg_SaveImage, \
    param_Corner_Width, param_Corner_Padding) :
    
#     '''###################
#         vars        
#     ###################'''
#     lo_Color_Names = []
    
    '''###################
        get : cv instance        
    ###################'''
    fpath_Image = fpath
#     fpath_Image = "%s\\%s" % (dpath_Images, fname)
    
    #debug
    print()
    print("[%s:%d] os.path.basename(fpath) => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , os.path.basename(fpath)
            ), file=sys.stderr)
    
    # validate
    res = os.path.isfile(fpath_Image)
    
    if res == False : #if res == True

        print("[%s:%d] file NOT exist! => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image
        ), file=sys.stderr)
        
        # set dic
        msg = "file NOT exist : %s" % fpath_Image
        
        # return
        return False, msg
    
        # cv instance
    img_Orig = cv2.imread(fpath_Image)

#     '''###################
#         validate : image obtained
#     ###################'''
#     #ref https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python#541394
#     filename, file_extension = os.path.splitext('/path/to/somefile.ext')
#     
#     if file_extension == ".mov" \
#         or file_extension == ".MOV" : #if file_extension == 
#         
#         msg = "NOT an image file : '%s'\nreturning default 'others'" %\
#                                 (fpath_Image)
#                          
#         msg_Log = "[%s / %s:%d] %s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg)
#          
#         libs.write_Log(msg_Log, True)
#          
#         print()
#         print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg_Log
#         ), file=sys.stderr)
#          
#         # return default
#         return "others"
#     #/if file_extension == 


    
#    #ref https://stackoverflow.com/questions/17198466/none-python-error-bug#17198511
#     if isinstance(img_Orig, type(None)) : #if img_Orig == None
#         
#         msg = "file NOT obtained (NoneType) : '%s'\nreturning default 'others'" %\
#                                 (fpath_Image)
#                         
#         msg_Log = "[%s / %s:%d] %s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg)
#         
#         libs.write_Log(msg_Log, True)
#         
#         print()
#         print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg_Log
#         ), file=sys.stderr)
#         
#         # return default
#         return "others"
#         
#     if not img_Orig.all() : #if img_Orig == None
# #     if (img_Orig == None) : #if img_Orig == None
# #     if img_Orig == None : #if img_Orig == None
#     
#         msg = "file NOT obtained (all() returns False) : '%s'\nreturning default 'others'" %\
#                                 (fpath_Image)
#                         
#         msg_Log = "[%s / %s:%d] %s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg)
#         
#         libs.write_Log(msg_Log, True)
#         
#         print()
#         print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg_Log
#         ), file=sys.stderr)
#         
#         # return default
#         return "others"
#         
#     #/if img_Orig == None
    
    print()
    print("[%s:%d] cv2 image ==> loaded" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        set : RGB
    ###################'''
    # convert to RGB
    img_RGB = img_Orig

    '''###################
        get : meta data
    ###################'''
    # data
    height, width, channels = img_RGB.shape
    
#     print()
#     print("[%s:%d] height = %d, width = %d, channels = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , height, width, channels
#         ), file=sys.stderr)

    '''###################
        get : 4 corners        
    ###################'''
    corner_Length = param_Corner_Width
#     corner_Length = corner_Width
#     corner_Length = 280
    
    padding = param_Corner_Padding
#     padding = 0
    
    img_Corners = get_Corner_Images(img_RGB, corner_Length, padding)
    
#     print()
#     print("[%s:%d] len(img_Corners) = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(img_Corners)
#         ), file=sys.stderr)

    '''###################
        save : images of 4 corners        
    ###################'''
    save_Image = flg_SaveImage
#     save_Image = True
#     save_Image = False

    fname_Image = os.path.basename(fpath)
    
    lo_Names_Of_Corner_Images = \
            get_4_corners__SaveImage_4Corners(img_Corners, fname_Image, save_Image)
#             saveImage_4Corners(img_Corners, fname_Image, save_Image)
#             _exec_get_4_corners__SaveImage_4Corners(img_Corners, fname_Image)

#     print()
#     print("[%s:%d] lo_Names_Of_Corner_Images =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     print(lo_Names_Of_Corner_Images)

    '''###################
        get : basic data
    ###################'''
    lo_Image_MetaData = get_4_corners__Get_MetaData(img_Corners)
#     lo_Image_MetaData = _exec_get_4_corners__Get_MetaData(img_Corners)

    '''###################
        get : stat data
    ###################'''
    lo_Image_StatsData = get_4_corners__Get_StatsData(img_Corners)
#     lo_Image_StatsData = _exec_get_4_corners__Get_StatsData(img_Corners)

    '''###################
        get : color name of the corner
    ###################'''
    lo_Color_Names = []
    lo_Color_Names_2 = []
    
    lenOf_Lo_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
#     for i in lenOf_Lo_Names_Of_Corner_Images:
    for i in range(lenOf_Lo_Names_Of_Corner_Images) :
    
        nameOf_CornerImage = lo_Names_Of_Corner_Images[i]
        
        #debug
#         print()
        
#         msg = "[%s:%d] inspecting ===> %s" % \
        msg = "[%s / %s:%d] inspecting ===> %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile())
                , libs.linenum()
                , nameOf_CornerImage
                )
        
#         print(msg, file=sys.stderr)
#         print("[%s:%d] inspecting ===> %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , nameOf_CornerImage
#                 ), file=sys.stderr)
        
        #debug
        libs.write_Log(msg, True)
        
        stats_Data = lo_Image_StatsData[i]
        
        color_Name = get_Color_Name_From_StatsData(stats_Data)
        
        # append
        lo_Color_Names.append([nameOf_CornerImage, color_Name])
        
        '''###################
            lo_Color_Names_2        
        ###################'''
        img_Corner = img_Corners[i]
        
        dpath_Images = dpath_Images
        fname_Image = nameOf_CornerImage
        
        ind = i

        color_Name_2 = get_ColorName_From_CornerImage(
                    img_Corner, dpath_Images, fname_Image, ind)

        # append
        lo_Color_Names_2.append([nameOf_CornerImage, color_Name_2])
        
    #/for i in lenOf_Lo_Names_Of_Corner_Images:
    
#     #debug
#     print()
#     print("[%s:%d] lo_Color_Names_2 =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     for item in lo_Color_Names_2:
#     
#         print(item)
#         
    #/for item in lo_Color_Names_2:
    
    #debug
    libs.write_Log(msg, True)
    
    for item in lo_Color_Names:

#         print(item)

        #debug
        msg = "%s => %s" % (item[0], item[1])
        
        libs.write_Log(msg, True)
        
    #/for item in lo_Color_Names:

#     print(lo_Color_Names)

    '''###################
        write log : file names
    ###################'''
#     _exec_get_4_corners__Write_Log(
#     get_4_corners__Write_Log(
    get_4_corners__Write_Log__V2(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    )
    
    '''###################
        return        
    ###################'''
    return lo_Color_Names_2
#     return lo_Color_Names
    
#/ get_ColorName_Set_From_Image(dpath_Images, file_Name)

'''###################
    func : get_NamesOf_CornerColors
    
    at    : 2018/06/12 13:07:10
    
    color names : (3 colors)
        yellow red green
    
    @return: list of color names
    
            [
                ['img...1.png', 'other']
                ,['img...1.png', 'yellow']
                ,['img...1.png', 'yellow']
                ,['img...1.png', 'other']
            ]
    
###################'''
def get_NamesOf_CornerColors \
(dpath_Images, fname_Image, flg_SaveImage = False, \
    corner_Width = 280, param_Corner_Padding = 0) :
    
    '''###################
                
    ###################'''
    '''###################
        get : cv instance        
    ###################'''
    fpath_Image = "%s\\%s" % (dpath_Images, fname_Image)
    
    # validate
    res = os.path.isfile(fpath_Image)
    
    if res == False : #if res == True

        print("[%s:%d] file NOT exist! => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image
        ), file=sys.stderr)
        
        # set dic
        msg = "file NOT exist : %s" % fpath_Image
        
        # return
        return False, msg
    
        # cv instance
    img_Orig = cv2.imread(fpath_Image)
    
    print()
    print("[%s:%d] cv2 image ==> loaded" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    # convert to RGB
    img_RGB = img_Orig


    '''###################
        get : meta data
    ###################'''
    # data
    height, width, channels = img_RGB.shape
    
    print()
    print("[%s:%d] height = %d, width = %d, channels = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , height, width, channels
        ), file=sys.stderr)

    '''###################
        get : 4 corners        
    ###################'''
    corner_Length = corner_Width
#     corner_Length = 280
    
    padding = param_Corner_Padding
#     padding = 0
    
    img_Corners = get_Corner_Images(img_RGB, corner_Length, padding)
    
    print()
    print("[%s:%d] len(img_Corners) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(img_Corners)
        ), file=sys.stderr)

    '''###################
        save : images of 4 corners        
    ###################'''
    save_Image = flg_SaveImage
#     save_Image = True
#     save_Image = False
    
    lo_Names_Of_Corner_Images = \
            get_4_corners__SaveImage_4Corners(img_Corners, fname_Image, save_Image)
#             saveImage_4Corners(img_Corners, fname_Image, save_Image)
#             _exec_get_4_corners__SaveImage_4Corners(img_Corners, fname_Image)
    
    print()
    print("[%s:%d] lo_Names_Of_Corner_Images =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_Names_Of_Corner_Images)

    '''###################
        get : basic data
    ###################'''
    lo_Image_MetaData = get_4_corners__Get_MetaData(img_Corners)
#     lo_Image_MetaData = _exec_get_4_corners__Get_MetaData(img_Corners)

    '''###################
        get : stat data
    ###################'''
    lo_Image_StatsData = get_4_corners__Get_StatsData(img_Corners)
#     lo_Image_StatsData = _exec_get_4_corners__Get_StatsData(img_Corners)


    '''###################
        filtering : a corner of green ?
    ###################'''
    # lo_Image_StatsData[0] => left bottom corner
#         res = lib_ip.is_CornerOf_Green(lo_Image_StatsData[0])
#     res, comment = lib_ip.is_CornerOf_Green__PhotoOf_Sweets(lo_Image_StatsData[0])
    res, comment = is_CornerOf_Green__PhotoOf_Sweets(lo_Image_StatsData[0])

    '''###################
        get : color name of the corner
    ###################'''
    lo_Color_Names = []
    
    lenOf_Lo_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
#     for i in lenOf_Lo_Names_Of_Corner_Images:
    for i in range(lenOf_Lo_Names_Of_Corner_Images) :
    
        nameOf_CornerImage = lo_Names_Of_Corner_Images[i]
        
        #debug
        print()
        
#         msg = "[%s:%d] inspecting ===> %s" % \
        msg = "[%s / %s:%d] inspecting ===> %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile())
                , libs.linenum()
                , nameOf_CornerImage
                )
        
        print(msg, file=sys.stderr)
#         print("[%s:%d] inspecting ===> %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , nameOf_CornerImage
#                 ), file=sys.stderr)
        
        #debug
        libs.write_Log(msg, True)
        
        stats_Data = lo_Image_StatsData[i]
        
        color_Name = get_Color_Name_From_StatsData(stats_Data)
        
        # append
        lo_Color_Names.append([nameOf_CornerImage, color_Name])
        
    #/for i in lenOf_Lo_Names_Of_Corner_Images:
    
    print()
    
#     msg = "[%s:%d] lo_Color_Names =>" % \
    msg = "[%s / %s:%d] lo_Color_Names =>" % \
        (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
        
        )
    
    print(msg, file=sys.stderr)
#     print("[%s:%d] lo_Color_Names =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
    
    #debug
    libs.write_Log(msg, True)
    
    for item in lo_Color_Names:

#         print(item)

        #debug
        msg = "%s => %s" % (item[0], item[1])
        
        libs.write_Log(msg, True)
        
    #/for item in lo_Color_Names:

#     print(lo_Color_Names)

    '''###################
        write log : file names
    ###################'''
#     _exec_get_4_corners__Write_Log(
    get_4_corners__Write_Log(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    , comment
                    )

    '''###################
        return        
    ###################'''
#     msg = "done"
    
    return res, comment, (height, width, channels)
#     return res, comment
#     return False, msg
    
#/ def is_PhotoOf__Sweets(dir_path, file_name) :

'''###################
    get_Color_Name_From_StatsData(stats_Data)
    
    @return: nameOf_Color :: string
            ==> name of color
                "green"
                "yellow"
                "red"
###################'''
def get_Color_Name_From_StatsData(stats_Data) :
    
    '''###################
        vars        
    ###################'''
    nameOf_Color = "other"
    
    '''###################
        judge : green
    ###################'''
    #debug
#     print()

    msg = "[%s / %s:%d] inspecting : green ------------" % \
            (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
            
            )
            
#     print(msg, file=sys.stderr)
    
#    libs.write_Log(msg, True)
    
#     print("[%s:%d] inspecting : green ------------" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
    
    res, msg = is_ColorName_Green(stats_Data)
    
    # green ?
    if res == True : #if res == True
    
        nameOf_Color = "green"
        
        return nameOf_Color
    
    else :
        
        #debug
        msg = "[%s / %s:%d] %s" % \
                (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile())
                    , libs.linenum()
                    , msg
                )
            
#        libs.write_Log(msg, True)
    
    '''###################
        judge : yellow
    ###################'''
    #debug
#     print()
    
    msg = "[%s / %s:%d] inspecting : yellow ------------" % \
            (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
            
            )
            
#     print(msg, file=sys.stderr)


#    libs.write_Log(msg, True)
    
#     print("[%s:%d] inspecting : yellow ------------" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)

    res, msg = is_ColorName_Yellow(stats_Data)
    
    # green ?
    if res == True : #if res == True
    
        nameOf_Color = "yellow"
        
        return nameOf_Color
    
    else :

        #debug
        msg = "[%s / %s:%d] %s" % \
                (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile())
                    , libs.linenum()
                    , msg
                )
            
#        libs.write_Log(msg, True)
        
    
    #/if res == True
    
    '''###################
        judge : red
    ###################'''
#     print()
    
#     msg = "[%s:%d] inspecting : red ------------" % \
    msg = "[%s / %s:%d] inspecting : red ------------" % \
            (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
            
            )
            
    #libs.write_Log(msg, True)
#     libs.write_Log(msg, dpath_Log, fname_Log, True)


    res, msg = is_ColorName_Red(stats_Data)
    
    # green ?
    if res == True : #if res == True
    
        nameOf_Color = "red"
        
        return nameOf_Color
    
    else :
        
        #debug
        msg = "[%s / %s:%d] %s" % \
                (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile())
                    , libs.linenum()
                    , msg
                )
            
        #libs.write_Log(msg, True)
    
    #/if res == True
    
    '''###################
        judge : white
    ###################'''
#     print()
    
    msg = "[%s / %s:%d] inspecting : white ------------" % \
            (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
            
            )
            
    #libs.write_Log(msg, True)

    res, msg = is_ColorName_White(stats_Data)
    
    # white ?
    if res == True : #if res == True
    
        nameOf_Color = "white"
        
        return nameOf_Color
    
    else :
        
        #debug
        msg = "[%s / %s:%d] %s" % \
                (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile())
                    , libs.linenum()
                    , msg
                )
            
        #libs.write_Log(msg, True)
    
    #/if res == True
    
    '''###################
        judge : black
    ###################'''
#     print()
    
    msg = "[%s / %s:%d] inspecting : black ------------" % \
            (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
            
            )
            
    #libs.write_Log(msg, True)

    res, msg = is_ColorName_Black(stats_Data)
    
    # white ?
    if res == True : #if res == True
    
        nameOf_Color = "black"
        
        return nameOf_Color
    
    else :
        
        #debug
        msg = "[%s / %s:%d] %s" % \
                (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile())
                    , libs.linenum()
                    , msg
                )
            
        #libs.write_Log(msg, True)
    
    #/if res == True
    
    '''###################
        return        
    ###################'''
#     nameOf_Color = "other"
    
    return nameOf_Color
    
#/ def get_Color_Name_From_StatsData(stats_Data) :

def get_4_corners__SaveImage_4Corners(img_Corners, fname_Image, save_Image = True) :
    
    # count
    cntOf_Corners = 1
    
    
    # time label
    tlabel = libs.get_TimeLabel_Now()

    # paths
    dpath_Plot= "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\img.corners"
    
    lo_Names_Of_Corner_Images = []
    
    for item in img_Corners:

#             xpixels = item.shape[1]
#             ypixels = item.shape[0]
#             
#             dpi = 72
#             scalefactor = 1
# 
#             xinch = xpixels * scalefactor / dpi
#             yinch = ypixels * scalefactor / dpi
#         
#             fig = plt.figure(figsize=(xinch,yinch))
#             
#             plt.imshow(item)
        
#             dpath_Plot= "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\img.corners"
        
        fname_Plot = "img.%s.%s.%d.png" % (tlabel, fname_Image, cntOf_Corners)
#             fname_Plot = "%s.%s.%d.png" % (fname_Image, tlabel, cntOf_Corners)
        
        fpath_Plot = "%s\\%s" % (dpath_Plot, fname_Plot)
        
        # increment
        cntOf_Corners += 1
        
#             plt.savefig(fpath_Plot, dpi=dpi)

        # cv2 : save image
        #ref https://www.tutorialkart.com/opencv/python/opencv-python-save-image-example/
        if save_Image == True : cv2.imwrite(fpath_Plot, item)
#         cv2.imwrite(fpath_Plot, item)
        
#         #debug
#         print()
#         print("[%s:%d] fpath_Plot => '%s'" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , fpath_Plot
#         ), file=sys.stderr)
        
        # append file name
        lo_Names_Of_Corner_Images.append(fname_Plot)
        
#             # reset plot
#             plt.clf()
#             plt.cla()
        
    #/for item in im_Corners:    
    
    '''###################
        return        
    ###################'''
    return lo_Names_Of_Corner_Images

    
#/ def saveImage_4Corners(img_Corners, fname_Image) :

def get_4_corners__Get_MetaData(img_Corners) :
    
    # data
    lo_Image_MetaData = []

    for item in img_Corners:
        '''###################
            vars        
        ###################'''
        max_R = -1; max_G = -1; max_B = -1
        min_R = 256; min_G = 256; min_B = 256
    #     min_R = 255; min_G = 255; min_B = 255
    
        # counter
        cntOf_Row = 0
        cntOf_Cell = 0
        
        # values
        valsOf_R = [0] * 256
        valsOf_G = [0] * 256
        valsOf_B = [0] * 256

        for row in item:
        
            for cell in row:
                
#                 #debug
#                 print()
#                 print("[%s:%d] len(cell) => %d" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , len(cell)
#                     ), file=sys.stderr)
#                 return
                
                # get value
                R = cell[0]; G = cell[1]; B = cell[2]
                
                # histogram
                valsOf_R[R] += 1
                valsOf_G[G] += 1
                valsOf_B[B] += 1
                
                # max value
                if R > max_R : max_R = R
                if G > max_G : max_G = G
                if B > max_B : max_B = B
                
                # min value
                if R < min_R : min_R = R
                if G < min_G : min_G = G
                if B < min_B : min_B = B
                
                # count
                cntOf_Cell += 1
            
            # reset count of cells
            cntOf_Cell = 0
            
            # count
            cntOf_Row += 1
            
        #/for row in item:
        
        # append data
        lo_Image_MetaData.append(
            [
#                 valsOf_R
#                 , valsOf_G
#                 , valsOf_B
                
#                 , max_R
                max_R
                , max_G
                , max_B
                
                , min_R
                , min_G
                , min_B
                
                , valsOf_R
                , valsOf_G
                , valsOf_B
                ]
        )
            
    #/for item in img_Corners:
    
    '''###################
        return        
    ###################'''
    #debug
#    print()
#    print("[%s:%d] len(lo_Image_MetaData) => %d" % \
#                        (os.path.basename(libs.thisfile()), libs.linenum()
#                        , len(lo_Image_MetaData)
#                        ), file=sys.stderr)
        
    return lo_Image_MetaData

#/ def get_4_corners__Get_MetaData(img_Corners) :

def get_4_corners__Get_StatsData(img_Corners) :
    
    # data
    lo_Image_StatsData = []
    
    for img_Data in img_Corners:
        
        # var
        do_StasData = {}
        
        '''###################
            skews        
        ###################'''
        
#         print("[%s:%d] getting skew values..." % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stderr)
        
        skew_Values = get_Skews(img_Data)
#         skew = lib_ip.get_Skew(img_Data)
        
        do_StasData['skew_values'] = skew_Values
#         do_StasData['skew'] = skew
        
        # append
        lo_Image_StatsData.append(do_StasData)
        
        '''###################
            index of max        
        ###################'''
#         idxOf_Max_R, idxOf_Max_G, idxOf_Max_B = lib_ip.get_IdxOf_Maxes(img_Data)
        idxOf_Max_R, idxOf_Max_G, idxOf_Max_B, maxVal_R, maxVal_G, maxVal_B \
                    = get_IdxOf_Maxes(img_Data)
        
#         print()
#         print("[%s:%d] idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , idxOf_Max_R, idxOf_Max_G, idxOf_Max_B
#         ), file=sys.stderr)
        
        do_StasData['idxOf_Maxes'] = [idxOf_Max_R, idxOf_Max_G, idxOf_Max_B]
        
        do_StasData['max_Vals'] = [maxVal_R, maxVal_G, maxVal_B]
        
    #/for img in img_Corners:

    '''###################
        return        
    ###################'''
    return lo_Image_StatsData
    
#/ def get_4_corners__Get_StatsData(img_Corners) :

def get_4_corners__Write_Log(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    , comment
                    ) :
    
    dpath_Log = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\logs"
    
    fname_Log = "get_4_corners.log"
    
    fpath_Log = "%s\\%s" % (dpath_Log, fname_Log)
    
    fout_Log = open(fpath_Log, "a")
    
    # header
    fout_Log.write(
        "[%s %s:%s] =============== Get 4 corners" % \
                (libs.get_TimeLabel_Now(), 
                 os.path.basename(libs.thisfile()), 
                 libs.linenum()))
    
    fout_Log.write("\n")
    
    '''###################
        write : meta info        
    ###################'''
    msg = "dpath_Images = %s" % (dpath_Images)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    
    msg = "fname_Image = %s" % (fname_Image)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    fout_Log.write('\n')
    
    
    # iterate
    idxOf_Images = 0
    
    lenOf_LO_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
#     for item in lo_Names_Of_Corner_Images:
    for i in range(lenOf_LO_Names_Of_Corner_Images):
    
        # items
        name = lo_Names_Of_Corner_Images[i]
        
        # meta data
        metaData = lo_Image_MetaData[i]
        
        # stats
                #         [{'skew_values': {'skew_B': 533.0519884872008, 'skew_R': 236.23069368923885, 'sk
                # ew_G': 238.3791814689376}}, {'skew_values': {'skew_B': 56.682440339675104, 'skew
                # _R': 149.4848026940312, 'skew_G': 78.97239727258551}}, {'skew_values': {'skew_B'
                # : 494.3158542205711, 'skew_R': 312.1150017522547, 'skew_G': 465.10712589168577}}
                # , {'skew_values': {'skew_B': 481.71441048360913, 'skew_R': 323.66383568902853, '
                # skew_G': 475.05481070433}}]
        do_Stats = lo_Image_StatsData[i]
        
        do_Skews = do_Stats['skew_values']
#         print()
#         print("[%s:%d] lo_Image_StatsData =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         print(lo_Image_StatsData)
#         
#         print()
#         print("[%s:%d] do_Stats =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         print(do_Stats)
        
        skew_R = do_Skews['skew_R']
        skew_G = do_Skews['skew_G']
        skew_B = do_Skews['skew_B']
#         skew_R = do_Stats['skew_R']
#         skew_G = do_Stats['skew_G']
#         skew_B = do_Stats['skew_B']
        
        '''###################
            file name
        ###################'''
        # file name
        fout_Log.write(name)
#         fout_Log.write(item)
        fout_Log.write('\n')
        
        # meta data
#         print()
#         print("[%s:%d] type(metaData) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData)
#                 ), file=sys.stderr)
#         
#         print("[%s:%d] type(metaData[0]) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData[0])
#                 ), file=sys.stderr)
#         
#         print("[%s:%d] type(metaData[1]) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData[1])
#                 ), file=sys.stderr)

                #         max_R
                #         , max_G
                #         , max_B
                #         
                #         , min_R
                #         , min_G
                #         , min_B
                
                #         , valsOf_R
                #         , valsOf_G
                #         , valsOf_B
        
        msg = "R=(%d,%d) G=(%d,%d) B=(%d,%d)" % \
                (metaData[0], metaData[3], metaData[1]
                 , metaData[4], metaData[2], metaData[5]
                 )
#         msg = "\t".join(metaData)
        
        #fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        #fout_Log.write('\n')
        
        '''###################
            skews        
        ###################'''
        msg = "skew_R = %.04f, skew_G = %.04f, skew_B = %.04f" % \
                (
                    skew_R, skew_G, skew_B
                 )
#         msg = "\t".join(metaData)
        
        #fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        #fout_Log.write('\n')
        
        '''###################
            index of max values,
            max values
        ###################'''
        idxOf_MaxVals = do_Stats['idxOf_Maxes']
        
        max_Vals = do_Stats['max_Vals']

#         msg = "idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
        msg = "idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
                (
                    idxOf_MaxVals[0], idxOf_MaxVals[1], idxOf_MaxVals[2]
                 )
#         msg = "\t".join(metaData)
        
        #fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        #fout_Log.write('\n')
        
        msg = "max_Vals_R = %d, max_Vals_G = %d, max_Vals_B = %d" % \
                (
                    max_Vals[0], max_Vals[1], max_Vals[2]
                 )
#         msg = "\t".join(metaData)
        
        #fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        #fout_Log.write('\n')
        
        '''###################
            raw data : histogram        
        ###################'''
        dat = [str(x) for x in metaData[6]]
        msg = "\t".join(dat)
#         msg = "\t".join(metaData[6])
        #fout_Log.write(msg)
        #fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[7]]
        msg = "\t".join(dat)
        #fout_Log.write(msg)
        #fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[8]]
        msg = "\t".join(dat)
        #fout_Log.write(msg)
        #fout_Log.write('\n')
        
        
        #fout_Log.write('\n')
        
    #/for item in lo_Names_Of_Corner_Images:

    # separator line
#     fout_Log.write('\n')
    
    '''###################
        write : judge        
    ###################'''
#     fout_Log.write('\n')
    
#     msg = "dpath_Images = %s" % (dpath_Images)
#     
#     fout_Log.write(msg)
#     fout_Log.write('\n')
#     
#     msg = "fname_Image = %s" % (fname_Image)
#     
#     fout_Log.write(msg)
#     fout_Log.write('\n')
    
    
    msg = "is_CornerOf_Green__PhotoOf_Sweets => %s (%s)" % (res, comment)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    
    # close file
    fout_Log.close()
#/ get_4_corners__Write_Log

def get_4_corners__Write_Log__V2(
                    lo_Names_Of_Corner_Images, 
                    lo_Image_MetaData, 
                    lo_Image_StatsData
                    , dpath_Images
                    , fname_Image
                    , res
                    ) :
    
    dpath_Log = cons_ip.FilePaths.dpath_LogFile.value

    fname_Log = cons_ip.FilePaths.fname_LogFile.value
#     fname_Log = cons_fx.FPath.fname_LogFile.value
#     dpath_Log = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\logs"
#     
#     fname_Log = "get_4_corners.log"
    
    fpath_Log = "%s\\%s" % (dpath_Log, fname_Log)
    
    fout_Log = open(fpath_Log, "a")
    
    # header
    fout_Log.write(
        "[%s %s:%s] =============== Get 4 corners" % \
                (libs.get_TimeLabel_Now(), 
                 os.path.basename(libs.thisfile()), 
                 libs.linenum()))
    
    fout_Log.write("\n")
    
    '''###################
        write : meta info        
    ###################'''
    msg = "dpath_Images = %s" % (dpath_Images)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    
    msg = "fname_Image = %s" % (fname_Image)
    
    fout_Log.write(msg)
    fout_Log.write('\n')
    fout_Log.write('\n')
    
    '''###################
        return (forced)        
    ###################'''
    return
    
    # iterate
    idxOf_Images = 0
    
    lenOf_LO_Names_Of_Corner_Images = len(lo_Names_Of_Corner_Images)
    
#     for item in lo_Names_Of_Corner_Images:
    for i in range(lenOf_LO_Names_Of_Corner_Images):
    
        # items
        name = lo_Names_Of_Corner_Images[i]
        
        # meta data
        metaData = lo_Image_MetaData[i]
        
        # stats
                #         [{'skew_values': {'skew_B': 533.0519884872008, 'skew_R': 236.23069368923885, 'sk
                # ew_G': 238.3791814689376}}, {'skew_values': {'skew_B': 56.682440339675104, 'skew
                # _R': 149.4848026940312, 'skew_G': 78.97239727258551}}, {'skew_values': {'skew_B'
                # : 494.3158542205711, 'skew_R': 312.1150017522547, 'skew_G': 465.10712589168577}}
                # , {'skew_values': {'skew_B': 481.71441048360913, 'skew_R': 323.66383568902853, '
                # skew_G': 475.05481070433}}]
        do_Stats = lo_Image_StatsData[i]
        
        do_Skews = do_Stats['skew_values']
#         print()
#         print("[%s:%d] lo_Image_StatsData =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         print(lo_Image_StatsData)
#         
#         print()
#         print("[%s:%d] do_Stats =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         print(do_Stats)
        
        skew_R = do_Skews['skew_R']
        skew_G = do_Skews['skew_G']
        skew_B = do_Skews['skew_B']
#         skew_R = do_Stats['skew_R']
#         skew_G = do_Stats['skew_G']
#         skew_B = do_Stats['skew_B']
        
        '''###################
            file name
        ###################'''
        # file name
        fout_Log.write(name)
#         fout_Log.write(item)
        fout_Log.write('\n')
        
        # meta data
#         print()
#         print("[%s:%d] type(metaData) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData)
#                 ), file=sys.stderr)
#         
#         print("[%s:%d] type(metaData[0]) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData[0])
#                 ), file=sys.stderr)
#         
#         print("[%s:%d] type(metaData[1]) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(metaData[1])
#                 ), file=sys.stderr)

                #         max_R
                #         , max_G
                #         , max_B
                #         
                #         , min_R
                #         , min_G
                #         , min_B
                
                #         , valsOf_R
                #         , valsOf_G
                #         , valsOf_B
        
        msg = "R=(%d,%d) G=(%d,%d) B=(%d,%d)" % \
                (metaData[0], metaData[3], metaData[1]
                 , metaData[4], metaData[2], metaData[5]
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        '''###################
            skews        
        ###################'''
        msg = "skew_R = %.04f, skew_G = %.04f, skew_B = %.04f" % \
                (
                    skew_R, skew_G, skew_B
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        '''###################
            index of max values,
            max values
        ###################'''
        idxOf_MaxVals = do_Stats['idxOf_Maxes']
        
        max_Vals = do_Stats['max_Vals']

#         msg = "idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
        msg = "idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
                (
                    idxOf_MaxVals[0], idxOf_MaxVals[1], idxOf_MaxVals[2]
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        msg = "max_Vals_R = %d, max_Vals_G = %d, max_Vals_B = %d" % \
                (
                    max_Vals[0], max_Vals[1], max_Vals[2]
                 )
#         msg = "\t".join(metaData)
        
        fout_Log.write(msg)
#         fout_Log.write("\t".join(metaData))
        fout_Log.write('\n')
        
        '''###################
            raw data : histogram        
        ###################'''
        dat = [str(x) for x in metaData[6]]
        msg = "\t".join(dat)
#         msg = "\t".join(metaData[6])
        fout_Log.write(msg)
        fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[7]]
        msg = "\t".join(dat)
        fout_Log.write(msg)
        fout_Log.write('\n')
        
        dat = [str(x) for x in metaData[8]]
        msg = "\t".join(dat)
        fout_Log.write(msg)
        fout_Log.write('\n')
        
        
        fout_Log.write('\n')
        
    #/for item in lo_Names_Of_Corner_Images:

    # separator line
#     fout_Log.write('\n')
    
    '''###################
        write : judge        
    ###################'''
    
#     msg = "is_CornerOf_Green__PhotoOf_Sweets => %s (%s)" % (res, comment)
#     
#     fout_Log.write(msg)
#     fout_Log.write('\n')
    
    # close file
    fout_Log.close()
#/ get_4_corners__Write_Log

'''###################
    @param color_Names: ["o", "r", "o", "o"]
###################'''
def get_Memo_From_ColorNames_Set(color_Names) :
    
    #ref https://stackoverflow.com/questions/15046242/how-to-sort-the-letters-in-a-string-alphabetically-in-python
    str_ColorNames = ''.join(sorted(color_Names))
    
    memo = ""
    
    '''###################
        judge        
    ###################'''
    if str_ColorNames in cons_ip.ColorNameSet.lo_Color_Sets.value : #if str_ColorNames in cons_ip.ColorNameSet.lo_Color_Sets.value
        
        do_Color_Sets_Memo = cons_ip.ColorNameSet.do_Color_Sets_Memo.value
        
        memo = do_Color_Sets_Memo[str_ColorNames]
    
    else :
        
        memo = cons_ip.ColorNameSet.memo_Unknown.value
        
    #/if str_ColorNames in cons_ip.ColorNameSet.lo_Color_Sets.value
    
    
    
#     if str_ColorNames == cons_ip.ColorNameSet.colSet_OOOO.value: #if str_ColorNames == 
#     
#         memo = cons_ip.ColorNameSet.memo_OOOO.value
#     
#     elif str_ColorNames == cons_ip.ColorNameSet.colSet_GGOO.value : #if str_ColorNames ==
#         
#         memo = cons_ip.ColorNameSet.memo_GGOO.value
#          
#     elif str_ColorNames == cons_ip.ColorNameSet.colSet_OOOY.value : #if str_ColorNames ==
#         
#         memo = cons_ip.ColorNameSet.memo_OOOY.value
#          
#     else : #if str_ColorNames == 
#     
#         memo = "%s (%s)" % (cons_ip.ColorNameSet.memo_Unknown.value, str_ColorNames)
# #         memo = cons_ip.ColorNameSet.memo_Unknown.value
#     
#     #/if str_ColorNames == 
    
    # return
    return memo
    
#/ def get_Memo_From_ColorNames_Set(color_Names) :

def test__get_Opt_IP():
    
    '''###################
        vars
    ###################'''
    lo_Args_Pairs = []
    
    charOf_Option_Switch = "-"
    
    '''###################
        get : args        
    ###################'''
    args = sys.argv
    
    print()
    print("[%s:%d] args =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(args)

    '''###################
        validate : no option elements        
    ###################'''
    if len(args) < 2 : #if len(args) < 2

        print()
        print("[%s:%d] no args =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(args)
        
        return lo_Args_Pairs
        
    #/if len(args) < 2
    
    '''###################
        ops
    ###################'''
    # length : omit program name element
    args_Options = args[1:]
    
    lenOf_Args_Options = len(args_Options)
#     lenOf_Args = len(args)
    
    # each element in the args
    for i in range(lenOf_Args_Options):

        # start with : "-"
        elem = args_Options[i]
        
        #ref https://stackoverflow.com/questions/8802860/checking-whether-a-string-starts-with-xxxx#8802889
        judge = elem.startswith(charOf_Option_Switch)
        
        if judge == True : #if judge == True

            print()
            print("[%s:%d] option swith => %s (char is '%s', index = %d)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , elem, elem[1:], i
                ), file=sys.stderr)
            
            '''###################
                validate : list length --> enough
            ###################'''
            if (lenOf_Args_Options - 2) >= i : #if (lenOf_Args_Options - 2) >= i
    
                pass
            
            else : #if (lenOf_Args_Options - 2) >= i
            
                print()
                print("[%s:%d] option-related value => not given" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
            
            #/if (lenOf_Args_Options - 2) >= i
    
    
        
        else : #if judge == True
        
            pass
        
        #/if judge == True


        
    #/for i in range(lenOf_Args):

    
   
    '''###################
        returen        
    ###################'''
    return lo_Args_Pairs


    
#/ def get_Opt_IP():

def get_ColorName_Set_From_CornerImage(img_Corner):
    
    height, width, channels = img_Corner.shape
    
    msg = "height = %d, width = %d, channels = %d" %\
                            (height, width, channels)
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)

    print()
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg_Log
            ), file=sys.stderr)

#/ def get_ColorName_Set_From_CornerImage(img_Corner):

'''###################
    @param img: RGB data        
###################'''
def get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image):
# def get_StatsData_Of_Image__HSV(img):
    
    '''###################
        convert : to HSV        
    ###################'''
    img_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    
    '''###################
        vars        
    ###################'''
    Hs = []
    Ss = []
    Vs = []
    
    '''###################
        ops        
    ###################'''
#     #debug
#     print("[%s:%d] img_HSV[0][:10] =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print(img_HSV[0][:10])
    
    for row in img_HSV:
        
        for pix in row:
        
            Hs.append(pix[0])
            Ss.append(pix[1])
            Vs.append(pix[2])
            
        #/for pix in row:
        
    #/for row in img_HSV:
    
#     #debug
#     print()
#     print("[%s:%d] Hs[:10] =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     print(Hs[:10])
    
#     #debug : average
#     print()
#     print("[%s:%d] Hs ==> average = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , sum(Hs) * 1.0 / len(Hs)
#         ), file=sys.stderr)
    
    #debug
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
#     val_Average, val_Variance, sd = get_StatsData(Hs)
    
#     print()
#     print("[%s:%d] val_Average = %.03f, val_Variance = %.03f, sd = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , val_Average, val_Variance, sd
#         ), file=sys.stderr)
    
    '''###################
        save : stats data        
    ###################'''
    msg = "file = %s / val_Average = %.04f\tval_Variance = %.04f\tsd = %.04f\tmax = %d\tmin = %d" %\
                            (fname_Image, val_Average, val_Variance, sd, val_Max, val_Min)
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)

    
#     #debug : plot
#     img_Plot_Target = Hs
# #     img_Plot_Target = Hs[:1000]
#     
#     rng = np.arange(len(img_Plot_Target))
#     
#     # reset plot
#     plt.clf()
#     plt.cla()
# 
#     
#     plt.plot(rng, img_Plot_Target, 'r-', label='Hs')
# #     plt.plot(rng, Hs[:100], 'r-', label='Hs')
# #     plt.plot(rng, Hs[:100])
# #     plt.plot(Hs)
#     
#     plt.legend(loc='best')
#     
#     ax = plt.gca()
#      
#     #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
#     ax.grid(which='major', axis='both', linestyle='--')
#     ax.grid(which='minor', axis='both', linestyle='--')
#  
# #     ax.set(aspect=1,
#     ax.set(
#            xlim=(0, len(img_Plot_Target)),
# #            xlim=(0, len(Hs[:100])),
# #            xlim=(0, len(lo_Rs)),
#            ylim=(0, 250))
#     
#     
#     dpath_Savefig = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
#     
#     fname = "savefig.%s.%s.png" % (libs.get_TimeLabel_Now(), fname_Image)
#     
#     fpath_Savefig = os.path.join(dpath_Savefig, fname)
#     
#     plt.savefig(fpath_Savefig)
#     
#     print("[%s:%d] plot ==> saved (%s)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , fpath_Savefig
#                     ), file=sys.stderr)
#     
#     # reset plot
#     plt.clf()
#     plt.cla()
    
    '''###################
        return        
    ###################'''
    return Hs, Ss, Vs

#/ def get_StatsData_Of_Image__HSV(img):

'''###################
    @param img: HSV data        
    @return: res, msg
###################'''
def is_ColorName_Yellow__2(img, dpath_Images, fname_Image):
    
# def is_ColorName_Yellow__2(img):
    
    '''###################
        get : stats        
    ###################'''
    Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image)
#     Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img)
    
    #debug
    msg = "len(Hs) = %d, len(Ss) = %d, len(Vs) = %d" %\
                (len(Hs), len(Ss), len(Vs))
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    '''###################
        get : Hue data
    ###################'''
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
    
    '''###################
        judge
    ###################'''
    # default values
    result = False
    msg = "other"

    # variance
#        (val_Variance < cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value \
#            and val_Variance > cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value) :
    if not \
        (val_Variance <= cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value \
            and val_Variance >= cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value) :
        
#         msg = "variance --> out of range (variance = %.03f / upper = %.03f / loweer = %.03f " %\
        msg = "yellow : variance --> out of range (variance = %.03f / upper = %.03f / lower = %.03f)" %\
                            (val_Variance
                             , cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value
                             , cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)

        
        return result, msg
    
    # average
    if not \
        (val_Average < cons_ip.ColorThresholds.isYellow_HSV_Average__Upper.value \
            and val_Average > cons_ip.ColorThresholds.isYellow_HSV_Average__Lower.value): #if val_Variance > cons_ip.ColorThresholds

#         msg = "average --> out of range (average = %.03f / upper = %.03f / lower = %.03f " %\
        msg = "yellow : average --> out of range (average = %.03f / upper = %.03f / lower = %.03f)" %\
                            (val_Average
                             , cons_ip.ColorThresholds.isYellow_HSV_Average__Upper.value
                             , cons_ip.ColorThresholds.isYellow_HSV_Average__Lower.value)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)
                    
        return result, msg
    
    '''###################
        set : is yellow
    ###################'''
    result = True
    msg = "yellow"
    
    '''###################
        return        
    ###################'''
#     result = False
#     
#     msg = "other"
    
    return result, msg

#/ def is_ColorName_Yellow__2(img):

'''###################
    @param img: HSV data        
    @return: res, msg
###################'''
def is_ColorName_Red__2(img, dpath_Images, fname_Image):
    
# def is_ColorName_Yellow__2(img):
    
    '''###################
        get : stats        
    ###################'''
    Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image)
#     Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img)
    
    #debug
    msg = "len(Hs) = %d, len(Ss) = %d, len(Vs) = %d" %\
                (len(Hs), len(Ss), len(Vs))
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    '''###################
        get : Hue data
    ###################'''
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
    
    '''###################
        judge
    ###################'''
    # default values
    result = False
    msg = "other"
    
    color_Name = cons_ip.ColorNameSet.colName_Red.value
    
    variance_Upper = cons_ip.ColorThresholds.isRed_HSV_Variance__Upper.value
    variance_Lower = cons_ip.ColorThresholds.isRed_HSV_Variance__Lower.value
    
    average_Upper = cons_ip.ColorThresholds.isRed_HSV_Average__Upper.value
    average_Lower = cons_ip.ColorThresholds.isRed_HSV_Average__Lower.value
    
    # variance
    if not \
        (val_Variance <= variance_Upper \
            and val_Variance >= variance_Lower) :
#        (val_Variance < variance_Upper \
#            and val_Variance > variance_Lower) :
#         (val_Variance < cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value \
#             and val_Variance > cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value) :
        
#         msg = "variance --> out of range (variance = %.03f / upper = %.03f / loweer = %.03f " %\
        msg = "%s : variance --> out of range (variance = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Variance
                             , variance_Upper
                             , variance_Lower)
#                              , cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value
#                              , cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)

        
        return result, msg
    
    # average
    if not \
        (val_Average < average_Upper \
            and val_Average > average_Lower) :
#         (val_Average < cons_ip.ColorThresholds.isYellow_HSV_Average__Upper.value \
#             and val_Average > cons_ip.ColorThresholds.isYellow_HSV_Average__Lower.value): #if val_Variance > cons_ip.ColorThresholds

#         msg = "average --> out of range (average = %.03f / upper = %.03f / lower = %.03f " %\
        msg = "%s : average --> out of range (average = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Average
                             , average_Upper
                             , average_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)
                    
        return result, msg
    
    '''###################
        set : is red
    ###################'''
    result = True
    msg = color_Name
    
    '''###################
        return        
    ###################'''
#     result = False
#     
#     msg = "other"
    
    return result, msg

#/ def is_ColorName_Yellow__2(img):

'''###################
    <descriptions>
        1. using RGB values for judgement 

    @param img: HSV data        
    @return: res, msg
###################'''
def is_ColorName_Green__2(img, dpath_Images, fname_Image):
    
    '''###################
        get : stats        
    ###################'''
    Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image)
    
    #debug
    msg = "len(Hs) = %d, len(Ss) = %d, len(Vs) = %d" %\
                (len(Hs), len(Ss), len(Vs))
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    '''###################
        get : Hue data
    ###################'''
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
    
    '''###################
        judge
    ###################'''
    # default values
    result = False
    msg = "other"
    
    color_Name = cons_ip.ColorNameSet.colName_Green.value
    
    variance_Upper = cons_ip.ColorThresholds.isGreen_HSV_Variance__Upper.value
    variance_Lower = cons_ip.ColorThresholds.isGreen_HSV_Variance__Lower.value
    
    average_Upper = cons_ip.ColorThresholds.isGreen_HSV_Average__Upper.value
    average_Lower = cons_ip.ColorThresholds.isGreen_HSV_Average__Lower.value
    
    # variance
    if not \
        (val_Variance <= variance_Upper \
            and val_Variance >= variance_Lower) :
#        (val_Variance < variance_Upper \
#            and val_Variance > variance_Lower) :

#         (val_Variance < cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value \
#             and val_Variance > cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value) :
        
#         msg = "variance --> out of range (variance = %.03f / upper = %.03f / loweer = %.03f " %\
        msg = "%s : variance --> out of range (variance = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Variance
                             , variance_Upper
                             , variance_Lower)
#                              , cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value
#                              , cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)

        
        return result, msg
    
    # average
    if not \
        (val_Average < average_Upper \
            and val_Average > average_Lower) :
#         (val_Average < cons_ip.ColorThresholds.isYellow_HSV_Average__Upper.value \
#             and val_Average > cons_ip.ColorThresholds.isYellow_HSV_Average__Lower.value): #if val_Variance > cons_ip.ColorThresholds

#         msg = "average --> out of range (average = %.03f / upper = %.03f / lower = %.03f " %\
        msg = "%s : average --> out of range (average = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Average
                             , average_Upper
                             , average_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)
                    
        return result, msg
    
    '''###################
        set : is red
    ###################'''
    result = True
    msg = color_Name
    
    '''###################
        return        
    ###################'''
#     result = False
#     
#     msg = "other"
    
    return result, msg

#/ def is_ColorName_Yellow__2(img):

'''###################
    <descriptions>
        1. using RGB values for judgement 

    @param img: HSV data        
    @return: res, msg
###################'''
def is_ColorName_Blue__2(img, dpath_Images, fname_Image):
    
    '''###################
        get : stats        
    ###################'''
    Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image)
    
    #debug
    msg = "len(Hs) = %d, len(Ss) = %d, len(Vs) = %d" %\
                (len(Hs), len(Ss), len(Vs))
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    '''###################
        get : Hue data
    ###################'''
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
    
    '''###################
        judge
    ###################'''
    # default values
    result = False
    msg = "other"
    
    color_Name = cons_ip.ColorNameSet.colName_Blue.value
    
    variance_Upper = cons_ip.ColorThresholds.isBlue_HSV_Variance__Upper.value
    variance_Lower = cons_ip.ColorThresholds.isBlue_HSV_Variance__Lower.value
    
    average_Upper = cons_ip.ColorThresholds.isBlue_HSV_Average__Upper.value
    average_Lower = cons_ip.ColorThresholds.isBlue_HSV_Average__Lower.value
    
    # variance
    if not \
        (val_Variance <= variance_Upper \
            and val_Variance >= variance_Lower) :
        
        msg = "%s : variance --> out of range (variance = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Variance
                             , variance_Upper
                             , variance_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)

        
        return result, msg
    
    # average
    if not \
        (val_Average < average_Upper \
            and val_Average > average_Lower) :

        msg = "%s : average --> out of range (average = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Average
                             , average_Upper
                             , average_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)
                    
        return result, msg
    
    '''###################
        set : is red
    ###################'''
    result = True
    msg = color_Name
    
    '''###################
        return        
    ###################'''
#     result = False
#     
#     msg = "other"
    
    return result, msg

#/ is_ColorName_Blue__2(img, dpath_Images, fname_Image)

'''###################
    <descriptions>
        1. using RGB values for judgement 

    @param img: HSV data        
    @return: res, msg
###################'''
def is_ColorName_Pink__2(img, dpath_Images, fname_Image):
    
    '''###################
        get : stats        
    ###################'''
    Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image)
    
    #debug
    msg = "len(Hs) = %d, len(Ss) = %d, len(Vs) = %d" %\
                (len(Hs), len(Ss), len(Vs))
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    '''###################
        get : Hue data
    ###################'''
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
    
    '''###################
        judge
    ###################'''
    # default values
    result = False
    msg = "other"
    
    color_Name = cons_ip.ColorNameSet.colName_Pink.value
    
    variance_Upper = cons_ip.ColorThresholds.isPink_HSV_Variance__Upper.value
    variance_Lower = cons_ip.ColorThresholds.isPink_HSV_Variance__Lower.value
    
    average_Upper = cons_ip.ColorThresholds.isPink_HSV_Average__Upper.value
    average_Lower = cons_ip.ColorThresholds.isPink_HSV_Average__Lower.value
    
    # variance
    if not \
        (val_Variance <= variance_Upper \
            and val_Variance >= variance_Lower) :
        
        msg = "%s : variance --> out of range (variance = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Variance
                             , variance_Upper
                             , variance_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)

        
        return result, msg
    
    # average
    if not \
        (val_Average < average_Upper \
            and val_Average > average_Lower) :

        msg = "%s : average --> out of range (average = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Average
                             , average_Upper
                             , average_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)
                    
        return result, msg
    
    '''###################
        set : is red
    ###################'''
    result = True
    msg = color_Name
    
    '''###################
        return        
    ###################'''
#     result = False
#     
#     msg = "other"
    
    return result, msg

#/ is_ColorName_Pink__2(img, dpath_Images, fname_Image)

'''###################
    @param img: HSV data        
    @return: res, msg
###################'''
def is_ColorName_Black__2(img, dpath_Images, fname_Image):
    
    '''###################
        get : stats        
    ###################'''
    Hs, Ss, Vs = get_StatsData_Of_Image__HSV(img, dpath_Images, fname_Image)
    
    #debug
    msg = "len(Hs) = %d, len(Ss) = %d, len(Vs) = %d" %\
                (len(Hs), len(Ss), len(Vs))
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    '''###################
        get : Hue data
    ###################'''
    val_Average, val_Variance, sd, val_Max, val_Min = get_StatsData(Hs)
    
    '''###################
        judge
    ###################'''
    # default values
    result = False
    msg = "other"
    
    color_Name = cons_ip.ColorNameSet.colName_Black.value
    
    variance_Upper = cons_ip.ColorThresholds.isBlack_HSV_Variance__Upper.value
    variance_Lower = cons_ip.ColorThresholds.isBlack_HSV_Variance__Lower.value
    
    average_Upper = cons_ip.ColorThresholds.isBlack_HSV_Average__Upper.value
    average_Lower = cons_ip.ColorThresholds.isBlack_HSV_Average__Lower.value
    
    # variance
    if not \
        (val_Variance <= variance_Upper \
            and val_Variance >= variance_Lower) :
#         (val_Variance < cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value \
#             and val_Variance > cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value) :
        
#         msg = "variance --> out of range (variance = %.03f / upper = %.03f / loweer = %.03f " %\
        msg = "%s : variance --> out of range (variance = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Variance
                             , variance_Upper
                             , variance_Lower)
#                              , cons_ip.ColorThresholds.isYellow_HSV_Variance__Upper.value
#                              , cons_ip.ColorThresholds.isYellow_HSV_Variance__Lower.value)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)

        
        return result, msg
    
    # average
    if not \
        (val_Average <= average_Upper \
            and val_Average >= average_Lower) :
#         (val_Average < cons_ip.ColorThresholds.isYellow_HSV_Average__Upper.value \
#             and val_Average > cons_ip.ColorThresholds.isYellow_HSV_Average__Lower.value): #if val_Variance > cons_ip.ColorThresholds

#         msg = "average --> out of range (average = %.03f / upper = %.03f / lower = %.03f " %\
        msg = "%s : average --> out of range (average = %.03f / upper = %.03f / lower = %.03f)" %\
                            ( color_Name
                            , val_Average
                             , average_Upper
                             , average_Lower)
                        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, True)
                    
        return result, msg
    
    '''###################
        set : is red
    ###################'''
    result = True
    msg = color_Name
    
    '''###################
        return        
    ###################'''
#     result = False
#     
#     msg = "other"
    
    return result, msg

#/ def is_ColorName_Yellow__2(img):

'''###################
    @param ind: index of the img_Corner
                |------------------------|
                |(2)                  (3)|
                |                        |
                |                        |
                |                        |
                |(0)                  (1)|
                |------------------------|

    @return: msg
                "other"
                "yellow"
                "green"
                "red"

###################'''
# def get_ColorName_From_CornerImage(img_Corner, dpath_Images, fname_Image):
def get_ColorName_From_CornerImage(img_Corner, dpath_Images, fname_Image, ind):

    height, width, channels = img_Corner.shape
    
    '''###################
        meta data        
    ###################'''
#     msg = "%s %d" %\
    #msg = "\n%s %d" %\
    msg = "\n%s %d ---------------------" %\
                (fname_Image, ind)
#                 (fname_Image)
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)

    
    print()
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg_Log
            ), file=sys.stderr)

    '''######################################
        get : color name        
    ###################'''
#     # default
#     msg = "other"
    
    '''###################
        yellow
    ###################'''
    res, msg = is_ColorName_Yellow__2(img_Corner, dpath_Images, fname_Image)

    # yellow
    if res == True : #if res == True
    
        return msg
    
    '''###################
        red
    ###################'''
    res, msg = is_ColorName_Red__2(img_Corner, dpath_Images, fname_Image)
    
    # red
    if res == True : #if res == True
    
        return msg

    '''###################
        green
    ###################'''
    res, msg = is_ColorName_Green__2(img_Corner, dpath_Images, fname_Image)

    # green
    if res == True : #if res == True
    
        return msg
    
    '''###################
        blue
    ###################'''
    res, msg = is_ColorName_Blue__2(img_Corner, dpath_Images, fname_Image)

    # green
    if res == True : #if res == True
    
        return msg
    
    '''###################
        pink
    ###################'''
    res, msg = is_ColorName_Pink__2(img_Corner, dpath_Images, fname_Image)

    # green
    if res == True : #if res == True
    
        return msg
    
    '''###################
        black
    ###################'''
    res, msg = is_ColorName_Black__2(img_Corner, dpath_Images, fname_Image)
    
    # black
    if res == True : #if res == True
    
        return msg
    
    '''###################
        other
    ###################'''
    # debug
    msg = "file : %s %d (%s)" %\
                                (fname_Image, ind, msg)
                        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)

    '''###################
        return        
    ###################'''
    # default
    msg = "other"
   
    return msg
#     return res, msg
    
#/ def get_ColorName_Set_From_CornerImage(img_Corner):

'''###################
    @param lo_Data: [188, 187, 188, ...]
    
    @return: val_Average, val_Variance, sd
    
###################'''
def get_StatsData(lo_Data):
    
    lenOf_LO_Data = len(lo_Data)
    
#     print()
#     print("[%s:%d] lo_Data[:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(lo_Data[:10])
    
    
    val_Average = sum(lo_Data) * 1.0 / lenOf_LO_Data

#     print()
#     print("[%s:%d] val_Average =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(val_Average)
    
            #     [lib_ip.py:3837] val_Average =>
            # 94.75623456790123
            
    '''###################
        variance        
    ###################'''
    #ref http://www.geisya.or.jp/~mwm48961/kou3/prob_variance1.htm
    # �ｼ剃ｹ励�ｮ蟷ｳ蝮�
    lo_Squares = [1.0 * x * x for x in lo_Data]
#     lo_Squares = [x * x for x in lo_Data]
#     lo_Squares = np.power(lo_Data, 2)
#     lo_Squares = [np.power(lo_Data, 2)]
    
#     print()
#     print("[%s:%d] lo_Squares[:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(lo_Squares[:10])
    
#     print()
#     print("[%s:%d] lo_Data[0] = %.03f, lo_Data[0] * lo_Data[0] = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , lo_Data[0], lo_Data[0] * lo_Data[0]
#         ), file=sys.stderr)
# #     print(lo_Data[0] * lo_Data[0])
    
    
#     print()
#     print("[%s:%d] lo_Data[:10] =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(lo_Data[:10])

    
    avgOf_LO_Squares = sum(lo_Squares) / lenOf_LO_Data
#     avgOf_LO_Squares = lo_Squares / lenOf_LO_Data

#     print()
#     print("[%s:%d] avgOf_LO_Squares =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(avgOf_LO_Squares)
    
    # variance : �ｼ剃ｹ励�ｮ蟷ｳ蝮� - 蟷ｳ蝮�縺ｮ莠御ｹ�
    #ref power https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html
    val_Variance = avgOf_LO_Squares - np.power(val_Average, 2)
    
#     print()
#     print("[%s:%d] val_Variance =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(val_Variance)
    
    '''###################
        standard dev        
    ###################'''
    sd = np.sqrt(val_Variance)

    
    '''###################
        min, max
    ###################'''
    val_Max = max(lo_Data)
    val_Min = min(lo_Data)
    
    '''###################
        return
    ###################'''
    return val_Average, val_Variance, sd, val_Max, val_Min
#     return val_Average, val_Variance, sd
    
#     , val_Variance, sd

#/ def get_StatsData(img):

'''###################
    
    @param file: file pull path
    
    @return: dictionary

    ref https://www.lifewithpython.com/2014/12/python-extract-exif-data-like-data-from-images.html        
###################'''
def get_exif_of_image(file):
    """Get EXIF of an image if exists.

    謖�螳壹＠縺溽判蜒上�ｮEXIF繝�繝ｼ繧ｿ繧貞叙繧雁�ｺ縺咎未謨ｰ
    @return exif_table Exif 繝�繝ｼ繧ｿ繧呈�ｼ邏阪＠縺溯ｾ樊嶌
    """
    im = Image.open(file)

    # Exif 繝�繝ｼ繧ｿ繧貞叙蠕�
    # 蟄伜惠縺励↑縺代ｌ縺ｰ縺昴�ｮ縺ｾ縺ｾ邨ゆｺ� 遨ｺ縺ｮ霎樊嶌繧定ｿ斐☆
    try:
        exif = im._getexif()
    except AttributeError:
        return {}

    # 繧ｿ繧ｰID縺昴�ｮ縺ｾ縺ｾ縺ｧ縺ｯ莠ｺ縺瑚ｪｭ繧√↑縺�縺ｮ縺ｧ繝�繧ｳ繝ｼ繝峨＠縺ｦ
    # 繝�繝ｼ繝悶Ν縺ｫ譬ｼ邏阪☆繧�
    exif_table = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    return exif_table

'''###################
    
    get_GPS_Data(fpath_Image)
    
    @return: tuple
             => (('N', 35, 35, 24.14), ('E', 139, 34, 48.01))
             
             False
             => no key "GPSInfo"
    
    @param fpath_Image: file full path
    
    @example file : C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload\2018-08-22_15-42-10_000.jpg
    
    [ops_1.py:126] dicOf_Exif['GPSInfo'] =>
        {1: 'N', 2: ((35, 1), (35, 1), (2414, 100)), 3: 'E', 4: ((139, 1), (34, 1), (480
        1, 100)), 5: b'\x00', 6: (24268, 387), 7: ((6, 1), (42, 1), (900, 100)), 12: 'K'
        , 13: (0, 1), 16: 'T', 17: (80093, 231), 23: 'T', 24: (80093, 231), 29: '2018:08
        :22', 31: (10, 1)}        
###################'''
def get_GPS_Data(fpath_Image):

    #debug
    print()
    print("[%s:%d] getting GPS data for ... : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Image
            ), file=sys.stderr)
    
    dicOf_Exif = get_exif_of_image(fpath_Image)# def get_GPS_Data():
    
    '''###################
        validate : GPSInfo
    ###################'''
    if not "GPSInfo" in dicOf_Exif : #if not "GPSInfo" in dicOf_Exif
        
        msg = "no key 'GPSInfo' for file : %s" %\
                                        (fpath_Image)
                                
        msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
        libs.write_Log(msg_Log, True)
        
        return False
        
    #/if not "GPSInfo" in dicOf_Exif
            
            
    # get data
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
