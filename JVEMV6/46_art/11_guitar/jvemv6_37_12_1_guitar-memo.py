# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\jvemv6_37_12_1_guitar-memo.py
orig : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_8.5\44_8.5_build-result-csv-data.py
at : 2019/09/17 08:48:46

pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\
python jvemv6_37_12_1_guitar-memo.py

### env
pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL
start_env.bat

<Usage> 2019/09/17 09:51:58
    1. file : memo_guitar.txt // C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar
        1. prep text
    2. run this program
        pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL
        start_env.bat
        pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\
        python jvemv6_37_12_1_guitar-memo.py
    3. open the newly-gen-ed file : memo_guitar.(replaced).(20190917_094828).txt

<git>
r a && s


'''
###############################################
import sys
from _datetime import datetime
from numpy import append

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os, re

'''###################
    import : others
###################'''
#ref https://uxmilk.jp/39307 2019/09/01 15:22:25
# import urllib2
#ref https://teratail.com/questions/47744 2019/09/01 15:25:52
import urllib.request, urllib.error
#ref https://tonari-it.com/python-beautiful-soup-html-parse/#toc2
#import bs4

'''###################
    vars : global
###################'''
SWITCH_DEBUG = True

DPATH_DAT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Files\\Logs\\20190829_223434[eap-2.id-1].[EURJPY-1].dir"

FNAME_DAT_FILE = "[eap-2.id-1].(20190829_223434).dat"

DPATH_REPORT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Logs\\logs_trading"

FNAME_REPORT_FILE = "DetailedStatement.[20190901_145309].htm"

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    '''
    
    print (msg)

'''###################
    _build_result_csv_data__Dat_File()

    @return: lo_Order_Numbers

###################'''
def _build_result_csv_data__Dat_File():
    
    '''###################
        step : 1
            prep : vars
    ###################'''
#     DPATH_DAT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Files\\Logs\\20190829_223434[eap-2.id-1].[EURJPY-1].dir"
#     
#     FNAME_DAT_FILE = "[eap-2.id-1].(20190829_223434).dat"
    
    fpath_Dat_File = os.path.join(DPATH_DAT_FILE, FNAME_DAT_FILE)
    
    # lists
    lo_Order_Numbers = []
    
    '''###################
        step : 2
            read : file
    ###################'''
    '''###################
        step : 2 : 1
            open
    ###################'''
    f_in_Dat_File = open(fpath_Dat_File, "r")
    
    '''###################
        step : 2 : 2
            read
    ###################'''
    linesOf_Dat_File = f_in_Dat_File.readlines()

            # [2019.08.29 22:34:35 / lib_ea_2.mqh:249]    17307984    117.639    117.636    4    8    117.632    117.647    

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        cntOf_Lines = len(linesOf_Dat_File)
        
        msg = "[%s:%d] cntOf_Lines ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , cntOf_Lines
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : 3
            build list
    ###################'''
    for item in linesOf_Dat_File:
        '''###################
            step : 3 : 1
                split each line
        ###################'''
        tokens = item.split("\t")
        
        '''###################
            step : 3 : 2
                get : order number
        ###################'''
        tokeOf_Order_Number = tokens[1]
        
        # append
        lo_Order_Numbers.append(int(tokeOf_Order_Number))
        
    #/for item in linesOf_Dat_File:

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        msg = "[%s:%d] len(lo_Order_Numbers) ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , len(lo_Order_Numbers)
                        )

        print()
        print(msg, file=sys.stderr)
        
        print(lo_Order_Numbers[0:10])
        
    #/if SWITCH_DEBUG == True

    
    '''###################
        step : 4
            file : close
    ###################'''
    f_in_Dat_File.close()
    
    #_20190901_150006:tmp
    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        msg = "[%s:%d] file ==> closed : %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Dat_File
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : X
            return
    ###################'''
    return lo_Order_Numbers
    
#/ def build_result_csv_data():

