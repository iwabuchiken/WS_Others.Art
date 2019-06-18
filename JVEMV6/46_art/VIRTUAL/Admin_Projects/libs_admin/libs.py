'''
    file    : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\libs_admin\libs.py
    orig    : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libs.py
    at      : 2018/05/22 10:46:35
'''

import inspect
import os
import sys

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
# from __builtin__ import str
from sympy.physics.vector.printing import params

from enum import Enum

from libs_admin import cons_ip

'''#########################################################
    enums        
#########################################################'''
class TimeLabel(Enum):
    
    STRING_TYPE_BASIC = "basic"
    STRING_TYPE_SERIAL = "serial"

'''#########################################################
    functions        
#########################################################'''
def linenum(depth=0):
#     print "line"
    
    #ref https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number 'answered Jul 25 '11 at 1:31'
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                        # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
#     return info.filename                       # __FILE__     -> Test.py
    #     print info.filename                       # __FILE__     -> Test.py
    #     print info.function                       # __FUNCTION__ -> Main
    #     print info.lineno                         # __LINE__     -> 13
    return info.lineno                         # __LINE__     -> 13

    
    '''
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno
    
    '''

def thisfile(depth=0):
# def _file(depth=0):
#     print "line"

    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    return info.filename                       # __FILE__     -> Test.py
#     print info.filename                       # __FILE__     -> Test.py
#     print info.function                       # __FUNCTION__ -> Main
#     print info.lineno                         # __LINE__     -> 13
    
    '''    
        frame = inspect.currentframe(0)
    #     frame = inspect.currentframe(depth+1)
        
        return os.path.basename(frame.f_code.co_filename)
    #     return frame.f_code.co_filename
    '''
#/def thisfile(depth=0):

def get_opt(arg_ary):
    
#     print "[%s:%d] args =>" % (thisfile(), linenum())
    
#     print arg_ary
    
    # validate
    if len(arg_ary) < 1 :
        
        print ("[%s:%d] no args" % (thisfile(), linenum()))
        
        return (None, None)
    
    # return tuple
    result = []
    # loop
    for elem in arg_ary :
        
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
        if elem.startswith('-E') and len(elem) > 2 :
            
            #ref append https://stackoverflow.com/questions/1878470/add-tuple-to-list-of-tuples-in-python
            #ref slice http://www.pythonweb.jp/tutorial/string/index11.html
            result.append(('-E', elem[2:]))
    
        elif elem.startswith('-s') and len(elem) > 2 :
            
            result.append(('-s', elem[2:]))
    
        elif elem.startswith('-e') and len(elem) > 2 :
            
            result.append(('-e', elem[2:]))
    
        elif elem.startswith('-t') and len(elem) > 2 :
            
            result.append(('-t', elem[2:]))
    
        elif elem.startswith('-V') and len(elem) > 2 :
            
            result.append(('-V', elem[2:]))
    
        elif elem.startswith('--') and len(elem) > 2 :
            
            if elem == '--PLOT_GO' :
                
                result.append(('PLOT_GO', ''))
#                 result.append('PLOT_GO')
    
            elif elem == '--SAVE_IMAGE_GO' :
                
                result.append(('SAVE_IMAGE_GO', ''))
    
    return result

'''###################
    get_opt_2(arg_ary, keychars)
    
    at : 2018/01/22 07:28:58
    
    <Usage>
    [Code]
        arg_ary = sys.argv
        keychars = "l"
    
        result = get_opt_2(arg_ary, keychars)
    
    [Console]
        python ..\libs\cp_log.py -labcde
        
        ("python" command string ---> MUST)
    
    @return: [('-l', 'abcde')]
           
    @param keychars: if None ---> ['a','b','c',...,'z','A','B',...,'Z']
###################'''
def get_opt_2(arg_ary, keychars = None):
    
    
    # validate
    if len(arg_ary) < 1 :
        
        print ("[%s:%d] no args" % (thisfile(), linenum()))
        
        return (None, None)
    
    '''###################
        validate : keychars        
    ###################'''
    if keychars == None : #if keychars == None

        ab = "abcdefghijklmnopqrstuvwxyz"
        
        #ref https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters
        keychars = list(ab + ab.upper())
        
#         print()
#         print ("[%s:%d] keychars => %s" % (os.path.basename(thisfile()), linenum(), keychars))
    
#         return None
    #/if keychars == None
    
    # return tuple
    result = {}
#     result = []
    # loop
    for elem in arg_ary :
        
#         print()
#         print ("[%s:%d] elem => %s" % (os.path.basename(thisfile()), linenum(), elem))
#         
#         print()
        
        
#         print "[%s:%d] elem = '%s'" % (thisfile(), linenum(), elem)
            
        #ref list http://nekoyukimmm.hatenablog.com/entry/2015/10/01/223148
        for char in list(keychars) :
            
