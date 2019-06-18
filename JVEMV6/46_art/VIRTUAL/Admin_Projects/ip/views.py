'''###################


data dir
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data
    
###################'''


# from django.shortcuts import render
'''###################
    django modules
###################'''
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from mailbox import fcntl

'''###################
    import : built-in modules        
###################'''
import subprocess, copy, re, clipboard, time, \
        os, datetime, ftplib, glob, sys, cv2 \
        , matplotlib.pyplot as plt, codecs, shutil, numpy as np

'''###################
    import : orig modules        
###################'''
# sys.path.append('.')
# sys.path.append('..')

# sys.path.append('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/VIRTUAL/Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects')
from libs_admin import libs, lib_ip, cons_ip
# from Admin_Projects.libs_admin import libs

# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
# 
# from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    vars : global        
###################'''
numOf_DosAttack = 0

# Create your views here.
# def index():
def index(request):
    
    now = datetime.datetime.now()


    action = "index"
    message = "yes"

    page_Title = "Image Processing"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    return render(request, 'ip/index.html', dic)

#     return HttpResponse(html)
# #     return HttpResponse("Hello Django (new urls.py file)")

def test(request):
    
    now = datetime.datetime.now()


    action = "test"
    message = "yes"

    page_Title = "Image Processing"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    return render(request, 'ip/test.html', dic)

#     return HttpResponse(html)
# #     return HttpResponse("Hello Django (new urls.py file)")

def _anims__Load_LO_Actions():
    
    dpath_List = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data"

    fname_List = "anims_listof_commands.dat"
    
    fpath_List = os.path.join(dpath_List, fname_List)
    
    f = open(fpath_List, "r")

    # header line
    f.readline()
    
    # body lines
    lines = f.readlines()
    
    # close file
    f.close()
    
    lo_Commands = []
    
    # build list
    for item in lines:

        lo_Commands.append(item.split("\t")[1:])
        
    #/for item in lines:
    
    #debug
    print()
    print("[%s:%d] lo_Commands =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(lo_Commands)
    
    return lo_Commands
    
#/ def _anims__Load_LO_Actions()(request):


def _anims_JS__1_Move_Leaves__Test_1_Resize__exec(angle, scale, img, center, fpath_Dst):
    
#     angle_45 = 45
#     scale = 1.0

    (h, w) = img.shape[:2]
#     center = (365, 203)
#     center = (w / 2, h / 2)
    
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(img, M, (h, w))
    
#     tokens = fname_Image_File.split(".")
#     fname_Dst = "%s.%s.(rotate=%d).%s.%s" \
#             % (tokens[0], tokens[1], angle_45, libs.get_TimeLabel_Now(), tokens[2])
    
#     fpath_Image_File__Dst = os.path.join(dpath_Image_File, fname_Dst)
    
    cv2.imwrite(fpath_Dst, rotated)
    
#/ def _anims_JS__1_Move_Leaves__Test_1_Resize__exec():
    
def _anims_JS__1_Move_Leaves__Test_1_Resize(request):

    '''###################
        prep        
    ###################'''
    dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
    
    fname_Image_File = "leaf-2.1.png"   # orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\4_animations\1_\5_\images
    
    fpath_Image_File = os.path.join(dpath_Image_File, fname_Image_File)
    
    print("[%s:%d] fpath_Image_File = %s (exists = %s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image_File, os.path.isfile(fpath_Image_File)
        ), file=sys.stderr)

    '''###################
        prep : params
            main.js :: _anims_Action_LinkTo__1(_param)
            , option_tick_move_X : _option_tick_move_X
            , option_tick_move_Y : _option_tick_move_Y
            
            , opt_rotate_Start : _opt_rotate_Start
            , opt_rotate_End : _opt_rotate_End

    ###################'''
    param_Loc_Start_X = request.GET.get('option_loc_start_X', False)
    param_Loc_Start_Y = request.GET.get('option_loc_start_Y', False)
    
    param_Cut_Width = request.GET.get('opt_cut_width', False)
    param_Cut_Height = request.GET.get('opt_cut_height', False)
    
    # modify
    # ref tertiary https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
    param_Loc_Start_X = 0 if (param_Loc_Start_X == False) else int(param_Loc_Start_X)
    param_Loc_Start_Y = 0 if (param_Loc_Start_Y == False) else int(param_Loc_Start_Y)
    
    param_Cut_Width = 100 if (param_Cut_Width == False) else int(param_Cut_Width)
    param_Cut_Height = 100 if (param_Cut_Height == False) else int(param_Cut_Height)
    
#     print("[%s:%d] param_Loc_Start_X = %d, param_Loc_Start_Y = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , param_Loc_Start_X, param_Loc_Start_Y
#         ), file=sys.stderr)
    #abcde
    
    '''###################
        op        
    ###################'''
    '''###################
        img : read
    ###################'''
    #ref http://peaceandhilightandpython.hatenablog.com/entry/2016/01/09/214333
    #ref alpha channel http://opencv.blog.jp/python/alpha_channel
    img = cv2.imread(fpath_Image_File, cv2.IMREAD_UNCHANGED)
#     img = cv2.imread(fpath_Image_File)
#     img = cv2.imread(fpath_Image_File, cv2.IMREAD_COLOR)
    
