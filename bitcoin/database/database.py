#!/bin/python
# -*- coding: utf-8 -*-

"""Database connection."""

import pymysql
import json


class Database():
    """Create service."""

    def __init__(self):
        """Initialize."""
        try:
            with open('dbConfig.json') as data_file:
                data = json.load(data_file)
        except Exception as e:
            raise e
        else:
            self.host = data.get("host", 'localhost')
            self.user = data.get("user", 'root')
            self.password = data.get('password', 'r00t')
            self.db = data.get('database', 'bitcoin')

    def connect(self):
        """Connect to mysql database."""
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.conn.autocommit(True)
            self.c = self.conn.cursor()
        except Exception as e:
            raise ValueError(e)

        return self.c, self.conn

    def close(self):
        """Close database connection"""
        self.conn.close()
