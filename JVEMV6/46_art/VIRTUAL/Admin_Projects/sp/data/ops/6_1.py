# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\6_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
at : 2018/07/15 08:09:48

r w && r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops
python 6_1.py -s1.0

python 6_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

20180721_111655
C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\images\
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

'''###################
    constants : global        
###################'''
# import math as math
refPt_Start = [-1] * 2
refPt_End = [-1] * 2
# refPt_Start = []
# refPt_End = []

flg_Set_Points  = ""
flg_Get_RGB_Vals  = False

POINTS_START    = "START"
POINTS_END      = "END"
POINTS_NEUTRAL  = "NEUTRAL"

KEY_INPUTS__END    = 'e'
KEY_INPUTS__RGB    = 'g'
KEY_INPUTS__HELP    = 'h'
KEY_INPUTS__QUIT    = 'q'
KEY_INPUTS__RESET    = 'r'
KEY_INPUTS__START    = 's'
KEY_INPUTS__EXECUTE    = 'x'

DPATH_IMAGE_OUTPUT = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects\\ip\\data\\ops\\images"

###############################################
# def show_Message() :
#     
#     msg = '''
#     <Options>
#     -v	Volume down the amplitude --> 1.0 * v / 1000
#     -f	Base frequency ---> e.g. 262 for the A tone
#     -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
#     
#     print (msg)

'''###################
    click_and_crop(event, x, y, flags, param)
    
    at : 2018/06/30 09:53:22
    
###################'''
#ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
def click_and_crop(event, x, y, flags, param):
    
    #ref https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    if event == cv2.EVENT_LBUTTONDOWN:
        
#         #debug
#         print("[%s:%d] type(param) => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , type(param)
#                 ), file=sys.stderr)
        
        if flg_Set_Points == POINTS_START : #if flg_Set_Points == POINTS_START

            refPt_Start[0] = x
            refPt_Start[1] = y
            
            print()
    #         print("[%s:%d] EVENT_LBUTTONDOWN (x = %d / y = %d)" % \
            print("[%s:%d] EVENT_LBUTTONDOWN ==> starting point set" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
    #                 , x, y
                    ), file=sys.stderr)
            
            print(refPt_Start)
        
#             '''###################
#                 RGB vals        
#             ###################'''
#             if flg_Get_RGB_Vals == True : #if flg_Get_RGB_Vals == True
#             
#                 print(param[x][y])
                
            #/if flg_Get_RGB_Vals == True
            
            
        
        elif flg_Set_Points == POINTS_END : #if flg_Set_Points == POINTS_START

            refPt_End[0] = x
            refPt_End[1] = y
            
            print()
    #         print("[%s:%d] EVENT_LBUTTONDOWN (x = %d / y = %d)" % \
            print("[%s:%d] EVENT_LBUTTONDOWN ==> ending point set" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
    #                 , x, y
                    ), file=sys.stderr)
            
            print(refPt_End)
        
        
        else : #if flg_Set_Points == POINTS_START
        
            print()
            print("[%s:%d] EVENT_LBUTTONDOWN ==> unknown flag value : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , flg_Set_Points
                    ), file=sys.stderr)
            
            print([x, y])
            
        '''###################
            RGB vals
        ###################'''
        if flg_Get_RGB_Vals == True : #if flg_Get_RGB_Vals == True
        
            print("[%s:%d] RGB of the point ==>" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
            print(param[y][x])
#             print(param[x][y])
            
        #/if flg_Get_RGB_Vals == True
        
        
        
    #/if flg_Set_Points == POINTS_START

#/ def click_and_crop(event, x, y, flags, param):

def show_Message():

#     print("'q' to quit")
#     print("'x' to execute")
#     print("'h' to show this key list")
    print("'g'\tset flag for getting RGB values")
    print("'h'\tshow this key list")
    print("'q'\tquit")
    print("'r'\treset start/end")
    print("'x'\texecute")
#             print("'e' to execute")
#             print("left click ==> set the starting point")
#             print("right click ==> set the ending point")
    print("'s' then left click ==> set the starting point")
    print("'e' then right click ==> set the ending point")
    print()

#/ def show_Message():


'''###################
    get_RGB_Vals      
    
    from : test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub)
    at : 2018/07/15 08:17:58
    
    @return: list of RGB vals
            e.g. [156, 167, 153,...], [156, 167, 153,...], [156, 167, 153,...]
    
###################'''
def get_RGB_Vals(img_Sub):
    
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
    
            '''###################
                append        
            ###################'''
            lo_Rs.append(cell[0])
            lo_Gs.append(cell[1])
            lo_Bs.append(cell[2])
            
        #/for cell in row:
        
    #/for row in img_Sub:
    
    '''###################
        return        
    ###################'''
    return lo_Rs, lo_Gs, lo_Bs

#/ def test_7__SubImage_RGB_Vals__Get_RGB_Vals(img_Sub):

'''###################
    get_Scaling        
    
    from : test_7__SubImage_RGB_Vals__Get_Scaling(args)
    at : 2018/07/15 08:22:52
    
###################'''
def get_Scaling(args):
    
    # scaling
    scaling = 1.0
    
#     #debug
#     print("[%s:%d] args =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#     print(args)
    
    if len(args) > 0 : #if len(args) > 1
    
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

'''###################
    resize_Image()
    
    <description>
        - add listener to ==> image
        - hover on the image ==> x, y coordinates displayed in the console
        - use ==> argv for window size
    
    <Example>
    python 1_1.py -s0.25
        
    <quit program>
    return key
    
###################'''
# def test_5__Resize_Image(width, height, scaling, scr_W, scr_H):
def resize_Image(width, height, scaling, scr_W, scr_H):
    
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

def __key_Inputs__RGB(img_ForDisp):
    
    global flg_Get_RGB_Vals
    
    if flg_Get_RGB_Vals == True : #if flg_Get_RGB_Vals == True

        flg_Get_RGB_Vals = False
        
        print("[%s:%d] flg_Get_RGB_Vals ==> now : %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , flg_Get_RGB_Vals
        ), file=sys.stderr)
    
    else : #if flg_Get_RGB_Vals == True
    
        flg_Get_RGB_Vals = True
        
        print("[%s:%d] flg_Get_RGB_Vals ==> now : %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , flg_Get_RGB_Vals
        ), file=sys.stderr)
    
    #/if flg_Get_RGB_Vals == True



