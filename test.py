from pathlib import Path
print('\nRunning' if __name__ == '__main__' else '\nImporting', Path(__file__).resolve())

from src.package_KosSasha.module_logger import Logger

l = Logger(level=Logger.DEBUG, stackTraceLines=2)
l.dbg()
l.inf()
l.wrn()
l.err()