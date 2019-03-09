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

