import logging

from config.appconfig import get_log_filename

class Logger(object):
    class __Logger:
        def __init__(self):
            self.val = None
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
            self.fileHandler = logging.FileHandler(get_log_filename())
            self.fileHandler.setFormatter(formatter)

        def debug(self, message):
            self.fileHandler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.fileHandler)
            self.logger.debug(message)

        def error(self, message):
            self.fileHandler.setLevel(logging.ERROR)
            self.logger.addHandler(self.fileHandler)
            self.logger.error(message)
        
        def __str__(self):
            return self.val
            
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        return Logger.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)