'''###################
    _build_result_csv_data__Write_Full_Data()
    
    at : 2019/09/03 12:46:56
    
    @return: lo_TRs_With_Order_TDS
    
            ==> [ [tag_TR, lo_TDs], [tag_TR, lo_TDs], ...]

###################'''
def _build_result_csv_data__Write_Full_Data(\
                                            
            _lo_Orders_Full
            , _dpath_Log__ROOT
            , _strOf_Project
            , _dname_Log
            , _tlabel
            
                                            ):

#_20190903_124741:caller
#_20190903_124745:head
#_20190903_124751:wl


    '''###################
        step : 1
            vars
    ###################'''
#     fname_Log__Dat_Full = "%s.(%s).dat" % (_strOf_Project, _tlabel)
    
    fname_Log__Dat_Full = "%s.[data-full].(%s).dat" % (_strOf_Project, _tlabel)

    dpath_Log__Dat_Full = os.path.join(_dpath_Log__ROOT, _dname_Log)
    
    fpath_Log__Dat_Full = os.path.join(dpath_Log__Dat_Full, fname_Log__Dat_Full)
    
    '''###################
        step : 2
            gen : dirs
    ###################'''
    if not os.path.isdir(dpath_Log__Dat_Full) : #if not os.path.isdir(dpath_Log__Dat_Full)
        
        res = os.makedirs(dpath_Log__Dat_Full)

        #debug
        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
            
            msg = "[%s:%d] os.makedirs ==> %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , res
                            )
    
            print()
            print(msg, file=sys.stderr)
            
        #/if SWITCH_DEBUG == True
    
    #/if not os.path.isdir(dpath_Log__Dat_Full)

    '''###################
        step : 3
            write
    ###################'''
    '''###################
        step : 3 : 1
            file : open
    ###################'''
    f_out_Dat_Full = open(fpath_Log__Dat_Full, "w")

    '''###################
        step : 2 : 5.2 : 5.2.1
            file : header
    ###################'''
    #"Ticket", "Open Time", "Type", "Size", "Item", "Price", "S / L", "T / P", "Close Time", "Price", "Commission", "Taxes", "Swap", "Profit"
    lo_Col_Names = ["Ticket", "Open Time", "Type", "Size", "Item", "Price", "S / L", "T / P", "Close Time", "Price", "Commission", "Taxes", "Swap", "Profit"]
    
    f_out_Dat_Full.write("this file\t%s" % fname_Log__Dat_Full)
    f_out_Dat_Full.write("\n")
    
#     f_out_Dat_Full.write("source dir\t%s" % DPATH_REPORT_FILE)
#     f_out_Dat_Full.write("\n")
#     
    f_out_Dat_Full.write("\n")
    
    f_out_Dat_Full.write("s.n.")
    f_out_Dat_Full.write("\t")
    
    f_out_Dat_Full.write("\t".join(lo_Col_Names))
    f_out_Dat_Full.write("\n")
    f_out_Dat_Full.write("\n")
    
    '''###################
        step : 2 : 5.2 : 5.3
            file : write
    ###################'''
    #_20190902_130031:tmp
    cntOf_Loop = 0
    
    for item in _lo_Orders_Full:
        '''###################
            step : 2 : 5.2 : 5.3 : 0
                count
        ###################'''
        cntOf_Loop += 1
        
        '''###################
            step : 2 : 5.2 : 5.3 : 1
                get : TDs
        ###################'''
        # TDs
        lo_TDs = item[1]
        
        '''###################
            step : 2 : 5.2 : 5.3 : 2
                get : texts
        ###################'''
        lo_Tmp_TD_Texts = []
        
        # s.n.
        lo_Tmp_TD_Texts.append("%d" % cntOf_Loop)
        lo_Tmp_TD_Texts.append("\t")
        
        lo_Tmp_TD_Texts.append("\t".join([x.getText() for x in lo_TDs]))
        
        f_out_Dat_Full.write("".join(lo_Tmp_TD_Texts))
        f_out_Dat_Full.write("\n")
        
    #/for item in lo_TRs_With_Order_TDS:

    
    
    '''###################
        step : 2 : 5.2 : 5.X
            file : close
    ###################'''
    f_out_Dat_Full.close()

#/ def _build_result_csv_data__Write_Full_Data():