#     orgHeight, orgWidth = img.shape[:2]
#     size = (int(orgWidth/2), int(orgHeight/2))
# #     size = (int(orgHeight/2), int(orgWidth/2))
#     
# #     size = (orgHeight/2, orgWidth/2)
#     
#     halfImg = cv2.resize(img, size)
#     
#     tokens = fname_Image_File.split(".")
#     fname_Half = "%s.%s.(half).%s.%s" \
#             % (tokens[0], tokens[1], libs.get_TimeLabel_Now(), tokens[2])
# 
#     cv2.imwrite(os.path.join(dpath_Image_File, fname_Half), halfImg)
#     cv2.imwrite('half.jpg', halfImg)
    
    '''###################
        rotate        
    ###################'''
    tokens = fname_Image_File.split(".")
    (h, w) = img.shape[:2]
     
    tlabel = libs.get_TimeLabel_Now()
#     
#     for i in range(0, 10):
# #     for i in range(0, 5):
#         
#         angle = i * 5
#         scale = 1.0
#         
#         #ref radians https://docs.scipy.org/doc/numpy/reference/generated/numpy.radians.html
#         span = int((370 - w / 2) * np.sin(np.radians(angle)))
#         span_w = int((370 - w / 2) * np.cos(np.radians(angle)))
#         
#         center = (w / 2 + span_w, h / 2 + span)
# #         center = (w / 2, h / 2 + span)
# #         center = (w / 2, h / 2 - span)
# #         (h, w) = img.shape[:2]
# #         center = (w / 2, h / 2)
#     
#         fname_Dst = "%s.%s.(rotate=%d).%s.(center=%d,%d).%s" \
#                 % (tokens[0], tokens[1], angle, tlabel, center[0], center[1], tokens[2])
# #                 % (tokens[0], tokens[1], angle, tlabel, tokens[2])
# #                 % (tokens[0], tokens[1], angle, libs.get_TimeLabel_Now(), tokens[2])
#          
#         fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
#         
#         _anims_JS__1_Move_Leaves__Test_1_Resize__exec(angle, scale, img, center, fpath_Dst)
#         
#         
#     #/for i in range(0, 10):

    '''###################
        move image        
    ###################'''
    #ref https://stackoverflow.com/questions/23464495/fastest-way-to-move-image-in-opencv
    fname_Dst = "%s.%s.(moved).%s.%s" \
        % (tokens[0], tokens[1], tlabel, tokens[2])
        
    fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
    
    print("[%s:%d] fname_Dst => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Dst
        ), file=sys.stderr)
    
    img_Partial = img[
                param_Loc_Start_Y : param_Loc_Start_Y + param_Cut_Height
                , param_Loc_Start_X : param_Loc_Start_X + param_Cut_Width
                
                ]  # h, w
#     img_Partial = img[param_Loc_Start_Y : 270, param_Loc_Start_X : 420]  # h, w
#     img_Partial = img[150 : 270, 300 : 420]  # h, w
#     img_Partial = img[0 : 100, 0 : 50]  # h, w
#     img_Partial = img[cv2.Rect(0, 0, 100, 100)]
#     img_Partial = img(cv2.Rect(0, 0, 100, 100))
    
    cv2.imwrite(fpath_Dst, img_Partial)
#     cv2.imwrite(fname_Dst, img_Partial)
    
    
#     #ref https://www.tutorialkart.com/opencv/python/opencv-python-rotate-image/#opencv-python-rotate-image
#     angle_45 = 45
#     scale = 1.0

#     (h, w) = img.shape[:2]
#     center = (365, 203)
# #     center = (w / 2, h / 2)
#     
#     M = cv2.getRotationMatrix2D(center, angle_45, scale)
#     rotated_45 = cv2.warpAffine(img, M, (h, w))
# #     rotated90 = cv2.warpAffine(img, M, (h, w))
#     
#     tokens = fname_Image_File.split(".")
#     fname_Dst = "%s.%s.(rotate=%d).%s.%s" \
#             % (tokens[0], tokens[1], angle_45, libs.get_TimeLabel_Now(), tokens[2])
#     
#     fpath_Image_File__Dst = os.path.join(dpath_Image_File, fname_Dst)
#     
#     cv2.imwrite(fpath_Image_File__Dst, rotated_45)
    
    
#/ def _anims_JS__1_Move_Leaves__Test_1_Resize():
    
def _anims_JS__1_Move_Leaves(request):
    
    '''###################
        ops
    ###################'''
    _anims_JS__1_Move_Leaves__Test_1_Resize(request)
    
    '''###################
        return        
    ###################'''
    status = 1
    
    msg = "OK"
    
    return (status, msg)
    
#/ def _anims_JS__1_Move_Leaves(request):
    
def anims_JS(request):
    
    '''###################
        time        
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    dic = {
        
        "message" : ""
        , "message_2" : ""
        }
    
    render_Page = 'ip/anims/plain_anims.html'
    
    '''###################
        params
    ###################'''
    param = request.GET.get('param', False)
    
    #debug
#     print("[%s:%d] param => %s" % \
    print("[%s:%d] param => %s ============================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param
            ), file=sys.stderr)

    '''###################
        dispatch
    ###################'''
    if param == cons_ip.Anims_Params.PARAM__1_MOVE_LEAVES.value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM__1_MOVE_LEAVES        
        ###################'''
        # call func
        (status, msg) = _anims_JS__1_Move_Leaves(request)

        dic['message'] += "move leaves"
        
        dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)

    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start

    dic['message_2'] += "(time = %s) (elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)


    '''###################
        render
    ###################'''
    return render(request, render_Page, dic)
    
    
