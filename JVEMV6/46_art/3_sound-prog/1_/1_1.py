# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\3_\1_\1_1.py
orig : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\1_\1_1.py
at : 2018/03/21 11:55:27


pushd C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\3_\1_
python 1_1.py


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

'''###################
    import : specifics
###################'''
import midi, pretty_midi

'''###################
    import : built-in modules        
###################'''
import getopt, os, inspect, math as math, random as rnd

###############################################
import wave
import struct
import numpy as np
# from pylab import *

from matplotlib import pylab as plt

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

def test_5():
    
    print("[%s:%d] test_5()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    for i in range(128):
    
        name_Inst = pretty_midi.program_to_instrument_name(i)
        
        print("num = %d / %s" % (i, name_Inst))
        
    #/for i in range(127):

    
#/ def test_1():

def test_4():
    
    print("[%s:%d] test_4()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
    # Create a PrettyMIDI object
    cello_c_chord = pretty_midi.PrettyMIDI()
    # Create an Instrument instance for a cello instrument
    cello_program = pretty_midi.instrument_name_to_program('Cello')
    cello = pretty_midi.Instrument(program=cello_program)
    # Iterate over note names, which will be converted to note number later
    for note_name in ['C5', 'E5', 'G5']:
        # Retrieve the MIDI note number for this note name
        note_number = pretty_midi.note_name_to_number(note_name)
        # Create a Note instance for this note, starting at 0s and ending at .5s
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=.5)
        # Add it to our cello instrument
        cello.notes.append(note)
    # Add the cello instrument to the PrettyMIDI object
    cello_c_chord.instruments.append(cello)
    # Write out the MIDI data
    cello_c_chord.write('cello-C-chord.mid')
    
#/ def test_1():

def test_3():
    
    print("[%s:%d] test_3()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
#     fname = "test.%s.mid" % (libs.get_TimeLabel_Now())
    
    pitch_1 = midi.A_4
    pitch_2 = midi.G_4
    pitch_3 = midi.F_4
    pitch_4 = midi.E_4
    pitch_5 = midi.D_4
    pitch_6 = midi.C_4
    pitch_7 = midi.B_4
    
    ps = [
        
        midi.A_4,
        midi.G_4,
        midi.F_4,
        midi.E_4,
        midi.D_4,
        midi.C_4,
        midi.B_4,

    ]
#     ps = [pitch_1, pitch_2, pitch_3, pitch_4]
    
    lenOf_PS = len(ps)
    
    numOf_Notes = 32
    
    # file name
    fname = "test.%s.ps-%02d.notes-%02d.mid" %\
         (libs.get_TimeLabel_Now(), len(ps), numOf_Notes)
    
    
    pattern = midi.Pattern(resolution=960) #このパターンがmidiファイルに対応しています。
    
    track = midi.Track() #トラックを作ります
    pattern.append(track) #パターンに作ったトラックを追加します。
    
    ev = midi.SetTempoEvent(tick=0, bpm=120) #テンポを設定するイベントを作ります
    track.append(ev) #イベントをトラックに追加します。
    
    '''###################
        set : notes        
    ###################'''
    for i in range(numOf_Notes):
#     for i in range(8):
        
        num = rnd.randint(0, lenOf_PS - 1)
        
#         print("[%s:%d] num => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , num
#         ), file=sys.stderr)
#         num = rnd.randint(1, lenOf_PS)
        
        e = midi.NoteOnEvent(tick=0, velocity=100, pitch= ps[num]) #ソの音を鳴らし始めるイベントを作ります。
        track.append(e)
        
        e = midi.NoteOffEvent(tick=960, velocity=100, pitch= ps[num]) #ソの音を鳴らし終えるイベントを作ります。
        track.append(e)
#         e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_1) #ソの音を鳴らし始めるイベントを作ります。
#         track.append(e)
#         
#         e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_1) #ソの音を鳴らし終えるイベントを作ります。
#         track.append(e)
        
    #/for i in range(8):

    '''###################
        track : end        
    ###################'''
    eot = midi.EndOfTrackEvent(tick=1) #トラックを終えるイベントを作ります
    track.append(eot)
    
    midi.write_midifile(fname, pattern) #パターンをファイルに書き込みます。    
    
    '''###################
        read mid        
    ###################'''
#     pattern = midi.read_midifile(fname)
#     
#     print(pattern)
    
#/ def test_1():

def test_2():
    
    print("[%s:%d] test_2()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
    file = "test.%s.mid" % (libs.get_TimeLabel_Now())
    
    pitch_1 = midi.A_4
    pitch_2 = midi.G_4
    
    pattern = midi.Pattern(resolution=960) #このパターンがmidiファイルに対応しています。
    
    track = midi.Track() #トラックを作ります
    pattern.append(track) #パターンに作ったトラックを追加します。
    
    ev = midi.SetTempoEvent(tick=0, bpm=120) #テンポを設定するイベントを作ります
    track.append(ev) #イベントをトラックに追加します。
    
    '''###################
        set : notes        
    ###################'''
#     e = midi.NoteOnEvent(tick=0, velocity=100, pitch=midi.G_4) #ソの音を鳴らし始めるイベントを作ります。
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_1) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_1) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_2) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_2) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_1) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_1) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_2) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_2) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_1) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_1) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch= pitch_2) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch= pitch_2) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    '''###################
        track : end        
    ###################'''
    eot = midi.EndOfTrackEvent(tick=1) #トラックを終えるイベントを作ります
    track.append(eot)
    
    midi.write_midifile(file, pattern) #パターンをファイルに書き込みます。    
    
#/ def test_1():

def test_1():
    
    print("[%s:%d] test_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
    file = "test.mid"

    pattern = midi.Pattern(resolution=960) #このパターンがmidiファイルに対応しています。
    
    track = midi.Track() #トラックを作ります
    pattern.append(track) #パターンに作ったトラックを追加します。
    
    ev = midi.SetTempoEvent(tick=0, bpm=120) #テンポを設定するイベントを作ります
    track.append(ev) #イベントをトラックに追加します。
    
    e = midi.NoteOnEvent(tick=0, velocity=100, pitch=midi.G_4) #ソの音を鳴らし始めるイベントを作ります。
    track.append(e)
    
    e = midi.NoteOffEvent(tick=960, velocity=100, pitch=midi.G_4) #ソの音を鳴らし終えるイベントを作ります。
    track.append(e)
    
    eot = midi.EndOfTrackEvent(tick=1) #トラックを終えるイベントを作ります
    track.append(eot)
    
    midi.write_midifile(file, pattern) #パターンをファイルに書き込みます。    
    
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_5()
#     test_4()
#     test_3()
#     test_2()
#     test_1()
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
