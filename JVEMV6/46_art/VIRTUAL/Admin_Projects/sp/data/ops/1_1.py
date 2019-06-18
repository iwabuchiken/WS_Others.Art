# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\sounds\mp3\1_1.py
at : 2018/06/30 09:32:18

r w && r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops
python 1_1.py
python 1_1.py -s1.0

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''
###############################################
import sys, cv2
# from pandas.compat import str_to_bytes
from numpy.distutils.from_template import item_re
#ref https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
from win32api import GetSystemMetrics
from matplotlib import pylab as plt

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

# import math as math

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

'''###################
    click_and_crop(event, x, y, flags, param)
    
    at : 2018/06/30 09:53:22
    
###################'''
#ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
def click_and_crop(event, x, y, flags, param):
    
    print()
    print("[%s:%d] x = %d, y = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , x, y
            ), file=sys.stderr)
    
#/ def click_and_crop(event, x, y, flags, param):

def test_8__Matplotlib__Bar_Chart():
    
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]
    
    performance.reverse()
#     performance = [10,8,6,4,2,1]
     
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')
     
    plt.show()    
    
#/ def test_8__Matplotlib__Bar_Chart():

def test_7__SubImage_RGB_Vals__Get_Scaling(args):
    
    # scaling
    scaling = 1.0
    
    #debug
    print("[%s:%d] args =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(args)
    
    
    
    if len(args) > 0 : #if len(args) > 1
#     if len(args) > 1 : #if len(args) > 1
    
        optlist, args = getopt.getopt(args, "s:")
        
        print("[%s:%d] optlist =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(optlist)
        
        for item in optlist:
            
            #debug
            print("[%s:%d] item =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
            print(item)
    
            if item[0].startswith("-s") : #if item.startswith("-s")
    
                scaling = float(item[1])
#                 scaling = item[1]
                
                break
                
            #/if item.startswith("-s")
            
        #/for item in optlist:

    
    else : #if len(args) > 1
    
        print("[%s:%d] len(args) < 2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    #/if len(args) > 1
    
    #debug
    print("[%s:%d] scaling => %.3f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , scaling
            ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return scaling

#/ def test_7__SubImage_RGB_Vals__Get_Scaling():
    
def test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub):
    
    '''###################
        message        
    ###################'''
    cntOf_Rows = 0
    
    lo_Rs = []
    lo_Gs = []
    lo_Bs = []
    
    for row in img_Sub:
        
        # counter
        cntOf_Rows += 1
        
        for cell in row:
    
#             print()
#             print("[%s:%d] cell(%d) => " % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , cntOf_Rows
#             ), file=sys.stderr)
#             print(cell)
            
            '''###################
                append        
            ###################'''
            lo_Rs.append(cell[0])
            lo_Gs.append(cell[1])
            lo_Bs.append(cell[2])
            
#             break
            
        #/for cell in row:

        
    #/for row in img_Sub:
    
    '''###################
        return        
    ###################'''
    return lo_Rs, lo_Gs, lo_Bs

#/ def test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub):

def test_7__SubImage_RGB_Vals():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_7__SubImage_RGB_Vals =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)
    
    '''######################################
        get : args
    ##################
    ####################'''
    args = sys.argv[1:]
#     args = sys.argv
    
    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images"

    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    img_ForDisp = img_Orig
    
    # meta data
    height, width, channels = img_ForDisp.shape
#     height, width, channels = img_Orig.shape
    
    #debug
    print("[%s:%d] source image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Ops_Image
            ), file=sys.stderr)
    
    print("[%s:%d] width = %d, height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , width, height
            ), file=sys.stderr)
    
    '''###################
        sub image        
    ###################'''
    # height, width
    img_Sub = img_ForDisp[19:69, 245:246]
#     img_Sub = img_ForDisp[19:186, 245:246]
    
    # meta data
    height_Sub, width_Sub, channels_Sub = img_Sub.shape
    
    print("[%s:%d] width_Sub = %d, height_Sub = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , width_Sub, height_Sub
        ), file=sys.stderr)
    
    print()
    print("[%s:%d] img_Sub[0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(img_Sub[0])
    print("[%s:%d] img_Sub[0][0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(img_Sub[0][0])
    
    '''###################
        get : RGB vals        
    ###################'''
    lo_Rs, lo_Gs, lo_Bs = test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub)
    
#     print()
#     print("[%s:%d] lo_Rs =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                
#                 ), file=sys.stderr)
#     print(lo_Rs)
    
    '''###################
        plot        
    ###################'''
#     yax_vals = [200, 100,0]
#     plt.bar(yax_vals, lo_Rs)
# #     plt.bar(lo_Rs, yax_vals)
# #     plt.bar(lo_Rs)
# #     plt.plot(lo_Rs)
#     
#     plt.show()

#     objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(lo_Rs))
#     y_pos = np.arange(len(objects))
#     y_pos = [10, 20, 30]
    performance = lo_Rs
#     performance = [30,8,6,4,2,1]
#     performance = [10,8,6,4,2,1]
    
#     performance.reverse()
#     performance = [10,8,6,4,2,1]
     
#     plt.bar(y_pos, performance, align='center', alpha=0.5)

#     plt.plot(lo_Rs)
#     plt.plot(lo_Bs)
#     plt.plot(lo_Rs, lo_Bs)

#     plt.xticks(y_pos, objects)
#     plt.yticks([140, 180])


#     plt.ylabel('Usage')
#     plt.title('Programming language usage')
#     
#     ax = plt.gca()
#     
#     #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
#     ax.grid(which='major', axis='both', linestyle='--')
#     ax.grid(which='minor', axis='both', linestyle='--')
# 
#     ax.set(aspect=1,
#            xlim=(0, len(lo_Rs)),
#            ylim=(140, 170))
#     
#     plt.show()    

#     #ref https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure#4805456
#     plotHandles = []
#     labels = []
#     
#     plotHandles.append(lo_Rs)
#     labels.append("lo_Rs")
#     plotHandles.append(lo_Gs)
#     labels.append("lo_Gs")
# 
#     plt.legend(plotHandles, labels, 'upper left',ncol=1)
    
    #ref https://stackoverflow.com/questions/21254472/multiple-plot-in-one-figure-in-python
    plt.plot(y_pos, lo_Rs, 'r-', label='lo_Rs')
    plt.plot(y_pos, lo_Gs, 'g-', label='lo_Gs')
    plt.plot(y_pos, lo_Bs, 'b-', label='lo_Bs')
    
    plt.legend(loc='best')
    
    ax = plt.gca()
     
    #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
    ax.grid(which='major', axis='both', linestyle='--')
    ax.grid(which='minor', axis='both', linestyle='--')
 
    ax.set(aspect=1,
           xlim=(0, len(lo_Rs)),
           ylim=(140, 250))
    
    fpath_Save_Image = os.path.join(dpath_Ops_Images, "plot_" + libs.get_TimeLabel_Now() + ".png")
    
    
    result = plt.savefig(fpath_Save_Image)
    
    print("[%s:%d] save fig => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , result, fpath_Save_Image
        ), file=sys.stderr)
    
    plt.show()
    
    
    #debug
    return
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    '''###################
        get : scaling        
    ###################'''
    scaling = test_7__SubImage_RGB_Vals__Get_Scaling(args)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    '''###################
        resize image        
    ###################'''
    win_Resize_Width, win_Resize_Height = test_5__Resize_Image(width, height, scaling, scr_W, scr_H)

    '''###################
        disp : image
    ###################'''
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
    
    '''###################
        mouse events
    ###################'''
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_Sub)
#     cv2.imshow('window', img_ForDisp)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#/ def test_5():