#/ def __key_Inputs__RGB():

def __key_Inputs__EXECUTE__V2__Plot_RGB(lo_Rs, lo_Gs, lo_Bs, fpath_Image):
    
    y_pos = np.arange(len(lo_Rs))

    performance = lo_Rs
    
    '''###################
        reset : plot        
    ###################'''
    #ref https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib#8228808
    plt.clf()
    
    #ref https://stackoverflow.com/questions/21254472/multiple-plot-in-one-figure-in-python
#     plt.plot(lo_Rs, 'r-', label='lo_Rs')
#     plt.plot(lo_Rs, 'r+', label='lo_Rs')
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
           ylim=(0, 260))
#            ylim=(140, 250))
    
    fpath_Save_Image = fpath_Image
#     fpath_Save_Image = os.path.join(dpath_Ops_Images, "plot_" + libs.get_TimeLabel_Now() + ".png")
    
    result = plt.savefig(fpath_Save_Image)
    
    plt.show()
    
#     print("[%s:%d] save fig => %s (%s)" % \
    print("[%s:%d] save fig (graph) => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , result, fpath_Save_Image
        ), file=sys.stderr)

#/ def __test_1__Set_Starting_Point__Plotting():

# def __test_1__Set_Starting_Point__Key_Inputs():

def __test_1__Set_Starting_Point__Plotting(lo_Rs, lo_Gs, lo_Bs, dpath_Ops_Images):
    
    y_pos = np.arange(len(lo_Rs))

    performance = lo_Rs
    
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
           ylim=(0, 260))
#            ylim=(140, 250))
    
    fpath_Save_Image = os.path.join(dpath_Ops_Images, "plot_" + libs.get_TimeLabel_Now() + ".png")
    
    result = plt.savefig(fpath_Save_Image)
    
#     print("[%s:%d] save fig => %s (%s)" % \
    print("[%s:%d] save fig (graph) => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , result, fpath_Save_Image
        ), file=sys.stderr)
#/ def __test_1__Set_Starting_Point__Plotting():

# def __test_1__Set_Starting_Point__Key_Inputs():

