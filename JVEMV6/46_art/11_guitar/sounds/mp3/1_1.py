# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\sounds\mp3\1_1.py
orig : C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\1_\82_1.py
at : 2018/06/29 15:11:08


pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\sounds\mp3
python 1_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''
###############################################
import sys
from pandas.compat import str_to_bytes
from numpy.distutils.from_template import item_re

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects') # libs_mm

from libs_admin import libs

'''###################
    import : built-in modules        
###################'''
# import getopt
import os, glob
# import inspect

import math as math

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

def test_1():
    
    '''###################
        list : file names in the dir        
    ###################'''
    dpath = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\11_guitar\\sounds\\mp3"
    
    fpath_Glob = "%s\\*.mp3" % (dpath)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    lo_Files = [os.path.basename(x) for x in lo_Files]
    
    #ref https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python answered Mar 24 '09 at 16:43
    lo_Files_Trunk = [os.path.splitext(os.path.basename(x))[0] for x in lo_Files]
#     lo_Files_Trunk = [os.path.splitext(x)[0] for x in lo_Files]

    lo_Name_Sets = list(zip(lo_Files, lo_Files_Trunk))

    # report
    print()
    print("[%s:%d] lo_Name_Sets =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    for item in lo_Name_Sets:
    
        print(item)
        
    #/for item in lo_Name_Sets:

    '''###################
        list : file names in the text file        
    ###################'''
    fname_ListFile = "list-of-new-file-names.txt"
    
    fpath_ListFile = "%s\\%s" % (dpath, fname_ListFile)
    
#     #debug
#     print()
#     print("[%s:%d] fpath_ListFile => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , fpath_ListFile
#             ), file=sys.stderr)
#     return
    
    fin = open(fpath_ListFile, "r")
    
    lo_FileName_Final = []
    
    lo_file_Lines = []
    
    lo_file_Lines = fin.readlines()
    
    #ref strip https://hydrocul.github.io/wiki/programming_languages_diff/string/trim.html
    lo_file_Lines = [x.strip() for x in lo_file_Lines]
    
    print()
    print("[%s:%d] lo_file_Lines =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_file_Lines)
    
    lo_file_Lines_Trunk = [x.split(".") for x in lo_file_Lines]
    
    print()
    print("[%s:%d] lo_file_Lines_Trunk =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_file_Lines_Trunk)

#     return    

    lo_file_Lines_Trunk = [x[0] for x in lo_file_Lines_Trunk]

    print()
    print("[%s:%d] lo_file_Lines_Trunk ('x[0] for x in ...') =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_file_Lines_Trunk)

    lo_file_Lines_Trunk = [x.split(" ") for x in lo_file_Lines_Trunk]
#     lo_file_Lines_Trunk = [x.split("_") for x in lo_file_Lines_Trunk]
    lo_file_Lines_Trunk = [x[0] + "_" + x[1] for x in lo_file_Lines_Trunk]
#     lo_file_Lines_Trunk = [x[0] + " " + x[1] for x in lo_file_Lines_Trunk]
#     lo_file_Lines_Trunk = [(x[0], x[1]) for x in lo_file_Lines_Trunk]
    
    print()
    print("[%s:%d] lo_file_Lines_Trunk (modified) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_file_Lines_Trunk)
    
    # zip
    lo_file_Lines = list(zip(lo_file_Lines, lo_file_Lines_Trunk))
    
    print()
    print("[%s:%d] lo_file_Lines =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            ), file=sys.stderr)
     
    for item in lo_file_Lines:
    
        print(item)
        
    #/for item in lo_file_Lines:
    
    '''###################
        judge        
    ###################'''
    lenOf_Name_Sets = len(lo_Name_Sets)
    
    cntOf_Changed_Files = 0
    
    # file
    fpath_Log = os.path.join(dpath, "ops.log")
    
    f_log = open(fpath_Log, "a")
    
    f_log.write("[%s / %s:%d]=======================" % \
                (libs.get_TimeLabel_Now()
                 , os.path.basename(libs.thisfile())
                 , libs.linenum()))
    
    f_log.write("\n")
    
    for i in range(lenOf_Name_Sets):
    
        name_Set = lo_Name_Sets[i]
        
        
        for item in lo_file_Lines:
    
            # judge
            if name_Set[1] == item[1] : #if name_Set[1] == item[1]
                
                msg = "[%s / %s:%d] change file name => name_Set[1] = %s, item[1] = %s" % \
                    (libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile())
                    , libs.linenum()
                    , name_Set[1], item[1]
                    )

                print()
                print(msg, file=sys.stderr)
#                 print("[%s:%d] change file name => name_Set[1] = %s, item[1] = %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , name_Set[1], item[1]
#                     ), file=sys.stderr)
                
                f_log.write(msg)
                f_log.write("\n")
                
                msg = "from : %s / to : %s" % (name_Set[0], item[0])
                print(msg)
#                 print("from : %s / to : %s" % (name_Set[0], item[0]))
                
                f_log.write(msg)
                f_log.write("\n")
                
                # rename
                fpath_Curr = os.path.join(dpath, name_Set[0])
                fpath_New = os.path.join(dpath, item[0])
                
                #ref rename https://qiita.com/clarinet758/items/307d01a6634b372e8fa9
                os.rename(fpath_Curr, fpath_New)
                
                # count
                cntOf_Changed_Files += 1
                
                break
                
            #/if name_Set[1] == item[1]

    
            
        #/for item in lo_file_Lines:

    #/for i in range(lenOf_Name_Sets):
    
    # write count
    f_log.write("renamed : %d files" % cntOf_Changed_Files)
    
    f_log.write("\n")
    
    f_log.write("\n")   # <= spacer line
    
    # close log file
    f_log.close()
    
    '''###################
        report        
    ###################'''
    print()
    print("[%s:%d] cntOf_Changed_Files => %d" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , cntOf_Changed_Files
                    ), file=sys.stderr)
     
#     print(lo_file_Lines)
    
#     #debug
#     return
    
    
#     print()
#     print("[%s:%d] lo_file_Lines =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     print(lo_file_Lines)
#     
#     fin.close()
# 
#     # edit
#     lenOf_Name_Sets = len(lo_Name_Sets)
#     lenOf_file_Lines = len(lo_file_Lines)
#     
#     print()
#     print("[%s:%d] lenOf_Name_Sets = %d, lenOf_file_Lines = %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , lenOf_Name_Sets, lenOf_file_Lines
#                 ), file=sys.stderr)
#     
#     for i in range(lenOf_Name_Sets):
#     
#         name_Set = lo_Name_Sets[i]
#         
#         print()
#         print("[%s:%d] name_Set => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , name_Set
#             ), file=sys.stderr)
#         
#         # judge
#         for file_Line in lo_file_Lines:
#     
#             file_Line = lo_file_Lines[i]
#             
#             temp_Tlabel = file_Line.split(".")[0]
#             
#             tokens = temp_Tlabel.split("_")
#             
#             str_Tokens = tokens[0] + " " + tokens[1]
#             
# #             print(str_Tokens)
#             
#             # judge
# #             if str_Tokens == name_Set : #if str_Tokens == name_Set
#             if str_Tokens == name_Set[1] : #if str_Tokens == name_Set
#     
# #                 print()
# #                 print("[%s:%d] hit => str_Tokens = %s, name_Set = %s, file_Line = %s" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         , str_Tokens, name_Set, file_Line
# #                         ), file=sys.stderr)
#                 
# #                 # change file name
# #                 print()
# #                 print("[%s:%d] change file name : from => %s / to => %s" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     , name_Set[0], file_Line
# #                     ), file=sys.stderr)
#                 
#                 # change
#                 #ref join https://stackoverflow.com/questions/7132861/building-full-path-filename-in-python#7133204
#                 fpath_Curr = os.path.join(dpath, name_Set[0])
#                 fpath_New = os.path.join(dpath, file_Line)
#                 
#                 # validate
#                 res = os.path.isfile(fpath_Curr)
#                 
#                 print()
#                 print("[%s:%d] fpath_Curr exists? (%s) ==> %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , fpath_Curr, res
#                         ), file=sys.stderr)
#                 
#                 # rename
#                 if res : 
#                     
#                     os.rename(fpath_Curr, file_Line)
#                     
#                     print()
#                     print("[%s:%d] renamed => %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , file_Line
#                         ), file=sys.stderr)
#                 
#                 else :
#                     
#                     print()
#                     print("[%s:%d] file not exists : %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , fpath_Curr
#                         ), file=sys.stderr)
# #                 os.rename(fpath_Curr, fpath_New)
#                 
# #                 os.rename(name_Set[0], file_Line)
#                 
#                 continue
#                 
#             #/if str_Tokens == name_Set
#     
#     
#             
#             
#         #/for file_Line in lo_file_Lines:
# 
#         
#         
#     #/if str_Tokens == 
#     
#     
#         
#         
#         
# #         print(tokens)
#         
#     #/for i in range(lenOf_Name_Sets):



#     print()
#     print("[%s:%d] len(lo_Files) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(lo_Files)
#         ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] lo_Files_Trunk =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print(lo_Files_Trunk)
    
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
#     test_2()
    test_1()
    
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
