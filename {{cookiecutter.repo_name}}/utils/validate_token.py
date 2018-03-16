#!/bin/python
# -*- coding: utf-8 -*-

"""Validate token."""
from bitcoin.utils.exceptions import AccessDenied
from bitcoin.database.database import Database


def validate_token(token):
    """
    Validate Token.

    :param cursor: database cursor object
    :param connection: database connection object
    :param token: user token
    :param endpoint: route name
    """
    if token is None:
        raise AccessDenied("No token", 403)
    db = Database()
    cursor, conn = db.connect()
    cursor.execute(
        """
        select exists(select id from user where token='{}') as token
        """.format(token)
    )
    if cursor.fetchone()['token'] == 0:
        raise AccessDenied("Invalid Token", status_code=403)
