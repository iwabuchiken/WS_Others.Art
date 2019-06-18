'''###################
created : 2018/06/17 10:59:46

pushd

###################'''
import os, sys

sys.path.append('C:/WORKS_2/WS/WS_Others.Art/JVEMV6/46_art/VIRTUAL/Admin_Projects')
from libs_admin import libs

# import urllib
# from lxml import html
# import urllib2
import requests, time
import threading
# import urllib3, requests

# from html.parser import HTMLParser
from bs4 import BeautifulSoup as BS

'''######################################
    funcs        
######################################'''
#ref https://pymotw.com/2/threading/
def worker():
    """thread worker function"""
    
    r = requests.get('http://localhost:8001/ip/dos_attack/')
#     r = requests.get('http://localhost:8001/ip/dos_attack')
 
    #ref https://qiita.com/itkr/items/513318a9b5b92bd56185
    #ref r.text https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len#36709275 answered Apr 19 '16 at 5:25
    soup = BS(r.text, "html.parser")
#     soup = BS(r.text)

    print()
    print("[%s:%d] soup => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     soup = BS(r)
 
#     print ('Worker')
    
    return

def test_4__Thread__V2():
    
    threads = []
#     for i in range(500):
    for i in range(120):
#     for i in range(130):
#     for i in range(150):
#     for i in range(160):
#     for i in range(200):
#     for i in range(50):
#     for i in range(5):
        
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()    
        
def test_4__Thread():
    
    # Create two threads as follows
    try:
       thread.start_new_thread( print_time, ("Thread-1", 2, ) )
       thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    except:
       print ("Error: unable to start thread")
    
#     #ref https://qiita.com/Taillook/items/a0f2c59d8e17381fc835
#     r = requests.get('http://localhost:8001/ip/dos_attack')
# 
#     #ref https://qiita.com/itkr/items/513318a9b5b92bd56185
#     #ref r.text https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len#36709275 answered Apr 19 '16 at 5:25
#     soup = BS(r.text)
# #     soup = BS(r)
#     
#     print()
#     print("[%s:%d] soup => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , soup
#             ), file=sys.stderr)
    

#     r = urllib3.urlopen("http://localhost:8001/ip/dos_attack")
    
#     print()
#     print("[%s:%d] r.text => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , r.text
#             ), file=sys.stderr)
    
def test_3():
    
    #ref https://qiita.com/Taillook/items/a0f2c59d8e17381fc835
    r = requests.get('http://localhost:8001/ip/dos_attack')

    #ref https://qiita.com/itkr/items/513318a9b5b92bd56185
    #ref r.text https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len#36709275 answered Apr 19 '16 at 5:25
    soup = BS(r.text)
#     soup = BS(r)
    
    print()
    print("[%s:%d] soup => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , soup
            ), file=sys.stderr)
    

#     r = urllib3.urlopen("http://localhost:8001/ip/dos_attack")
    
#     print()
#     print("[%s:%d] r.text => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , r.text
#             ), file=sys.stderr)
    
def test_2():
    
    #ref https://qiita.com/Taillook/items/a0f2c59d8e17381fc835
    r = requests.get('http://localhost:8001/ip/dos_attack')
    
    print()
    print("[%s:%d] r.text => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , r.text
            ), file=sys.stderr)
    
    parser = Parser()
    parser.feed(r.text)
    
    parser.close()
    
    print()
    print("[%s:%d] parser => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , parser
            ), file=sys.stderr)
    
    print()
    print("[%s:%d] parser.data => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , parser.data
            ), file=sys.stderr)
    
    for i in parser.data:
        print("Title: " + i["title"], "\nLink: " + i["link"] + "\n")
    
#     print()
#     print("[%s:%d] r => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , r
#             ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] r.text => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , r.text
#             ), file=sys.stderr)
    
#     response = urllib2.urlopen('http://python.org/')
#     html = response.read()
    
#     print()
#     print("[%s:%d] html => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , html
#             ), file=sys.stderr)
    
#     #ref https://stackoverflow.com/questions/4489550/how-to-get-an-html-file-using-python#4492108
# #     url = "http://www.infolanka.com/miyuru_gee/art/art.html"
#     url = "http://localhost:8001/ip/dos_attack/"
#     page = html.fromstring(urllib.urlopen(url).read())
#     
#     print()
#     print("[%s:%d] page => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , page
#             ), file=sys.stderr)
    
#/ def test_1():

def test_1():
    
    #ref https://urllib3.readthedocs.io/en/latest/
    http = urllib3.PoolManager()
#     r = http.request('GET', 'http://httpbin.org/robots.txt')
    r = http.request('GET', 'http://localhost:8001/ip/dos_attack')
    
    print()
    print("[%s:%d] r => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , r
            ), file=sys.stderr)
    
    print()
    print("[%s:%d] r.data => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , r.data
            ), file=sys.stderr)
    
    print()
    print("[%s:%d] type(r.data) => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , type(r.data)
            ), file=sys.stderr)
    
    print()
    print("[%s:%d] r.text => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , r.text
            ), file=sys.stderr)
    
#     response = urllib2.urlopen('http://python.org/')
#     html = response.read()
    
#     print()
#     print("[%s:%d] html => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , html
#             ), file=sys.stderr)
    
#     #ref https://stackoverflow.com/questions/4489550/how-to-get-an-html-file-using-python#4492108
# #     url = "http://www.infolanka.com/miyuru_gee/art/art.html"
#     url = "http://localhost:8001/ip/dos_attack/"
#     page = html.fromstring(urllib.urlopen(url).read())
#     
#     print()
#     print("[%s:%d] page => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , page
#             ), file=sys.stderr)
    
#/ def test_1():

#ref https://qiita.com/Taillook/items/a0f2c59d8e17381fc835
# class Parser(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.title = False
#         self.link = False
#         self.data = []
# 
#     def handle_starttag(self, tag, attrs):
#         attrs = dict(attrs)
#         if tag == "h2" and "class" in attrs and attrs['class'] == "esc-lead-article-title":
#             self.data.append({})
#             self.title = True
#             self.link = True
# 
#         if tag == "a" and self.link == True:
#             self.data[-1].update({"link": attrs["href"]})
# 
#     def handle_data(self, data):
#         if self.title == True or self.link == True:
#             self.data[-1].update({"title": data})
#             self.title = False
#             self.link = False

#ref https://www.tutorialspoint.com/python/python_multithreading.htm
# Define a function for the thread

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
#       print "%s: %s" % ( threadName, time.ctime(time.time()) )
      print ("%s: %s") % ( threadName, time.ctime(time.time()) )

def exec_prog(): # from : 
    
    test_4__Thread__V2()
#     test_4__Thread()
#     test_3()
#     test_2()
#     test_1()
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog(): # from : 20180116_103908



'''
<usage>
'''
if __name__ == "__main__" :

    '''###################
        evecute        
    ###################'''
    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))

