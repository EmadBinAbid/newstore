import logging

from config.appconfig import get_log_filename

class Logger(object):
    """
    This class handles logging in all Newstore modules. It implements 
    Singleton design pattern to make sure only one instance of this 
    class is created throughout the running state of application.
    """

    class __Logger:
        def __init__(self):
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
            self.fileHandler = logging.FileHandler(get_log_filename())
            self.fileHandler.setFormatter(formatter)

        def debug(self, message) -> None:
            """
            Logs application flow statements in the log file

            Parameters:
            message (str): The message to be logged

            Returns:
            None

            """
            self.fileHandler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.fileHandler)
            self.logger.debug(message)

        def error(self, message) -> None:
            """
            Logs application error statements in the log file

            Parameters:
            message (str): The message to be logged

            Returns:
            None

            """
            self.fileHandler.setLevel(logging.ERROR)
            self.logger.addHandler(self.fileHandler)
            self.logger.error(message)
            
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        return Logger.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)