'''###################
    _build_result_csv_data__Full_Data_List()
    
    at : 2019/09/03 12:46:56
    
    @return: lo_TRs_With_Order_TDS
    
            ==> [ [tag_TR, lo_TDs], [tag_TR, lo_TDs], ...]

###################'''
def _build_result_csv_data__Full_Data_List(_lo_TRs_With_Order_TDS, _lo_Order_Numbers):

#_20190903_124229:caller
#_20190903_124234:head
#_20190903_124239:wl

    '''###################
        step : 1
            vars
    ###################'''
    lo_Orders_Full = []
    
    '''###################
        step : 2
            build
    ###################'''
    for item in _lo_TRs_With_Order_TDS:
    
        lo_TDs = item[1]
        
        numOf_Order = int(lo_TDs[0].getText())
        
        # judge
        if numOf_Order in _lo_Order_Numbers : #if numOf_Order in lo_Order_Numbers
            
            # append
            lo_Orders_Full.append(item)
        
        #/if numOf_Order in lo_Order_Numbers

        
    #/for item in lo_TRs_With_Order_TDS:

    # report
    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        lenOf_LO_Orders_Full = len(lo_Orders_Full)
        
        msg = "[%s:%d] lenOf_LO_Orders_Full ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , lenOf_LO_Orders_Full
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : 3
            return
    ###################'''
    return lo_Orders_Full
    
#/ def _build_result_csv_data__Full_Data_List():

'''###################
    _build_result_csv_data__Report_File()

    @return: lo_TRs_With_Order_TDS
    
            ==> [ [tag_TR, lo_TDs], [tag_TR, lo_TDs], ...]

###################'''
def _build_result_csv_data__Report_File(\
                                        
            _dpath_Log__ROOT
            , _strOf_Project
            , dname_Log
            , _tlabel
                                        
                                        ):

#_20190901_151726:caller
#_20190901_151733:head
#_20190901_151746:wl

    '''###################
        step : 1 : 1
            prep : vars : file names, paths
    ###################'''
    #C:\Users\iwabuchiken\AppData\Roaming\MetaQuotes\Terminal\34B08C83A5AAE27A4079DE708E60511E\MQL4\Logs\logs_trading
#     DPATH_REPORT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Logs\\logs_trading"
#     
#     FNAME_REPORT_FILE = "DetailedStatement.[20190901_145309].htm"
    
    fpath_Report_File = os.path.join(DPATH_REPORT_FILE, FNAME_REPORT_FILE)
    
    #_20190902_124906:tmp
#     _tlabel = libs.get_TimeLabel_Now()
    
#     #C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\log
#     _dpath_Log__ROOT = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
#     
#     _strOf_Project = "[44_8.5].[order-csv-data]"
#     
#     dname_Log = "%s.(%s).dir" % (_strOf_Project, _tlabel)
    
    fname_Log__Dat = "%s.(%s).dat" % (_strOf_Project, _tlabel)
    
    fname_Log__Dat_Report_File = "%s.[report-file].(%s).dat" % (_strOf_Project, _tlabel)

    '''###################
        step : 1 : 1.1
            gen : dirs
    ###################'''
    #_20190902_125615:tmp
    dpath_Log__Dat = os.path.join(_dpath_Log__ROOT, dname_Log)
    
    if not os.path.isdir(dpath_Log__Dat) : #if not os.path.isdir(dpath_Log__Dat)
        
        res = os.makedirs(dpath_Log__Dat)

        #debug
        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
            
            msg = "[%s:%d] os.makedirs ==> %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , res
                            )
    
            print()
            print(msg, file=sys.stderr)
            
        #/if SWITCH_DEBUG == True
    
    #/if not os.path.isdir(dpath_Log__Dat)

    
    '''###################
        step : 1 : 2
            prep : vars : lists
    ###################'''
    # 
    lo_Orders = []
    
    # [ [tag_TR, lo_TDs], [], ...]
    lo_TR_and_TDs = []
    
    #
    lo_Orders_From_Report_File = []
    
    # list of TRs with order TDs
    lo_TRs_With_Order_TDS = []
    
    '''###################
        step : 2 : 1
            read : source file
    ###################'''
    f_in_Report_File = open(fpath_Report_File, "r")
    
    contentOf_Report_File = f_in_Report_File.read()

    '''###################
        step : 2 : 1.1
            source file : close
    ###################'''
    f_in_Report_File.close()
    
    '''###################
        step : 2 : 2
            read : as html
    ###################'''
    #ref https://tonari-it.com/python-beautiful-soup-html-parse/#toc2
    soup = bs4.BeautifulSoup(contentOf_Report_File, "html.parser")
    
    print()
    print(soup.title)

    '''###################
        step : 2 : 3
            read : TR tags
    ###################'''
    #ref https://tonari-it.com/python-html-tag-list-bs4/#toc5
    lo_TRs = soup.select("tr")

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        cntOf_LO_TRs = len(lo_TRs)
        
        msg = "[%s:%d] cntOf_LO_TRs ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , cntOf_LO_TRs
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : 2 : 4
            read : TD tags
    ###################'''
    for item in lo_TRs:
        
        '''###################
            step : 2 : 4.1
                select : TD tags
        ###################'''
        lo_TDs = item.select("td")
        
        '''###################
            step : 2 : 4.2
                append
        ###################'''
        lo_TR_and_TDs.append([item, lo_TDs])
        
    #/for item in lo_TRs:

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        cntOf_LO_TR_and_TDs = len(lo_TR_and_TDs)
        
        msg = "[%s:%d] cntOf_LO_TR_and_TDs ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , cntOf_LO_TR_and_TDs
                        )

        print()
        print(msg, file=sys.stderr)
        
