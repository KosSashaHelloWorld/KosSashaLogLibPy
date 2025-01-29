'''Small logger module'''
import string
import sys
import threading
from traceback import print_stack


class Logger:
    '''
    This is the main conception of local logging object

    To start do "logger = Logger(Logger.DEBUG, 0)" and "logger.inf("My info message")"
    '''

    __NONE          = 0
    ERROR           = 10
    WARNING         = 20
    INFO            = 30
    DEBUG           = 40

    __DEBUG_STR     = " [DEBUG]   "
    __INFO_STR      = " [INFO]    "
    __WARNING_STR   = " [WARNING] "
    __ERROR_STR     = " [ERROR]   "

    __ANSI_WHITE    = "\033[37m"
    __ANSI_GREEN    = "\033[32m"
    __ANSI_YELLOW   = "\033[33m"
    __ANSI_RED      = "\033[31m"
    __ANSI_CLEAR    = "\033[0m"

    __FRAMES_BACK   = 3
    __LOG_DELIMITER = "/------------------------------------------------/\n"

    def __init__(self, level: int = DEBUG, stackTraceLines: int = 0):
        ''':Example:
        :logger = Logger(Logger.DEBUG, False)
        :logger.inf("log")
        :>> [therad=BD0] [INFO] log

        :If you do not want to create new object you can use:
        :
        
        :param  level: Describes the level of logger
        :param stackTraceLines: if 0 - disable printing stacktrace after each log operation
        :return: local logger instance
        '''
        self.__levelProperty = level
        self.__stackTraceLines = stackTraceLines
    
    @staticmethod
    def __printStackTrace(stackTraceLines: int = 0):  
        # __FRAMES_BACK(3) is an actual amount of (frame.f_back) 
        # times to do not to show log lib logic in user's code
        print_stack(
            f=sys._getframe(Logger.__FRAMES_BACK), 
            limit=stackTraceLines)
        print()

    @staticmethod
    def logShot(stackTraceLines: int = 0, msg: string = ""):
        threadStr = "\n[thread={threadStr:X}] [LOGSHOT]".format(threadStr = threading.get_ident())
        print(threadStr + msg)

        if (stackTraceLines):
            Logger.__printStackTrace(stackTraceLines=stackTraceLines)
    
    def __levelIs(self, level: int) -> bool:
        ''':return: true if level of current operation is equal or less than the logger level'''
        return self.__levelProperty >= level
    
    def __log(self, msg: string):
        threadStr = self.__LOG_DELIMITER + "[thread={threadStr:X}]".format(threadStr = threading.get_ident())
        print(threadStr + msg)

        if (self.__stackTraceLines):
            Logger.__printStackTrace(stackTraceLines=self.__stackTraceLines)
        
    def __color(self, color: string, str: string) -> string:
        return color + str + self.__ANSI_CLEAR
    
    def dbg(self, msg: string = ""):
        '''Shorthand for "logger.log(Logger.DEBUG, msg)", but faster'''
        if self.__levelIs(Logger.DEBUG):
            self.__log(self.__color(self.__ANSI_WHITE, Logger.__DEBUG_STR + msg))

    def inf(self, msg: string = ""):
        '''Shorthand for "logger.log(Logger.INFO, msg)", but faster'''
        if self.__levelIs(Logger.INFO):
            self.__log(self.__color(self.__ANSI_GREEN, Logger.__INFO_STR + msg))

    def wrn(self, msg: string = ""):
        '''Shorthand for "logger.log(Logger.WARNING, msg)", but faster'''
        if self.__levelIs(Logger.WARNING):
            self.__log(self.__color(self.__ANSI_YELLOW, Logger.__WARNING_STR + msg))
    
    def err(self, msg: string = ""):
        '''Shorthand for "logger.log(Logger.ERROR, msg)", but faster'''
        if self.__levelIs(Logger.ERROR):
            self.__log(self.__color(self.__ANSI_RED, Logger.__ERROR_STR + msg))

    def log(self, level: int = DEBUG, msg: string = ""):
        ''':Printig your message at defined level, 
        but "logger.log(Logger.INFO, msg)" works slower 
        than just "logger.inf(msg)"
        
        :param level: The level of log message ()
        :param msg: Message to log
        '''
        if self.__levelIs(level):

            # Choose a color based on logger level
            # Works slower than just logger.inf(msg)
            if (level >= self.DEBUG):
                color = self.__ANSI_WHITE
                logstr = self.__DEBUG_STR
            elif (level >= self.INFO):
                color = self.__ANSI_GREEN
                logstr = self.__INFO_STR
            elif (level >= self.WARNING):
                color = self.__ANSI_YELLOW
                logstr = self.__WARNING_STR
            elif (level >= self.ERROR):
                color = self.__ANSI_RED
                logstr = self.__ERROR_STR
            else:
                color = self.__ANSI_CLEAR
                logstr = self.__DEBUG_STR

            self.__log(self.__color(color, logstr + msg))