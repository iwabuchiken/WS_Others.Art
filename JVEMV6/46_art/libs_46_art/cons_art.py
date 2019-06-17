#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

TypeOf_Data_OpenClose   = "OpenClose"

'''###################
    Used in :
        libfx : def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
###################'''
class FPath(Enum):
    
#     fname_In_XML = "Materials_Science.mm"
    fname_In_XML = "test.mm"
#     fname_In_XML = "copy.mm"
#    dpath_In_CSV = "C:/WORKS_2/WS/FM_2/Materials_Science"
    dpath_In_CSV = "C:/WORKS_2/WS/FM_2_20171104_225946/Materials_Science"
#     fpath_In_CSV = dpath_In_CSV + "/" + fname_In_CSV
    

class NodeVar(Enum):
    
    ATTRIB_NAME_WIDTH   = 75
    ATTRIB_VALUE_WIDTH   = 120
    
    