#         print(lo_TR_and_TDs[10])
        
    #/if SWITCH_DEBUG == True
    
    '''###################
        step : 2 : 5
            read : TD texts
    ###################'''
#     for item in lo_TR_and_TDs:
#     for item in lo_TR_and_TDs[:50] :
#     for item in lo_TR_and_TDs[:20] :
    for item in lo_TR_and_TDs :
         
        '''###################
            step : 2 : 5.1
                get : TDs
        ###################'''
        lo_TDs = item[1]
        
        '''###################
            step : 2 : 5.2
                get : texts
        ###################'''
        for item_2 in lo_TDs:

            '''###################
                step : 2 : 5.2 : 1
                    get : "title" attribute value
            ###################'''
            # get text
            textOf_TD_With_Title_Attribute = item_2.get("title")
#             textOf_TD = item_2.getText()

            '''###################
                step : 2 : 5.2 : 2
                    validate
            ###################'''
            if textOf_TD_With_Title_Attribute == None : #if textOf_TD == None
        
#                 #debug
#                 if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#     
#                     msg = "[%s:%d] textOf_TD_With_Title_Attribute ==> none" % \
#                                     (os.path.basename(libs.thisfile()), libs.linenum()
#                                      
#                                     )
#              
#                     print(item_2)
#                     print(msg, file=sys.stderr)
#                      
#                 #/if SWITCH_DEBUG == True
                
                # continue
                continue
            
            #/if textOf_TD == None

            '''###################
                step : 2 : 5.2 : 3
                    if "My order" in the text ==> append
            ###################'''
            '''###################
                step : 2 : 5.2 : 3.1
                    log
            ###################'''
           #_20190901_161624:next
           
            if "My order" in textOf_TD_With_Title_Attribute : #if "My order" in textOf_TD_With_Title_Attribute

                '''###################
                    step : 2 : 5.2 : 3.2
                        append
                ###################'''
                # append
                lo_TRs_With_Order_TDS.append(item)
                
                #_20190901_161249:tmp
#                 #debug
#                 if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#     
#                     msg = "[%s:%d] My order ==> detected" % \
#                                     (os.path.basename(libs.thisfile()), libs.linenum()
#                                      
#                                     )
#              
#                     print(item_2)
#                     print(msg, file=sys.stderr)
#                      
#                 #/if SWITCH_DEBUG == True
                
            #/if "My order" in textOf_TD_With_Title_Attribute