#/ def anims_JS(request):
    
    
def anims(request):
    
    now = datetime.datetime.now()


    action = "anims"
    message = "yes"

    page_Title = "IP / anims"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    '''###################
        list of commands
    ###################'''
    lo_Commands = _anims__Load_LO_Actions()
#     lo_Commands = [
#          
#         ["move_leaves", "image sequence for moving leaves"],
#          
#         ["???", "unknown"],
#     ]
     
     
    # set var
    dic["lo_Commands"] = lo_Commands
    
    dic["count"] = 0

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/anims/anims.html', dic)
#         return render(request, 'ip/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/anims/anims_full.html', dic)
#         return render(request, 'ip/basics_full.html', dic)

#/ anims

def basics(request):
    
    now = datetime.datetime.now()


    action = "basics"
    message = "yes"

    page_Title = "IP / basics"

    dic = {
            'action' : action, 
            "message" : message, 
#             "lo_Commands" : lo_Commands,
            "page_Title" : page_Title,
    }
#     dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}

#     dic = {message : _message}

    '''###################
        list of commands
    ###################'''
    lo_Commands = [
        
        ["get_4_Corners", "4 corners of an image file"],
        
        ["???", "unknown"],
    ]
    
    
    # set var
    dic["lo_Commands"] = lo_Commands

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/basics_full.html', dic)

def get_4_corners(request):
    
    '''###################
        vars        
    ###################'''
    dic = {}

    '''###################
        get : files list
    ###################'''
    dpath_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6" \
                + "\\46_art\\VIRTUAL\\Admin_Projects" \
                + "\\ip" \
                + "\\images"
    
    fpath_Glob = "%s\\*" % (dpath_Images)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    # files only
    lo_Files_Filtered = []
    
#     #debug
#     print()
#     print("[%s:%d] os.path.isfile(dpath_Images + \"\\\" + lo_Files[0]) => %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , os.path.isfile(dpath_Images + "\\" + lo_Files[0])
#                     ), file=sys.stderr)
#     
#     print("[%s:%d] dpath_Images + \"\\\" + lo_Files[0] => %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , dpath_Images + "\\" + lo_Files[0]
#                     ), file=sys.stderr)
    
    for item in lo_Files:

#         if os.path.isfile(dpath_Images + "\\" + item) == True : 
        if os.path.isfile(item) == True : 
            lo_Files_Filtered.append(item)
        
    #/for item in lo_Files:

    # update the list
    
    lo_Files = lo_Files_Filtered
    
    lo_Files.sort()


    # set list
    dic['lo_Files'] = [os.path.basename(x) for x in lo_Files]
    
    # set : dpath
    dic['dpath_Images'] = dpath_Images
    
    '''###################
        dflt : corner values        
    ###################'''
    dic['dflt_Corner_Width'] = cons_ip.DfltVals.get_4Corners__Corner_Width.value
    dic['dflt_Corner_Padding'] = cons_ip.DfltVals.get_4Corners__Corner_Padding.value

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8001/ip/basics/"
#     referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/get_4_corners.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/get_4_corners_full.html', dic)

'''###################
    __ip_ops__gradation
    
    at : 2018/06/30 09:15:53
    
###################'''
def __ip_ops__gradation(request):
    
    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    # meta data
    height, width, channels = img_Orig.shape
    
    '''###################
        return        
    ###################'''
    url_Path_Full = "ip/ops/ip_ops__gradation_full.html"
    url_Path = "ip/ops/ip_ops__gradation.html"

    dic = {"msg" : "gradation : ip_ops__gradation.html"}

    return (url_Path_Full, url_Path, dic)
    
#/ def __ip_ops__gradation(request):
    
    
    
'''###################
    ip_ops        
###################'''
def ip_ops(request):
    
    '''###################
        params
    ###################'''
    request_Commands = request.GET.get('commands', False)
    
    '''###################
        vars        
    ###################'''
    dic = {}

    '''###################
        ops
    ###################'''
    reqCmd_Gradation = "gradation"
    
    if request_Commands : #if request_Commands
        
        if request_Commands == reqCmd_Gradation : #if request_Commands == reqCmd_Gradation
    
            url_Path_Full, url_Path, dic = __ip_ops__gradation(request)
    
        else : #if request_Commands == reqCmd_Gradation
        
            url_Path_Full = "ip/ops/ip_ops_full.html"
            url_Path = "ip/ops/ip_ops.html"
            
            dic['msg'] = "commands => %s" % request_Commands

        
        #/if request_Commands == reqCmd_Gradation
    
    
        
        
    
    else : #if request_Commands
    
        url_Path_Full = "ip/ops/ip_ops_full.html"
        url_Path = "ip/ops/ip_ops.html"
        
        dic['msg'] = "ip_ops.html"

    
    #/if request_Commands
        
        
#     url_Path_Full, url_Path, dic = __ip_ops__gradation(request)
#     url_Path_Full = "ip/ops/ip_ops_full.html"
#     url_Path = "ip/ops/ip_ops.html"
#     url_Path_Full, url_Path, dic = __ip_ops__gradation(request)
#     url_Path_Full = "ip/ops/ip_ops_full.html"
#     url_Path = "ip/ops/ip_ops.html"
    
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8001/ip/basics/"
#     referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, url_Path, dic)
#         return render(request, 'ip/get_4_corners.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, url_Path_Full, dic)
#         return render(request, 'ip/get_4_corners_full.html', dic)

