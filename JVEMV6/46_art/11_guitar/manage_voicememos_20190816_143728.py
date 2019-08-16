# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\manage_voicememos_20190816_143728.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\others\voice_recog.py
at : 2019/08/16 14:38:58

r d4
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\
python manage_voicememos_20190816_143728.py


'''
###############################################
import sys, os, shutil

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\mm') # libs_mm
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')    # libs_VX7GLZ

from libs_mm import libs


'''###################
    vars : global
###################'''
SWITCH_DEBUG = False

'''###################
    funcs
###################'''
def show_Message() :
    
    msg = '''
    manage voice memos'''
    
    print (msg)

def test_1():

    '''###################
        step: 1
            vars
    ###################'''
    dpath_Main = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\11_guitar"
    
    dpath_Target_Dir = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\11_guitar\\for_conversion.dir"
    
    fname_ListOf_Data = "list_of_data.dat"
    
    '''###################
        step: 2
            get : list of : dir list in dpath_Target_Dir
    ###################'''
    strOf_M4A_Ext = "m4a"
    
    #ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    #ref https://www.tutorialspoint.com/python/string_endswith.htm
    lo_Source_M4A_Files = [f for f in os.listdir(dpath_Target_Dir) if f.endswith(strOf_M4A_Ext)]
    
    if SWITCH_DEBUG == True :
    
        #debug
        msg = "[%s:%d] lo_Source_M4A_Files ==> " % (os.path.basename(libs.thisfile()), libs.linenum())
             
        print("%s" % (msg), file=sys.stderr)
        
        print(lo_Source_M4A_Files)
        print("total : %d" % len(lo_Source_M4A_Files))
        
    '''###################
        step: 3
            build : list of final fnames set
    ###################'''
    '''###################
        step: 3 : 1
            dat file : read lines
    ###################'''
    # file : open
    f_in_dat = open(os.path.join(dpath_Target_Dir, fname_ListOf_Data), "r")
    
    lo_Dat_File_Lines = f_in_dat.readlines()
    
    if SWITCH_DEBUG == True :
        
        #debug
        msg = "[%s:%d] lo_Dat_File_Lines ==> " % (os.path.basename(libs.thisfile()), libs.linenum())
             
        print("%s" % (msg), file=sys.stderr)
        
        print(lo_Dat_File_Lines)
        print("total : %d" % len(lo_Dat_File_Lines))

    '''###################
        step: 3 : X
            close : file
    ###################'''
    # file : open
    f_in_dat.close()

    '''###################
        step: 3 : 2
            build : each line ==> tokenise
    ###################'''
    lo_Dat_File_Lines__Tokenized = []
    
    for item in lo_Dat_File_Lines:
    
        lo_Dat_File_Lines__Tokenized.append((item.strip()).split("\t"))
#         lo_Dat_File_Lines__Tokenized.append(item.split("\t"))
        
    #/for item in lo_Dat_File_Lines:
    
    if SWITCH_DEBUG == True :
        
        #debug
        msg = "[%s:%d] lo_Dat_File_Lines__Tokenized ==> " % (os.path.basename(libs.thisfile()), libs.linenum())
             
        print("%s" % (msg), file=sys.stderr)
        
        for item in lo_Dat_File_Lines__Tokenized:
        
            print(item)
            
        #/for item in lo_Dat_File_Lines__Tokenized:

        print("total : %d" % len(lo_Dat_File_Lines__Tokenized))
    
    #_20190816_153352:tmp

    '''###################
        step: 3 : 3
            build : lo_Final
    ###################'''
    lo_Final = []
    
    for item in lo_Dat_File_Lines__Tokenized:
    
        # item ==> ['21', '20190815 180358.m4a', 'g-0815-6']
        lenOf_Item = len(item)
        
        if lenOf_Item == 3 : #if lenOf_Item == 3
            
            # new file name
            tokens = item[1].split(".")   # 20190815 171714.m4a
            
            tokens_2 = tokens[0].split(" ") #=> "20190815" "171714"
            
            fname_New = "%s.[%s_%s].m4a" % (item[2], tokens_2[0], tokens_2[1])
#             fname_New = "%s.[%s].m4a" % (item[2], item[1])
            
            # build the final set
            setOf_Final_Entries = [
                    
                    item[1]     # '20190815 180358.m4a' (source file name)
                    , fname_New
#                     , "%s.[%s].m4a" % (item[2], item[1])
                                   
                                   ]
            
            # append
            lo_Final.append(setOf_Final_Entries)
        
        #/if lenOf_Item == 3

        
    #/for item in lo_Dat_File_Lines__Tokenized:

    #debug
    msg = "[%s:%d] lo_Final ==> "
         
    print("%s" % (msg), file=sys.stderr)
    
    for item in lo_Final:
    
        print(item)
        
    #/for item in lo_Dat_File_Lines__Tokenized:

    print("total : %d" % len(lo_Final))
    
    '''###################
        step: 4
            copy : new files
    ###################'''
    cntOf_Copy = 0
    
    for item in lo_Final:
    
        #_20190816_154557:tmp
        
        # fpath : src
        fpath_Src = os.path.join(dpath_Target_Dir, item[0])
        fpath_Dst = os.path.join(dpath_Target_Dir, item[1])
        
        #ref https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
        res = shutil.copyfile(fpath_Src, fpath_Dst)
            # [manage_voicememos_20190816_143728.py:203] res => C:\WORKS_2\WS\WS_Others.Art\JV
            # EMV6\46_art\11_guitar\for_conversion.dir\g-0815-5.[20190815_174452].m4a


#         msg = "[%s:%d] res => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum(), res)
#              
#         print("%s" % (msg), file=sys.stderr)
        
        # count
        cntOf_Copy += 1
        
    #/for item in lo_Final:

#     if True :
        
    #debug
    msg = "[%s:%d] cntOf_Copy ==> %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), cntOf_Copy)
         
    print("%s" % (msg), file=sys.stderr)
    
#     for item in lo_Dat_File_Lines__Tokenized:
#     
#         print(item)
#         
#     #/for item in lo_Dat_File_Lines__Tokenized:
# 
#     print("total : %d" % len(lo_Dat_File_Lines__Tokenized))

    
#     '''###################
#         step: 3 : X
#             close : file
#     ###################'''
#     # file : open
#     f_in_dat.close()


    msg = "[%s:%d] test_1 : done" % \
        (os.path.basename(libs.thisfile()), libs.linenum())
         
    print("%s" % (msg), file=sys.stderr)
        
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