#             #debug
#             if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
# 
#                 msg = "[%s:%d] textOf_TD ==> %s" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum()
#                                  , textOf_TD
#                                 )
#          
#                 print()
#                 print(msg, file=sys.stderr)
#                  
#             #/if SWITCH_DEBUG == True
            
#             # 
#             #ref https://www.afternerd.com/blog/python-string-contains/
#             if "My order" in textOf_TD : #if "My order" in textoff
#                 
#                 #debug
#                 if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
# 
#                     msg = "[%s:%d] My order ==> detected" % \
#                                     (os.path.basename(libs.thisfile()), libs.linenum()
#                                      
#                                     )
#              
#                     print()
#                     print(msg, file=sys.stderr)
#                      
#                     print(item)
#                      
#                 #/if SWITCH_DEBUG == True
#             
#             #/if "My order" in textoff

            
#             #debug
#             if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                 
#                 # count
#                 cntOf_LO_TR_and_TDs = len(lo_TR_and_TDs)
#                 
#                 msg = "[%s:%d] cntOf_LO_TR_and_TDs ==> %d" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum()
#                                  , cntOf_LO_TR_and_TDs
#                                 )
#         
#                 print()
#                 print(msg, file=sys.stderr)
#                 
#                 print(lo_TR_and_TDs[10])
#                 
#             #/if SWITCH_DEBUG == True
            
            
        #/for item_2 in lo_TDs:

    #/for item in lo_TR_and_TDs:
    '''###################
        step : 2 : 5.2 : 4
            extract texts
    ###################'''
    #_20190902_124052:tmp
    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True

        msg = "[%s:%d] len(lo_TRs_With_Order_TDS) ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , len(lo_TRs_With_Order_TDS)
                        )
 
        print(msg, file=sys.stderr)
         
    #/if SWITCH_DEBUG == True
    
    '''###################
        step : 2 : 5.2 : 5
            write to file
    ###################'''
    #_20190902_124906:tmp
    '''###################
        step : 2 : 5.2 : 5.1
            file path
    ###################'''
    fpath_Log__Dat_Report_File = os.path.join(_dpath_Log__ROOT, dname_Log, fname_Log__Dat_Report_File)
#     fpath_Log__Dat = os.path.join(_dpath_Log__ROOT, dname_Log, fname_Log__Dat)
    
    '''###################
        step : 2 : 5.2 : 5.2
            file : open
    ###################'''
    f_out_Dat_Report_File = open(fpath_Log__Dat_Report_File, "w")

    '''###################
        step : 2 : 5.2 : 5.2.1
            file : header
    ###################'''
    #"Ticket", "Open Time", "Type", "Size", "Item", "Price", "S / L", "T / P", "Close Time", "Price", "Commission", "Taxes", "Swap", "Profit"
    lo_Col_Names = ["Ticket", "Open Time", "Type", "Size", "Item", "Price", "S / L", "T / P", "Close Time", "Price", "Commission", "Taxes", "Swap", "Profit"]
    
    f_out_Dat_Report_File.write("source file\t%s" % fname_Log__Dat_Report_File)
    f_out_Dat_Report_File.write("\n")
    
    f_out_Dat_Report_File.write("source dir\t%s" % DPATH_REPORT_FILE)
    f_out_Dat_Report_File.write("\n")
    
    f_out_Dat_Report_File.write("\n")
    
    f_out_Dat_Report_File.write("s.n.")
    f_out_Dat_Report_File.write("\t")
    
    f_out_Dat_Report_File.write("\t".join(lo_Col_Names))
    f_out_Dat_Report_File.write("\n")
    f_out_Dat_Report_File.write("\n")
    
    '''###################
        step : 2 : 5.2 : 5.3
            file : write
    ###################'''
    #_20190902_130031:tmp
    cntOf_Loop = 0
    
    for item in lo_TRs_With_Order_TDS:
        '''###################
            step : 2 : 5.2 : 5.3 : 0
                count
        ###################'''
        cntOf_Loop += 1
        
        '''###################
            step : 2 : 5.2 : 5.3 : 1
                get : TDs
        ###################'''
        # TDs
        lo_TDs = item[1]
        
        '''###################
            step : 2 : 5.2 : 5.3 : 2
                get : texts
        ###################'''
        lo_Tmp_TD_Texts = []
        
        # s.n.
        lo_Tmp_TD_Texts.append("%d" % cntOf_Loop)
        lo_Tmp_TD_Texts.append("\t")
        
        lo_Tmp_TD_Texts.append("\t".join([x.getText() for x in lo_TDs]))
        
