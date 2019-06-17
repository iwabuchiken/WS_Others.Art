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

#     return render(request, 'ip/index2.html', dic)
#     return render(request, 'ip/index.html', dic)
    return render(request, 'anims/index.html', dic)

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

    return render(request, 'anims/test.html', dic)

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

def test_OpenCV__NewImage():

    '''###################
        prep        
    ###################'''
    dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\data\\data_images"
#     dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
    
    fname_Image_File = "leaf-2.1.png"   # orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\4_animations\1_\5_\images
    
    fpath_Image_File = os.path.join(dpath_Image_File, fname_Image_File)
    
    print("[%s:%d] fpath_Image_File = %s (exists = %s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image_File, os.path.isfile(fpath_Image_File)
        ), file=sys.stderr)

    '''###################
        prep : image
    ###################'''
    #ref http://peaceandhilightandpython.hatenablog.com/entry/2016/01/09/214333
    #ref alpha channel http://opencv.blog.jp/python/alpha_channel
    img = cv2.imread(fpath_Image_File, cv2.IMREAD_UNCHANGED)
    
    print("[%s:%d] img.shape =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(img.shape)
    print()
    
    '''###################
        ops
    ###################'''
    tokens = fname_Image_File.split(".")
    (h, w) = img.shape[:2]
     
    tlabel = libs.get_TimeLabel_Now()

    fname_Dst = "%s.%s.(test_OpenCV__NewImage).%s.%s" \
        % (tokens[0], tokens[1], tlabel, tokens[2])
        
    fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
    
    print("[%s:%d] fname_Dst => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Dst
        ), file=sys.stderr)
    
    '''###################
        image : blank        
    ###################'''
    # blank image
    #ref https://stackoverflow.com/questions/12881926/create-a-new-rgb-opencv-image-using-python
    blank_image = np.zeros((img.shape[0], img.shape[1], 4), np.uint8)
    
    print("[%s:%d] blank_image.shape =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(blank_image.shape)
    
    # shape
    (h2, w2) = blank_image.shape[:2]
    
    # coloring
    # BGRA : A --> 0 for transpanrent
#     blank_image[:, 0 : int(0.5*w2)] = (255, 0, 0, 255)
#     blank_image[:, 0 : int(0.5*w2)] = (100, 100, 100, 200)
#     blank_image[:, 0 : int(0.5*w2)] = (100, 100, 100, 100)
#     blank_image[:, 0 : int(0.5*w2)] = (255,0,0, 0)
#     blank_image[:,0:0.5*w2] = (255,0,0, 0)
#     blank_image[:,0:0.5*width] = (255,0,0, 0)
#     blank_image[:, :] = (255, 0, 0, 0)
#     blank_image[:, :] = (255, 0, 0)

    # copy a partial image of img to blank_image
    cut_height = 120
    cut_width = 120
    
    blank_image[100 : 100 + cut_height, 250 : 250 + cut_width] \
            = img[150:270, 300:420]
#     blank_image[150:270, 300:420] = img[150:270, 300:420]
    
    
    #write
    cv2.imwrite(fpath_Dst, blank_image)
#     cv2.imwrite(fpath_Dst, mask)
    
#     #ref https://stackoverflow.com/questions/48384516/python-opencv-cropping-images-and-isolating-specific-objects
#     mask = np.zeros(img.shape[:2],np.uint8)
#     
#     print()
#     print("[%s:%d] mask[0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(mask[0])
#                 ), file=sys.stderr)
#     print(mask[0])
#     
#     print()
#     print("[%s:%d] img[0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(img[0])
#                 ), file=sys.stderr)
#     print(img[0])
#     
#     print()
#     print("[%s:%d] img[0][0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(img[0][0])
#                 ), file=sys.stderr)
#     print(img[0][0])
    
#     print()
#     print("[%s:%d] mask[0][0] => (len = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(mask[0][0])
#                 ), file=sys.stderr)
#     print(mask[0][0])
    
#     print("[%s:%d] mask.shape[0] = %d, mask.shape[1] = %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , mask.shape[0], mask.shape[1]
#                 ), file=sys.stderr)
#     
#     for i in range(0, mask.shape[0]):   # height
#         for j in range(0, mask.shape[1]):   # width
#          
#             mask[i][j][0] = 255
#             mask[i][j][1] = 0
#             mask[i][j][2] = 0
#              
#         #/for i in range(0, mask.shape[0]:
# 
#     #write
#     cv2.imwrite(fpath_Dst, mask)


#/ def test_OpenCV__NewImage():
    
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
        prep : params
            main.js :: _anims_Action_LinkTo__1(_param)
            , option_tick_move_X : _option_tick_move_X
            , option_tick_move_Y : _option_tick_move_Y
            
            , opt_rotate_Start : _opt_rotate_Start
            , opt_rotate_End : _opt_rotate_End

    ###################'''
    param_Loc_Start_X = request.GET.get('option_loc_start_X', False)
    param_Loc_Start_Y = request.GET.get('option_loc_start_Y', False)
    
    param_Source_Dir = request.GET.get('opt_source_Dir', False)
    param_Source_File = request.GET.get('opt_source_File', False)
    
    param_Cut_Width = request.GET.get('opt_cut_width', False)
    param_Cut_Height = request.GET.get('opt_cut_height', False)
    
    param_Rotate_Start = request.GET.get('opt_rotate_Start', False)
    param_Rotate_End = request.GET.get('opt_rotate_End', False)
    param_Rotate_Tick = request.GET.get('opt_rotate_Tick', False)
    
    print("[%s:%d] param_Rotate_Tick => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , param_Rotate_Tick
        ), file=sys.stderr)
    # modify
    # ref tertiary https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
    param_Loc_Start_X = 0 if (param_Loc_Start_X == False) else int(param_Loc_Start_X)
    param_Loc_Start_Y = 0 if (param_Loc_Start_Y == False) else int(param_Loc_Start_Y)
    
    param_Cut_Width = 100 if (param_Cut_Width == False) else int(param_Cut_Width)
    param_Cut_Height = 100 if (param_Cut_Height == False) else int(param_Cut_Height)
    
    param_Rotate_Start = 0 if (param_Rotate_Start == False) else int(param_Rotate_Start)
    param_Rotate_End = 45 if (param_Rotate_End == False) else int(param_Rotate_End)
    param_Rotate_Tick = 5 if (param_Rotate_Tick == False) else int(param_Rotate_Tick)
    
    param_Source_Dir = cons_ip.FilePaths.dpath_Anims_Image_Files.value \
                    if (param_Source_Dir == False) else param_Source_Dir
    
    param_Source_File = cons_ip.FilePaths.fname_Anims_Image_Files.value \
                    if (param_Source_File == False) else param_Source_File
    

    print("[%s:%d] param_Source_Dir = %s\nparam_Source_File = %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param_Source_Dir, param_Source_File
            ), file=sys.stderr)
    
    print("[%s:%d] param_Cut_Width = %d, param_Cut_Height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param_Cut_Width, param_Cut_Height
            ), file=sys.stderr)
    
