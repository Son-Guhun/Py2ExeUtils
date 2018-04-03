# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 12:52:43 2018

This is library of useful functions, classes and variables to be used alongside
py2exe. It includes routines for runtime and compilation of the program.

Variables:
    =>scriptDir
    This is a unicode string that is equivalent to the current path
    of the script (excluding the script's name itself). It is valid when used
    in a .py script or a py2exe executable.
    =>frozen
    This is the frozen attribute of the system. If running from a .py file, the
    value is an empty string. Otherwise, the value is a string containing
    information on how the file was frozen.
    
    
@author: SonGuhun
"""
class version:
    major = 1
    minor = 0
    patch = 0
    
    version = str(major) + '.' + str(minor) + '.' + str(patch)
# =============================================================================
# 
# =============================================================================

import sys

def ConvertPath(path, directoriesFrom = 0, directoriesUntil = None, lastFowardSlash = True):
    """
    Recieves a string which should be a path to a file. If the directory separator
    is '\\', then it is converted to '/' and the path is returned. The return value
    is a path string with '/' as directory separators and with '/' at the end.
    
    Optional varaibles:
        directoriesFrom => Removes the specified number of directories from the start of the path.
        directoriesUntil => Removes the specified number of directories from the end of the path.
        lastFowardSlash => If false, remove the last foward slash from the return value.
    """
    if directoriesUntil:
        directoriesUntil = -directoriesUntil
        
    if '\\' in path: 
        pathList = path.split("\\")
    else: 
        pathList = path.split("/")
    
    if pathList[-1] == "":
        del pathList[-1]

    path = "/".join(pathList[directoriesFrom:directoriesUntil])
    
    if lastFowardSlash:
        path += '/'
        
    return path

# =============================================================================
# 
# =============================================================================
import os
frozen = getattr(sys, 'frozen', '')

if not frozen:
    # not frozen: in regular python interpreter
    scriptDir = ConvertPath(os.path.abspath(sys.argv[0],0,1))

elif frozen in ('dll', 'console_exe', 'windows_exe'):
    # py2exe:
    scriptDir = ConvertPath(sys.executable,0,1)
    
elif frozen in ('macosx_app',):
    # py2app:
    # Notes on how to find stuff on MAC, by an expert (Bob Ippolito):
    # http://mail.python.org/pipermail/pythonmac-sig/2004-November/012121.html
    scriptDir = os.environ['RESOURCEPATH']
    
#Code for retrieving file path by Peter Hansen
#https://stackoverflow.com/questions/1511461/py2exe-and-the-file-system
# =============================================================================
# 
# =============================================================================
import subprocess
import shutil
class Compiler:
    """
    Easily compile your script and copy any relevant files into the distribution
    folder. The file names can contain a directory, but it must be a relative
    path. Each file will have the same relative path to the executable as it had
    to the original script file.
    
    Additionally, you can specify a list of source files, which will be copied
    into a folder named 'src' inside the the distribution folder.
    
    a = Compiler(yourSources,yourOtherFiles)
    a.Compile()
    """
    sourceFiles = []
    auxilaryFiles = []
    
    _distributionFolder = 'dist/'
    _sourceFolder = 'src/'
    _fullSourcePath = _distributionFolder + _sourceFolder
    distUtilsArgs = []
    
    def changeFolderNames(self,dist='dist/',src='src/'):
        """
        Changes the path of the distutils directory when compiling with py2exe
        and/or the path of the directory which contains the distributed source
        files.
        """
        self._distributionFolder = ConvertPath(dist)
        self._sourceFolder = ConvertPath(src)
        self._fullSourcePath = self._distributionFolder + self._sourceFolder
    
    
    def __init__(self, sourceFiles = None, auxilaryFiles = None):
        if sourceFiles:
            self.sourceFiles = sourceFiles[:]
        if auxilaryFiles:
            self.auxilaryFiles = auxilaryFiles[:]
        
    
    @staticmethod
    def _CopyFiles(fileNameList,destinationDirectory):
        for fileName in fileNameList:
            directories = fileName.split("/")[:-1]
            path = destinationDirectory
            for directory in directories:
                path += directory+'/'
                if not os.path.exists(path):
                    os.makedirs(path)
            if os.path.exists(destinationDirectory+fileName):
                
                with open(fileName,'r') as f:
                    a = f.readlines()
                    with open(destinationDirectory+fileName,'r') as f2:
                        b = f2.readlines()
                if a == b:
                    pass
                else:
                    shutil.copy2(fileName, destinationDirectory+fileName)
                    print (fileName + ' was updated.')
            else:
                shutil.copy2(fileName, destinationDirectory+fileName)
    
    def Compile(self):
        """
        Create the executable and copy any updated auxilary/source files to the
        distribution folder.
        """
        subprocess.call(['python','setup.py','py2exe','--dist-dir='+self._distributionFolder] + self.distUtilsArgs)
        if len(self.auxilaryFiles):
            Compiler._CopyFiles(self.auxilaryFiles,self._distributionFolder)
        if len(self.sourceFiles):
            if not os.path.exists(self._fullSourcePath[:-1]):
                os.makedirs(self._fullSourcePath[:-1])
            Compiler._CopyFiles(self.sourceFiles,self._fullSourcePath)