#/ def ip_ops(request):
    
    
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
def get_Corner_Images(img_Src, corner_Length) :
    
    height, width, channels = img_Src.shape
    
    clips = [
    
        img_Src[(height - corner_Length) : height, 0 : corner_Length], # clp_LB
        img_Src[(height - corner_Length) : height, width - corner_Length : width], # clp_RB
        img_Src[0 : corner_Length, 0 : corner_Length], # clp_LU
        img_Src[0 : corner_Length, width - corner_Length : width], # clp_RU
    ]
    
    # return
    return clips
    
#/ def get_Corner_Images(img_RGB, corner_Length) :

# def _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images, lo_Image_MetaData):
def _exec_get_4_corners__Write_Log \
(lo_Names_Of_Corner_Images, lo_Image_MetaData, lo_Image_StatsData
                        , dpath_Images
                        , fname_Image
                        , res
                        , comment

):
    
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

    
#/ def _exec_get_4_corners__Write_Log(lo_Names_Of_Corner_Images):
    
def _exec_get_4_corners__Get_MetaData(img_Corners):
    
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
    print()
    print("[%s:%d] len(lo_Image_MetaData) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_Image_MetaData)
                        ), file=sys.stderr)
        
    return lo_Image_MetaData
    
#/ def _exec_get_4_corners__Get_MetaData(img_Corners):

'''==============================================
    _exec_get_4_corners__Get_StatsData(img_Corners)
    
    at : 2018/05/28 07:35:40
    
    @param img_Corners: list of opencv image data (4 corners of a original image)
    
    @return: list of dictionaries
        [{'skew' : 3.032, 'kurtosis' : 1.2230, 'integral' : 3428322},...]
=============================================='''
def _exec_get_4_corners__Get_StatsData(img_Corners):
    
    # data
    lo_Image_StatsData = []
    
    for img_Data in img_Corners:
        
        # var
        do_StasData = {}
        
        '''###################
            skews        
        ###################'''
        
        print("[%s:%d] getting skew values..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
        
        skew_Values = lib_ip.get_Skews(img_Data)
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
                    = lib_ip.get_IdxOf_Maxes(img_Data)
        
        print()
        print("[%s:%d] idxOf_Max_R = %d, idxOf_Max_G = %d, idxOf_Max_B = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , idxOf_Max_R, idxOf_Max_G, idxOf_Max_B
        ), file=sys.stderr)
        
        do_StasData['idxOf_Maxes'] = [idxOf_Max_R, idxOf_Max_G, idxOf_Max_B]
        
        do_StasData['max_Vals'] = [maxVal_R, maxVal_G, maxVal_B]
        
    #/for img in img_Corners:

    '''###################
        return        
    ###################'''
    return lo_Image_StatsData

#/ def _exec_get_4_corners__Get_StatsData(img_Corners):
    
def _exec_get_4_corners__SaveImage_4Corners(img_Corners, fname_Image):
    
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
        cv2.imwrite(fpath_Plot, item)
        
        #debug
        print()
        print("[%s:%d] fpath_Plot => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Plot
        ), file=sys.stderr)
        
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
    
#/ def _exec_get_4_corners__SaveImage_4Corners(img_Corners):
    
def gen_Cake_CSV__Get_Params(request):
    
    '''###################
        get : params
    ###################'''
    dpath_Images = request.GET.get('dpath_images', False)

    '''###################
        get : params : save image
    ###################'''
    # ref : function exec_Get_4Corners(fname) :: main.js
    flg_save_image = request.GET.get('flg_save_image', False)
    
    # set flag
    flg_SaveImage = False
    
    if flg_save_image == "true" : #if flg_save_image

        flg_SaveImage = True
        
    #/if flg_save_image

    '''###################
        get : params : corner_width
    ###################'''
    # ref : function exec_Get_4Corners(fname) :: main.js
    param_Corner_Width = request.GET.get('corner_width', False)
    
    #debug
    print()
    print("[%s:%d] param_Corner_Width => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , int(param_Corner_Width)
        ), file=sys.stderr)
    
    # convert
    param_Corner_Width = int(param_Corner_Width)
    
    '''###################
        get : params : corner_Padding
    ###################'''
    # ref : function exec_Get_4Corners(fname) :: main.js
    param_Corner_Padding = request.GET.get('corner_Padding', False)
    
    #debug
    print()
    print("[%s:%d] param_Corner_Padding => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , int(param_Corner_Padding)
        ), file=sys.stderr)
    
    # convert
    param_Corner_Padding = int(param_Corner_Padding)
    
    '''###################
        return        
    ###################'''
    return dpath_Images, flg_SaveImage, param_Corner_Width, param_Corner_Padding

#/ def gen_Cake_CSV__Get_Params(request):
    
    
def gen_Cake_CSV__Get_ListOf_Files(dpath_Images):
    
    fpath_Glob = "%s\\*" % (dpath_Images)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    # files only
    lo_Files_Filtered = []
    
    for item in lo_Files:

        if os.path.isfile(item) == True : 
            lo_Files_Filtered.append(item)
        
    #/for item in lo_Files:

    # update the list
    lo_Files = lo_Files_Filtered
    
    lo_Files.sort()    
    
    # return
    return lo_Files
        