def __key_Inputs__EXECUTE__Save_SubImage(img_ForDisp):
    
    '''###################
        validate
    ###################'''
    if refPt_Start == [-1,-1] or refPt_End == [-1,-1] : #if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
    
        print("[%s:%d] start/end points ==> not yet set" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        
        return
        
    #/if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
    
    
    
    
    '''###################
        sub image        
    ###################'''
    
    img_Sub = img_ForDisp[
                refPt_Start[1] : refPt_End[1]
                , refPt_Start[0] : refPt_End[0]
#                 , refPt_Start[0] : refPt_Start[0] + 10
#                 refPt_Start[0] : refPt_Start[0] + 10
#                 , refPt_Start[1] : refPt_End[1]
                          ]
    
    # file name
    fname = "subimage_%s.png" % libs.get_TimeLabel_Now()
    
    fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
    
    #ref save image https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    result = cv2.imwrite(fpath_Save_Image, img_Sub)
    
    print("[%s:%d] saving image ==> %s (%s)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , result, fpath_Save_Image
                ), file=sys.stderr)

    '''###################
        return        
    ###################'''
    return img_Sub

#/ def __key_Inputs__EXECUTE__Save_SubImage(img_ForDisp):
    
def __key_Inputs__EXECUTE__Gen_RGBGraph(img_Target):
    
    '''###################
        get : values        
    ###################'''
    lo_Rs, lo_Gs, lo_Bs = get_RGB_Vals(img_Target)
    
    print()
    print("[%s:%d] len(lo_Rs) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_Rs)
                ), file=sys.stderr)
    
    '''###################
        plot        
    ###################'''
    dpath_Ops_Images = DPATH_IMAGE_OUTPUT
    
    __test_1__Set_Starting_Point__Plotting(lo_Rs, lo_Gs, lo_Bs, dpath_Ops_Images)

#/ def __key_Inputs__EXECUTE__Gen_RGBGraph(img_Target):
    
def __key_Inputs__EXECUTE__V2__Save_SubImage(key_inputs, img_ForDisp, time_Label):
    
    '''###################
        validate
    ###################'''
    if refPt_Start == [-1,-1] or refPt_End == [-1,-1] : #if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
      
        print("[%s:%d] start/end points ==> not yet set" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
              
            ), file=sys.stderr)
          
        return
          
    #/if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
      
      
      
      
    '''###################
        sub image        
    ###################'''
      
    img_Sub = img_ForDisp[
#                 refPt_Start[0] : refPt_End[0]     # x axis
#                 , refPt_Start[1] : refPt_End[1]       # y axis
                refPt_Start[1] : refPt_End[1]       # y axis
                , refPt_Start[0] : refPt_End[0]     # x axis
#                 , refPt_Start[0] : refPt_Start[0] + 10
#                 refPt_Start[0] : refPt_Start[0] + 10
#                 , refPt_Start[1] : refPt_End[1]
                          ]
      
    # file name
#             % (libs.get_TimeLabel_Now()
    fname = "subimage_%s.%d-%d_%d-%d.png" \
            % (time_Label
               , refPt_Start[1], refPt_End[1]
               , refPt_Start[0], refPt_End[0])
      
    fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
      
    #ref save image https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    result = cv2.imwrite(fpath_Save_Image, img_Sub)
      
    print("[%s:%d] saving image ==> %s (%s)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , result, fpath_Save_Image
                ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return img_Sub
    
#/ def __key_Inputs__EXECUTE__V2__Save_SubImage(key_inputs, img_ForDisp):

# def __key_Inputs__EXECUTE__V2__RGB_Graph(key_inputs, img_ForDisp):
# def __key_Inputs__EXECUTE__V2__RGB_Graph(key_inputs, img_Sub):
def __key_Inputs__EXECUTE__V2__RGB_Graph(key_inputs, img_Sub, time_Label):
    

    '''###################
        get : RGB vals
    ###################'''
    '''###################
        get : 1-pixel-col sub image
    ###################'''
    height, width, channels = img_Sub.shape
    
    img_Sub_1_Pixel_Col = img_Sub[
        
            0 : height       # y axis
                , 0 : 1 # x axis
#                 , refPt_Start[0] : refPt_Start[0] + 1 # x axis
        
        ]

    print()
#     print("[%s:%d] img_Sub_1_Pixel_Col[0]" % \
    print("[%s:%d] img_Sub_1_Pixel_Col[:5]" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
    print(img_Sub_1_Pixel_Col[:5])
#     print(img_Sub_1_Pixel_Col[0])

    lo_Rs, lo_Gs, lo_Bs = get_RGB_Vals(img_Sub_1_Pixel_Col)
# 
    print()
    print("[%s:%d] lo_Rs =>" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                      
                    ), file=sys.stderr)
    print(lo_Rs[:5])

    '''###################
        get : 1-pixel-image from the img_Sub        
    ###################'''
#     img_Sub_1_Pixel_Col = img_Sub[
#         
#             refPt_Start[1] : refPt_End[1]       # y axis
#                 , refPt_Start[0] : refPt_Start[0] + 1 # x axis
#         
#         ]

    
    # file name
#             % (libs.get_TimeLabel_Now()
    fname = "subimage_%s.%d-%d_%d-%d.RGB-GRAPH.png" \
            % (time_Label
               , 0, height   # y axis
               , 0, 1   # x axis
               )
#                , refPt_Start[1], refPt_End[1]
#                , refPt_Start[0], refPt_End[0])
      
    fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)

    #ref save image https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    result = cv2.imwrite(fpath_Save_Image, img_Sub_1_Pixel_Col)
