'''Small logger module'''
import string
import sys
import threading
import traceback


class Logger:
    '''
    This is the main conception of local logging object

    To start do "logger = Logger(Logger.DEBUG, 0)" and "logger.inf("My info message")"
    '''

    __NONE  = 0
    ERROR   = 10
    WARNING = 20
    INFO    = 30
    DEBUG   = 40

    DEBUG_STR   = " [DEBUG]   "
    INFO_STR    = " [INFO]    "
    WARNING_STR = " [WARNING] "
    ERROR_STR   = " [ERROR]   "

    def __init__(self, level: int, stackTraceLines: int):
        ''':Example:
        >>>logger = Logger(Logger.LoggerLevel.DEBUG, False)
        >>>logger.inf("log")
        :Result:
        :>> [thread=CurrentThread] [INFO] log

        :param  level: Describes the level of logger
        :param stackTraceLines: if 0 - disable printing stacktrace after each log operation
        :return: local logger instance
        '''
        self.__levelProperty = level
        self.__stackTraceLines = stackTraceLines
    
    def __levelIs(self, level: int) -> bool:
        ''':return: true if level of current operation is equal or less than the logger level'''
        return self.__levelProperty >= level
    
    def __log(self, msg: string):
        threadStr = "\n[therad={threadStr:X}]".format(threadStr = threading.get_ident())
        print(threadStr + msg)

        if (self.__stackTraceLines):
            traceback.print_stack(f=sys._getframe(2), limit=self.__stackTraceLines)
        
    def __bold(self, str: string) -> string:
        return "\033[37m" + str + "\033[0m"
        
    def __green(self, str: string) -> string:
        return "\033[32m" + str + "\033[0m"
        
    def __yellow(self, str: string) -> string:
        return "\033[33m" + str + "\033[0m"
        
    def __red(self, str: string) -> string:
        return "\033[31m" + str + "\033[0m"
    
    def dbg(self, msg: string = ""):
        '''Printing your message at debug level'''
        if self.__levelIs(Logger.DEBUG):
            self.__log(self.__bold(Logger.DEBUG_STR + msg))

    def inf(self, msg: string = ""):
        '''Printing your message at info level'''
        if self.__levelIs(Logger.INFO):
            self.__log(self.__green(Logger.INFO_STR + msg))

    def wrn(self, msg: string = ""):
        '''Printing your message at warning level'''
        if self.__levelIs(Logger.WARNING):
            self.__log(self.__yellow(Logger.WARNING_STR + msg))
    
    def err(self, msg: string = ""):
        '''Printing your message at error level'''
        if self.__levelIs(Logger.ERROR):
            self.__log(self.__red(Logger.ERROR_STR + msg))