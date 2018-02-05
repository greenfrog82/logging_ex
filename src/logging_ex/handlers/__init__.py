import logging
import pwd
import grp
import os


class RotatingFileHandlerEx(logging.handlers.RotatingFileHandler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0, owner=None, chmod=None):
        self.owner = owner
        self.chmod = chmod

        logging.handlers.RotatingFileHandler.__init__(
            self, filename, mode, maxBytes, backupCount, encoding, delay)

    def _open(self):
        stream = logging.handlers.RotatingFileHandler._open(self)

        if self.owner:
            uid = pwd.getpwnam(self.owner[0]).pw_uid
            gid = grp.getgrnam(self.owner[1]).gr_gid

            os.chown(self.baseFilename, uid, gid)
            os.chmod(self.baseFilename, self.chmod)

        return stream


logging.handlers.RotatingFileHandlerEx = RotatingFileHandlerEx