#/ def gen_Cake_CSV__Get_ListOf_Files(dpath_Images):
    
    
def gen_Cake_CSV__Get_ColorName_Set(\
    dpath_Images
   , lo_Files
   , flg_SaveImage
   , param_Corner_Width
   , param_Corner_Padding
           ):
    
    '''###################
        vars        
    ###################'''
    lo_ColorName_Set = []
    
    '''###################
        get color name set        
    ###################'''
#     flg_SaveImage = False
    
    #debug
    cnt = 0
#     maxOf_Cnt = 30
#     maxOf_Cnt = 20
#    maxOf_Cnt = 5
    maxOf_Cnt = 999
#     maxOf_Cnt = 15
#     maxOf_Cnt = 10
#     maxOf_Cnt = 5
#     maxOf_Cnt = 2
    
    '''###################
        time        
    ###################'''
    time_Exec_Start = time.time()
    
    for fpath in lo_Files:
#     for fname in lo_Files:
        
        # count
        print()
        print("[%s:%d] processing image ===> %d -------------------" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , cnt
        ), file=sys.stderr)
        
        # judge
        lo_ColorNames = lib_ip.get_ColorName_Set_From_Image(\
                dpath_Images, fpath, flg_SaveImage, \
                param_Corner_Width, param_Corner_Padding)
        
        # append
        lo_ColorName_Set.append([fpath, lo_ColorNames])
        
        #debug
        cnt += 1
        
        if cnt >= maxOf_Cnt : break #if cnt >= maxOf_Cnt
    
    #/for fname in lo_Files:


    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start

    #msg = "gen csv => complete (%s)(elapsed = %02.3f sec)" % \
    msg = "gen csv => complete (%s)(elapsed = %02.3f sec / %d files / %02.3f sec per file)" % \
                (libs.get_TimeLabel_Now(), time_Exec_Elapsed, len(lo_Files), time_Exec_Elapsed / len(lo_Files))
                #(libs.get_TimeLabel_Now(), time_Exec_Elapsed)
                
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)


    '''###################
        return        
    ###################'''
    return lo_ColorName_Set
    
#/ def gen_Cake_CSV__Get_ColorName_Set(dpath_Images, lo_Files):
    
def gen_Cake_CSV__Gen_CSVFile(\
      dpath_CSV, fname_CSV
      , lo_ColorName_Set__Modified_2
      , dpath_Images):
# def gen_Cake_CSV__Gen_CSVFile(dpath_CSV, fname_CSV, lo_ColorName_Set__Modified_2):
    #_20190322_074835
    '''###################
        vars
    ###################'''
    lines = []
    
    cnt = 1
    
    '''###################
        header
    ###################'''
    #_20190322_075440
    #hdr = "no\tfile_name\tmemos\tGPS"
    hdr = "no\tfile_name\tmemos\t\t\tGPS"	# 20190322_075500
#     hdr = "no\tfile_name\tmemos"
    
    lines.append(hdr)
    
    '''###################
        color name set        
    ###################'''
    for item in lo_ColorName_Set__Modified_2:
        
        '''###################
            vars        
        ###################'''
        fname = item[0]
        
        '''###################
            var : color_Names        
            
            e.g. "oooo" (string)
            
        ###################'''
        color_Names = item[1]

        '''###################
            build : csv        
        ###################'''
        tmp_Line = []
        
        tmp_Line.append(str(cnt))
#         tmp_Line.append(cnt)
        tmp_Line.append(fname)
        
        '''###################
            image content        
        ###################'''
        line_Memo = lib_ip.get_Memo_From_ColorNames_Set(color_Names)
        
        tmp_Line.append(line_Memo)
#         tmp_Line.append(line_Memo)
#         tmp_Line.append("".join(color_Names))

        '''###################
            exif : gps data        
        ###################'''
        fpath_Image = os.path.join(dpath_Images, fname)
        
        data_GPS = lib_ip.get_GPS_Data(fpath_Image)
        
        # validate
        if not data_GPS == False : #if not data_GPS == False

            # tuple --> to list
            data_GPS_Lat = [str(x) for x in data_GPS[0]]  # N,S
            data_GPS_Longi = [str(x) for x in data_GPS[1]] # E,W
            
            # build text
            gps_Lat = "-".join(data_GPS_Lat)
            gps_Longi = "-".join(data_GPS_Longi)
            
            #_20190322_075014
            # add to csv line
            tmp_Line.append("\t")
            
            tmp_Line.append("%s %s" % (gps_Lat, gps_Longi))
    
        #/if not data_GPS == False


        
