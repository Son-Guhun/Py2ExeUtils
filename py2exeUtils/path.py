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
    return os.path.abspath(os.path.join(path ,"/".join(['..' for i in range(n)]))) \
           + (os.path.sep if lastSeparator else '')

rstrrstrip=up

def relative(path, depth=1, lastSeparator=True):
    return os.path.relpath(path,up(path,depth,False)) \
           + (os.path.sep if lastSeparator else '')

def lstrip(path, n=1, lastSeparator=True):
    return os.path.relpath(path,up(path,1-n+os.path.abspath(path).count(os.path.sep),False)) \
           + (os.path.sep if lastSeparator else '')
    
def strip(path, left=0, right = 0, lastSeparator=True):
    return lstrip(up(path, right,False),left,False) + (os.path.sep if lastSeparator else '')
