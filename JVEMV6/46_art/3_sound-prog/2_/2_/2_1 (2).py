# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\3_sound-prog\2_\2_\2_1.py
orig : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\3_sound-prog\2_\1_\1_1.py
at : 2018/03/21 11:55:27


pushd C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\3_sound-prog\2_\2_\
python 2_1.py


'''
from __future__ import print_function

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

'''###################
    import : specifics
###################'''
# import midi, pretty_midi

'''###################
    import : built-in modules        
###################'''
import getopt, os, inspect, math as math, random as rnd

###############################################
import wave, struct
import numpy as np
# from pylab import *

from matplotlib import pylab as plt

#ref http://nbviewer.jupyter.org/github/librosa/librosa/blob/master/examples/LibROSA%20demo.ipynb
# import librosa
# We'll need numpy for some mathematical operations
import numpy as np

# matplotlib for displaying the output
import matplotlib.pyplot as plt
import matplotlib.style as ms
# ms.use('seaborn-muted') % matplotlib inline

# and IPython.display for audio output
# import IPython.display

# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display
# import random as rnd

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

def show_WavInfos(fpath):
    
    wr = wave.open(fpath, "rb")
    
    '''###################
        infos        
    ###################'''
    print("[%s:%d] file : %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath
        ), file=sys.stderr)
    
    print("channel : ", wr.getnchannels())
    print("sample size : ", wr.getsampwidth())
    print("getframerate() : ", wr.getframerate())
    print("getnframes() : ", wr.getnframes())
    print("getnframes() : ", wr.getparams())
    
    nchan = wr.getparams()
    
    print("nchan => %s (type = %s)" % (nchan, type(nchan)))
            #     type = <class 'wave._wave_params'>

#/ def show_WavInfos(fpath):

def test_2():
    
    fpath = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\3_sound-prog\\2_\\2_\\data\\audio.wav"
    
#     wr = wave.open(fpath, "rb")
    
    show_WavInfos(fpath)
    
#/ def test_2():

def test_1():
    
    print("[%s:%d] test_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #ref https://librosa.github.io/librosa/tutorial.html    
    # 1. Get the file path to the included audio example
    filename = librosa.util.example_audio_file()
    
    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(filename)
    
    # 3. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    print("[%s:%d] file => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , filename
        ), file=sys.stderr)
    print("[%s:%d] tempo = %0.2f / len(beat_frames) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , tempo, len(beat_frames)
        ), file=sys.stderr)
    
#     print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
    
    # 4. Convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    print('Saving output to beat_times.csv')
    librosa.output.times_csv('beat_times.csv', beat_times)
    
    '''###################
        file : 2        
    ###################'''
    filename = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\3_sound-prog\\2_\\2_\\data\\audio.wav"
    
    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(filename)
    
    # 3. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    print("[%s:%d] file => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , filename
        ), file=sys.stderr)
    print("[%s:%d] tempo = %0.2f / len(beat_frames) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , tempo, len(beat_frames)
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
