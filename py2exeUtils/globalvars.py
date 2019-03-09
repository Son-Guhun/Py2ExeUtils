import os
import sys
import path

FROZEN = getattr(sys, 'frozen', '')

if not FROZEN:
    # not frozen: in regular python interpreter
    DIRECTORY = path.up(sys.argv[0],1)

elif FROZEN in ('dll', 'console_exe', 'windows_exe'):
    # py2exe:
    DIRECTORY = path.up(sys.executable,1)
    
elif FROZEN in ('macosx_app',):
    # py2app:
    # Notes on how to find stuff on MAC, by an expert (Bob Ippolito):
    # http://mail.python.org/pipermail/pythonmac-sig/2004-November/012121.html
    DIRECTORY = os.environ['RESOURCEPATH']

#Code for retrieving file path by Peter Hansen
#https://stackoverflow.com/questions/1511461/py2exe-and-the-file-system