#             print()
#             print ("[%s:%d] char => %c" % (os.path.basename(thisfile()), linenum(), char))
#             
#             print()
            
            
#             print "[%s:%d] elem = '%s' / char = '%c'" % (thisfile(), linenum(), elem, char)
            
            
            if elem.startswith('-' + char) \
                    and len(elem) > 2 \
                    and not elem.startswith("--"):
#             if elem.startswith(char) and len(elem) > 2 :
#             if elem.startswith(char) and len(elem) > 2 :
                
#                 #debug
#                 print ("[%s:%d] appending... : %s" % (os.path.basename(thisfile()), linenum(), elem))
#                 print()
                
                if not '-' + char in [x[0] for x in result] : 
                    
                    result['-' + char] = elem[2:]
#                     result.append(('-' + char, elem[2:]))
#                     #debug
#                     print()
#                     print ("[%s:%d] appended => %s" % (os.path.basename(thisfile()), linenum(), ('-' + char, elem[2:])))
        
                
#                 print "[%s:%d] '-' + char : appended => '%s'" % (thisfile(), linenum(), elem[2:])
                
            
            elif elem.startswith('--') and len(elem) > 2 :
                
                if not (elem[2:], '') in result : result[elem[2:]] = ''
#                 if not (elem[2:], '') in result : result.append((elem[2:], ''))
             
    return result

'''###################
    @param string_type
            serial    "20160604_193404"
            basic     "2016/06/04 19:34:04"
###################'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
#     str = strftime("%Y%m%d_%H%M%S", t)
#     str = strftime("%Y%m%d_%H%M%S", localtime())

    '''###################
        build string        
    ###################'''
    if string_type == "serial" : #if string_type == "serial"
    
        str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    elif string_type == "basic" : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    else : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    #/if string_type == "serial"
    
    
#     str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
    if mili == True :

        if string_type == "serial" : #if string_type == "serial"
            
            str = "%s_%03d" % (str, int(t % 1 * 1000))
        
        else : #if string_type == "serial"
        
            str = "%s.%03d" % (str, int(t % 1 * 1000))

        #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
#         str = "%s_%03d" % (str, int(t % 1 * 1000))
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():

'''###################
def is_Open(filepath):

    2018/01/31 12:34:10
    
    @problem
        - file being opened in Mindmanager app
        - returns "True"
###################'''
def is_Open(filepath):

    print()
    print("[%s:%d] is_Open : '%s'" % \
        (os.path.basename(thisfile()), linenum()
        , filepath
        ), file=sys.stderr)
    print()

    #ref https://stackoverflow.com/questions/37515574/how-to-check-if-a-file-is-already-opened-in-the-same-process answered May 29 '16 at 23:09    
    if os.path.exists(filepath):
#     if os.path.exists(file_name):
        try:
            os.rename(filepath, filepath + ".tmp") #can't rename an open file so an error will be thrown
#             os.rename(filepath, filepath) #can't rename an open file so an error will be thrown
            return False
        except:
            return True
    raise NameError

def write_Log(\
      content
#    , dpath_LogFile = cons_ip.FilePaths.dpath_LogFile.value
#    , fname_LogFile = cons_ip.FilePaths.fname_LogFile.value
#       , dpath_LogFile
#       , fname_LogFile
#       , fname_Main
#       , line_Num
      , flg_Return = True):
    
    fpath_Log = "%s\\%s" % \
             (cons_ip.FilePaths.dpath_LogFile.value
              , cons_ip.FilePaths.fname_LogFile.value)

#            (dpath_LogFile
#             , fname_LogFile)
#             (cons_ip.FilePaths.dpath_LogFile.value
#              , cons_ip.FilePaths.fname_LogFile.value)
    
    fout_Log = open(fpath_Log, "a")
    
    # header
    fout_Log.write(content)
    
    # return char
    if flg_Return == True : fout_Log.write("\n")

    # close file
    fout_Log.close()
    
    
#/ def write_Log(dpath_LogFile, fname_LogFile, fname_Main, line_Num):

def write_Log_2(\
      content
    , dpath_LogFile = cons_ip.FilePaths.dpath_LogFile.value
    , fname_LogFile = cons_ip.FilePaths.fname_LogFile.value
#       , dpath_LogFile
#       , fname_LogFile
#       , fname_Main
#       , line_Num
      , numOf_Return = 1):
    
    fpath_Log = "%s\\%s" % \
            (dpath_LogFile
             , fname_LogFile)
#             (cons_ip.FilePaths.dpath_LogFile.value
#              , cons_ip.FilePaths.fname_LogFile.value)
    
    fout_Log = open(fpath_Log, "a")
    
    # header
    fout_Log.write(content)
    
    # return char
    for i in range(numOf_Return):
    
        fout_Log.write("\n")
        
    #/for i in range(numOf_Return):

#     if flg_Return == True : fout_Log.write("\n")

    # close file
    fout_Log.close()
    
    
#/ def write_Log(dpath_LogFile, fname_LogFile, fname_Main, line_Num):