#         # tuple --> to list
#         data_GPS_Lat = [str(x) for x in data_GPS[0]]  # N,S
#         data_GPS_Longi = [str(x) for x in data_GPS[1]] # E,W
# #         data_GPS_Lat = [x for x in data_GPS[0]]  # N,S
# #         data_GPS_Longi = [x for x in data_GPS[1]] # E,W
#         
#         # build text
#         gps_Lat = "-".join(data_GPS_Lat)
#         gps_Longi = "-".join(data_GPS_Longi)
#         
#         # add to csv line
#         tmp_Line.append("%s %s" % (gps_Lat, gps_Longi))
#         tmp_Line.append("\t%s %s" % (gps_Lat, gps_Longi))
#         lines.append("\t%s %s" % (gps_Lat, gps_Longi))
        
        '''###################
            append
        ###################'''
        lines.append("\t".join(tmp_Line))
        
        # count
        cnt += 1
        
    '''###################
        write        
    ###################'''
    fpath_CSV = "%s/%s" % (dpath_CSV, fname_CSV)
    
    fin = codecs.open(fpath_CSV, "w", 'utf-8')
    
    # write
    for item in lines:
    
        fin.write(item)
        fin.write("\n")
        
    #/for item in lines:

    # close
    fin.close()

    #debug
    print()
    print("[%s:%d] csv written : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , fpath_CSV
                    ), file=sys.stderr)
    
#/ def gen_Cake_CSV__Gen_CSVFile(dpath_CSV, fname_CSV, lo_ColorName_Set__Modified_2):

def gen_Cake_CSV__Exec(request):
    
    '''###################
        vars        
    ###################'''
    dic = {}

    '''###################
        get : params
    ###################'''
    dpath_Images, flg_SaveImage, param_Corner_Width, param_Corner_Padding \
            = gen_Cake_CSV__Get_Params(request)
    
    #debug
    print()
    print("[%s:%d] flg_SaveImage => %s" % \
    (os.path.basename(libs.thisfile()), libs.linenum()
    , flg_SaveImage
#     , flg_SaveImage
    ), file=sys.stderr)

    '''###################
        set : vars
    ###################'''
    dic['dpath_Images'] = dpath_Images
    
    '''###################
        get : files list
    ###################'''
    lo_Files = gen_Cake_CSV__Get_ListOf_Files(dpath_Images)
    
#     print()
#     print("[%s:%d] lo_Files[0] => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , lo_Files[0]
#         ), file=sys.stderr)
    
    
    print()
    print("[%s:%d] dpath_Images => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Images
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] len(lo_Files) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files)
            ), file=sys.stderr)

    '''###################
        get : color name set
        
        [
            [
                "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\images",
                [
                    [
                        "2018-08-21_23-28-01_000.1.mov",
                        "others"
                    ],
                    [
                        "2018-08-21_23-28-01_000.2.mov",
                        "others"
                    ],
                    ...
                ],
                ...
            ],
            ...
        ]
    ###################'''
#     lo_ColorName_Set = gen_Cake_CSV__Get_ColorName_Set(dpath_Images, lo_Files)
    lo_ColorName_Set = gen_Cake_CSV__Get_ColorName_Set(\
                       dpath_Images
                       , lo_Files
                       , flg_SaveImage
                       , param_Corner_Width
                       , param_Corner_Padding)
    
    '''###################
        get : list of color names
    ###################'''
    lo_ColorName_Set__Modified = []
    
    for item in lo_ColorName_Set:

        fname = os.path.basename(item[0])
        
        colorName_Set = []
        
        for item2 in item[1]:
            
            colorName_Set.append(item2[1])
        
        # append
        lo_ColorName_Set__Modified.append([fname, colorName_Set])
        
    
    msg = "lo_ColorName_Set__Modified =>"
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
#    libs.write_Log(msg_Log, True)
    
    # counter
    cntOf_Write_FileData = 1
    
    for item in lo_ColorName_Set__Modified:

        fname = item[0]
        
        color_Names = item[1]
        
        strOf_Fname_Block = "%d)\t%s => \t" % (cntOf_Write_FileData, fname)
        
        # increment
        cntOf_Write_FileData += 1
        
        # file name
        libs.write_Log(strOf_Fname_Block, False)
#         libs.write_Log(fname, False)
#         libs.write_Log(" => ", False)
        
        # color names
        strOf_Color_Names = ""
        
        for item2 in color_Names:
        
            strOf_Color_Names += item2 + " "
            
        #/for iteim2 in color_Names:
        
        libs.write_Log(strOf_Color_Names, True)
        
    #/for item in lo_ColorName_Set__Modified:

    '''###################
        get : picture genre
    ###################'''
    lo_ColorName_Set__Modified_2 = []
    
    for item in lo_ColorName_Set__Modified:
        
        fname = item[0]
        
        color_Names = item[1]
        
        color_Names_New = []
        
        for item2 in color_Names:
        
            if item2 == "other" : colName = "o"
            
            elif item2 == "red" : colName = "r"
            elif item2 == "yellow" : colName = "y"
            elif item2 == "green" : colName = "g"
            
            elif item2 == "blue" : colName = "b"
            
            elif item2 == "white" : colName = "w"
            elif item2 == "black" : colName = "a"
            
            elif item2 == "pink" : colName = "p"
            
            else : colName = "u" #=> 'unknown'
            
            color_Names_New.append(colName)
            
        #/for item2 in color_Names:
        
        # modify
        color_Names_New.sort()
        
        strOf_Color_Names_New = "".join(color_Names_New)
        
        # append
        lo_ColorName_Set__Modified_2.append([fname, strOf_Color_Names_New])
         
     #/for item in lo_ColorName_Set__Modified:

    '''###################
        write : log : lo_ColorName_Set__Modified_2
    ###################'''
    msg = "lo_ColorName_Set__Modified_2 =>"
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    
    # counter
    cntOf_Write_FileData = 1
    
    for item in lo_ColorName_Set__Modified_2:

        fname = item[0]
        
        color_Names = item[1]
        
        strOf_Fname_Block = "%d)\t%s => \t" % (cntOf_Write_FileData, fname)
        
        # increment
        cntOf_Write_FileData += 1
        
        # file name
        libs.write_Log(strOf_Fname_Block, False)
        
        # color names
        strOf_Color_Names = ""
        
        for item2 in color_Names:
        
            strOf_Color_Names += item2 + " "
            
        #/for iteim2 in color_Names:
        
        libs.write_Log(strOf_Color_Names, True)
    
    '''###################
        gen : CSV file
    ###################'''
    #_20190322_074746
    dpath_CSV = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\csv"
    fname_CSV = "entries.%s.csv" % (libs.get_TimeLabel_Now())
    
    res = gen_Cake_CSV__Gen_CSVFile(
                dpath_CSV, fname_CSV
                , lo_ColorName_Set__Modified_2
                , dpath_Images)
        
    '''###################
        return        
    ###################'''
    return dic, lo_ColorName_Set__Modified_2

