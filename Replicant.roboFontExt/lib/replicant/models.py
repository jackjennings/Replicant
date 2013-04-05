import os
from time import time, strftime

class Replicant(object):
    
    font = None
    
    def __init__(self, font):
        if font and font.path:
            self.font = font.copy()    

    def replicate(self):
        if hasattr(self, 'font'):
            self.font.save(destDir=self.filepath())
        
    def path(self):
        archive = "_archive"
        return os.path.join(os.path.dirname(self.font.path), archive)
        
    def filepath(self):
        filename = "%s.ufo" % "_".join(self.parts())
        return os.path.join(self.path(), filename)
    
    def version(self):
        versionMajor = self.font.info.versionMajor or 0
        versionMinor = self.font.info.versionMinor or 0
        return "v%s-%s" % (versionMajor, versionMinor)

    def parts(self):
        familyName = self.font.info.familyName or None
        styleName = self.font.info.styleName or None
        date = strftime("%Y-%m-%d")
        time = strftime("%H-%M-%S")

        return self.filterParts([familyName, styleName, date, time, self.version()])

    def filterParts(self, parts):
        for part in parts:
            if part is not None: yield str(part)