# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\2_image-prog\1_gimp\1_\1_1.py
orig : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\3_sound-prog\2_\1_\1_1.py
at : 2018/03/21 11:55:27

C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\46_art\\2_image-prog\\1_gimp\\1_
C:/WORKS_2/WS/WS_Others/JVEMV6/46_art/2_image-prog/1_gimp/1_/1_1.py

pushd C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\2_image-prog\1_gimp\1_\
python 1_1.py


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

def test_1():
    
    print(os.getcwd())
    
    
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