def test_6__Get_SubImage():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_6__Get_SubImage =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)
    
    '''######################################
        get : args
    ##################
    ####################'''
    args = sys.argv[1:]
#     args = sys.argv
    
    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images"

    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    img_ForDisp = img_Orig
    
    # meta data
    height, width, channels = img_ForDisp.shape
#     height, width, channels = img_Orig.shape
    
    #debug
    print("[%s:%d] source image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Ops_Image
            ), file=sys.stderr)
    
    print("[%s:%d] width = %d, height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , width, height
            ), file=sys.stderr)
    
    '''###################
        sub image        
    ###################'''
    # height, width
    img_Sub = img_ForDisp[19:186, 245:246]
#     img_Sub = img_ForDisp[246:19, 247:186]
#     img_Sub = img_ForDisp[246:19, 246:186]
    
    # meta data
    height_Sub, width_Sub, channels_Sub = img_Sub.shape
    
    print("[%s:%d] width_Sub = %d, height_Sub = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , width_Sub, height_Sub
        ), file=sys.stderr)
    
    print()
    print("[%s:%d] img_Sub[0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(img_Sub[0])
    print("[%s:%d] img_Sub[0][0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(img_Sub[0][0])
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    # scaling
    scaling = 1.0
    
    #debug
    print("[%s:%d] args =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(args)
    
    
    
    if len(args) > 0 : #if len(args) > 1
#     if len(args) > 1 : #if len(args) > 1
    
        optlist, args = getopt.getopt(args, "s:")
        
        print("[%s:%d] optlist =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(optlist)
        
        for item in optlist:
            
            #debug
            print("[%s:%d] item =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
            print(item)
    
            if item[0].startswith("-s") : #if item.startswith("-s")
    
                scaling = float(item[1])
#                 scaling = item[1]
                
                break
                
            #/if item.startswith("-s")
            
        #/for item in optlist:

    
    else : #if len(args) > 1
    
        print("[%s:%d] len(args) < 2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    #/if len(args) > 1
    
    #debug
    print("[%s:%d] scaling => %.3f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , scaling
            ), file=sys.stderr)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    '''###################
        resize image        
    ###################'''
    win_Resize_Width, win_Resize_Height = test_5__Resize_Image(width, height, scaling, scr_W, scr_H)

    '''###################
        disp : image
    ###################'''
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
    
    '''###################
        mouse events
    ###################'''
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_Sub)
#     cv2.imshow('window', img_ForDisp)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#/ def test_5():


'''###################
    test_5()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        - use ==> argv for window size
    
    <Example>
    python 1_1.py -s0.25
        
    <quit program>
    return key
    
###################'''
def test_5__Resize_Image(width, height, scaling, scr_W, scr_H):
    
    q1 = 1.0 * width / height

    s = scaling
    
    flg_WorH = ""
    
    # j1
    if s >= 0 : #if s >= 0
            
        ### j1 : p1
        A = 0
        
        if width >= height : #if width > height
            
                flg_WorH = "width"
                
                A = width
            
        else : #if width > height
        
            flg_WorH = "height"
        
            A = height
            
        #/if width > height
        
        ### j1 : p2
        m = A * s
        
        print("[%s:%d] m => %.03f" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , m
                ), file=sys.stderr)
        
        ### j1 : p3
        Z = 0
        
        if flg_WorH == "width" : #if flg_WorH == "width"
            
            Z = scr_W
            
        else : #if flg_WorH == "width"
        
            Z = scr_H
        
        #/if flg_WorH == "width"
        
        ### j2
        result = (m > Z)

        '''###################
            vars
        ###################'''
        win_Resize_Height = 0
        win_Resize_Width = 0
        
        if result == True : #if result == True

            print("[%s:%d] m > Z : m = %.03f, Z = %d, flg_WorH = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , m, Z, flg_WorH
                ), file=sys.stderr)
            
            ### j2 : p1
            q2 = 1.0 * Z / A
            
            print("[%s:%d] q2 => %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , q2
                    ), file=sys.stderr)

            '''###################
                calc
            ###################'''
            win_Resize_Height = math.floor(height * q2)
            win_Resize_Width = math.floor(width * q2)
#             win_Resize_Height = int(height * q2)
#             win_Resize_Width = int(width * q2)
#             win_Resize_Height = height * q2
#             win_Resize_Width = width * q2
            
        else : #if result == True
        
            print("[%s:%d] m <= Z" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
            
        
            '''###################
                calc
            ###################'''
            win_Resize_Height = math.floor(scaling * height)
            win_Resize_Width = math.floor(scaling * width)

        
        #/if result == True
        
    else : #if s >= 0
    
        '''###################
            calc
        ###################'''
        win_Resize_Height = math.floor(scaling * height)
        win_Resize_Width = math.floor(scaling * width)
    
    #/if s >= 0

#     '''###################
#         calc
#     ###################'''
#     win_Resize_Height = math.floor(scaling * height)
#     win_Resize_Width = math.floor(scaling * width)

    '''###################
        return        
    ###################'''
    #debug
    print("[%s:%d] win_Resize_Width = %d, win_Resize_Height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , win_Resize_Width, win_Resize_Height
            ), file=sys.stderr)
    print()
    
    return win_Resize_Width, win_Resize_Height
    
#/ def test_5():

def test_5():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_5 =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)
    
    '''######################################
        get : args
    ##################
    ####################'''
    args = sys.argv[1:]
