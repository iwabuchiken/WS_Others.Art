'''
=========================================== 2018/01/30 17:49:44
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art
python -m virtualenv VIRTUAL

            C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art>python -m virtualenv VIRTUAL
            Using base prefix 'C:\\WORKS_2\\Programs\\Python\\Python_3.5.1'
            New python executable in C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Scrip
            ts\python.exe
            Installing setuptools, pip, wheel...done.

pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art
VIRTUAL\Scripts\activate.bat
python -m pip install django==1.10

            Collecting django==1.10
              Downloading https://files.pythonhosted.org/packages/4b/4c/059f68d8f029f7054e4e
            6bb0b1ed2fde7f28d07a3727325727d5a95ae1b8/Django-1.10-py2.py3-none-any.whl (6.8MB
            )
                100% |################################| 6.8MB 758kB/s
            Installing collected packages: django
            Successfully installed django-1.10

pip install sympy numpy matplotlib

(VIRTUAL) C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects>pip i
nstall sympy numpy matplotlib
            Collecting sympy
              Downloading https://files.pythonhosted.org/packages/91/26/4e477dbd1f9260eb743d
            9f221af3044648a8fb2fcf3f2f23daee4dc831a4/sympy-1.1.1.tar.gz (4.6MB)
                100% |################################| 4.6MB 853kB/s
            Collecting numpy
              Downloading https://files.pythonhosted.org/packages/20/09/6f302aba4a08ffcd34b2
            0a6ee94f34a76207105f59acd83462b81469c06e/numpy-1.14.3-cp35-none-win_amd64.whl (1
            3.4MB)
                100% |################################| 13.4MB 487kB/s
            Collecting matplotlib
              Downloading https://files.pythonhosted.org/packages/ce/02/d0fb7dc284a56449f782
            5ef7d1e8b682bf44cef540a6d615e1fa0faa543a/matplotlib-2.2.2-cp35-cp35m-win_amd64.w
            hl (8.7MB)
                100% |################################| 8.7MB 853kB/s
            Collecting mpmath>=0.19 (from sympy)
              Downloading https://files.pythonhosted.org/packages/7a/05/b3d1472885d8dc060693
            6ea5da0ccb1b4785682e78ab15e34ada24aea8d5/mpmath-1.0.0.tar.gz (511kB)
                100% |################################| 512kB 1.0MB/s
            Collecting python-dateutil>=2.1 (from matplotlib)
              Downloading https://files.pythonhosted.org/packages/cf/f5/af2b09c957ace60dcfac
            112b669c45c8c97e32f94aa8b56da4c6d1682825/python_dateutil-2.7.3-py2.py3-none-any.
            whl (211kB)
                100% |################################| 215kB 930kB/s
            Collecting six>=1.10 (from matplotlib)
              Downloading https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa
            78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
            Collecting cycler>=0.10 (from matplotlib)
              Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440
            ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
            Collecting pytz (from matplotlib)
              Downloading https://files.pythonhosted.org/packages/dc/83/15f7833b70d3e067ca91
            467ca245bae0f6fe56ddc7451aa0dc5606b120f2/pytz-2018.4-py2.py3-none-any.whl (510kB
            )
                100% |################################| 512kB 1.0MB/s
            Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
              Downloading https://files.pythonhosted.org/packages/6a/8a/718fd7d3458f9fab8e67
            186b00abdd345b639976bc7fb3ae722e1b026a50/pyparsing-2.2.0-py2.py3-none-any.whl (5
            6kB)
                100% |################################| 61kB 945kB/s
            Collecting kiwisolver>=1.0.1 (from matplotlib)
              Downloading https://files.pythonhosted.org/packages/67/57/834881c80cd1361792a1
            8b467ac8c1638c224a484956582e51d2f9e16e30/kiwisolver-1.0.1-cp35-none-win_amd64.wh
            l (57kB)
                100% |################################| 61kB 1.4MB/s
            Requirement already satisfied: setuptools in c:\works_2\ws\ws_others.art\jvemv6\
            46_art\virtual\lib\site-packages (from kiwisolver>=1.0.1->matplotlib) (39.1.0)
            Building wheels for collected packages: sympy, mpmath
              Running setup.py bdist_wheel for sympy ... done
              Stored in directory: C:\Users\iwabuchiken\AppData\Local\pip\Cache\wheels\6d\47
            \7c\40a7cd9b9bd5bad329fcd21d8e50629700fcc6e5520a66a2de
              Running setup.py bdist_wheel for mpmath ... done
              Stored in directory: C:\Users\iwabuchiken\AppData\Local\pip\Cache\wheels\33\15
            \0f\9ca5f2ad88a5456803098daa189f382408a81556aa209e97ff
            Successfully built sympy mpmath
            Installing collected packages: mpmath, sympy, numpy, six, python-dateutil, cycle
            r, pytz, pyparsing, kiwisolver, matplotlib
            Successfully installed cycler-0.10.0 kiwisolver-1.0.1 matplotlib-2.2.2 mpmath-1.
            0.0 numpy-1.14.3 pyparsing-2.2.0 python-dateutil-2.7.3 pytz-2018.4 six-1.11.0 sy
            mpy-1.1.1
            
#------------------------------------ 20180518_133227
pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL

django-admin startproject Admin_Projects

pushd Admin_Projects

#) python manage.py runserver

python manage.py migrate > migrate.log

# start : ip (image processing)
python manage.py startapp ip

pip install clipboard

pip install subprocess copy
pip install re clipboard time os datetime ftplib glob



'''