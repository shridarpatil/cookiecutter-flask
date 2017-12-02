#!/bin/python
# -*- coding: utf-8 -*-

"""Log client details"""


class LogClient(object):
    """Docstring for LogClient."""

    def __init__(self, arg):
        """Initialise."""
        super(LogClient, self).__init__()
        self.arg = arg
        self.log_client()

    def log_client(self):
        """Log client."""
        from server import logger
        logger.info('Client-IP: ' + self.arg.remote_addr)
        logger.info('User-Agent: ' + self.arg.headers.get('User-Agent'))