#         for item_2 in lo_TDs:
#         
#             textOf_TD = item_2.getText()
#             
#             lo_Tmp_TD_Texts.append(textOf_TD)
#             lo_Tmp_TD_Texts.append("\t")
#             
#         #/for item_2 in lo_TDs:

#         # separator
#         lo_Tmp_TD_Texts.append("\n")
        
#         # first TD
#         TD_0 = lo_TDs[0]
#         
#         textOf_TD = TD_0.getText()
#         
#         f_out_Dat.write(textOf_TD)
        f_out_Dat_Report_File.write("".join(lo_Tmp_TD_Texts))
        f_out_Dat_Report_File.write("\n")
        
    #/for item in lo_TRs_With_Order_TDS:

    
    
    '''###################
        step : 2 : 5.2 : 5.X
            file : close
    ###################'''
    f_out_Dat_Report_File.close()
    
    '''###################
        step : X
            return
    ###################'''
    return lo_TRs_With_Order_TDS

#/ def _build_result_csv_data__Report_File():


def build_result_csv_data():
    
    '''###################
        step : 1
            dat file
    ###################'''
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    #C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\log
    dpath_Log__ROOT = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
    
    strOf_Project = "[44_8.5].[order-csv-data]"
    
    dname_Log = "%s.(%s).dir" % (strOf_Project, tlabel)
    
    '''###################
        step : 1
            dat file
    ###################'''
    lo_Order_Numbers = _build_result_csv_data__Dat_File()
    
    '''###################
        step : 2
            file : report file
    ###################'''
    #_20190901_151726:caller
    lo_TRs_With_Order_TDS = lo_Order_Reports = \
                _build_result_csv_data__Report_File(\
                   
                        dpath_Log__ROOT
                        , strOf_Project
                        , dname_Log
                        , tlabel

                                                    )
    
                # 17257299    2019.08.27 08:26:03    buy    1.00    eurjpy    117.345    117.338    117.353    2019.08.27 08:26:27    117.338    0    0    0    -700

    '''###################
        step : 3
            build : a full-data list
    ###################'''
    #_20190902_132829:tmp
    #_20190903_124229:caller
    lo_Orders_Full = _build_result_csv_data__Full_Data_List(lo_TRs_With_Order_TDS, lo_Order_Numbers)
    
#     '''###################
#         step : 3.1
#             vars
#     ###################'''
#     lo_Orders_Full = []
#     
#     for item in lo_TRs_With_Order_TDS:
#     
#         lo_TDs = item[1]
#         
#         numOf_Order = int(lo_TDs[0].getText())
#         
#         # judge
#         if numOf_Order in lo_Order_Numbers : #if numOf_Order in lo_Order_Numbers
#             
#             # append
#             lo_Orders_Full.append(item)
#         
#         #/if numOf_Order in lo_Order_Numbers
# 
#         
#     #/for item in lo_TRs_With_Order_TDS:
# 
#     # report
#     #debug
#     if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#         
#         # count
#         lenOf_LO_Orders_Full = len(lo_Orders_Full)
#         
#         msg = "[%s:%d] lenOf_LO_Orders_Full ==> %d" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          , lenOf_LO_Orders_Full
#                         )
# 
#         print()
#         print(msg, file=sys.stderr)
#         
#     #/if SWITCH_DEBUG == True
    
    '''###################
        step : 4
            write : file
    ###################'''
    #_20190903_124102:tmp
    #_20190903_124741:caller
    _build_result_csv_data__Write_Full_Data(\
                                            
            lo_Orders_Full
            , dpath_Log__ROOT
            , strOf_Project
            , dname_Log
            , tlabel
                                            
                                            )
    
    
#/ def build_result_csv_data():