#/ def gen_Cake_CSV(request):
    
def gen_Cake_CSV(request):
    
    '''###################
        set : log file name
    ###################'''
#     tlabel = libs.get_TimeLabel_Now()
#     fname_Log = "get_4_corners.%s.log" % (tlabel)
# 
#     cons_ip.FilePaths.fname_LogFile.value = fname_Log
    
    '''###################
        title
    ###################'''
    msg = "gen_Cake_CSV(request) ==> starting... ======================="
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)

    '''###################
        get : dic, color name set        
    ###################'''
    dic, lo_ColorName_Set__Modified_2 = gen_Cake_CSV__Exec(request)
    
    '''###################
        ending message
    ###################'''
    msg = "gen_Cake_CSV(request) ==> ending... =======================//"
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, True)
    libs.write_Log("", True)

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8001/ip/get_4_corners/"
#     referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/gen_cake_csv.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/gen_cake_csv_full.html', dic)
    
#/ def gen_Cake_CSV(request):
    
def exec_get_4_corners(request):
    
    '''###################
        debug        
    ###################'''
    msg = "exec_get_4_corners(request) ================================"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    dpath_Log = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\logs"
    
    fname_Log = "get_4_corners.log"

    libs.write_Log(msg_Log, True)
    
    '''###################
        debug
        
        http://127.0.0.1:8001/ip/exec_get_4_corners?dpath_images=C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\images&fname_image=IMG_3154.PNG
        
    ###################'''
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    '''###################
        get : params
    ###################'''
    dpath_Images = request.GET.get('dpath_images', False)
    
    fname_Image = request.GET.get('fname_image', False)
    
    '''###################
        get : params : save image
    ###################'''
    # ref : function exec_Get_4Corners(fname) :: main.js
    flg_save_image = request.GET.get('flg_save_image', False)
    
    # set flag
    flg_SaveImage = False
    
    if flg_save_image == "true" : #if flg_save_image

        flg_SaveImage = True
        
    #/if flg_save_image
    
    #debug
    print()
    print("[%s:%d] flg_SaveImage => %s" % \
    (os.path.basename(libs.thisfile()), libs.linenum()
    , flg_SaveImage
    ), file=sys.stderr)


    '''###################
        get : params : corner_width
    ###################'''
    # ref : function exec_Get_4Corners(fname) :: main.js
    param_Corner_Width = request.GET.get('corner_width', False)
    
    #debug
    print()
    print("[%s:%d] param_Corner_Width => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , int(param_Corner_Width)
        ), file=sys.stderr)
    
    # convert
    param_Corner_Width = int(param_Corner_Width)
    
    '''###################
        get : params : corner_Padding
    ###################'''
    # ref : function exec_Get_4Corners(fname) :: main.js
    param_Corner_Padding = request.GET.get('corner_Padding', False)
    
    #debug
    print()
    print("[%s:%d] param_Corner_Padding => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , int(param_Corner_Padding)
        ), file=sys.stderr)
    
    # convert
    param_Corner_Padding = int(param_Corner_Padding)
    
    '''###################
        judge        
    ###################'''
    res, msg, (height, width, channels) = \
                lib_ip.is_PhotoOf__Sweets(
                        dpath_Images
                        , fname_Image
                        , flg_SaveImage
                        , param_Corner_Width
                        , param_Corner_Padding
                        )

    '''###################
        set : vars
    ###################'''
    dic['dpath_Images'] = dpath_Images
    dic['fname_Image'] = fname_Image
    
    dic['height'] = height
    dic['width'] = width
    dic['channels'] = channels
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8001/ip/get_4_corners/"
#     referer_MM = "http://127.0.0.1:8000/ip/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/exec_get_4_corners.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'ip/exec_get_4_corners_full.html', dic)

#/ def exec_get_4_corners(request):
#     return render(request, 'ip/basics.html', dic)

#/ def basics(request):

def open_image_dir(request):
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    print()
    print("[%s:%d] opening image dir..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

    '''###################
        build : command string        
    ###################'''
    command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\utils\\open_image_dir.bat"
#     command = "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\utils\open_image_dir.bat"
#     command = "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\images"
#     command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\images"
#     command = "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\images"
#     command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)

#     print()
#     print("[%s:%d] _im_actions__Ops_13()" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)

    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    print()
    print("[%s:%d] command => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , command
            ), file=sys.stderr)

    '''###################
        subprocess        
    ###################'''
    #ref https://stackoverflow.com/questions/13525882/tasklist-output answered Nov 23 '12 at 9:36
    res = subprocess.call(cmd_Full)