#     result = cv2.imwrite(fpath_Save_Image, img_Sub)
      
    print("[%s:%d] saving image ==> %s (%s)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , result, fpath_Save_Image
                ), file=sys.stderr)

    '''###################
        plot        
    ###################'''
    fpath_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
    
    __key_Inputs__EXECUTE__V2__Plot_RGB(lo_Rs, lo_Gs, lo_Bs, fpath_Image)


#/ def __key_Inputs__EXECUTE__V2__RGB_Graph(key_inputs, img_ForDisp):
    
'''###################
    __key_Inputs__EXECUTE__V2(key_inputs, img_ForDisp)
    
    <description>
    
    
###################'''
def __key_Inputs__EXECUTE__V2(key_inputs, img_ForDisp):
    
    print("[%s:%d] __key_Inputs__EXECUTE__V2" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)


    '''###################
        save : sub image
    ###################'''
    time_Label = libs.get_TimeLabel_Now()
    
    img_Sub = __key_Inputs__EXECUTE__V2__Save_SubImage(key_inputs, img_ForDisp, time_Label)
#     img_Sub = __key_Inputs__EXECUTE__V2__Save_SubImage(key_inputs, img_ForDisp)
    
    
    
    '''###################
        graph
    ###################'''
    __key_Inputs__EXECUTE__V2__RGB_Graph(key_inputs, img_Sub, time_Label)
#     __key_Inputs__EXECUTE__V2__RGB_Graph(key_inputs, img_Sub)
    
#     '''###################
#         validate
#     ###################'''
#     if refPt_Start == [-1,-1] or refPt_End == [-1,-1] : #if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
#       
#         print("[%s:%d] start/end points ==> not yet set" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#               
#             ), file=sys.stderr)
#           
#         return
#           
#     #/if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
#       
#       
#       
#       
#     '''###################
#         sub image        
#     ###################'''
#       
#     img_Sub = img_ForDisp[
#                 refPt_Start[1] : refPt_End[1]
#                 , refPt_Start[0] : refPt_End[0]
# #                 , refPt_Start[0] : refPt_Start[0] + 10
# #                 refPt_Start[0] : refPt_Start[0] + 10
# #                 , refPt_Start[1] : refPt_End[1]
#                           ]
#       
#     # file name
#     fname = "subimage_%s.png" % libs.get_TimeLabel_Now()
#       
#     fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
#       
#     #ref save image https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
#     result = cv2.imwrite(fpath_Save_Image, img_Sub)
#       
#     print("[%s:%d] saving image ==> %s (%s)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , result, fpath_Save_Image
#                 ), file=sys.stderr)

#/ def __key_Inputs__EXECUTE__V2(key_inputs, img_ForDisp):
    
def __key_Inputs__EXECUTE(key_inputs, img_ForDisp):
    
    print("[%s:%d] key_inputs => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , key_inputs
        ), file=sys.stderr)
#     print("refPt_Start =>")
#     print(refPt_Start)
#     print("refPt_End =>")
#     print(refPt_End)

    '''###################
        ops : V2        
    ###################'''
    __key_Inputs__EXECUTE__V2(key_inputs, img_ForDisp)
    
    '''###################
        exec : gen sub image        
    ###################'''