#     print("[%s:%d] param_Loc_Start_X = %d, param_Loc_Start_Y = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , param_Loc_Start_X, param_Loc_Start_Y
#         ), file=sys.stderr)

    '''###################
        prep        
    ###################'''
    dpath_Image_File = param_Source_Dir
#     dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\data\\data_images"
#     dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
    
    fname_Image_File = param_Source_File
#     fname_Image_File = "leaf-2.1.png"   # orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\4_animations\1_\5_\images
    
    fpath_Image_File = os.path.join(dpath_Image_File, fname_Image_File)
    
    print("[%s:%d] fpath_Image_File = %s (exists = %s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image_File, os.path.isfile(fpath_Image_File)
        ), file=sys.stderr)

    
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
    
    tokens_2 = os.path.splitext(fname_Image_File)
    
    tlabel = libs.get_TimeLabel_Now()

    # paths
    dir_Tmp = tlabel
    
    dpath_Tmp = os.path.join(dpath_Image_File, dir_Tmp)
    
    #ref mkdir https://www.tutorialspoint.com/python/os_mkdir.htm
    if not os.path.isdir(dpath_Tmp) :
        os.mkdir(dpath_Tmp)

    #ref step https://www.pythoncentral.io/pythons-range-function-explained/
#     for i in range(param_Rotate_Start, param_Rotate_End):
    for i in range(param_Rotate_Start, param_Rotate_End, param_Rotate_Tick):
