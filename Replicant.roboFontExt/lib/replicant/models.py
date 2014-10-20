import os
from time import time, strftime


class Replicant(object):

    font = None
    archive_dir = "_archive"

    def __init__(self, font):
        if font and font.path:
            self.font = font

    def replicate(self):
        if hasattr(self, 'font'):
            self.font.copy().save(destDir=self.filepath)

    @property
    def path(self):
        return os.path.join(os.path.dirname(self.font.path), self.archive_dir)

    @property
    def filepath(self):
        filename = "%s.ufo" % "_".join(self.parts)
        return os.path.join(self.path, filename)

    @property
    def version(self):
        versionMajor = self.font.info.versionMajor or 0
        versionMinor = self.font.info.versionMinor or 0
        return "v%s-%s" % (versionMajor, versionMinor)

    @property
    def parts(self):
        familyName = self.font.info.familyName or None
        styleName = self.font.info.styleName or None
        date = strftime("%Y-%m-%d")
        time = strftime("%H-%M-%S")

        ps = [familyName, styleName, date, time, self.version]
        return [str(p) for p in ps if p is not None]
