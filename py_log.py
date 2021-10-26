#! /usr/bin/python
# -*- coding: utf-8 -*-
# Create by zhoubaicun
"""
log.py
"""

import logging


def getLogger(name, level=logging.WARN, filename='', f_level=logging.INFO):
    """
    name: logger name
    level: StreamHandler level
    filename: FileHandler filename
    f_level: FileHandler level
    """
    logger = logging.getLogger("logger")
    logger.propagate = False
    if logger.hasHandlers():
        return logger

    logger.setLevel(min(level, f_level) if filename else level)
    fmt = logging.Formatter(fmt="[%(asctime)s][%(process)d][%(levelname)s] %(message)s" ,datefmt="%Y/%m/%d %H:%M:%S")
    sh = logging.StreamHandler()
    sh.setLevel(level)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    if filename:
        fh = logging.FileHandler(filename=filename, mode='w')
        fh.setFormatter(fmt)
        fh.setLevel(f_level)
        logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    logger = getLogger('log', logging.WARN, 'fh.log', logging.INFO)
    logger.debug("This is  DEBUG of logger1 !!")
    logger.info("This is  INFO of logger1 !!")
    logger.warning("This is  WARNING of logger1 !!")
    logger.error("This is  ERROR of logger1 !!")
    logger.critical("This is  CRITICAL of logger1 !!")
    # try logger with same name
    logger = getLogger('log')
    logger.debug("This is  DEBUG of logger1 !!")
    logger.info("This is  INFO of logger1 !!")
    logger.warning("This is  WARNING of logger1 !!")
    logger.error("This is  ERROR of logger1 !!")
    logger.critical("This is  CRITICAL of logger1 !!")