#     for i in range(0, 10):
#     for i in range(0, 5):
         
#         angle = i * 5
        angle = i
        scale = 1.0
         
        #ref radians https://docs.scipy.org/doc/numpy/reference/generated/numpy.radians.html
        span = int((370 - w / 2) * np.sin(np.radians(angle)))
        span_w = int((370 - w / 2) * np.cos(np.radians(angle)))
         
        center = (w / 2 + span_w, h / 2 + span)
#         center = (w / 2, h / 2 + span)
#         center = (w / 2, h / 2 - span)
#         (h, w) = img.shape[:2]
#         center = (w / 2, h / 2)
        
        
#         # paths
#         dir_Tmp = tlabel
#         
#         dpath_Tmp = os.path.join(dpath_Image_File, dir_Tmp)
#         
#         #ref mkdir https://www.tutorialspoint.com/python/os_mkdir.htm
#         if not os.path.isdir(dpath_Tmp) :
#             os.mkdir(dpath_Tmp)
#         
        fname_Dst = "%s.(rotate=%d).%s.(center=%d,%d).%s" \
                % (tokens_2[0], angle, tlabel, center[0], center[1], tokens_2[1])
#         fname_Dst = "%s.%s.(rotate=%d).%s.(center=%d,%d).%s" \
#                 % (tokens[0], tokens[1], angle, tlabel, center[0], center[1], tokens[2])
#                 % (tokens[0], tokens[1], angle, tlabel, tokens[2])
#                 % (tokens[0], tokens[1], angle, libs.get_TimeLabel_Now(), tokens[2])
          
        fpath_Dst = os.path.join(dpath_Image_File, dir_Tmp, fname_Dst)
#         fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
         
        _anims_JS__1_Move_Leaves__Test_1_Resize__exec(angle, scale, img, center, fpath_Dst)
    
    '''###################
        return        
    ###################'''
    status = 1
    
    msg = "file created at : %s" % dpath_Tmp
    
    return (status, msg)
         
         
    #/for i in range(0, 10):

#     '''###################
#         move image        
#     ###################'''
#     #ref https://stackoverflow.com/questions/23464495/fastest-way-to-move-image-in-opencv
#     fname_Dst = "%s.%s.(moved).%s.%s" \
#         % (tokens[0], tokens[1], tlabel, tokens[2])
#         
#     fpath_Dst = os.path.join(dpath_Image_File, fname_Dst)
#     
#     print("[%s:%d] fname_Dst => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , fname_Dst
#         ), file=sys.stderr)
#     
#     img_Partial = img[
#                 param_Loc_Start_Y : param_Loc_Start_Y + param_Cut_Height
#                 , param_Loc_Start_X : param_Loc_Start_X + param_Cut_Width
#                 
#                 ]  # h, w
# #     img_Partial = img[param_Loc_Start_Y : 270, param_Loc_Start_X : 420]  # h, w
# #     img_Partial = img[150 : 270, 300 : 420]  # h, w
# #     img_Partial = img[0 : 100, 0 : 50]  # h, w
# #     img_Partial = img[cv2.Rect(0, 0, 100, 100)]
# #     img_Partial = img(cv2.Rect(0, 0, 100, 100))
#     
#     cv2.imwrite(fpath_Dst, img_Partial)
# #     cv2.imwrite(fname_Dst, img_Partial)
    
    
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
        tests
    ###################'''
#     test_OpenCV__NewImage()
    
    '''###################
        ops
    ###################'''
    (status, msg) = _anims_JS__1_Move_Leaves__Test_1_Resize(request)
#     _anims_JS__1_Move_Leaves__Test_1_Resize(request)
    
    '''###################
        return        
    ###################'''
