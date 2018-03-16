#!/bin/env python
# -*- coding: utf-8 -*-
"""Logger"""
import logging
import os
from datetime import datetime


TAGS = ["bitcoin"]
LOGGER_APP_NAME = {{cookiecutter.package}}
# add extra field to logstash message
DIR = 'logs'
FILE_PATH = './{}/{}-logs-{}.log'.format(
    DIR, LOGGER_APP_NAME, datetime.now().strftime("%Y-%m-%d")
)


def get_logger():
    """
    Return Logger.

    Setup Logstash Logger.
    """
    logger = logging.getLogger(LOGGER_APP_NAME)

    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    d = os.path.dirname(FILE_PATH)
    if not os.path.exists(d):
        os.makedirs(d)

    ch = logging.FileHandler(FILE_PATH)

    formatter = logging.Formatter("%(levelname)s [%(asctime)s]: %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    if not logger.handlers:
        logger.addHandler(ch)

    return logger
