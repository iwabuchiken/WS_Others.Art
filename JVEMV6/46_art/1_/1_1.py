# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\1_\82_1.py
orig : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\1_\1_1.py
at : 2018/02/25 20:55:36


pushd C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\1_\
python 1_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''
###############################################
import sys

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\mm') # libs_mm
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')    # libs_VX7GLZ

from libs_mm import libs

from libs_VX7GLZ import libs_VX7GLZ
from libs_VX7GLZ import wablibs

# from libs.libs import *		#=> C:\WORKS_2\WS\Eclipse_Luna\C_SoundProg\python\libs
# import libs.libs as lib
# from libs.libs import *		#=> in 'libs' subdirectory --> see : https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory 'community wiki'
    						#=> ref : http://qiita.com/Usek/items/86edfa0835292c80fff5
# from libs import *		#=> in 'libs' subdirectory --> see : https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory 'community wiki'
    					#=> libs.py : C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1\libs.py



# import libs.labs2 as labs
# # import libs.labs as labs
# 
# import libs.wablibs as wl
# import wablibs
# import wablibs as wl

'''###################
    import : built-in modules        
###################'''
import getopt
import os
import inspect

import math as math

###############################################
import wave
import struct
import numpy as np
# from pylab import *

from matplotlib import pylab as plt

import random as rnd

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

def test_2():
    
    A = 1     #振幅
    fs = 16000 #サンプリング周波数
#     fs = 8000 #サンプリング周波数
    f0 = 392  #周波数
#     f0 = 262  #周波数
#     f0 = 440  #周波数
    sec = 5   #秒
    
    phase_Param = 0
#     phase_Param = 4
    
    phase = np.pi * 0
#     phase = f0 * (4 / 2)
#     phase = f0 / 2
    
    # bin data
    phase = np.pi * ( 1 / 4 )
    pow_Param = 1
    scalar_Param = 2
    
    binwave = wablibs.gen_WaveData(fs, f0, phase, sec, A, pow_Param, scalar_Param)
#     binwave = gen_WaveData(fs, f0, phase, sec, A)
    
#     #サイン波をwavファイルとして書き出し
    wave_Params = (1, 2, fs, len(binwave), 'NONE', 'not compressed')
#     wave_Params = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')

    '''###################
        dirs, paths        
    ###################'''
    dname_Audios = "data.46_1\\audios"
    
    graph_Type = "sin"
    
    if not os.path.isdir(dname_Audios) : os.makedirs(dname_Audios)

#     fname_Out = "audio/output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
    
#     fname_Out = "%s\\output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
    fname_Out = "%s\\output_%s.%s.fs-%d_f0-%d.(phase-%s)(pow-%.1f)(scalar-%.1f)(sec-%d).wav" % \
                (dname_Audios
                , libs.get_TimeLabel_Now()
                , graph_Type
                , fs, f0
                , "%.1fpi" % (phase / np.pi)
                , pow_Param
                , scalar_Param
#                 , "%1.2f" % (phase_Param / 4.0) + "pi"
                , sec)

    '''###################
        save        
    ###################'''
    wablibs.save_Wave(fname_Out, wave_Params, binwave)
#     save_Wave(fname_Out, wave_Params, binwave)
    
    print()
    print("[%s:%d] save wave => done : %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Out
        ), file=sys.stderr)
        
#/ def test_1():

def test_1():
    
    A = 1     #振幅
    fs = 16000 #サンプリング周波数
#     fs = 8000 #サンプリング周波数
    f0 = 392  #周波数
#     f0 = 262  #周波数
#     f0 = 440  #周波数
    sec = 5   #秒
    
    phase_Param = 0
#     phase_Param = 4
    
    phase = f0 * (phase_Param / 2)
#     phase = f0 * (4 / 2)
#     phase = f0 / 2
    
    # bin data
    phase = np.pi * ( 1 / 4 )
    
    binwave = wablibs.gen_WaveData(fs, f0, phase, sec, A)
#     binwave = gen_WaveData(fs, f0, phase, sec, A)
    
#     #サイン波をwavファイルとして書き出し
    wave_Params = (1, 2, fs, len(binwave), 'NONE', 'not compressed')
#     wave_Params = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')

    '''###################
        dirs, paths        
    ###################'''
    dname_Audios = "data.46_1\\audios"
    
    if not os.path.isdir(dname_Audios) : os.makedirs(dname_Audios)

#     fname_Out = "audio/output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
    
    fname_Out = "%s\\output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
                (dname_Audios
                , libs.get_TimeLabel_Now()
                , fs, f0
                , "%1.2f" % (phase_Param / 4.0) + "pi", sec)

    '''###################
        save        
    ###################'''
    wablibs.save_Wave(fname_Out, wave_Params, binwave)
#     save_Wave(fname_Out, wave_Params, binwave)
    
    print()
    print("[%s:%d] save wave => done : %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Out
        ), file=sys.stderr)
        
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_2()
#     test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print ("[%s:%d] exec_prog" % (thisfile(), linenum()))
    
#     #debug
#     return
    
    
#     A = 1     #振幅
#     fs = 16000 #サンプリング周波数
# #     fs = 8000 #サンプリング周波数
#     f0 = 392  #周波数
# #     f0 = 262  #周波数
# #     f0 = 440  #周波数
#     sec = 5   #秒
#     
#     phase_Param = 4
#     
#     phase = f0 * (phase_Param / 2)
# #     phase = f0 * (4 / 2)
# #     phase = f0 / 2
#     
#     # bin data
#     binwave = gen_WaveData(fs, f0, phase, sec, A)
#     
# #     #サイン波をwavファイルとして書き出し
#     wave_Params = (1, 2, fs, len(binwave), 'NONE', 'not compressed')
# #     wave_Params = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
# 
#     '''###################
#         dirs        
#     ###################'''
#     dname_Audios = "data.46_1\\audios"
#     
#     if not os.path.isdir(dname_Audios) : os.makedirs(dname_Audios)
# 
# #     fname_Out = "audio/output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
#     fname_Out = "%s\\output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
#                 (dname_Audios
#                 , libs.get_TimeLabel_Now()
#                 , fs, f0
#                 , "%1.2f" % (phase_Param / 4.0) + "pi", sec)
# #     fname_Out = "audios/output_%s.sin.fs-%d_f0-%d_phase-%s_sec-%d.wav" % \
# #                 (libs.get_TimeLabel_Now(), fs, f0, "%1.2f" % (phase_Param / 4.0) + "pi", sec)
# #                 (get_TimeLabel_Now(), fs, f0, "%1.2f" % (phase_Param / 4.0) + "pi", sec)
# #     fname_Out = "audio/output_%s.sin.fs-%d_f0-%d_phase-%d_sec-%d.wav" % \
# #                 (get_TimeLabel_Now(), fs, f0, phase, sec)
#     
#     save_Wave(fname_Out, wave_Params, binwave)
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
