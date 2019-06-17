# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\2_\2_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\1_1.py
at : 2018/05/13 12:06:10


pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\2_\
python 2_1.py


'''
# from __future__ import print_function

###############################################
import sys

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\2_image-prog') # libs_mm
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')    # libs_VX7GLZ

from libs_image_prog import libs
# from libs_mm import libs

# from libs_VX7GLZ import libs_VX7GLZ
# from libs_VX7GLZ import wablibs

'''###################
    import : specifics
###################'''
# import midi, pretty_midi

'''###################
    import : built-in modules        
###################'''
import getopt, os, inspect, cv2, \
        math as math, random as rnd, numpy as np, \
        matplotlib.pyplot as plt, matplotlib.style as ms

###############################################

from matplotlib import pylab as plt

def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

# def save_Wave(fname_Out,  wave_Params, binwave):
#     
#         #サイン波をwavファイルとして書き出し
# #     fname_Out = "audio/output_%s.sin.wav" % (get_TimeLabel_Now())
# #     fname_Out = "output_%s.sin.wav" % (get_TimeLabel_Now())
# #     fname_Out = "output_%s.pow-%d.wav" % (get_TimeLabel_Now(), pow_Val)
#     
#     w = wave.Wave_write(fname_Out)
# #     w = wave.Wave_write("output.wav")
# #     p = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
#     p = wave_Params
#     w.setparams(p)
#     w.writeframes(binwave)
#     w.close()

# '''###################
#     gen_WaveData(fs, sec, A)
#     2017/12/31 15:21:22
#     @param fs: Sampling frequency ---> e.g. 8000
#     @param f0: Base frequency ---> e.g. 440 for 'A' note
#     @param sec: Length (seconds)
#     @param A: Amplitude ---> e.g. 1.0    
#     
#     @return: binwave: array, "-32768から32767の整数値"
# ###################'''
# def gen_WaveData(fs, f0, phase, sec, A):
#     
#     swav=[]
# 
#     #test
#     phase = np.pi  * ( 1 / 6 )
# #     phase = np.pi  * 1
# #     phase = np.pi  * (3/2)
# #     phase = np.pi / 2
# #     phase = fs
# #     phase = f0
#     
#     for n in np.arange(fs * sec):
#     #サイン波を生成
# 
#         s = A * np.sin(2 * np.pi * f0 * n / fs - phase)
# #         s = A * np.sin(2 * np.pi * f0 * n / fs)
#         
#         if s > 1.0:  s = 1.0
#         if s < -1.0: s = -1.0
#         
#         swav.append(s)
#         
#     #サイン波を-32768から32767の整数値に変換(signed 16bit pcmへ)
#     swav = [int(x * 32767.0) for x in swav]
#      
#     #バイナリ化
#     binwave = struct.pack("h" * len(swav), *swav)
#     
#     return binwave
# #gen_WaveData(fs, sec, A)

def get_mean(lo_Data):
    
    sumOf_Data = 0
    
    for d in lo_Data:

        sumOf_Data += d
        
    #/for d in lo_Data:

    # return
    return sumOf_Data
    
#/ def get_mean(lo_Data):