#     img_Sub = __key_Inputs__EXECUTE__Save_SubImage(img_ForDisp)
# 
#     print()
#     print("[%s:%d] type(img_Sub) => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , type(img_Sub)
#             ), file=sys.stderr)
#      
#     '''###################
#         exec : gen : RGB graph
#     ###################'''
#     height, width, channels = img_Sub.shape
#      
#     img_Target = img_Sub[
# #                 refPt_Start[1] : refPt_End[1]
#                 0:1
#                 , 0 : height
#                           ]
# #     img_Target = img_ForDisp[
# # #                 refPt_Start[1] : refPt_End[1]
# #                 refPt_Start[1] : refPt_End[0]
# #                 , refPt_Start[0] : refPt_End[0]
# #                           ]
#      
#     print()
#     print("[%s:%d] img_Target[0] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      
#                     ), file=sys.stderr)
#     print(img_Target[0])
    
#     __key_Inputs__EXECUTE__Gen_RGBGraph(img_Target)
# #     __key_Inputs__EXECUTE__Gen_RGBGraph(img_Sub)
    
#     '''###################
#         validate
#     ###################'''
#     if refPt_Start == [-1,-1] or refPt_End == [-1,-1] : #if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
#       
#         print("[%s:%d] start/end points ==> not yet set" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#               
#             ), file=sys.stderr)
#           
#         return
#           
#     #/if refPt_Start == [-1,-1] or refPt_End == [-1,-1]
#       
#       
#       
#       
#     '''###################
#         sub image        
#     ###################'''
#       
#     img_Sub = img_ForDisp[
#                 refPt_Start[1] : refPt_End[1]
#                 , refPt_Start[0] : refPt_End[0]
# #                 , refPt_Start[0] : refPt_Start[0] + 10
# #                 refPt_Start[0] : refPt_Start[0] + 10
# #                 , refPt_Start[1] : refPt_End[1]
#                           ]
#       
#     # file name
#     fname = "subimage_%s.png" % libs.get_TimeLabel_Now()
#       
#     fpath_Save_Image = os.path.join(DPATH_IMAGE_OUTPUT, fname)
#       
#     #ref save image https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
#     result = cv2.imwrite(fpath_Save_Image, img_Sub)
#       
#     print("[%s:%d] saving image ==> %s (%s)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , result, fpath_Save_Image
#                 ), file=sys.stderr)
    

#/ def __key_Inputs__EXECUTE(key_inputs, img_ForDisp):
    
def __key_Inputs(key_inputs, img_ForDisp):
    
    '''######################################
        dispatch        
    ###################'''
    '''###################
        key : x        
    ###################'''
    if key_inputs == KEY_INPUTS__EXECUTE: #if key
        
        __key_Inputs__EXECUTE(key_inputs, img_ForDisp)
        
#         print("[%s:%d] key_inputs => '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , key_inputs
#             ), file=sys.stderr)
#         print("refPt_Start =>")
#         print(refPt_Start)
#         print("refPt_End =>")
#         print(refPt_End)
        
    else : #if key
    
        print("[%s:%d] unknown key ==> '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , key_inputs
            ), file=sys.stderr)
    
    #/if key
        
        

#/ def __key_Inputs(KEY_INPUTS__EXECUTE, img_ForDisp):

def __test_1__Set_Starting_Point__Key_Inputs(img_ForDisp):
    
    '''###################
        vars        
    ###################'''
    #ref scope https://www.saltycrane.com/blog/2008/01/python-variable-scope-notes/
    global flg_Set_Points
    
    while True :
        
        k = cv2.waitKey(0) & 0xFF
    
        #ref https://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html
        if k == ord(KEY_INPUTS__QUIT):
#         if k == ord('q'):
            
            break
        
        elif k == ord(KEY_INPUTS__RGB):
            
            __key_Inputs__RGB(img_ForDisp)
            
        elif k == ord(KEY_INPUTS__HELP):
#         elif k == ord('h'):
            
            show_Message()
            
        elif k == ord(KEY_INPUTS__RESET):
#         elif k == ord('r'):

            print("[%s:%d] reset the flag...." % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
            
            flg_Set_Points = POINTS_NEUTRAL
            
            print("flag is => %s" % flg_Set_Points)
            
#         elif k == ord('x'):
        elif k == ord(KEY_INPUTS__EXECUTE):
            
            __key_Inputs(KEY_INPUTS__EXECUTE, img_ForDisp)
            
#             print("[%s:%d] executing...." % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#             print("refPt_Start =>")
#             print(refPt_Start)
#             print("refPt_End =>")
#             print(refPt_End)
            
        elif k == ord(KEY_INPUTS__START):
#         elif k == ord('s'):
            
            flg_Set_Points = POINTS_START
            
            print("[%s:%d] flag set ==> %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , flg_Set_Points
                    ), file=sys.stderr)
        
            
        elif k == ord(KEY_INPUTS__END):