#     res = subprocess.check_output(cmd_Full)



    return render(request, 'ip/open_image_dir.html', dic)

    
#/ def open_image_dir(request):

def open_dir(request):
    
    '''###################
        params
    ###################'''
    param = request.GET.get('param', False)
    
    print("[%s:%d] param => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , param
        ), file=sys.stderr)
    
    '''###################
        vars        
    ###################'''
    dic = {}
    
    print()
    print("[%s:%d] opening dir..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

    '''###################
        build : command string        
    ###################'''
    command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\utils\\open_anims_log_dir.bat"

    cmd_Full = [command]  #=> 

    print()
    print("[%s:%d] command => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , command
            ), file=sys.stderr)

    '''###################
        subprocess        
    ###################'''
    #ref https://stackoverflow.com/questions/13525882/tasklist-output answered Nov 23 '12 at 9:36
    res = subprocess.call(cmd_Full)
#     res = subprocess.check_output(cmd_Full)

    '''###################
        render
    ###################'''
    return render(request, 'ip/anims/plain_anims.html', dic)
    
#/ def open_image_dir(request):

def prep_gen_Cake_CSV(request):
    
    '''###################
        vars        
    ###################'''
    dic = {}

    '''###################
        ops
    ###################'''
    '''###################
        ops : delete image files
    ###################'''
    '''###################
        get : files list
    ###################'''
    dpath_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6" \
                + "\\46_art\\VIRTUAL\\Admin_Projects" \
                + "\\ip" \
                + "\\images"
    
    fpath_Glob = "%s\\*" % (dpath_Images)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    # files only
    lo_Files_Filtered = []
    
    for item in lo_Files:

#         if os.path.isfile(dpath_Images + "\\" + item) == True : 
        if os.path.isfile(item) == True : 
            lo_Files_Filtered.append(item)
        
    #/for item in lo_Files:

    # update the list
    lo_Files = lo_Files_Filtered
    
    lo_Files.sort()
    
#     #debug
#     print("[%s:%d] lo_Files =>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         ), file=sys.stderr)
#     print(lo_Files)

    '''###################
        move files
    ###################'''
    dpath_Dest = "%s\\storage_images" % dpath_Images
    
    # counter
    cntOf_Move = 0
    
    for item in lo_Files:
        
        # file name
        fname = os.path.basename(item)
        
        fpath_Src = "%s\\%s" % (dpath_Images, fname)
        fpath_Dst = "%s\\%s" % (dpath_Dest, fname)
        
        #ref https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python answered Jan 13 '12 at 22:19
        shutil.move(fpath_Src, fpath_Dst)
        
        # count
        cntOf_Move += 1
        
    #/for item in lo_Files:
    
    #debug
    print("[%s:%d] cntOf_Move => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , cntOf_Move
            ), file=sys.stderr)

    '''###################
        copy
    ###################'''
    '''###################
        get : files list
    ###################'''
    dpath_Images_Copy_Src = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\iphone"
    
    fpath_Glob = "%s\\*" % (dpath_Images_Copy_Src)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    # files only
    lo_Files_Filtered = []
    
    for item in lo_Files:

#         if os.path.isfile(dpath_Images + "\\" + item) == True : 
        if os.path.isfile(item) == True : 
            lo_Files_Filtered.append(item)
        
    #/for item in lo_Files:

    # update the list
    lo_Files = lo_Files_Filtered
    
    lo_Files.sort()
    
    '''###################
        copy files
    ###################'''
#     dpath_Dest = "%s\\storage_images" % dpath_Images
#     aa
    # counter
    cntOf_Copy = 0
    
    for item in lo_Files:
        
        # file name
        fname = os.path.basename(item)
        
        fpath_Src = "%s\\%s" % (dpath_Images_Copy_Src, fname)
        fpath_Dst = "%s\\%s" % (dpath_Images, fname)
#         fpath_Dst = "%s\\%s" % (dpath_Dest, fname)
        
        #ref https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python answered Jan 13 '12 at 22:19
        shutil.copy(fpath_Src, fpath_Dst)
        #shutil.copyfile(fpath_Src, fpath_Dst)
#         shutil.move(fpath_Src, fpath_Dst)
        
        # count
        cntOf_Copy += 1
        
    #/for item in lo_Files:
    
    #debug
    print("[%s:%d] cntOf_Copy => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , cntOf_Copy
            ), file=sys.stderr)
    
    '''###################
        render
    ###################'''
    return render(request, 'ip/prep_gen_Cake_CSV.html', dic)

    
#/ def prep_gen_Cake_CSV(request):

def dos_attack(request): 
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        ops        
    ###################'''
    numOf_DosAttack = cons_ip.DfltVals.numOf_DosAttack.value
    
    numOf_DosAttack += 1
    
    dic['time_label'] = libs.get_TimeLabel_Now()
#     dic['numOf_DosAttack'] = numOf_DosAttack
    
    '''###################
        template        
    ###################'''
    return render(request, 'ip/dos_attack.html', dic)
    
#/ def dos_attack(request): 
