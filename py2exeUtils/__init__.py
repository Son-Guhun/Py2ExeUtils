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

from Compiler import Compiler
import globalvars

class version:
    major = 2
    minor = 0
    patch = 0
    
    version = str(major) + '.' + str(minor) + '.' + str(patch)

frozen = globalvars.FROZEN
FROZEN = globalvars.FROZEN
scriptDir = globalvars.DIRECTORY
DIRECTORY = globalvars.DIRECTORY


# =============================================================================
del globalvars