#     status = 1
#     
#     msg = "OK"
    
    return (status, msg)
    
#/ def _anims_JS__1_Move_Leaves(request):
    
def _anims_JS__2_Move_Leaves__V2(request):
    
    '''###################
        tests
    ###################'''
#     test_OpenCV__NewImage()
    
    '''###################
        ops
    ###################'''
#     (status, msg) = _anims_JS__1_Move_Leaves__Test_1_Resize(request)
#     _anims_JS__1_Move_Leaves__Test_1_Resize(request)
    
    '''###################
        return        
    ###################'''
    status = 1
     
    msg = "_anims_JS__2_Move_Leaves__V2"
    
    return (status, msg)
    
#/ def _anims_JS__2_Move_Leaves__V2(request):
    
def _anims_JS__3_Clusters__Clusters(request, cv_Img, fpath_Dst__Sub):
    
    img_Tmp = cv_Img
#     img_Tmp = copy.deepcopy(cv_Img)
    
    a = 200
#     a = 100
#     a = 50
#     a = 20
    
    '''###################
        processing        
    ###################'''
    print("[%s:%d] cv_Img[0][0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    cntOf_Row = 0
    cntOf_Pixels = 0
    
    flg_Break = False
    
    print("[%s:%d] message" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cv_Img[0][0])
    
#     for row in cv_Img:
    for row in img_Tmp:
         
        for col in row:
            
#             print("[%s:%d] col[0] = %d, col[1] = %d, col[2] = %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , col[0], col[1], col[2]
#                 ), file=sys.stderr)
            
#             col[0] = 255 - col[0]
#             col[1] = 255 - col[1]
#             col[2] = 255 - col[2]
            col[0] = int(col[0] / a) * a
            col[1] = int(col[1] / a) * a
            col[2] = int(col[2] / a) * a
#             col[0] = 50
#             col[1] = 50
#             col[2] = 50

#             print("[%s:%d] (processed) col[0] = %d, col[1] = %d, col[2] = %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , col[0], col[1], col[2]
#                 ), file=sys.stderr)
         
#             # count
#             cntOf_Pixels += 1
#             
#             print("[%s:%d] cntOf_Pixels => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , cntOf_Pixels
#                 ), file=sys.stderr)
#             
#             
#             if cntOf_Pixels > 10 : #if cntOf_Pixels > 10
#                 
#                 flg_Break = True
#                 
#                 break
                
             #/if cntOf_Pixels > 10
            
            
         
        #/for col in row:
        
#         # debug
#         if flg_Break == True : #if flg_Break == True
#         
#             break
#             
#         #/if flg_Break == True
#         
#         # count
#         cntOf_Row += 1
#          
#         if cntOf_Row % 100 == 0 : #if cntOf_Row % 100 == 0
#          
#             print("[%s:%d] cntOf_Row => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , cntOf_Row
#                 ), file=sys.stderr)
#              
#         #/if cntOf_Row % 100 == 0
         
 
 
    print("[%s:%d] processing --> done" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 
                ), file=sys.stderr)

    '''###################
        save : image
    ###################'''
    res = cv2.imwrite(fpath_Dst__Sub, img_Tmp)
    
    print("[%s:%d] save image => %s (%s)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , res, fpath_Dst__Sub
            ), file=sys.stderr)
    
    #/for row in cv_Img:

    
#     print("[%s:%d] cv_Img[0][0] =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#     
#     print(cv_Img[0][0])
# 
# #     print("[%s:%d] cv_Img[0][0][0] =>" % \
# #                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                 
# #                 ), file=sys.stderr)
# #     
# #     print(cv_Img[0][0][0])
#     
#     R_New = int(cv_Img[0][0][0] / a) * a
#     G_New = int(cv_Img[0][0][1] / a) * a
#     B_New = int(cv_Img[0][0][2] / a) * a
# #     R_New = (cv_Img[0][0][0] % a) * a
# #     G_New = (cv_Img[0][0][1] % a) * a
# #     B_New = (cv_Img[0][0][2] % a) * a
#     
#     print("[%s:%d] R_New = %d, G_New = %d, B_New = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , R_New, G_New, B_New
#         ), file=sys.stderr)
#     
#     cv_Img[0][0][0] = R_New
#     cv_Img[0][0][1] = G_New
#     cv_Img[0][0][2] = B_New
#     
#     print("[%s:%d] cv_Img[0][0](processed) =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#     
#     print(cv_Img[0][0])
    