def test_1():

    '''###################
        get : args
    ###################'''
    
    '''###################
        file path
    ###################'''
    #_20190917_090405:tmp
    #C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar
    dpath_Text = "C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\11_guitar"
    
    fname_Text = "memo_guitar.txt"
    
    #_20190917_094525:tmp
    fname_Text_Replaced = "memo_guitar.(replaced).(%s).txt" % libs.get_TimeLabel_Now()
    
    fpath_Text = os.path.join(dpath_Text, fname_Text)
    
    # validate
    if not os.path.isfile(fpath_Text) : #if not os.path.isfile(fpath_CSV)
        
        print()
        print("[%s:%d] text file NOT exist : %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Text
                        ), file=sys.stderr)
        
        return
    
    #/if not os.path.isfile(fpath_CSV)

    '''###################
        file : open
    ###################'''
    f_in_Text = open(fpath_Text, "r")
    
    '''###################
        read file content
    ###################'''
    data = f_in_Text.read()
    
    print("[%s:%d] len(data) = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(data)
            ), file=sys.stderr)
    
    '''###################
        file : close
    ###################'''
    f_in_Text.close()

    '''###################
        step : A : 1
            replace
    ###################'''
    #_20190917_090843:tmp
    #ref https://www.tutorialspoint.com/python/python_reg_expressions.htm
    # \|\|     \r\n
    #ref https://uxmilk.jp/8662
    txt_Replaced = re.sub(r"\|\| ", "\r", data)
#     txt_Replaced = re.sub(r"\|\| ", "\r\n", data)

    print("[%s:%d] txt_Replaced => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , txt_Replaced
            ), file=sys.stderr)

    #ref https://stackoverflow.com/questions/5984633/python-re-sub-group-number-after-number
    lo_Replaces = [
#                    ["(s\.\d+):", "$1\t"]
                   ["(s\.\d+):", "\g<1>\t"]
                   , ["\.N", "\t"]
                   , ["\.n", "\t"]	# 20191009_102653
                   , ["(\d),rev", "\g<1>\trev"]
                   , ["(\d);v", "\g<1>\tv"]
                   , ["(\d),var", "\g<1>\tvar"]	# 20191006_075953
                   , ["(-\d+),section", "\g<1>\tsection"]	# 20191006_075953
                   , ["(-\d+),practice", "\g<1>\tpractice"]	# 20191006_075953
                   , ["(-\d+),play", "\g<1>\tplay"]	# 20191008_100412
                   , ["(\d),rec", "\g<1>\trec"]
                   , ["s\.(\d+?)",    "\g<1>"]
                   , ["^(\d+?\t.+-\d+),",    "\g<1>\t"]
                   , ["(\d);var",    "\g<1>\tvar"]
                   , [",R=",    "\tR="]
                   ]
    
    for item in lo_Replaces:

        print("[%s:%d] item[0] = '%s', item[1] = '%s'" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , item[0], item[1]
                ), file=sys.stderr)
    
    
        txt_Replaced = re.sub(item[0], item[1], txt_Replaced)
        
    #/for item in lo_Replaces:

    
#     txt_Replaced = re.sub(r"\|\| ", "\r\n", data)

    print("[%s:%d] txt_Replaced => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , txt_Replaced
            ), file=sys.stderr)

    '''###################
        step : A : 2
            clipboard
    ###################'''
#     #_20190917_094226:tmp
# #     command = 'echo ' + text.strip() + '| clip'
# #     command = 'echo ' + txt_Replaced.strip() + '| clip'
#     command = "echo \"" + txt_Replaced.strip() + "\" | clip"
#     os.system(command)
# 
#     print("[%s:%d] command => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , command
#             ), file=sys.stderr)
#     
#     print("[%s:%d] text => to clipboard" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)

    '''###################
        step : A : 3
            to file
    ###################'''
    f_out_Text_Replaced = open(os.path.join(dpath_Text, fname_Text_Replaced), "w")
    
    f_out_Text_Replaced.write(txt_Replaced)
    
    # close
    f_out_Text_Replaced.close()

    print("[%s:%d] text => written : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , fname_Text_Replaced
            ), file=sys.stderr)
    
    '''###################
        report
    ###################'''
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
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
