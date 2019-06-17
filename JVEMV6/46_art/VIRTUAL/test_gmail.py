'''###################
    file : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\test_gmail.py
    
    at : 2018/02/08 21:19:37

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL
python test_gmail.py
            
###################'''


import sys

import os

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs
from libs import libfx

from libs import cons

# from libs_D_7 import cons_D_7
# from libs_31 import libmt

import getopt
import os
import inspect

import math as math

import struct

from shutil import copyfile

import xml.etree.ElementTree as ET

from smtplib import SMTP

from poplib import POP3_SSL

import imaplib, re, email, six, dateutil.parser


def exec_prog():

    user = 'iwabuchik2010'
    passwd = 'connectdots0145'
    
    gmail = imaplib.IMAP4_SSL("imap.gmail.com")
    gmail.login(user, passwd)
#     gmail.login("user","password")
    
    gmail.close()
    gmail.logout()
    
            #       File "C:\WORKS_2\Programs\Python\Python_3.5.1\lib\imaplib.py", line 582, in lo
            # gin
            #     raise self.error(dat[-1])
            # imaplib.error: b'[AUTHENTICATIONFAILED] Invalid credentials (Failure)'
    
#     host, port = 'pop.gmail.com', 995
#     
#     user = 'iwabuchik2010'
#     passwd = 'connectdots0145'
#     
#     popServ = POP3_SSL(host)
#     popServ.user(user)
#     popServ.pass_(passwd)
#     
#     print()
#     print("[%s:%d] popServ.pass_(passwd) => done" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     msg_ct, mbox_siz = popServ.stat()
#     
#     rsp, msg, siz = popServ.retr(msg_ct)
#     
#     for line in msg:
#         
#         print(line)
#         
#     popServ.quit()
    
            #       File "C:\WORKS_2\Programs\Python\Python_3.5.1\lib\poplib.py", line 152, in _ge
            # tresp
            #     raise error_proto(resp)
            # poplib.error_proto: b'-ERR [AUTH] Username and password not accepted.'
            
    return None
    
#/def exec_prog():


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
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))

