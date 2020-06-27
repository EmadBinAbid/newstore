import logging

class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        self.fileHandler = logging.FileHandler('logs/' + self.filename)
        self.fileHandler.setFormatter(formatter)

    def debug(self, message):
        self.fileHandler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.fileHandler)
        self.logger.debug(message)

    def error(self, message):
        self.fileHandler.setLevel(logging.ERROR)
        self.logger.addHandler(self.fileHandler)
        self.logger.error(message)