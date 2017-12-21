# coding=utf-8

import logging
import logging.config
import traceback
from color import Color


class ColoreFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Color.BLUE,
        'INFO': Color.WHITE,
        'WARNING': Color.YELLOW,
        'ERROR': Color.RED,
        'CRITICAL': Color.PURPLE
    }
    COLOR_SEQ = "\033[%dm"
    COLOR_RESET = "\033[0m"

    def __init__(self, fmt, datefmt):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        levelname = record.levelname
        if levelname in self.COLORS:
            fore_color = self.COLORS[levelname]
            record.name = self.COLOR_SEQ % fore_color + record.name
            record.msg = str(record.msg) + self.COLOR_RESET
            return logging.Formatter.format(self, record)


class Logger(object):

    LOG_FILE = ''

    def __init__(self, name='', configpath=None):
        self.name = name
        try:
            if not configpath:
                msgformat = '%(name)-12s %(asctime)s %(levelname)-8s %(message)s'
                dateformat = '%d %b %Y %H:%M:%S'

                self.logger = logging.getLogger(name)
                self.logger.setLevel(logging.DEBUG)
                # Level: CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

                normal_formatter = logging.Formatter(msgformat, dateformat)
                color_formatter = ColoreFormatter(msgformat, dateformat)

                stream_handler = logging.StreamHandler()
                file_handler = logging.handlers.RotatingFileHandler(self.LOG_FILE,
                                                                    maxBytes=1*1024*1024,
                                                                    backupCount=5)

                stream_handler.setFormatter(color_formatter)
                file_handler.setFormatter(normal_formatter)

                self.logger.addHandler(file_handler)
                self.logger.addHandler(stream_handler)
            else:
                print configpath
                logging.config.fileConfig(configpath)
                self.logger = logging.getLogger(name)

        except Exception as e :
            traceback.print_exc()

        finally:
            pass

    def debug (self, msg):
        self.logger.debug(msg)

    def info (self, msg):
        self.logger.info(msg)

    def warning (self, msg):
        self.logger.warning(msg, exc_info=True)

    def error (self, msg):
        self.logger.error(msg, exc_info=True)

    def critical (self, msg):
        self.logger.critical(msg, exc_info=True)


logger = Logger("")


if __name__ == '__main__':
    logger = Logger("test")
    logger.debug("test")
    logger.info("test")
    logger.warning("test")
    logger.error("test")
    logger.error(1/0)
