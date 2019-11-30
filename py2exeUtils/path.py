import os

def commonpath(l):
    # Credits: Dan-d (https://stackoverflow.com/questions/21498939/how-to-circumvent-the-fallacy-of-pythons-os-path-commonprefix)
    cp = []
    ls = [p.split(os.path.sep) for p in l]
    ml = min( len(p) for p in ls )

    for i in range(ml):

        s = set( p[i] for p in ls )
        if len(s) != 1:
            break

        cp.append(s.pop())

    return os.path.sep.join(cp)

def up(path, n=1, lastSeparator=True):
    """Examples:
    
    up('C:/Users/SonGuhun') => 'C:\\Users\\'
    up('C:/Users/SonGuhun', lastSeparator=False) => 'C:\\Users'
    up('C:\\Users\\SonGuhun\\Documents', n=2) => 'C:\\Users\\'
    """
    return os.path.abspath(os.path.join(path ,"/".join(['..' for i in range(n)]))) \
           + (os.path.sep if lastSeparator else '')

rstrrstrip=up

def relative(path, depth=1, lastSeparator=True):
    """Returns a relative path. Examples:
    
    relative('C:\\Users\\SonGuhun\\Documents') => 'Documents\\'
    relative('C:\\Users\\SonGuhun\\Documents', depth=2 => 'SonGuhun\\Documents\\'
    """
    return os.path.relpath(path,up(path,depth,False)) \
           + (os.path.sep if lastSeparator else '')

def lstrip(path, n=1, lastSeparator=True):
    """Examples:
    
    lstrip('C:\\Users\\SonGuhun\\Documents', n=3) => 'Documents\\'
    lstrip('C:\\Users\\SonGuhun\\Documents') => 'Users\\SonGuhun\\Documents\\'
    """    
    return os.path.relpath(path,up(path,1-n+os.path.abspath(path).count(os.path.sep),False)) \
           + (os.path.sep if lastSeparator else '') if n>0 else path
    
def strip(path, left=0, right = 0, lastSeparator=True):
    """Examples:
    
    strip('C:\\Users\\SonGuhun\\Documents') => 'C:\\Users\\SonGuhun\\Documents\\'
    strip('C:\\Users\\SonGuhun\\Documents', left=2) => 'SonGuhun\\Documents\\'
    strip('C:\\Users\\SonGuhun\\Documents', left=2, right=1) => 'SonGuhun\\'
    """   
    return lstrip(up(path, right,False),left,False) + (os.path.sep if lastSeparator else '')