def test_6():
    
    print("[%s:%d] test_6()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        load : image        
    ###################'''
#     "C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\2_image-prog\2_projects\1_sort-out\images"
    dpath_Img = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images"
    fname_Img = "IMG_3171.JPG"
    fpath_Img = "%s/%s" % (dpath_Img, fname_Img)
    
    img = cv2.imread(fpath_Img)
#     img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
     
    '''###################
        get : data
    ###################'''
    # data
    height, width, channels = img2.shape
    off_set = 280
    
    tlabel = libs.get_TimeLabel_Now()
    
    plt_ = plt
    
    
    # save image
    '''###################
        corner : LB        
    ###################'''
    titles = ["clp_LB", "clp_RB", "clp_LU", "clp_RU"]
    
    clips = [
        
            img2[(height - off_set) : height, 0 : off_set], # clp_LB
            img2[(height - off_set) : height, width - off_set : width], # clp_RB
            img2[0 : off_set, 0 : off_set], # clp_LU
            img2[0 : off_set, width - off_set : width], # clp_RU
        ]
    
    '''###################
        max, min        
    ###################'''
#     idxOf_Clips = 1
    idxOf_Clips = 0
    
    clip_0 = clips[idxOf_Clips]
#     clip_0 = clips[0]
    
    max_R = -1; max_G = -1; max_B = -1

    # counter
    cntOf_Row = 0
    cntOf_Cell = 0
    
    # values
    valsOf_R = [0] * 255
    valsOf_G = [0] * 255
    valsOf_B = [0] * 255
    
    colNames = [str(x) for x in range(255)]
#     colNames = [x for x in range(255)]
    
    str_ColNames = "\t".join(colNames)
#     str_ColNames = colNames.join("\t")
    
    for row in clip_0:
        
        for cell in row:
            
            # get value
            R = cell[0]; G = cell[1]; B = cell[2]
            
            # addition
            valsOf_R[R] += 1
            valsOf_G[G] += 1
            valsOf_B[B] += 1
            
            if R > max_R : max_R = R
            if G > max_G : max_G = G
            if B > max_B : max_B = B
            
            # count
            cntOf_Cell += 1
        
        # reset count of cells
        cntOf_Cell = 0
        
        # count
        cntOf_Row += 1
        
    #/for row in clip_0:
    
    '''###################
        log        
    ###################'''
    dpath_Log = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6" \
                + "/46_art/2_image-prog/2_projects/1_sort-out/2_" \
                + "/data"
                
    # validate dir
    if not os.path.exists(dpath): os.makedirs(dpath)

        
    fname_Log = "3_.%s.log" % libs.get_TimeLabel_Now()
    
    fpath_Log = "%s/%s" % (dpath_Log, fname_Log)
    
    f = open(fpath_Log, "a")
    f.write("===================================")
    f.write("\n")
    
    msg = "[%s:%s:%d] result =>" % \
        (libs.get_TimeLabel_Now(), os.path.basename(libs.thisfile()), libs.linenum() \
         )
    f.write(msg)
    f.write("\n")
    
    msg = "file : %s" % \
        (fpath_Img)
    f.write(msg)
    f.write("\n")
        
    msg = "rows, cells : %d x %d" % (cntOf_Row, cntOf_Cell)
    
    f.write(msg)
    f.write("\n")

    # index
    msg = "index of clips : %d (%s)" % (idxOf_Clips, titles[idxOf_Clips])
    
    f.write(msg)
    f.write("\n")

    msg = "min, max : "
    
    f.write(msg)
#     f.write("\n")
    
    msg = "max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B)
    
    f.write(msg)
    f.write("\n")
#     f.write("\n")
    
#     print("[%s:%d] min, max -----------" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
# #     print("max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B))

    '''###################
        vals        
    ###################'''
    msg = "color\t%s" % str_ColNames
    
    f.write(msg)
    f.write("\n")

    lineOf_R = ""
    lineOf_G = ""
    lineOf_B = ""
    
    for i in range(255):
            
        lineOf_R += str(valsOf_R[i]) + "\t"
        lineOf_G += str(valsOf_G[i]) + "\t"
        lineOf_B += str(valsOf_B[i]) + "\t"
        
    #/for i in range(255):
    
    msg = "Rs\t%s" % lineOf_R
    
    f.write(msg)
    f.write("\n")
    
    msg = "Gs\t%s" % lineOf_G
    
    f.write(msg)
    f.write("\n")
    
    msg = "Bs\t%s" % lineOf_B
    
    f.write(msg)
    f.write("\n")
    
    
    '''###################
        stats
    ###################'''
    sumOf_Rs = 0
    
    # sum
    for d in valsOf_R: sumOf_Rs += d
    
    # mean
    mean_R = sumOf_Rs * 1.0 / len(valsOf_R)
    
    # summation
    summation = 0
    
    for d in valsOf_R:
    
        summation += np.power(d - mean_R, 4)
        
    #/for d in valsOf_R:

    # summation divided by length
    summation = summation / len(valsOf_R)
    
    # standard dev
    lo_tmp = [np.power(x, 2) for x in valsOf_R]
    
    # sum of squares
    sumOf_Squares_R = sum(lo_tmp)
    
    # dev
    deviation = sumOf_Squares_R * 1.0 / len(valsOf_R) - np.power(mean_R, 2)
    
    # std dev
    std_dev = np.sqrt(deviation)
    
    # skew
    #ref http://hs-www.hyogo-dai.ac.jp/~kawano/HStat/?plugin=cssj&page=2010%2F3rd%2FSkewness_Kurtosis
    skew = summation * 1.0 / np.power(std_dev, 4)
    
    # write to file
    msg = "sumOf_Rs = %d, mean_R = %.03f summation = %.03f std_dev = %.03f skew = %.03f" % \
             (sumOf_Rs, mean_R, summation, std_dev, skew)
#     msg = "sumOf_Rs = %d, mean_R = %.03f" % (sumOf_Rs, mean_R)
    
    
    
    f.write(msg)
    f.write("\n")
    
    # index of max
    idxOf_Max_R = -1
    
    maxOf_R = -1
    
    idx = 0
    
    for d in valsOf_R:
    
        if d > maxOf_R : #if d > maxOf_R
            
            # update : index of max
            idxOf_Max_R = idx
            
            # update : max of Rs
            maxOf_R = d
            
        #/if d > maxOf_R
        
        # increment
        idx += 1
        
    #/for d in valsOf_R:
    
    # write
    msg = "idxOf_Max_R = %d" % \
             (idxOf_Max_R)
#     msg = "sumOf_Rs = %d, mean_R = %.03f" % (sumOf_Rs, mean_R)
    
    
    
    f.write(msg)
    f.write("\n")
    
            #/for d in valsOf_R:

#     sumOf_Rs = get_mean(valsOf_R)
#     
#     mean_R = sumOf_Rs * 1.0 / len(valsOf_R)
    
    '''###################
        dividing line        
    ###################'''
    f.write("\n")
    
    '''###################
        close        
    ###################'''
    f.close()


#/ def test_5():

def test_5():
    
    print("[%s:%d] test_5()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        load : image        
    ###################'''
    dpath_Img = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images"
    fname_Img = "IMG_3171.JPG"
    fpath_Img = "%s/%s" % (dpath_Img, fname_Img)
    
    img = cv2.imread(fpath_Img)
#     img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
     
    '''###################
        get : data
    ###################'''
    # data
    height, width, channels = img2.shape
    off_set = 280
    
    tlabel = libs.get_TimeLabel_Now()
    
    plt_ = plt
    
    
    # save image
    '''###################
        corner : LB        
    ###################'''
    titles = ["clp_LB", "clp_RB", "clp_LU", "clp_RU"]
    
    clips = [
        
            img2[(height - off_set) : height, 0 : off_set], # clp_LB
            img2[(height - off_set) : height, width - off_set : width], # clp_RB
            img2[0 : off_set, 0 : off_set], # clp_LU
            img2[0 : off_set, width - off_set : width], # clp_RU
        ]
    
    '''###################
        max, min        
    ###################'''
    idxOf_Clips = 1
#     idxOf_Clips = 0
    
    clip_0 = clips[idxOf_Clips]
#     clip_0 = clips[0]
    
    max_R = -1; max_G = -1; max_B = -1

    # counter
    cntOf_Row = 0
    cntOf_Cell = 0
    
    # values
    valsOf_R = [0] * 255
    valsOf_G = [0] * 255
    valsOf_B = [0] * 255
    
    colNames = [str(x) for x in range(255)]
#     colNames = [x for x in range(255)]
    
    str_ColNames = "\t".join(colNames)
#     str_ColNames = colNames.join("\t")
    
    for row in clip_0:
        
        for cell in row:
            
            # get value
            R = cell[0]; G = cell[1]; B = cell[2]
            
            # addition
            valsOf_R[R] += 1
            valsOf_G[G] += 1
            valsOf_B[B] += 1
            
            if R > max_R : max_R = R
            if G > max_G : max_G = G
            if B > max_B : max_B = B
            
            # count
            cntOf_Cell += 1
        
        # reset count of cells
        cntOf_Cell = 0
        
        # count
        cntOf_Row += 1
        
    #/for row in clip_0:
    
    '''###################
        log        
    ###################'''
    dpath_Log = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_"
    fname_Log = "2_.log"
    
    fpath_Log = "%s/%s" % (dpath_Log, fname_Log)
    
    f = open(fpath_Log, "a")
    f.write("===================================")
    f.write("\n")
    
    msg = "[%s:%s:%d] result =>" % \
        (libs.get_TimeLabel_Now(), os.path.basename(libs.thisfile()), libs.linenum() \
         )
    f.write(msg)
    f.write("\n")
    
    msg = "file : %s" % \
        (fpath_Img)
    f.write(msg)
    f.write("\n")
        
    msg = "rows, cells : %d x %d" % (cntOf_Row, cntOf_Cell)
    
    f.write(msg)
    f.write("\n")

    # index
    msg = "index of clips : %d (%s)" % (idxOf_Clips, titles[idxOf_Clips])
    
    f.write(msg)
    f.write("\n")

    msg = "min, max : "
    
    f.write(msg)
#     f.write("\n")
    
    msg = "max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B)
    
    f.write(msg)
    f.write("\n")
#     f.write("\n")
    
#     print("[%s:%d] min, max -----------" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
# #     print("max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B))

    '''###################
        vals        
    ###################'''
    msg = "color\t%s" % str_ColNames
    
    f.write(msg)
    f.write("\n")

    lineOf_R = ""
    lineOf_G = ""
    lineOf_B = ""
    
    for i in range(255):
            
        lineOf_R += str(valsOf_R[i]) + "\t"
        lineOf_G += str(valsOf_G[i]) + "\t"
        lineOf_B += str(valsOf_B[i]) + "\t"
        
    #/for i in range(255):
    
    msg = "Rs\t%s" % lineOf_R
    
    f.write(msg)
    f.write("\n")
    
    msg = "Gs\t%s" % lineOf_G
    
    f.write(msg)
    f.write("\n")
    
    msg = "Bs\t%s" % lineOf_B
    
    f.write(msg)
    f.write("\n")
    
    f.write("\n")
    
    '''###################
        close        
    ###################'''
    f.close()


#/ def test_5():

def test_4():
    
    print("[%s:%d] test_4()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        load : image        
    ###################'''
    dpath_Img = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images"
    fname_Img = "IMG_3171.JPG"
    fpath_Img = "%s/%s" % (dpath_Img, fname_Img)
    
    img = cv2.imread(fpath_Img)
#     img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
     
    '''###################
        get : data
    ###################'''
    # data
    height, width, channels = img2.shape
    off_set = 280
    
    tlabel = libs.get_TimeLabel_Now()
    
    plt_ = plt
    
    
    # save image
    '''###################
        corner : LB        
    ###################'''
    titles = ["clp_LB", "clp_RB", "clp_LU", "clp_RU"]
    
    clips = [
        
            img2[(height - off_set) : height, 0 : off_set], # clp_LB
            img2[(height - off_set) : height, width - off_set : width], # clp_RB
            img2[0 : off_set, 0 : off_set], # clp_LU
            img2[0 : off_set, width - off_set : width], # clp_RU
        ]
    
    '''###################
        max, min        
    ###################'''
    clip_0 = clips[0]
    
    max_R = -1; max_G = -1; max_B = -1

    for item in clip_0[0]:
    
        R = item[0]; G = item[1]; B = item[2]
        
        if R > max_R : max_R = R
        if G > max_G : max_G = G
        if B > max_B : max_B = B
            
    #/for item in clip_0[0]:
    
    '''###################
        log        
    ###################'''
    dpath_Log = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_"
    fname_Log = "2_.log"
    
    fpath_Log = "%s/%s" % (dpath_Log, fname_Log)
    
    f = open(fpath_Log, "a")
    f.write("===================================")
    f.write("\n")
    
    msg = "[%s:%s:%d] file : %s" % \
        (libs.get_TimeLabel_Now(), os.path.basename(libs.thisfile()), libs.linenum() \
         , fpath_Img)
    f.write(msg)
    f.write("\n")
        
    msg = "[%s:%s:%d] min, max -----------" % \
        (libs.get_TimeLabel_Now(), os.path.basename(libs.thisfile()), libs.linenum())
    
    f.write(msg)
    f.write("\n")
    
    msg = "max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B)
    
    f.write(msg)
    f.write("\n")
    f.write("\n")
    
#     print("[%s:%d] min, max -----------" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
# #     print("max_R = %d, max_G = %d, max_B = %d" % (max_R, max_G, max_B))

    f.close()


#/ def test_4():

def test_3():
    
    print("[%s:%d] test_3()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        load : image        
    ###################'''
    img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     plt.imshow(img2)
#     
    dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
#     
#     fname = "image.%s.png" % (libs.get_TimeLabel_Now())
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     plt.savefig(fpath)
    
    #ref display image https://github.com/PrinzEugen7/ImageProcessing/blob/master/Image/Python/Matplotlib/draw_opencv_img.py
#     plt.show()
    
    '''###################
        get : data
    ###################'''
    # data
    height, width, channels = img2.shape
    off_set = 280
    
    tlabel = libs.get_TimeLabel_Now()
    
    plt_ = plt
    
    
    # save image
    '''###################
        corner : LB        
    ###################'''
    titles = ["clp_LB", "clp_RB", "clp_LU", "clp_RU"]
    
    clips = [
        
            img2[(height - off_set) : height, 0 : off_set], # clp_LB
            img2[(height - off_set) : height, width - off_set : width], # clp_RB
            img2[0 : off_set, 0 : off_set], # clp_LU
            img2[0 : off_set, width - off_set : width], # clp_RU
        ]
    
    # iterate
    cnt = 0 # counter
    
    for item in titles:

        # file name
        fname = "image.%s.%s.png" % (tlabel, item)
        
        # save fig
        test_2__SaveFig(item, dpath, fname, clips[cnt], plt_)
        
        # clear plot
        plt_.clf()
        
        # count
        cnt += 1
        
    #/for item in titles:

    
#     title = "clp_LB"
#     fname = "image.%s.%s.png" % (tlabel, title)
    
#     clp_LB = img2[(height - off_set) : height, 0 : off_set]
#     h_Clp_LB, w_Clp_LB, ch_Clp_Lb = clp_LB.shape
    
#     test_2__SaveFig(title, dpath, fname, clp_LB, plt_)
    
    '''###################
        corner : RB        
    ###################'''
#     title = "clp_RB"
#     fname = "image.%s.%s.png" % (tlabel, title)
    
#     clp_RB = img2[(height - off_set) : height, width - off_set : width]
    
#     plt_.clf()
#     plt_ = plt
    
#     test_2__SaveFig(title, dpath, fname, clp_RB, plt_)
    
    '''###################
        corner : LU        
    ###################'''
#     title = "clp_LU"
#     fname = "image.%s.%s.png" % (tlabel, title)
    
#     clp_LU = img2[0 : off_set, 0 : off_set]
    
#     plt_.clf()
# #     plt_ = plt
#     
#     test_2__SaveFig(title, dpath, fname, clp_LU, plt_)
    
    '''###################
        corner : RU        
    ###################'''
#     title = "clp_RU"
#     fname = "image.%s.%s.png" % (tlabel, title)
    
#     clp_RU = img2[0 : off_set, width - off_set : width]
    
#     plt_.clf()
# #     plt_ = plt
#     
#     test_2__SaveFig(title, dpath, fname, clp_RU, plt_)
    
    
#     title = "clp_LB"
#      
#     fname = "image.%s.%s.png" % (title, libs.get_TimeLabel_Now())
#      
#     fpath = "%s/%s" % (dpath, fname)
#     
#     xpixels = clp_LB.shape[1]
#     ypixels = clp_LB.shape[0]
#     
#     dpi = 72
#     scalefactor = 1
#     
#     xinch = xpixels * scalefactor / dpi
#     yinch = ypixels * scalefactor / dpi
# 
#     fig = plt.figure(figsize=(xinch,yinch))
#     
#     plt.imshow(clp_LB)
#     
# #     plt.savefig(fpath)
#     plt.savefig(fpath, dpi=dpi)

        
    
#/ def test_2():


def test_2__SaveFig(title, dpath, fname, clp_, plt_):
    
    # save image
#     title = "clp_LB"
     
#     fname = "image.%s.%s.png" % (title, libs.get_TimeLabel_Now())
     
    fpath = "%s/%s" % (dpath, fname)
    
    xpixels = clp_.shape[1]
    ypixels = clp_.shape[0]
    
    dpi = 72
    scalefactor = 1
    
    xinch = xpixels * scalefactor / dpi
    yinch = ypixels * scalefactor / dpi

    fig = plt_.figure(figsize=(xinch,yinch))
    
    plt_.imshow(clp_)
    
#     plt.savefig(fpath)
    plt_.savefig(fpath, dpi=dpi)
    
#/ def test_2():
    
def test_2():
    
    print("[%s:%d] test_2()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        load : image        
    ###################'''
    img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     plt.imshow(img2)
#     
    dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
#     
#     fname = "image.%s.png" % (libs.get_TimeLabel_Now())
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     plt.savefig(fpath)
    
    #ref display image https://github.com/PrinzEugen7/ImageProcessing/blob/master/Image/Python/Matplotlib/draw_opencv_img.py
#     plt.show()
    
    '''###################
        clip        
    ###################'''
    # data
    height, width, channels = img2.shape
    off_set = 280
    
    tlabel = libs.get_TimeLabel_Now()
    
    plt_ = plt
    
    
    # save image
    '''###################
        corner : LB        
    ###################'''
    title = "clp_LB"
    fname = "image.%s.%s.png" % (tlabel, title)
    
    clp_LB = img2[(height - off_set) : height, 0 : off_set]
#     h_Clp_LB, w_Clp_LB, ch_Clp_Lb = clp_LB.shape
    
    test_2__SaveFig(title, dpath, fname, clp_LB, plt_)
    
    '''###################
        corner : RB        
    ###################'''
    title = "clp_RB"
    fname = "image.%s.%s.png" % (tlabel, title)
    
    clp_RB = img2[(height - off_set) : height, width - off_set : width]
    
    plt_.clf()
#     plt_ = plt
    
    test_2__SaveFig(title, dpath, fname, clp_RB, plt_)
    
    '''###################
        corner : LU        
    ###################'''
    title = "clp_LU"
    fname = "image.%s.%s.png" % (tlabel, title)
    
    clp_LU = img2[0 : off_set, 0 : off_set]
    
    plt_.clf()
#     plt_ = plt
    
    test_2__SaveFig(title, dpath, fname, clp_LU, plt_)
    
    '''###################
        corner : RU        
    ###################'''
    title = "clp_RU"
    fname = "image.%s.%s.png" % (tlabel, title)
    
    clp_RU = img2[0 : off_set, width - off_set : width]
    
    plt_.clf()
#     plt_ = plt
    
    test_2__SaveFig(title, dpath, fname, clp_RU, plt_)
    
    
#     title = "clp_LB"
#      
#     fname = "image.%s.%s.png" % (title, libs.get_TimeLabel_Now())
#      
#     fpath = "%s/%s" % (dpath, fname)
#     
#     xpixels = clp_LB.shape[1]
#     ypixels = clp_LB.shape[0]
#     
    #ref https://stackoverflow.com/questions/13623301/convert-contour-matplotlib-or-opencv-to-image-of-the-same-size-as-the-original#13623960
#     dpi = 72
#     scalefactor = 1
#     
#     xinch = xpixels * scalefactor / dpi
#     yinch = ypixels * scalefactor / dpi
# 
#     fig = plt.figure(figsize=(xinch,yinch))
#     
#     plt.imshow(clp_LB)
#     
# #     plt.savefig(fpath)
#     plt.savefig(fpath, dpi=dpi)

        
    
#/ def test_2():

def test_1():
    
    print("[%s:%d] test_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        load : image        
    ###################'''
    img = cv2.imread('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/images/IMG_3171.JPG')
#     img = cv2.imread('../images/IMG_3171.JPG')
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     plt.imshow(img2)
#     
    dpath = "C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/2_image-prog/2_projects/1_sort-out/2_/images"
#     
#     fname = "image.%s.png" % (libs.get_TimeLabel_Now())
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     plt.savefig(fpath)
    
    #ref display image https://github.com/PrinzEugen7/ImageProcessing/blob/master/Image/Python/Matplotlib/draw_opencv_img.py
#     plt.show()
    
    '''###################
        clip        
    ###################'''
    height, width, channels = img2.shape
    
    #debug
    print()
    print("[%s:%d] height = %d, width = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , height, width
        ), file=sys.stderr)
    
    off_set = 280
    clp_LB = img2[(height - off_set) : height, 0 : off_set]
    
    h_Clp_LB, w_Clp_LB, ch_Clp_Lb = clp_LB.shape
    
    #debug
    print()
    print("[%s:%d] h_Clp_LB = %d, w_Clp_LB = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , h_Clp_LB, w_Clp_LB
        ), file=sys.stderr)
    
#     plt.imshow(clp_LB)
    
    # save image
    title = "clp_LB"
     
    fname = "image.%s.%s.png" % (title, libs.get_TimeLabel_Now())
     
    fpath = "%s/%s" % (dpath, fname)
    
    xpixels = clp_LB.shape[1]
    ypixels = clp_LB.shape[0]
    
    dpi = 72
    scalefactor = 1
    
    xinch = xpixels * scalefactor / dpi
    yinch = ypixels * scalefactor / dpi

    fig = plt.figure(figsize=(xinch,yinch))
    
    plt.imshow(clp_LB)
    
#     plt.savefig(fpath)
    plt.savefig(fpath, dpi=dpi)

        
    
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_6()
#     test_5()
#     test_4()
#     test_3()
#     test_2()
#     test_1()
    
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