#/ def _anims_JS__3_Clusters__Clusters(request):
    
def _anims_JS__3_Clusters(request):
    
    '''###################
        tests
    ###################'''
#     test_OpenCV__NewImage()
    
    '''###################
        ops
    ###################'''
    '''###################
        prep        
    ###################'''
#     dpath_Image_File = param_Source_Dir
    dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\data\\data_images"
#     dpath_Image_File = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\data_images"
    
#     fname_Image_File = param_Source_File
#     fname_Image_File = "leaf-2.1.png"   # orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\4_animations\1_\5_\images
#     fname_Image_File = "2018-10-25_05-27-52_000.jpg"   # orig : 
    fname_Image_File = "2018-10-25_05-27-52_000.(404x303).jpg"   # orig : 
    
    fpath_Image_File = os.path.join(dpath_Image_File, fname_Image_File)
    
    print("[%s:%d] fpath_Image_File = %s (exists = %s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Image_File, os.path.isfile(fpath_Image_File)
        ), file=sys.stderr)

            # [views.py:608] fpath_Image_File = C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRT
            # UAL\Admin_Projects\anims\data\data_images\2018-10-25_05-27-52_000.jpg (exists =
            # True)

    '''###################
        img : read
    ###################'''
    #ref http://peaceandhilightandpython.hatenablog.com/entry/2016/01/09/214333
    #ref alpha channel http://opencv.blog.jp/python/alpha_channel
    img = cv2.imread(fpath_Image_File, cv2.IMREAD_UNCHANGED)
    
    img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img_HSV_BGR = cv2.cvtColor(img_HSV, cv2.COLOR_RGB2BGR)

#aa
    '''###################
        subimage
    ###################'''
    orgHeight, orgWidth = img.shape[:2]
#     param_Start_X = 2437
#     param_Start_Y = 217
#     
#     param_End_X = 2537
#     param_End_Y = 317
#     param_Start_X = 237
#     param_Start_Y = 150
#     
#     param_End_X = 257
#     param_End_Y = 160
    param_Start_X = 0
    param_Start_Y = 0
    
    param_End_X = orgWidth - 1
    param_End_Y = orgHeight - 1
    
    #ref lib_ip :: get_Corner_Images
    img_Sub = img[
                    param_Start_Y : param_End_Y
                    , param_Start_X : param_End_X
                  ]
#     img_Sub = img[(height - corner_Length) : height - padding, \
#                     0 + padding : corner_Length], # clp_LB
    
    '''###################
        paths
    ###################'''
    tokens = fname_Image_File.split(".")
    (h, w) = img.shape[:2]
    
    tokens_2 = os.path.splitext(fname_Image_File)
    
    tlabel = libs.get_TimeLabel_Now()

    # paths
    dir_Tmp = tlabel
    
    dpath_Tmp = os.path.join(dpath_Image_File, dir_Tmp)
    
    #ref mkdir https://www.tutorialspoint.com/python/os_mkdir.htm
    if not os.path.isdir(dpath_Tmp) :
        os.mkdir(dpath_Tmp)
        
        print("[%s:%d] dir => created : '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Tmp
        ), file=sys.stderr)

    else :

        print("[%s:%d] dir => exists : '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Tmp
        ), file=sys.stderr)
        

    '''###################
        TEST : copy image to the new dir
    ###################'''
