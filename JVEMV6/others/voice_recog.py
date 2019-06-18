# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\others\voice_recog.py
orig : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\1_\82_1.py
at : 2018/10/08 15:30:46

r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\others\
python voice_recog.py

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

# from libs_VX7GLZ import libs_VX7GLZ
# from libs_VX7GLZ import wablibs

# from libs.libs import *        #=> C:\WORKS_2\WS\Eclipse_Luna\C_SoundProg\python\libs
# import libs.libs as lib
# from libs.libs import *        #=> in 'libs' subdirectory --> see : https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory 'community wiki'
                            #=> ref : http://qiita.com/Usek/items/86edfa0835292c80fff5
# from libs import *        #=> in 'libs' subdirectory --> see : https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory 'community wiki'
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

import requests

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
    -v    Volume down the amplitude --> 1.0 * v / 1000
    -f    Base frequency ---> e.g. 262 for the A tone
    -p    Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
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

def test_1():
    
    #ref https://qiita.com/kinpira/items/75513eaab6eed19da9a3
#     path = 'audio_sample_amivoice.raw'
    path = '20181008 151334.16bit-16khz.aiff'
#     path = '20181008 151334.16bit-16khz.wav'
#     path = '20181008-151334.wav'
#     path = '/home/pi/test.wav'
    
    #APIKEY = "58362f467950765273456f4652485a516c6258465a75794e79794a4835386869412f33576876774c767631"
    APIKEY = "71596d4e512e752e4e7a44507463445767694c70485254485251674174384c4a33576a7253457478495431"
    
    #ref https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_name=speech_recognition&p_name=api_amivoice_1#tag01
#     https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize
    
    url = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY={}".format(APIKEY)

    print("[%s:%d] url = %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum()
                                , url
                                ), file=sys.stderr)
    
    print("[%s:%d] path = %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum()
                                , path
                                ), file=sys.stderr)
    
        #     [voice_recog.py:148] 
        # url = https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY=58362f467950765273456f4652485a516c6258465a75794e79794a4835386869412f33576876774c767631
    
    # validate
#     f = open(path, "rb")
    
    if not os.path.isfile(path) : #if のｔos.path.isfile(path)

        print("[%s:%d] file not exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , path
            ), file=sys.stderr)
        
        return
    
    #/if のｔos.path.isfile(path)


    
    
    files = {"a": open(path, 'rb'), "v":"on"}
    
    r = requests.post(url, files=files)
    
    print("r =>")
    print(r)
    
            #     r =>
            # <Response [401]>

#     print (r.json())
#     print (r.json()['text'])
    
        #     r =>
        # <Response [200]>
        # {'utteranceid': '20181008/docomo-dds-test@1841153612-LOHwlMQ', 'results': [{'end
        # time': 6410, 'tokens': [{'endtime': 1970, 'confidence': 0.87, 'spoken': 'はー',
        # 'starttime': 1430, 'written': 'はあ'}, {'endtime': 2240, 'confidence': 0.3, 'spo
        # ken': '_', 'starttime': 1970, 'written': '。'}, {'endtime': 2710, 'confidence':
        # 0.67, 'spoken': 'はー', 'starttime': 2240, 'written': 'はあ'}, {'endtime': 2900,
        #  'confidence': 0.86, 'spoken': '_', 'starttime': 2710, 'written': '。'}, {'endti
        # me': 4130, 'confidence': 0.94, 'spoken': 'か', 'starttime': 3600, 'written': '下
        # '}, {'endtime': 4850, 'confidence': 1.0, 'spoken': 'か', 'starttime': 4340, 'wri
        # tten': 'か'}, {'endtime': 5540, 'confidence': 0.99, 'spoken': 'か', 'starttime':
        #  5080, 'written': '下'}, {'endtime': 6120, 'confidence': 0.99, 'spoken': 'か', '
        # starttime': 5590, 'written': 'か'}, {'endtime': 6410, 'confidence': 0.22, 'spoke
        # n': '_', 'starttime': 6120, 'written': '。'}], 'rulename': '', 'confidence': 0.6
        # 39, 'tags': [], 'starttime': 0, 'text': 'はあ。はあ。下か下か。'}], 'message': '
        # ', 'code': '', 'text': 'はあ。はあ。下か下か。'}
    
    # get keys
    #ref https://stackoverflow.com/questions/15789059/python-json-only-get-keys-in-first-level#15789236
    json = r.json()
    
    keys = json.keys()
    
    for item in keys:
    
        print(item)
        
    #/for item in keys:
    
    for item in keys:
        
        print("%s =>" % item)
        print(json[item])
            
        #/for item in keys:

    # results
    print()
    
    results = json['results']
    
#     keys_results = results.keys()
    
#     print("tokens => %d tokens" % len(results[0]['tokens']))
#     print(results[0]['tokens'])
    
    for item in results[0]['tokens']:
    
        print(item)
        
    #/for item in results[0]['tokens']:
            # {'starttime': 1430, 'endtime': 1970, 'confidence': 0.87, 'spoken': 'はー', 'writ
            # ten': 'はあ'}
            # {'starttime': 1970, 'endtime': 2240, 'confidence': 0.3, 'spoken': '_', 'written'
            # : '。'}
            # {'starttime': 2240, 'endtime': 2710, 'confidence': 0.67, 'spoken': 'はー', 'writ
            # ten': 'はあ'}
            # {'starttime': 2710, 'endtime': 2900, 'confidence': 0.86, 'spoken': '_', 'written
            # ': '。'}
            # {'starttime': 3600, 'endtime': 4130, 'confidence': 0.94, 'spoken': 'か', 'writte
            # n': '下'}
            # {'starttime': 4340, 'endtime': 4850, 'confidence': 1.0, 'spoken': 'か', 'written
            # ': 'か'}
            # {'starttime': 5080, 'endtime': 5540, 'confidence': 0.99, 'spoken': 'か', 'writte
            # n': '下'}
            # {'starttime': 5590, 'endtime': 6120, 'confidence': 0.99, 'spoken': 'か', 'writte
            # n': 'か'}
            # {'starttime': 6120, 'endtime': 6410, 'confidence': 0.22, 'spoken': '_', 'written
            # ': '。'}
    
# #     for item in keys_results:
#     for item in results:
#             
#         print(item)
#         
# #         print("[%s:%d] keys_results : %s" % \
# #                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                 , item
# #                 ), file=sys.stderr)
        
    #/for item in keys_results:

    
#     for item in json['results']:
#         
#         print(item)
#         
#     #/for item in json['results']:

    
    print("[%s:%d] test_1 : done" % \
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