#     args = sys.argv
    
    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images"

    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    img_ForDisp = img_Orig
    
    # meta data
    height, width, channels = img_ForDisp.shape
#     height, width, channels = img_Orig.shape
    
    #debug
    print("[%s:%d] source image => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Ops_Image
            ), file=sys.stderr)
    
    print("[%s:%d] width = %d, height = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , width, height
            ), file=sys.stderr)
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    # scaling
    scaling = 1.0
    
    #debug
    print("[%s:%d] args =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(args)
    
    
    
    if len(args) > 0 : #if len(args) > 1
#     if len(args) > 1 : #if len(args) > 1
    
        optlist, args = getopt.getopt(args, "s:")
        
        print("[%s:%d] optlist =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(optlist)
        
        for item in optlist:
            
            #debug
            print("[%s:%d] item =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
            print(item)
    
            if item[0].startswith("-s") : #if item.startswith("-s")
    
                scaling = float(item[1])
#                 scaling = item[1]
                
                break
                
            #/if item.startswith("-s")
    
    
            
        #/for item in optlist:

    
    else : #if len(args) > 1
    
        print("[%s:%d] len(args) < 2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    #/if len(args) > 1
    
    #debug
    print("[%s:%d] scaling => %.3f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , scaling
            ), file=sys.stderr)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
#     if win_Resize_Width > scr_W : win_Resize_Width = scr_W
#     if win_Resize_Height > scr_H : win_Resize_Width = scr_H
#     
#     #debug
#     print("[%s:%d] win_Resize_Width = %.03f, win_Resize_Height = %.03f" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , win_Resize_Width, win_Resize_Height
#                     ), file=sys.stderr)
#     print()

    '''###################
        resize image        
    ###################'''
    win_Resize_Width, win_Resize_Height = test_5__Resize_Image(width, height, scaling, scr_W, scr_H)
#     test_5__Resize_Image(width, height, scaling, scr_W, scr_H)
    
    
#     q1 = 1.0 * width / height
#     aa
#     s = scaling
#     
#     flg_WorH = ""
#     
#     # j1
#     if s >= 0 : #if s >= 0
#             
#         ### j1 : p1
#         A = 0
#         
#         if width >= height : #if width > height
#             
#                 flg_WorH = "width"
#                 
#                 A = width
#             
#         else : #if width > height
#         
#             flg_WorH = "height"
#         
#             A = height
#             
#         #/if width > height
#         
#         ### j1 : p2
#         m = A * s
#         
#         print("[%s:%d] m => %.03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , m
#                 ), file=sys.stderr)
#         
#         ### j1 : p3
#         Z = 0
#         
#         if flg_WorH == "width" : #if flg_WorH == "width"
#             
#             Z = scr_W
#             
#         else : #if flg_WorH == "width"
#         
#             Z = scr_H
#         
#         #/if flg_WorH == "width"
#         
#         ### j2
#         result = (m > Z)
#         
#         if result == True : #if result == True
# 
#             print("[%s:%d] m > Z : m = %.03f, Z = %d, flg_WorH = %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , m, Z, flg_WorH
#                 ), file=sys.stderr)
# 
#         else : #if result == True
#         
#             pass
#         
#         #/if result == True
# 
# 
#             
#         
#     else : #if s >= 0
#     
#         pass
#     
#     #/if s >= 0
#             
            
    
#     #debug
#     return
    

    '''###################
        disp : image
    ###################'''
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
    
    '''###################
        mouse events
    ###################'''
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_ForDisp)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#/ def test_5():

'''###################
    test_4()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        - use ==> argv for window size
    
    <Example>
    python 1_1.py -s0.25
        
    <quit program>
    return key
    
###################'''
def test_4():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_4 =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)

    '''######################################
        get : args
    ##################
    ####################'''
    args = sys.argv[1:]
#     args = sys.argv
    
    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images"

    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    img_ForDisp = img_Orig
    
    # meta data
    height, width, channels = img_ForDisp.shape
#     height, width, channels = img_Orig.shape
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    # scaling
    scaling = 1.0
    
    #debug
    print("[%s:%d] args =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    print(args)
    
    if len(args) > 0 : #if len(args) > 1
#     if len(args) > 1 : #if len(args) > 1
    
        optlist, args = getopt.getopt(args, "s:")
        
        print("[%s:%d] optlist =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(optlist)
        
        for item in optlist:
            
            #debug
            print("[%s:%d] item =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
            print(item)
    
            if item[0].startswith("-s") : #if item.startswith("-s")
    
                scaling = float(item[1])
#                 scaling = item[1]
                
                break
                
            #/if item.startswith("-s")
    
    
            
        #/for item in optlist:

    
    else : #if len(args) > 1
    
        print("[%s:%d] len(args) < 2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    #/if len(args) > 1
    
    
    
#     scaling = 0.5
    
    #debug
    print("[%s:%d] scaling => %.3f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , scaling
            ), file=sys.stderr)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    if win_Resize_Width > scr_W : win_Resize_Width = scr_W
    if win_Resize_Height > scr_H : win_Resize_Width = scr_H
    
        
        
    
    #debug
    print("[%s:%d] win_Resize_Width = %.03f, win_Resize_Height = %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , win_Resize_Width, win_Resize_Height
                    ), file=sys.stderr)
    print()
    
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
#     cv2.resizeWindow(window_1, 600,600)
    
#     cv2.namedWindow(window_1)
#     cv2.namedWindow('window')
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''
#     while True :
#         
#         cv2.imshow(window_1, img_Orig_RGB)
# #         cv2.imshow('window', img_Orig_RGB)
#     #     cv2.imshow('window', img_Orig)
#     #     cv2.imshow('window', I)
#         
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

    cv2.imshow('window', img_ForDisp)
#     cv2.imshow('window', img_Orig_RGB)
#     cv2.imshow('window', img_Orig)
#     cv2.imshow('window', I)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#     '''###################
#         message
#     ###################'''
#     print()
#     print("[%s:%d] test_2 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_1():


def test_3():

#     '''###################
#         get : args        
#     ###################'''
    lib_ip.test__get_Opt_IP()
	#ref https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments-in-python answered Oct 27 '10 at 13:27
#     args = sys.argv
#     
#     print()
#     print("[%s:%d] args =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     print(args)

#/ def test_3():

'''###################
    test_2()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        
        <quit program>
        return key
    
###################'''
def test_2():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_2 =======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()

        ), file=sys.stderr)

    '''######################################
        ops        
    ######################################'''
    dpath_Ops_Images = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images"

    fname_Ops_Image = "2018-06-24_19-14-31_000.jpg"
    
    fpath_Ops_Image = os.path.join(dpath_Ops_Images, fname_Ops_Image)
    
    '''###################
        get : image
    ###################'''
    # read image
    img_Orig = cv2.imread(fpath_Ops_Image)
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    img_ForDisp = img_Orig
    
    # meta data
    height, width, channels = img_ForDisp.shape
#     height, width, channels = img_Orig.shape
    
    '''######################################
        prep : window
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    scaling = 0.5
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    cv2.resizeWindow(window_1, win_Resize_Width, win_Resize_Height)
#     cv2.resizeWindow(window_1, 600,600)
    
#     cv2.namedWindow(window_1)
#     cv2.namedWindow('window')
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''
#     while True :
#         
#         cv2.imshow(window_1, img_Orig_RGB)
# #         cv2.imshow('window', img_Orig_RGB)
#     #     cv2.imshow('window', img_Orig)
#     #     cv2.imshow('window', I)
#         
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

    cv2.imshow('window', img_ForDisp)
#     cv2.imshow('window', img_Orig_RGB)
#     cv2.imshow('window', img_Orig)
#     cv2.imshow('window', I)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#     '''###################
#         message
#     ###################'''
#     print()
#     print("[%s:%d] test_2 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_1():

def test_1():

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
    
    img_Orig_RGB = cv2.cvtColor(img_Orig, cv2.COLOR_BGR2RGB)
    
    # meta data
    height, width, channels = img_Orig.shape
    
    '''######################################
        show : image
    ######################################'''
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    cv2.namedWindow(window_1)
#     cv2.namedWindow('window')
    
    '''###################
        mouse events
    ###################'''
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
    
    

        
    '''###################
        show
    ###################'''
#     while True :
#         
#         cv2.imshow(window_1, img_Orig_RGB)
# #         cv2.imshow('window', img_Orig_RGB)
#     #     cv2.imshow('window', img_Orig)
#     #     cv2.imshow('window', I)
#         
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

    cv2.imshow('window', img_Orig_RGB)
#     cv2.imshow('window', img_Orig)
#     cv2.imshow('window', I)
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
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
#     test_8__Matplotlib__Bar_Chart()
    test_7__SubImage_RGB_Vals()
#     test_6__Get_SubImage()
#     test_5()
#     test_4()
#     test_2()
#     test_3()
#     test_2()
#     test_1()
    
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