#     fname_Dst = "%s.(rotate=%d).%s.(center=%d,%d).%s" \
#     fname_Dst = "%s.(%s).%s" \
    fname_Dst_Orig = "%s.(orig).(%s)%s" \
            % (tokens_2[0], tlabel, tokens_2[1])
    fname_Dst_BGR = "%s.(BGR).(%s)%s" \
            % (tokens_2[0], tlabel, tokens_2[1])
    fname_Dst_HSV = "%s.(HSV).(%s)%s" \
            % (tokens_2[0], tlabel, tokens_2[1])
    fname_Dst_HSV_BGR = "%s.(HSV_BGR).(%s)%s" \
            % (tokens_2[0], tlabel, tokens_2[1])
            
    fname_Dst_Sub = "%s.(sub.%d,%d-%d,%d).(%s)%s" \
            % (tokens_2[0]
               , param_Start_X, param_Start_Y
               , param_End_X, param_End_Y
               , tlabel, tokens_2[1])
      
    fpath_Dst__Orig = os.path.join(dpath_Image_File, dir_Tmp, fname_Dst_Orig)
    fpath_Dst__BGR = os.path.join(dpath_Image_File, dir_Tmp, fname_Dst_BGR)
    fpath_Dst__HSV = os.path.join(dpath_Image_File, dir_Tmp, fname_Dst_HSV)
    fpath_Dst__HSV_BGR = os.path.join(dpath_Image_File, dir_Tmp, fname_Dst_HSV_BGR)
    fpath_Dst__Sub = os.path.join(dpath_Image_File, dir_Tmp, fname_Dst_Sub)
    
    
# #     res = cv2.imwrite(fpath_Dst, img_BGR)        
#     res = cv2.imwrite(fpath_Dst__Orig, img)
#     res = cv2.imwrite(fpath_Dst__BGR, img_BGR)        
#     res = cv2.imwrite(fpath_Dst__HSV, img_HSV)        
#     res = cv2.imwrite(fpath_Dst__HSV_BGR, img_HSV_BGR)        
#     res = cv2.imwrite(fpath_Dst__Sub, img_Sub)        
# #     res = cv2.imwrite(fpath_Dst, img)        
# #     cv2.imwrite(fpath_Dst, rotated)        
# 
#     print("[%s:%d] cv2.imwrite => '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , res
#             ), file=sys.stderr)

    '''###################
        clusters
    ###################'''
    _anims_JS__3_Clusters__Clusters(request, img_Sub, fpath_Dst__Sub)
#     _anims_JS__3_Clusters__Clusters(request, img, fpath_Dst__Sub)
#     _anims_JS__3_Clusters__Clusters(request, img_Sub, fpath_Dst__Sub)
    #aa
    
    '''###################
        return        
    ###################'''
    status = 1
     
    msg = "_anims_JS__3_Clusters"
    
    print("[%s:%d] msg => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            ), file=sys.stderr)
    
    return (status, msg)
    
#/ def _anims_JS__3_Clusters(request):
    
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
    
    render_Page = 'anims/anims/plain_anims.html'
    
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

    elif param == cons_ip.Anims_Params.PARAM__2_MOVE_LEAVES__V2.value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM__1_MOVE_LEAVES__V2        
        ###################'''
        # call func
#         (status, msg) = (1, "PARAM__2_MOVE_LEAVES__V2")
        (status, msg) = _anims_JS__2_Move_Leaves__V2(request)
        
        dic['message'] += "move leaves"
        
        dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)
        
    elif param == cons_ip.Anims_Params.PARAM__3_CLUSTERS.value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM__3_CLUSTERS        
        ###################'''
        # call func
#         (status, msg) = (1, "PARAM__2_MOVE_LEAVES__V2")
        (status, msg) = _anims_JS__3_Clusters(request)
#         (status, msg) = _anims_JS__2_Move_Leaves__V2(request)
        
        dic['message'] += "clusters"
        
        dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)
        
    else :
        (status, msg) = (1, "unknown param : '%s'" % param)

        dic['message'] += "unknown param"
        
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
    
        return render(request, 'anims/anims/anims.html', dic)
#         return render(request, 'ip/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'anims/anims/anims_full.html', dic)
#         return render(request, 'ip/basics_full.html', dic)
#/ def basics(request):

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
    command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\anims\\utils\\open_anims_log_dir.bat"
#     command = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\utils\\open_anims_log_dir.bat"

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
    return render(request, 'anims/anims/plain_anims.html', dic)
    
#/ def open_image_dir(request):