#         elif k == ord('e'):
            
            flg_Set_Points = POINTS_END
            
            print("[%s:%d] flag set ==> %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , flg_Set_Points
                    ), file=sys.stderr)
        
#         if k == ord('e'):   ### 'e' for execute
#             
#             print("[%s:%d] starting/ending points" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)
#             print("<starting point>")
#             print(refPt_Start)
#             print("<ending point>")
#             print(refPt_End)
        
        else:
            
            #ref str() https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python answered Sep 9 '10 at 2:51
#             print("[%s:%d] waitKey => %d (%s) (press 'q' to quit)" % \
            print("[%s:%d] waitKey => %d (%s)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , k, str(chr(k))
                ), file=sys.stderr)
            
            # message
            show_Message()
#             print("'q' to quit")
#             print("'x' to execute")
# #             print("'e' to execute")
# #             print("left click ==> set the starting point")
# #             print("right click ==> set the ending point")
#             print("'s' then left click ==> set the starting point")
#             print("'e' then right click ==> set the ending point")
            
            
#     while True :

    print("[%s:%d] waitKey => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , k
        ), file=sys.stderr)

#/ def __test_1__Set_Starting_Point__Key_Inputs:

def __test_1__Set_Starting_Point__Window_Ops(args, width, height, img_Sub, img_Main):
    
    window_1 = "window"
    
    #ref https://qiita.com/supersaiakujin/items/54a4671142d80ca962ec
    #ref resize window http://answers.opencv.org/question/84985/resizing-the-output-window-of-imshow-function/
    cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
    
    '''###################
        get : scaling        
    ###################'''
    scaling = get_Scaling(args)
#     scaling = test_7__SubImage_RGB_Vals__Get_Scaling(args)
    
    win_Resize_Height = math.floor(scaling * height)
    win_Resize_Width = math.floor(scaling * width)
    
    # validate
    scr_W = GetSystemMetrics(0)
    scr_H = GetSystemMetrics(1)
    
    '''###################
        resize image        
    ###################'''
    win_Resize_Width, win_Resize_Height = resize_Image(width, height, scaling, scr_W, scr_H)
#     win_Resize_Width, win_Resize_Height = test_5__Resize_Image(width, height, scaling, scr_W, scr_H)

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
#     cv2.setMouseCallback(window_1, click_and_crop, [img_Sub, img_Main])
    #ref param https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=setmousecallback
    cv2.setMouseCallback(window_1, click_and_crop, img_Main)
#     cv2.setMouseCallback(window_1, click_and_crop)
#     cv2.setMouseCallback("image", click_and_crop)
        
    '''###################
        show
    ###################'''

    cv2.imshow('window', img_Main)
#     cv2.imshow('window', img_Sub)
#     cv2.imshow('window', img_ForDisp)
    
    print("[%s:%d] key inputs ======================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    show_Message()
#     print("'q' to quit")
#     print("'x' to execute")
# #             print("'e' to execute")
# #             print("left click ==> set the starting point")
# #             print("right click ==> set the ending point")
#     print("'s' then left click ==> set the starting point")
#     print("'e' then right click ==> set the ending point")

#     print("[%s:%d] waiting for key(0)....." % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return win_Resize_Width, win_Resize_Height, scr_W, scr_H
    
#/ def __test_1__Set_Starting_Point__Window_Ops():

def test_1__Set_Starting_Point():

    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1__Set_Starting_Point =======================" % \
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
    lo_Rs, lo_Gs, lo_Bs = get_RGB_Vals(img_Sub)
    
    '''###################
        plot        
    ###################'''
    __test_1__Set_Starting_Point__Plotting(lo_Rs, lo_Gs, lo_Bs, dpath_Ops_Images)
    
    '''######################################
        prep : window
    ######################################'''

    win_Resize_Width, win_Resize_Height, scr_W, scr_H = \
                __test_1__Set_Starting_Point__Window_Ops(args, width, height, img_Sub, img_ForDisp)
    
    '''###################
        key inputs        
    ###################'''
    __test_1__Set_Starting_Point__Key_Inputs(img_ForDisp)
#     __test_1__Set_Starting_Point__Key_Inputs()
    
    '''###################
        window : close        
    ###################'''
    cv2.destroyAllWindows()
    
#/ def test_5():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
#     test_8__Matplotlib__Bar_Chart()
    
    test_1__Set_Starting_Point()
    
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
